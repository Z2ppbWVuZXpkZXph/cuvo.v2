#MODULOS
import os, sys, time
from random import *

def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def valletta(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)

#COLORES

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado


os.system("clear")

#---> INTERFAZ PRINECIPAL

corrida(GG+"\n       00000000            00         00        ")
corrida(GG+"      oo                   00         00        ")
corrida(GG+"     00          99    99   00       00   99999      ")
corrida(GG+"     00          99    99    00     00   pp   pp   ")
corrida(GG+"      oo         99    99     00   00    pp   pp   ")
corrida(GG+"       00000090   000000       00000      99999     ")
valletta(M+"                                                 VALLETTA\n")

#---> SALUDO

saludo(B+" Hola! Soy CuVo, tu asistente ¿Que es lo que necesitas?")

#---> M E N U - P R I N C I P A L <----

print (GG+"\n      1" + GL+")" + Y+" MENSAJE PARA GIFT CARDS")
print (GG+"      2" + GL+")" + Y+" SALIR\n")
respuesta = int(input(RR+"Elige una respuesta: " +WW))

# ============ OPCION 1 ==============

# - Preguntas -
if respuesta == 1:
	nombre = input(CC+"\n ¿Cual es el nombre de la victima? " +WW)
	dni = input(CC+" ¿Cual es el DNI de la victima? " +WW)
	ruc = input(CC+" ¿Cual es el RUC de la victima? " +WW)
	domicilio = input(CC+" ¿Cual es el domicilio de la victima? " +WW)

	sutil(B+"\n El mensaje fue creado!")

	os.system("sleep 1")

# ++- Mensaje -++

	print (W+"\n" + nombre + ", tenemos información personal suya, y tenemos la posibilidad de exponerlas si no hace caso a mis peticiones, solicito que usted compre una Gift Card de Google y me haga entrega del código, caso contrario, sus datos y sus cuentas serán hackeadas, expuestas y publicadas\n")

	os.system("sleep 1")

# ____ DNI ____

	if dni == "nose":
		os.system("sleep 0")

	else:
		print (G+" DNI " + R+"= " + Y+dni)

# ___ RUC ____

	if ruc == "nose":
		os.system("sleep 0")

	else:
		print (G+" RUC " + R+"= " + Y+ruc)

# ___ DOMICILIO ___

	if domicilio == "nose":
		os.system("sleep 0")

	else:
		print (G+" DOMICILIO " + R+"= " + Y+domicilio)

# <-- COMPILACION DE DATOS -->

	nombreA = ("Nombres de la Victima: " + nombre)
	dniA = ("DNI de la victima: " + dni)
	rucA = ("RUC de la victima: " + ruc)

# ___ Crear Archivo ___

	os.system("sleep 1")

	sutil(B+"\n Logre recopilar la informacion que colocaste.")
	sutil(B+" Quieres que lo ponga en un archivo para que no lo pierdas?\n")

	os.system("sleep 1")

	print (GG+"      1" + GL+")" + Y+" Si")
	print (GG+"      2" + GL+")" + Y+" No\n")

	respuesta2 = input(RR+"Elige una Opcion: " +WW)

# ___ Archivo ___

	if dni == "nose":
		dni = "nulo"
	else:
		("sleep 0")


	if ruc == "nose":
		ruc = "nulo"
	else:
		("sleep 0")




	if respuesta2 == "1":
		os.system("sleep 1")
		proceso(Y+"\n   CREANDO ARCHIVO...")

		os.system("sleep 1")

		archivo = open("archivo.txt","w")
		proceso(Y+"\n   COLOCANDO LOS DATOS...")

		archivo = open("archivo.txt","a")
		archivo.write("DATOS DE RECOPILACION\n")
		archivo.write("\n" + nombreA)
		archivo.write("\n" + dniA)
		archivo.write("\n" + rucA)

		sutil(B+"\n En donde quieres guardar el archivo?")

		os.system("sleep 1")

		print (GG+"\n       1" + GL+") " + Y+"Ruta actual")
		print (GG+"       2" + GL+") " + Y+"Crear Carpeta victimas")
		print (GG+"       3" + GL+") " + Y+"Crear carpeta personalizada")
		print (GG+"       4" + GL+") " + Y+"Omitir\n")

		respuesta3 = input(R+"Elige una opcion: " +WW)
		os.system("sleep 1")

# _________ RUTA ACTUAL _________

		if respuesta3 == "1":
			sutil(B+"\n El archivo esta listo.")
			sutil(B+" Si quieres verlo esta en tu ruta actual\n")

# __________ CREAR CARPETA VICTIMAS __________

		elif respuesta3 == "2":
			proceso(Y+"\n   CREANDO CARPETA NUEVA...")
			os.system("mkdir victimas")
			proceso(Y+"\n   MOVIENDO ARCHIVO...")
			os.system("mv archivo.txt /data/data/com.termux/files/home/cuvo/victimas")

			sutil(B+"\n El archivo esta listo.")
			sutil(B+" Si quieres verlo esta en la carpeta victimas\n")

# __________ CREAR CARPETA PERSONALIZADA _____________

		elif respuesta3 == "3":
			sutil(B+"\n Que nombre le quieres poner a la nueva carpeta")
			respuesta4 = input(R+"\nColoca un nombre: " +WW)
			proceso(Y+"\n CREANDO CARPETA " + respuesta4 + "...")
			os.system("mkdir " + respuesta4)
			proceso("\n MOVIENDO ARCHIVO...")
			os.system("mv archivo.txt /data/data/com.termux/files/home/cuvo/" + respuesta4)

			sutil(B+"\n El archivo esta listo.")
			sutil(B+" Si quieres verlo esta en la carpeta " + respuesta4 + "\n")

# __________ OMITIR __________

		elif respuesta3 == "4":
			sutil(B+"\n Lo guardare en una ruta aleatoria")

			aleatorio = ["actual","victimas"]
			indice = randrange(len(aleatorio))
			final = aleatorio[indice]

			if final == "actual":
				sutil(B+"\n El archivo esta listo.")
				sutil(B+" Lo coloque en tu ruta actual\n")

			elif final == "victimas":
				os.system("mkdir victimas")
				os.system("mv archivo.txt /data/data/com.termux/files/home/cuvo/victimas")
				sutil(B+"\n El archivo esta listo.")
				sutil(B+" Lo coloque en una nueva carpeta victimas\n")

# ____ OPCION NEGATIVA ____

	elif respuesta2 == "2":
		sutil(B+"SALIENNDO DEL PROGRAMA...")
		os.system("clear")

# ===============> OPCION 2 <=================

elif respuesta == 2:

# -- SALIDA --

	print ("Saliendo")
	os.system("clear")
	os.system("figlet VALLETTA")

# -- RESPUESTA INCORRECTA --

else:
	print ("ok")
	os.system("clear")

sutil(M+"   REGRESA PRONTO!\n" +WW)
