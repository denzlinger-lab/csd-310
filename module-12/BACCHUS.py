import mysql.connector

# ----------------------------------------
# CONNECT TO DATABASE
# ----------------------------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="classmate password",   # <<<< REPLACE THIS
    database="team3_bacchus"
)

cursor = db.cursor()

# ----------------------------------------
# LIST OF TABLES TO DISPLAY
# ----------------------------------------
tables = [
    "Supplier",
    "Department",
    "Employee",
    "Customer",
    "Inventory",
    "Orders",
    "Order_Items"
]

# ----------------------------------------
# PRINT DATA FROM EACH TABLE
# ----------------------------------------
for table in tables:
    print(f"\n===============================")
    print(f"   {table} TABLE DATA")
    print(f"===============================")

    try:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("(No data found)")

    except mysql.connector.Error as err:
        print(f"Error reading {table}: {err}")

# ----------------------------------------
# CLOSE CONNECTION
# ----------------------------------------
db.close()

print("\n\nAll tables displayed successfully!")


