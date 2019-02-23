FROM python:3.6
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 9974

# Migrates the database, uploads staticfiles, and runs the production server
ENTRYPOINT ["python", "__main__.py"]