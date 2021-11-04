#!/usr/bin/env python3
# -*- conding: utf-8 -*-
#################################################
# Autor: Perera Arturo                          #
# Version: 2.0                                  #
# Licencia: GPL                                 #
#################################################
import os
import subprocess
import time

print("\n")
print("Bienvenidos al modulo de prueba broker \n")
print("\n")

#Cambiar la variabre deacuerdo a nombre del broker.
os.environ['BROKER'] = 'BRKX001'


def menu():
    print("[1] Listar EG")
    print("[2] Cambiar JVM de EG en bytes, Min/Max")
    print("[3] Guardar Logs")
    print("[0] salir")


menu()
option = int(input("Selecione una opcion: "))
while option != 0:
    if option == 1:
          A = str(input("Escriba el EG a visualizar: \n"))
          subprocess.run(f"mqsireportproperties $BROKER -e {A} -o ComIbmJVMManager -r",shell=True)


    elif option == 2:

        B = str(input("Escriba el EG de la JVM a modificar: \n"))
        MA = int(input("Escriba el Max en bytes a modificar:  \n"))
        MI = int(input("Escriba el Min en byte a modificar: \n"))


        print("Inicio del cambio : %s" % time.ctime())
        print("\n")
        print("Cambiando El MaxHeapSize de EG_JVM... \n")

        subprocess.run(f"mqsichangeproperties $BROKER -e {B} -o ComIbmJVMManager -n jvmMaxHeapSize -v {MA}",shell=True)

        time.sleep(5)
        print("\n")
        print("Cambiando el MinHeapSize de EG-JVM... \n")

        subprocess.run(f"mqsichangeproperties $BROKER -e {B} -o ComIbmJVMManager -n jvmMinHeapSize -v {MI}",shell=True)

        time.sleep(5)
        print("\n")

        print("Cambio efectuado en el broker \n")
        print("\n")
        print("Bajando broker por favor espere \n")
        print("\n")
        subprocess.run("mqsistop -i $BROKER",shell=True)
        time.sleep(15)
        print("\n")
        subprocess.run("mqsilist -d1",shell=True)
        time.sleep(5)
        print("\n")
        print("iniciando broker \n")
        subprocess.run("mqsistart $BROKER",shell=True)
        time.sleep(5)
        print("\n")
        subprocess.run("mqsilist -d1",shell=True)
        print("Fin : %s" % time.ctime())


    elif option == 3:
        print("tomando Logs")
        subprocess.run("cat /var/log/message | grep error > error.log",shell=True)
        subprocess.run("cat /var/log/message | grep EG > eg.log",shell=True)
        subprocess.run(" cat /aplications/cyberbank/cmm-wmb/logs/BRK80001_workflow.log | grep error > Wkerror.log",shell=True)

    else:
        print("opcion invalida")


    print()
    menu()
    option = int(input("Selecciona una opcion: \n"))

print("\n")
print("Gracias vuelva pronto \n")
print("\n")