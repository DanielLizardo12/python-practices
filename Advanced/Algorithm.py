import codecs
# import sys
#
# sys.setdefaultencoding("utf-8")

print("Bienvenido al convertidor de datos a continuación se muestran las siguientes opciones del sistema")
print("---------------------------------------------------------------------------------------------------------------------")
print("| [asentamiento] Permite convertir datos a insertar en la tabla asentamiento                                        |")
print("| [localidad] Permite convertir datos a insertar en la tabla localidad                                              |")
print("| [seguira] Permite convertir datos a insertar en la tabla asentamiento sin la sentencia inicial de la insercion    |")
print("| [seguirl] Permite convertir datos a insertar en la tabla localidad sin la sentencia inicial de la insercion       |")
print("| Para que el programa funcione correctamente se debe insertar maximo 200 registros                                 |")
print("| Para que el programa funcione correctamente todos los datos deben tener un espacio antes y despues de cada dato   |")
print("| Y los datos deben estar separados por comas                                                                       |")
print("| Los datos se reciven así: 320580019 , Santa María De La Paz , El Zapotito , Rural                                 |")
print("| y se retornan así: insert into localidad values(320580019,"Santa María De La Paz","El Zapotito","Rural")          |")
print("---------------------------------------------------------------------------------------------------------------------")
print("Se recomenda el uso de esta herrramienta en linea para el separado de datos de excel: ")
print("https://www.textfixer.com/tools/remove-line-breaks.php")
print("")
tabla = input("Nombre de la tabla a la cual se le insertarán los datos: ").lower()
datos = input("Datos: ")



def loopit(cadena):
    resultado = []
    for item in cadena.split(","):
        resultado.append(item)

    return resultado

# print(cadena)

consulta = "insert into " + tabla + " values"

def cortar(dato):
    nuevo_dato = dato.split(" ")
    nuevo_dato.pop(0)
    nuevo_dato.pop(-1)
    cadena = ""

    for item in nuevo_dato:
        cadena = cadena + item + " "

    nueva_cadena = cadena[:len(cadena) -1]
    return nueva_cadena


def inserta_asentamiento(consulta):
    cadena = loopit(datos)
    while len(cadena) > 0:
        consulta = consulta + "(" + cadena[0].split(" ")[1] + ","
        consulta = consulta + '"' + cortar(cadena[1]) + '",'
        consulta = consulta + '"' + cortar(cadena[2]) + '",'
        consulta = consulta + '"' + cortar(cadena[3]) + '",'
        consulta = consulta +  cadena[4].split(" ")[1] + '),'
        cadena.pop(0)
        cadena.pop(0)
        cadena.pop(0)
        cadena.pop(0)
        cadena.pop(0)
    return consulta[:len(consulta) -1]


def inserta_localidad(consulta):
    cadena = loopit(datos)
    while len(cadena) > 0:
        consulta = consulta + "(" + cadena[0].split(" ")[1] + ","
        consulta = consulta + '"' + cortar(cadena[1]) + '",'
        consulta = consulta + '"' + cortar(cadena[2]) + '",'
        consulta = consulta + '"' + cortar(cadena[3]) + '"),'
        cadena.pop(0)
        cadena.pop(0)
        cadena.pop(0)
        cadena.pop(0)
    return consulta[:len(consulta) -1]


def crear_archivo(texto):
    f = codecs.open('consulta.txt','w', 'UTF-8')
    f.write(str(texto))
    f.close()

if tabla == "asentamiento":
    crear_archivo(inserta_asentamiento(consulta))
elif tabla == "localidad":
    crear_archivo(inserta_localidad(consulta))
elif tabla == "seguirl":
    crear_archivo(inserta_localidad(""))
elif tabla == "seguira":
    crear_archivo(inserta_asentamiento(""))
else:
    print("Esa Tabla no existe en el sistema!!")
