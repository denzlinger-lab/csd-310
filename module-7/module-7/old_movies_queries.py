# Abram Denzlinger
# November 29, 2025
# 7.2 Assignment - Movies Tables - Queries

# This program connects to a database using a .env
# file for configuration. It contains 4 separate
# queries of the database, and formats and prints
# the results of each query.

import mysql.connector
from mysql.connector import errorcode
from dotenv import dotenv_values

secrets = dotenv_values(".env")

"""database config object"""
config = {
    "user": secrets["DB_USER"],
    "password": secrets["DB_PASSWORD"],
    "host": secrets["DB_HOST"],
    "database": secrets["DB_NAME"],
    "raise_on_warnings": True #not in .env file
}

try:
    """try/catch block for handling potential MySQL database errors"""

    db = mysql.connector.connect(**config) # connect to ___ database

    # output the connection status
    print("\n Database user {} connected to MySQl on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

    # ======================  first query start ======================
    cursor_1 = db.cursor()
    #print("cursor_1 created.")

    studio_query = "SELECT * FROM studio"
    #print(f"Executing query: {studio_query}")
    cursor_1.execute(studio_query)

    field_names = [i[0] for i in cursor_1.description]
    #print(f"Detected Fields: {field_names}")

    results = cursor_1.fetchall()
    print(f"\n-- DISPLAYING Studio RECORDS --")

    for row in results:
        for field_name, data in zip(field_names, row):
            print(f"{field_name.capitalize():}: {data}")
        print()
    # ======================  first query end ======================
    # ======================  second query start ======================
    cursor_2 = db.cursor()
    #print("cursor_2 created.")

    genre_query = "SELECT * FROM genre"
    #print(f"Executing query: {genre_query}")
    cursor_2.execute(genre_query)

    field_names = [i[0] for i in cursor_2.description]
    #print(f"Detected Fields: {field_names}")

    results = cursor_2.fetchall()
    print(f"\n-- DISPLAYING Genre RECORDS --")

    for row in results:
        for field_name, data in zip(field_names, row):
            print(f"{field_name.capitalize():}: {data}")
        print()
    # ======================  second query end ======================
    # ======================  third query start ======================
    cursor_3 = db.cursor()
    #print("cursor_2 created.")

    short_film_query = "SELECT Film_name, Film_runtime FROM film WHERE Film_runtime < 120"
    #print(f"Executing query: {short_film_query}")
    cursor_3.execute(short_film_query)

    field_names = [i[0] for i in cursor_3.description]
    #print(f"Detected Fields: {field_names}")

    results = cursor_3.fetchall()
    print(f"\n-- DISPLAYING Short Film RECORDS --")

    for row in results:
        for field_name, data in zip(field_names, row):
            print(f"{field_name.capitalize():}: {data}")
        print()
    # ======================  third query end ======================
    # ======================  fourth query start ======================
    cursor_4 = db.cursor()
    #print("cursor_2 created.")

    director_sort_query = "SELECT Film_name, Film_director FROM film ORDER BY Film_director"
    #print(f"Executing query: {director_sort_query}")
    cursor_4.execute(director_sort_query)

    field_names = [i[0] for i in cursor_4.description]
    #print(f"Detected Fields: {field_names}")

    results = cursor_4.fetchall()
    print(f"\n-- DISPLAYING Director RECORDS in Order --")

    for row in results:
        for field_name, data in zip(field_names, row):
            print(f"{field_name.capitalize():}: {data}")
        print()
# ======================  fourth query end ======================

except mysql.connector.Error as err:
    """on error code"""

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    """close the connection to the MySQL"""
    db.close()
