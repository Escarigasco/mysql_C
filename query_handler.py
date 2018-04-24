# run with sudo python3

import MySQLdb
from email_sender import email_sender
import configparser


class query_handler(object):

    def run(self, first_date, second_date, email_address, info):
        config = configparser.ConfigParser()
        config.read("path/to/file")
        host = config.get("configuration", "host")
        user_name = config.get("configuration", "user_name")
        password = config.get("configuration", "password")
        database = config.get("configuration", "database")

        db = MySQLdb.connect(host, user_name, password, database)
        es = email_sender()
        cursor = db.cursor()

        first_minute = " 00:00:01 "
        second_minute = " 23:59:59 "

        first_date = first_date + first_minute
        second_date = second_date + second_minute

        apo = '\"'
        comma = ','
        newline = '\n'
        file = 'path/to/file'
        cursor.execute("""SELECT * FROM Climate_Data_def WHERE `Timestamp` BETWEEN %s AND %s INTO OUTFILE %s FIELDS TERMINATED BY %s ENCLOSED BY %s LINES TERMINATED BY %s """, (first_date, second_date, file, comma, apo, newline,))
        es.send(email_address, info)


if __name__ == "__main__":
    test = query_handler()
    email_address = "email@address.com"
    first_minute = " 00:00:01 "
    second_minute = " 23:59:59 "
    first_date = "2018-04-24"
    second_date = "2018-04-24"
    first_date = first_date + first_minute
    second_date = second_date + second_minute
    info = "test content"
    test.run(first_date, second_date, email_address, info)
