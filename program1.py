import mysql.connector
import csv

# MySQL database credentials
db_user = 'root'
db_password = 'root'
db_host = 'localhost'
db_name = 'data_mining'

# Table name
table_name = 'dm'
csv_file = 'data.csv'

def create_database():
    """Creates the 'data_mining' database if it doesn't exist."""
    try:
        conn = mysql.connector.connect(user=db_user, password=db_password, host=db_host)
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        conn.commit()
        print(f"Database '{db_name}' is ready!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def create_table():
    """Creates the 'dm' table if it doesn't exist."""
    try:
        conn = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        """)
        conn.commit()
        print(f"Table '{table_name}' is ready!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def generate_csv():
    """Generates a sample CSV file with 3 columns and 5 rows."""
    data = [
        ['id', 'name', 'age'],
        [1, 'Alice', 23],
        [2, 'Bob', 30],
        [3, 'Charlie', 27],
        [4, 'David', 25],
        [5, 'Eve', 29]
    ]

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"CSV file '{csv_file}' created!")

def load_csv_to_db():
    """Loads data from the CSV file into the MySQL table."""
    try:
        conn = mysql.connector.connect(user=db_user, password=db_password, host=db_host, database=db_name)
        cursor = conn.cursor()

        # Read CSV file
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row

            for row in reader:
                cursor.execute(f"INSERT INTO {table_name} (id, name, age) VALUES (%s, %s, %s)", row)

        conn.commit()
        print("CSV data loaded into the database!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        conn.close()

# Ensure database and table exist
create_database()
create_table()

# Generate CSV and load data into the database
generate_csv()
load_csv_to_db()
