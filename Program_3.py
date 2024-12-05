import sqlite3


def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Phones table.
    add_phones_table(cur)

    # Add rows to the Phones table.
    add_phones(cur)

    # Displays the phone list
    display_phones(cur)

    # Commit the changes.
    conn.commit()

    # Close the connection.
    conn.close()



# The add_phones_table function adds the Phones table to the database.
def add_phones_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS PhoneN')

    # Create the table.
    cur.execute('''CREATE TABLE PhoneN (
                    PhoneID INTEGER PRIMARY KEY NOT NULL,
                    Username TEXT,
                    Phone_number REAL)''')


# The add_phones function adds rows to the Phones table.
def add_phones(cur):
    user_phone = [(1, "Steve boy", "612-446-9924"),
                  (2, "Steve Jobs", "612-473-4784"),
                  (3, "Micheal Bay", "612-383-9834"),
                  (4, "Steve Carrel", "612-585-3947")]  # list of tuples

    for row in user_phone:
        cur.execute('''INSERT INTO PhoneN (PhoneID, Username, Phone_number)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

def display_phones(cur):
    print('Contents of phonebook.db/PhoneN table:')
    cur.execute('SELECT * FROM PhoneN')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]}')


if __name__ == "__main__":
    main()
