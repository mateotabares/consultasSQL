import mysql.connector
from tabulate import tabulate


def mostrar_tabla(cursor):
    # Visualizar las tablas en un formato mas atractivo incluyendo el titulo de las mismas
    nombrescolumnas = [i[0] for i in cursor.description]
    res = cursor.fetchall()
    print(tabulate(res, headers=nombrescolumnas, tablefmt='psql'))


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySQL",
        database="prueba"
    )
    my_cursor = mydb.cursor(buffered=True)
except:
    print("La conexion con la base de datos no fue exitosa")

while mydb.is_connected():
    try:
        eleccion = str(input(
            'Elige 1 si quieres conocer la poblacion de un pais \n Elige 2 si quieres conocer la poblacion de un '
            'estado \n Elige 3 si quieres conocer la poblacion por ciudad \n'))
        if eleccion not in ('1', '2', '3'):
            raise Exception
    except:
        print("Al parecer el valor que ingresaste no es valido. Intenta de nuevo \n \n")
        continue

    if eleccion == '1':

        pais = str(input('Ingresa el nombre del pais que quieres consultar \n'))
        query = "SELECT DISTINCT tp.state,tp.city,tp.population FROM tabla_poblacion tp WHERE tp.country = '{}' ".format(
            pais)
        my_cursor.execute(query)

        if my_cursor.rowcount:
            print(
                "Has escogido {}. Este pais cuenta con una poblacion distribuida de la siguiente forma: ".format(pais))
            mostrar_tabla(my_cursor)
        else:
            print("No se han encontrado resultados para el pais {}. Comprueba que esta bien escrito".format(pais))
        break

    if eleccion == '2':
        estado = str(input('Ingresa el nombre del estado que quieres consultar \n'))
        query = "SELECT DISTINCT tp.city,tp.population FROM tabla_poblacion tp WHERE tp.state = '{}' ".format(estado)
        my_cursor.execute(query)
        if my_cursor.rowcount:
            print("Has escogido {}. Este estado cuenta con una poblacion distribuida de la siguiente forma: ".format(
                estado))
            mostrar_tabla(my_cursor)
        else:
            print("No se han encontrado resultados para el estado {}. Comprueba que esta bien escrito".format(estado))
        break

    if eleccion == '3':
        ciudad = str(input('Ingresa el nombre de la ciudad que quieres consultar \n'))
        query = "SELECT DISTINCT tp.city, tp.population FROM tabla_poblacion tp WHERE tp.city = '{}' ".format(ciudad)
        my_cursor.execute(query)
        if my_cursor.rowcount:
            print("Has escogido {}. Esta ciudad cuenta con una poblacion distribuida de la siguiente forma: ".format(
                ciudad))
            mostrar_tabla(my_cursor)
        else:
            print("No se han encontrado resultados para la ciudad {}. Comprueba que esta bien escrito".format(ciudad))
        break

if mydb.is_connected():  # Si la conexion fue exitosa, se cierra la conexion antes de terminar.
    mydb.close()
