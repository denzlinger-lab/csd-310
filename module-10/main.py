"""import statements"""
import mysql.connector  # to connect
from dotenv import dotenv_values
from mysql.connector import errorcode

#using our .env files
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
    """try/catch block for handling potential mysql database errors"""

    db = mysql.connector.connect(**config) # connect to movies database

    # output the connection status
    print("\n Database user {} connected to MySql on host with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    """on error code"""

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    """close the connection to MySql"""

    db.close()