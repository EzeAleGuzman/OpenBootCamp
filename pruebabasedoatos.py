import sqlite3

conn= sqlite3.connect('ejerciciosbasedatos.db')



conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Mario', 'Garcia')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('ezequiel', 'Guzman')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Micaela', 'Romero')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('jorge', 'Aguirre')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Gaston', 'Edul')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('MAria', 'Olivera')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Martin', 'isas')")
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES ('Juan', 'Lopez')")

conn.commit



buscado = 'ezequiel'
cursor = conn.execute("SELECT id, nombre, apellido FROM Alumnos WHERE nombre=?", (buscado,))
alumno = cursor.fetchone()
if alumno:
    print(f"El alumno con nombre {buscado} tiene el ID {alumno[0]} y su apellido es {alumno[2]}.")
else:
    print(f"No se encontró ningún alumno con el nombre {buscado}.")
conn.close