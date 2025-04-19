import psycopg2
import re

# Connect to the database
def connect_to_db():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="0507",
        host="localhost",
        port="5432"
    )

# 1. Search by pattern
def search_by_pattern(pattern):
    conn = connect_to_db()
    cur = conn.cursor()

    query = """
    SELECT * FROM phonebook
    WHERE first_name ILIKE %s OR last_name ILIKE %s OR phone_number LIKE %s
    """
    cur.execute(query, (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 2. Insert or update a user
def insert_or_update_user(first_name, last_name, phone_number):
    conn = connect_to_db()
    cur = conn.cursor()

    # Check if the phone number already exists
    cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone_number,))
    exists = cur.fetchone()

    if exists:
        cur.execute("""
            UPDATE phonebook
            SET first_name = %s, last_name = %s
            WHERE phone_number = %s
        """, (first_name, last_name, phone_number))
    else:
        cur.execute("""
            INSERT INTO phonebook (first_name, last_name, phone_number)
            VALUES (%s, %s, %s)
        """, (first_name, last_name, phone_number))

    conn.commit()
    cur.close()
    conn.close()

# 3. Insert multiple users with phone validation
def insert_many_users(users):
    conn = connect_to_db()
    cur = conn.cursor()

    incorrect = []
    phone_pattern = re.compile(r'^\+?\d{7,15}$')  # Basic phone number pattern

    for user in users:
        fname, lname, phone = user
        if not phone_pattern.match(phone):
            incorrect.append(user)
            continue
        try:
            cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
            if cur.fetchone():
                cur.execute("""
                    UPDATE phonebook
                    SET first_name = %s, last_name = %s
                    WHERE phone_number = %s
                """, (fname, lname, phone))
            else:
                cur.execute("""
                    INSERT INTO phonebook (first_name, last_name, phone_number)
                    VALUES (%s, %s, %s)
                """, (fname, lname, phone))
        except Exception as e:
            print(f"Error for {user}: {e}")
            incorrect.append(user)

    conn.commit()
    cur.close()
    conn.close()

    return incorrect  # Return invalid entries

# 4. Pagination
def get_paginated(limit, offset):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM phonebook
        LIMIT %s OFFSET %s
    """, (limit, offset))

    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 5. Delete by name or phone number
def delete_user(value):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("""
        DELETE FROM phonebook
        WHERE first_name = %s OR last_name = %s OR phone_number = %s
    """, (value, value, value))

    conn.commit()
    cur.close()
    conn.close()

# Menu
def main():
    while True:
        print("\n1. Search by pattern")
        print("2. Add or update user")
        print("3. Bulk insert users")
        print("4. Get paginated data")
        print("5. Delete user by name/phone")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            pattern = input("Enter search pattern: ")
            results = search_by_pattern(pattern)
            if results:
                for r in results:
                    print(r)
            else:
                print("No records found.")

        elif choice == '2':
            fname = input("First name: ")
            lname = input("Last name: ")
            phone = input("Phone number: ")
            insert_or_update_user(fname, lname, phone)
            print("Done!")

        elif choice == '3':
            try:
                n = int(input("How many users to add? "))
                users = []
                for i in range(n):
                    print(f"\nUser {i+1}:")
                    fname = input("  First name: ")
                    lname = input("  Last name: ")
                    phone = input("  Phone number: ")
                    users.append((fname, lname, phone))
                incorrect = insert_many_users(users)
                if incorrect:
                    print("Invalid data (not added):")
                    for u in incorrect:
                        print(u)
                else:
                    print("All users added successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '4':
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            results = get_paginated(limit, offset)
            for r in results:
                print(r)

        elif choice == '5':
            value = input("Enter first name, last name or phone number to delete: ")
            delete_user(value)
            print("User(s) deleted.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
