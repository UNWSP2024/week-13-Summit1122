# Program 2 "Data Base Caller"
# By: Luis Amador
# 12/2/24

def display_cities(cur):
    print('Contents of cities.db/Cities table:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')


if __name__ == '__main__':
    import sqlite3
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    display_cities(cur)
    conn.close()