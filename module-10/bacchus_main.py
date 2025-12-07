# Group 3
# James, Noor, Abram Denzlinger
# 10.1 - Milestone 2 - Bacchus Winery

# This is the main program. Separate functions are defined for:
# connecting to a database using a .env file for configuration
# info, executing a query, and formatting and printing query
# results. Functions are called below to meet assignment criteria.

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

from bacchus_functions import get_db_connection, execute_query, format_and_print_results

# ----------- CONNECT TO DATABASE ----------- #
db_conn = get_db_connection(config)

if db_conn:
    # --------------- FIRST QUERY --------------- #
    print(f"\n-- DISPLAYING Departments RECORDS --")
    sql_1 = "SELECT * FROM Departments"
    results_1, fields_1 = execute_query(db_conn, sql_1)

    if results_1:
        format_and_print_results(results_1, fields_1)

    # --------------- SECOND QUERY --------------- #
    print(f"\n-- DISPLAYING Distributors RECORDS --")
    sql_2 = "SELECT * FROM Distributors"
    results_2, fields_2 = execute_query(db_conn, sql_2)

    if results_2:
        format_and_print_results(results_2, fields_2)

    # --------------- THIRD QUERY --------------- #
    print(f"\n-- DISPLAYING Employees RECORDS --")
    sql_3 = "SELECT * FROM Employees"
    results_3, fields_3 = execute_query(db_conn, sql_3)

    if results_3:
        format_and_print_results(results_3, fields_3)

    # --------------- FOURTH QUERY --------------- #
    print(f"\n-- DISPLAYING Suppliers RECORDS --")
    sql_4 = "SELECT * FROM Suppliers"
    results_4, fields_4 = execute_query(db_conn, sql_4)

    if results_4:
        format_and_print_results(results_4, fields_4)

    # --------------- Fifth QUERY --------------- #
    print(f"\n-- DISPLAYING Supplies RECORDS --")
    sql_5 = "SELECT * FROM Supplies"
    results_5, fields_5 = execute_query(db_conn, sql_5)

    if results_5:
        format_and_print_results(results_5, fields_5)

# --------- CLOSE DATABASE CONNECTION --------- #
if db_conn and db_conn.is_connected():
    db_conn.close()
    print("Main database connection is closed.")
    print()
    print()