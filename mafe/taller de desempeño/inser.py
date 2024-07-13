import mysql.connector
user = 'root'
password = ''
host = 'localhost'
database = 'inventario'

idproducto= 1111,
nombre= " arroz diana"
catidad = 12
precio =2000



try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    cursor = conexion.cursor()


    insert_query = """INSERT INTO productos (idproducto, nombre, catidad, precio )
                      VALUES (%s, %s, %s, %s)"""

    in_data = (idproducto, nombre, catidad, precio)

    cursor.execute(insert_query, in_data)


    conexion.commit()

    print("producto guardado correctamente.")

except mysql.connector.Error as error:
    print("Error al insertar el nuevo proudcto:", error)

finally:
    if 'conexion' in locals() or 'conexion' in globals():
        conexion.close()

