# Abram Denzlinger
# November 29, 2025
# 7.2 Assignment - Movies Tables - Queries

# This is the main program. Separate functions are defined for:
# connecting to a database using a .env file for configuration
# info, executing a query, and formatting and printing query
# results. Functions are called below to meet assignment criteria.

# My original effort is in 'old_movies_queries.py'. It was quick and
# easy, and it all works. I wanted more practice optimizing with
# functions, and below is the result of a lot of dialogue with
# Gemini to minimize repeating code.

import os

from dotenv import load_dotenv

load_dotenv()

secrets = os.environ

# database config object
config = {
    "user": secrets["DB_USER"],
    "password": secrets["DB_PASSWORD"],
    "host": secrets["DB_HOST"],
    "database": secrets["DB_NAME"],
    "raise_on_warnings": True #not in .env file
}

from query_functions import get_db_connection, execute_query, format_and_print_results

# ----------- CONNECT TO DATABASE ----------- #
db_conn = get_db_connection(config)

if db_conn:
    # --------------- FIRST QUERY --------------- #
    print(f"\n-- DISPLAYING Studio RECORDS --")
    sql_1 = "SELECT * FROM studio"
    results_1, fields_1 = execute_query(db_conn, sql_1)

    if results_1:
        format_and_print_results(results_1, fields_1)

    # --------------- SECOND QUERY --------------- #
    print(f"\n-- DISPLAYING Genre RECORDS --")
    sql_2 = "SELECT * FROM genre"
    results_2, fields_2 = execute_query(db_conn, sql_2)

    if results_2:
        format_and_print_results(results_2, fields_2)

    # --------------- THIRD QUERY --------------- #
    print(f"\n-- DISPLAYING Genre RECORDS --")
    sql_3 = "SELECT Film_name, Film_runtime FROM film WHERE Film_runtime < 120"
    results_3, fields_3 = execute_query(db_conn, sql_3)

    if results_3:
        format_and_print_results(results_3, fields_3)

    # --------------- FOURTH QUERY --------------- #
    print(f"\n-- DISPLAYING Director RECORDS in Order --")
    sql_4 = "SELECT Film_name, Film_director FROM film ORDER BY Film_director"
    results_4, fields_4 = execute_query(db_conn, sql_4)

    if results_4:
        format_and_print_results(results_4, fields_4)

# --------- CLOSE DATABASE CONNECTION --------- #
if db_conn and db_conn.is_connected():
    db_conn.close()
    print("Main database connection is closed.")
    print()
    print()