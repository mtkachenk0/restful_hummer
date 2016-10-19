import psycopg2

from restful_hummer.settings import DATABASES

conn_settings = "dbname='{NAME}'" \
                " user='{USER}'" \
                " host='{HOST}'" \
                " port='{PORT}'" \
                " password={PASSWORD}".format(**DATABASES['default'])

connection = psycopg2.connect(conn_settings)
cursor = connection.cursor()

query = cursor.mogrify(
    "UPDATE core_item SET price = price * 1.01;"
)
# we could use infinite loop and time.sleep(60) to execute the query every minute,
# but on my view cronjob will do that much better (it won't hold the process running)
try:
    cursor.execute(query)
    connection.commit()
except Exception as ex:
    print(ex)
    connection.rollback()

else:
    print('increased prices by 1%')