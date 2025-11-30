import mysql.connector
from mysql.connector import errorcode

def get_db_connection(config_dict):
    """
    Establishes a connection to the MySQL database.
    Returns a connection object if successful, otherwise None.
    """
    try:
        conn = mysql.connector.connect(**config_dict) # connect to ___ database
        print(f"\nConnected to database '{config_dict['database']}'")
        return conn
        # input("\n\n Press any key to continue...")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exist")

        else:
            print(err)
        return None

def execute_query(connection, query, params=None, fetch_results=True):
    """
    Executes a given SQL query using an existing connection.
    Handles cursor creation, execution, and closing the cursor.
    Returns results if a SELECT query, or None for CUD operations.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        # print(f"Executed: {query[:50]}...")

        results = cursor.fetchall()
        field_names = [i[0] for i in cursor.description]
        return results, field_names

    except mysql.connector.Error as err:
        print(f"Database operation failed: {err}")
        return None, None

    finally:
        cursor.close()

def format_and_print_results(results, field_names):
    """
    Formats query results into a 'Field: data' layout and prints them.
    """
    if not results:
        print("No data found for the query.")
        return

    for row in results:
        for name, data in zip(field_names, row):
            print(f"{name.capitalize():}: {data}")
        print()