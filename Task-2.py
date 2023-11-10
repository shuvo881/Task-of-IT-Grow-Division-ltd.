import psycopg2

# Connection parameters
database_name = "university"
user = "shuvo"
password = "root"
host = "127.0.0.1"
port = "5432"  # Default PostgreSQL port

# Connect to the PostgreSQL database
conn = None # it is connection variable
try:
    conn = psycopg2.connect(
        database=database_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()
    
    
    # Create the students table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            age INTEGER NOT NULL,
            major VARCHAR(100) NOT NULL
        )
    ''')

    # Function to add a student to the database
    def add_student(first_name, last_name, age, major):
        cursor.execute('INSERT INTO students (first_name, last_name, age, major) VALUES (%s, %s, %s, %s)',
                    (first_name, last_name, age, major))
        conn.commit()
        print(f"Student {first_name} {last_name} added to the database.")

    # Function to retrieve all students from the database
    def get_all_students():
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        for student in students:
            print(student)

    # Function to update student information in the database
    def update_student(student_id, first_name, last_name, age, major):
        cursor.execute('UPDATE students SET first_name=%s, last_name=%s, age=%s, major=%s WHERE student_id=%s',
                    (first_name, last_name, age, major, student_id))
        conn.commit()
        print(f"Student with ID {student_id} updated.")

    # Function to delete a student from the database
    def delete_student(student_id):
        cursor.execute('DELETE FROM students WHERE student_id=%s', (student_id,))
        conn.commit()
        print(f"Student with ID {student_id} deleted.")

    # Example Usage
    add_student("Md.", "shuvo", 27, "CSE")
    add_student("Md.", "Sumon", 22, "ME")
    get_all_students() # print/retrieving all student info from the table

    update_student(1, "Md. Shuvo", "Mia", 21, "CS")
    get_all_students() # print all student info from the table

    delete_student(2)
    get_all_students() # print/retrieving all student info from the table


except psycopg2.Error as e:
    print(f"Unable to connect to the database: {e}")

finally:
    # Close the connection in a finally block to ensure it gets closed even if an exception occurs
    if conn:
        conn.close()
        print("Connection closed.")