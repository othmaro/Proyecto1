import sys
from math import pi
from numpy import *
import os
import time

IPC=[]
Mes=[]
Year=[]

def tabla(alist1,alist2,alist3):
	print "Los Datos Ingresados son:"
	for i in range(len(alist1)):
		print "\t"	+ alist1[i]	+ "\t" + alist2[i]	+ "\t\t" + alist3[i]

def tabla1(alist1,alist2,alist3):
	print "Los Datos Ordenados son:"
	for i in range(len(alist1)):
		print "\t"	+ alist1[i]	+ "\t" + alist2[i]	+ "\t\t" + alist3[i]	
		
def quicksort(lista1,izq,der,lista2,lista3):
	i=izq
	j=der
	x=lista1[(izq+der)/2]
	while (i<=j):
		while lista1[i]<x and j<=der:
			i=i+1
		while x<lista1[j] and j>izq:
			j=j-1
		if i<=j:
			aux=lista1[i]
			lista1[i]=lista1[j]
			lista1[j]=aux
			temp2=lista2[i]
			lista2[i]=lista2[j]
			lista2[j]=temp2
			temp3=lista3[i]
			lista3[i]=lista3[j]
			lista3[j]=temp3
			i=i+1
			j=j-1
		if izq<j:
			quicksort(lista1,izq,j,lista2,lista3)
		if i<der:
			quicksort(lista1,i,der,lista2,lista3)
	
def burbbleSort(lista1,lista2,lista3):
    for recorrido in range(1,len(lista1)):
        for posicion in range(len(lista1)-recorrido):
            if lista1[posicion]>lista1[posicion+1]:
                temp=lista1[posicion]
                lista1[posicion]=lista1[posicion+1]
                lista1[posicion+1]=temp
                temp2=lista2[posicion]
                lista2[posicion]=lista2[posicion+1]
                lista2[posicion+1]=temp2
                temp3=lista3[posicion]
                lista3[posicion]=lista3[posicion+1]
                lista3[posicion+1]=temp3
				
def mergeSort(alist1):
	if len(alist1)>1:
		mid=len(alist1)//2
		lefthalf1 = alist1[:mid]
		righthalf1 = alist1[mid:]
		
		mergeSort(lefthalf1)
		mergeSort(righthalf1)

		i=0
		j=0
		k=0
		while i<len(lefthalf1) and j<len(righthalf1):
			if lefthalf1[i]<righthalf1[j]:
				alist1[k]=lefthalf1[i]
				i=i+1
			else:
				alist1[k]=righthalf1[j]
				j=j+1
			k=k+1

		
		while i<len(lefthalf1):
			alist1[k]=lefthalf1[i]
			i=i+1
			k=k+1

		while j<len(righthalf1):
			alist1[k]=righthalf1[j]
			j=j+1
			k=k+1

def menu3():
	os.system('cls')
	print "\t\t\t1. BurbbleSort"
	print "\t\t\t2. MergeSort"
	print "\t\t\t3. QuickSort"
	opcion4=raw_input("Introdusca su opcion: ")
	while True:
		if opcion4=='1':
			burbbleSort(IPC1,Mes1,Year1)
			tabla1(Year1,Mes1,IPC1)
			break
		elif opcion4=='2':
			mergeSort(IPC)
			mostrarListas()
			break
		elif opcion4=='3':
			quicksort(IPC,0,len(IPC)-1,Mes,Year)
			tabla1(Year,Mes,IPC)
			break
		else:
			break
            
    
def ingresoManual(ipc, mes, anio):
	IPC.append(ipc)
	Mes.append(mes)
	Year.append(anio)
	
def cargaMasiva(ruta):
	archivo=open(ruta,'r')
	while True:
		linea = archivo.readline()
		if not linea:
			break
		else:
			arreglo=linea.split()
			ingresoManual(arreglo[2], arreglo[0], arreglo[1])
	os.system('cls')

def menu4():
	print "\t\t\tDesea eliminar algun dato de la lista"
	print "\t\t\t1. Si"
	print "\t\t\t2. No"
	opcion5=raw_input("Introduzca una opcion: ")
	while True:
		if opcion5=='1':
			borrarDato()
			os.system('cls')
			print "\t\t\tDesea eliminar algun dato de la lista"
			print "\t\t\t1. Si"
			print "\t\t\t2. No"
			opcion5=raw_input("Introduzca una opcion: ")
		elif opcion5=='2':
			break
		else:
			break
	
def borrarDato():
	k=input("Introduzca la posicion de la lista que desea eliminar, recuerde que la lista va de 0 a n-1: ")
	ipc1=IPC[k]
	mes1=Mes[k]
	year1=Year[k]
	IPC.remove(ipc1)
	Mes.remove(mes1)
	Year.remove(year1)

def menu2():
	os.system('cls')
	print "\t\t\t1. Ingresar Datos"
	print "\t\t\t2. Salir"
	opcion3=raw_input("Introduzca su opcion: ")
	while True:
		if opcion3=='1':
			ipc=input("Ingrese el IPC: ")
			mes= str( raw_input("Ingrese el mes: "))
			anio= input("Ingrese el anio: ")
			ingresoManual(ipc, mes, anio)
			os.system('cls')
			print "\t\t\tDesea ingresar mas datos"
			print "\t\t\t1. Si"
			print "\t\t\t2. No"
			opcion3=raw_input("Ingrese una opcion: ")
		elif opcion3=='2':
			break
		else:
			print "No existe esa opcion"
			break
	os.system('cls')

def mostrarListas():
	os.system('cls')
	longitud=len(IPC)
	for i in range(0,longitud):
		print ("Listado de datos ingresados#" + str(i+1))
		print "El IPC es: " + str(IPC[i])
		print "El mes es: " + str(Mes[i])
		print "El Anio es: " + str(Year[i])

def menu1():
	os.system('cls')
	print "\t\t\t1. Ingreso Manual"
	print "\t\t\t2. Carga Masiva"
	opcion2=raw_input("Introdusca su opcion: ")
	while True:
		if opcion2=='1':
			menu2()
			break
		elif opcion2=='2':
			cargaMasiva('C:\Python27\IPC1.mate.txt')
			break
		else:
			print "No procesable"
			break
def menu():
	os.system('cls')
	print "\t\t\t**************************"
	print "\t\t\t********** MENU **********"
	print "\t\t\t***** 1. Ingresar IPC ****" 
	print "\t\t\t***** 2. Mostrar IPC *****"
	print "\t\t\t***** 3. Ordenar IPC *****"
	print "\t\t\t******** 4. Salir ********"
	print "\t\t\t**************************"
	opcion1=raw_input("Introdusca su opcion: ")
	while True:
		if opcion1=='1':
			menu1()
			print "\t\t\t**************************"
			print "\t\t\t********** MENU **********"
			print "\t\t\t***** 1. Ingresar IPC ****" 
			print "\t\t\t***** 2. Mostrar IPC *****"
			print "\t\t\t***** 3. Ordenar IPC *****"
			print "\t\t\t******** 4. Salir ********"
			print "\t\t\t**************************"
			opcion1=raw_input("Introdusca su opcion: ")
		elif opcion1=='2':
			tabla(Year,Mes,IPC)
			menu4()
			os.system('cls')
			print "\t\t\t**************************"
			print "\t\t\t********** MENU **********"
			print "\t\t\t***** 1. Ingresar IPC ****" 
			print "\t\t\t***** 2. Mostrar IPC *****"
			print "\t\t\t***** 3. Ordenar IPC *****"
			print "\t\t\t******** 4. Salir ********"
			print "\t\t\t**************************"
			opcion1=raw_input("Introdusca su opcion: ")
		elif opcion1=='3':
			menu3()
			print "\t\t\t**************************"
			print "\t\t\t********** MENU **********"
			print "\t\t\t***** 1. Ingresar IPC ****" 
			print "\t\t\t***** 2. Mostrar IPC *****"
			print "\t\t\t***** 3. Ordenar IPC *****"
			print "\t\t\t******** 4. Salir ********"
			print "\t\t\t**************************"
			opcion1=raw_input("Introdusca su opcion: ")
		elif opcion1=='4':
			break
		else:
			os.system('cls')
			print "Opcion incorrecta"
			print "\t\t\t**************************"
			print "\t\t\t********** MENU **********"
			print "\t\t\t***** 1. Ingresar IPC ****" 
			print "\t\t\t***** 2. Mostrar IPC *****"
			print "\t\t\t***** 3. Ordenar IPC *****"
			print "\t\t\t******** 4. Salir ********"
			print "\t\t\t**************************"
			opcion1=raw_input("Introdusca su opcion: ")

menu()