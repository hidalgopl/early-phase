import peewee_async

LOG_FORMAT = '%(asctime)-15s %(message)s'
DB_NAME = 'app'
DB_USER = 'app'
DB_PASSWORD = 'secret_pass'
DB_PORT = 5432
SERVICE_NAME = 'gis-service'
DB_HOST = 'app-db'

db = peewee_async.PostgresqlDatabase(
    DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT,
    host=DB_HOST,
)
