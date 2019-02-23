FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
     apt-get upgrade -y && \
     apt-get install -y apt-utils  && \
     apt-get install -y postgresql-client
RUN wget http://download.osgeo.org/geos/geos-3.6.1.tar.bz2
RUN tar -xjf geos-3.6.1.tar.bz2
RUN cd geos-3.6.1; ./configure; make; make install

RUN wget http://download.osgeo.org/gdal/2.2.1/gdal-2.2.1.tar.gz
RUN tar -xzf gdal-2.2.1.tar.gz
RUN cd gdal-2.2.1; ./configure; make; make install
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt-get install binutils
RUN export LD_LIBRARY_PATH=/usr/local/lib
RUN ldconfig
# Adds our application code to the image
COPY birdman2 code
WORKDIR code

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - birdman.wsgi:application

