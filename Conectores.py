import mysql.connector # Importa el conector de MySQL

config = { # Configuración de la conexión
    'port': 3306, # Puerto de conexión
    'user': 'your_username', # Usuario de la base de datos
    'password': 'your_password', # Contraseña de la base de datos
    'host': 'localhost', # Host de la base de datos
    'database': 'your_database' # Nombre de la base de datos
}

connection = mysql.connector.connect(**config) # Establece la conexión a la base de datos
cursor = connection.cursor() # Crea un cursor para ejecutar consultas

query = "SELECT * FROM your_table" # Define la consulta SQL
cursor.execute(query) # Ejecuta la consulta
results = cursor.fetchall() # Obtiene todos los resultados de la consulta

for row in results: # Itera sobre los resultados
    print(row) # Imprime cada fila de resultados


cursor.close() # Cierra el cursor
connection.close() # Cierra la conexión a la base de datos

-------------------------------------------

import mysql.connector # Importa el conector de MySQL

def print_user(user): # Función para imprimir información del usuario
    print("ID:", user[0]) # ID del usuario
    print("Nombre:", user[1]) # Nombre del usuario
    print("Email:", user[2]) # Email del usuario
    print("-------------------")

config = { # Configuración de la conexión
    'port': 3306, # Puerto de conexión
    'user': 'your_username', # Usuario de la base de datos
    'password': 'your_password', # Contraseña de la base de datos
    'host': 'localhost', # Host de la base de datos
    'database': 'your_database' # Nombre de la base de datos
}

connection = mysql.connector.connect(**config) # Establece la conexión a la base de datos
cursor = connection.cursor() # Crea un cursor para ejecutar consultas

query = "SELECT * FROM users where name ='" + user + "';" # Define la consulta SQL
print(query) # Imprime la consulta para depuración
cursor.execute(query) # Ejecuta la consulta
results = cursor.fetchall() # Obtiene todos los resultados de la consulta

for row in results: # Itera sobre los resultados
    print(row) # Imprime cada fila de resultados


cursor.close() # Cierra el cursor
connection.close() # Cierra la conexión a la base de datos

print_user(" '; update users set email='brais_updated@example.com' where name='brais'; --") # Imprime la información del usuario "brais"