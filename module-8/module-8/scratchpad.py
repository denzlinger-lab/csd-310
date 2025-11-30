import _mysql_connector
import mysql
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

secrets = dotenv_values(".env")

config = {
    "user": secrets["DB_USER"],
    "password": secrets["DB_PASSWORD"],
    "host": secrets["DB_HOST"],
    "database": secrets["DB_NAME"],
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

try:
    print("\n Database user{} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")


    def film_query_display(cursor, film_title):
        search_pattern = f"%{film_title}%"
        # cursor = db.cursor()
        query = """"
        SELECT
            film_name as Name,
            film_director as Director,
            genre_name as Genre,
            studio_name as Studio
        FROM
            film
        INNER JOIN
            genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id")
        """
        cursor.execute(query, (search_pattern,))
        results = cursor.fetchall()
        if results:
            print(f"\n Results for film title containing '{film_title}'")
            for row in results:
                print(f"  - **Name:** {row[0]}, **Director:** {row[1]}, **Genre:** {row[2]}, **Studio:** {row[3]}")
        else:
            print(f"\n No results for film title containing '{film_title}'")

    cursor = db.cursor()

    film_query_display(cursor, "title_1")

    cursor.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username and password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

finally:
    db.close()


