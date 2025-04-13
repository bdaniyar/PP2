import psycopg2
import csv

# Connect to the database
def connect_to_db():
    return psycopg2.connect(
        dbname="phonebook_db",  # Database name
        user="postgres",        # Username
        password="0507",        # Password
        host="localhost",       # Host
        port="5432"             # Port
    )

# Create the table
def create_table():
    conn = connect_to_db()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            phone_number VARCHAR(15) UNIQUE
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Table created!")

# Insert data from a CSV file
def insert_from_csv():
    conn = connect_to_db()
    cur = conn.cursor()
    
    with open('phonebook.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            cur.execute("""
                INSERT INTO phonebook (first_name, last_name, phone_number)
                VALUES (%s, %s, %s)
            """, (row[0], row[1], row[2]))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data loaded from CSV!")

# Insert data manually through the console
def insert_manually():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone_number = input("Enter phone number: ")

    conn = connect_to_db()
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO phonebook (first_name, last_name, phone_number)
        VALUES (%s, %s, %s)
    """, (first_name, last_name, phone_number))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data inserted!")

# Query data
def query_data():
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name, phone_number FROM phonebook")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    cur.close()
    conn.close()

# Update data
def update_data():
    name_to_update = input("Enter the first name of the user to update: ")
    new_phone_number = input("Enter the new phone number: ")

    conn = connect_to_db()
    cur = conn.cursor()
    
    cur.execute("""
        UPDATE phonebook
        SET phone_number = %s
        WHERE first_name = %s
    """, (new_phone_number, name_to_update))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data updated!")

# Delete data
def delete_data():
    name_to_delete = input("Enter the first name of the user to delete: ")

    conn = connect_to_db()
    cur = conn.cursor()
    
    cur.execute("""
        DELETE FROM phonebook
        WHERE first_name = %s
    """, (name_to_delete,))
    
    conn.commit()
    cur.close()
    conn.close()
    print("Data deleted!")

# Main menu
def main():
    print("1. Create table")
    print("2. Insert data from CSV")
    print("3. Insert data manually")
    print("4. Query data")
    print("5. Update data")
    print("6. Delete data")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        create_table()
    elif choice == '2':
        insert_from_csv()
    elif choice == '3':
        insert_manually()
    elif choice == '4':
        query_data()
    elif choice == '5':
        update_data()
    elif choice == '6':
        delete_data()
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()
