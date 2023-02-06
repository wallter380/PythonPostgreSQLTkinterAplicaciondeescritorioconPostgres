
from tkinter import Canvas, Frame, Tk, Label, W, E, Entry, Button, Listbox, END

from psycopg2 import connect

def save_new_user(name, lastname, age, nationality, dni):

    conn = connect(
        dbname="postgres",
        user="postgres",
        password="contrasena",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    query = ''' INSERT INTO users(name, lastname, age, nationality, dni) VALUES ( %s, %s, %s, %s, %s) '''

    cursor.execute(query, (name, lastname, age, nationality, dni))

    print("User Saved")

    conn.commit()

    conn.close()

    # Mostrar nuevo usuario

    mostrar_user()


def mostrar_user():

    conn = connect(
        dbname="postgres",
        user="postgres",
        password="contrasena",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    query = ''' SELECT * FROM users '''

    cursor.execute(query)

    row = cursor.fetchall()

    listbox = Listbox(frame, width=20, height=5)

    listbox.grid(row=14, columnspan=6, sticky=W+E)

    for x in row:

        listbox.insert(END, x)

    conn.commit()

    conn.close()


def search(id):

    conn = connect(
        dbname="postgres",
        user="postgres",
        password="contrasena",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    query = ''' SELECT * FROM users WHERE id= %s '''

    cursor.execute(query, id)

    row = cursor.fetchone()

    print(row)

    conn.commit()

    conn.close()


def delete_user(id):

    conn = connect(
        dbname="postgres",
        user="postgres",
        password="contrasena",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    query = ''' DELETE  FROM users WHERE id= %s '''

    cursor.execute(query, id)

    print("User delete")

    conn.commit()

    conn.close()

root = Tk()

root.title("Python and PostgreSQL")

# Canvas

canvas = Canvas(root, height=400, width=500)

canvas.pack()

frame = Frame()

frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Create User

label = Label(frame, text='Add user')

label.grid(row=0, column=3)

# Name Input

label = Label(frame, text='Name')

label.grid(row=2, column=0)

entry_name = Entry(frame)

entry_name.grid(row=2, column=2)

# LastName Input

label = Label(frame, text='LastName')

label.grid(row=3, column=0)

entry_lastname = Entry(frame)

entry_lastname.grid(row=3, column=2)

# Age Input

label = Label(frame, text='Age')

label.grid(row=4, column=0)

entry_age = Entry(frame)

entry_age.grid(row=4, column=2)

# Nationality Input

label = Label(frame, text='Nationality')

label.grid(row=5, column=0)

entry_nationality = Entry(frame)

entry_nationality.grid(row=5, column=2)

# DNI Input

label = Label(frame, text='DNI')

label.grid(row=6, column=0)

entry_dni = Entry(frame)

entry_dni.grid(row=6, column=2)

# Creando boton para agregar

button = Button(frame, text="Add User", command=lambda: save_new_user(

    entry_name.get(),
    entry_lastname.get(),
    entry_age.get(),
    entry_nationality.get(),
    entry_dni.get()
))

button.grid(row=8, column=5, sticky=W + E)

# Search

label = Label(frame, text="Search User")

label.grid(row=9, column=3)

label = Label(frame, text="Search by ID")

label.grid(row=10, column=0)

id_search = Entry(frame)

id_search.grid(row=10, column=1)

button = Button(frame, text="Search", command=lambda: search(id_search.get()))
button.grid(row=10, column=2)

# Delete

label = Label(frame, text="Delete User")

label.grid(row=12, column=3)

label = Label(frame, text="Delete by ID")

label.grid(row=13, column=0)

id_delete = Entry(frame)

id_delete.grid(row=13, column=1)

button = Button(frame, text="Delete", command=lambda: delete_user(id_delete.get()))
button.grid(row=13, column=2)

mostrar_user()

root.mainloop()
