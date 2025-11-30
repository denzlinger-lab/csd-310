import mysql
from dotenv import dotenv_values
from mysql.connector import errorcode

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

    def show_films(cursor, title):
        cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
        films = cursor.fetchall()

        print("\n -- {} --".format(title))

        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

    # calling the function
    cursor = db.cursor()
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username and password are invalid.")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")

    else:
        print(err)

finally:
    db.close()


# SQL used in console for table changes:

# --------- inserting a new movie into the table
# INSERT INTO film
# VALUES (4, 'Back to the Future', '1985', 116, 'Robert Zemeckis', 3, 2)

# --------- changing Alien's genre to horror
# UPDATE film
# SET genre_id = 1
# WHERE film_id = 2;

# --------- deleting Gladiator
# DELETE FROM film
# WHERE film_id = 1;


