#!/usr/bin/python3

from colorama import *
import subprocess
import sys
import os
import time
from pwn import *
import signal


# Variables
estado = "echo $?"
comando= "/usr/bin/ssh-keygen"
init()

def logo():

	print (Fore.LIGHTRED_EX+"    ______           __                   ____  _____ ___ ")
	print ("   / ____/_  _______/ /_____  _____      / __ \/ ___//   |")
	print ("  / /_  / / / / ___/ //_/ _ \/ ___/_____/ /_/ /\__ \/ /| |")
	print (" / __/ / /_/ / /__/ ,< /  __/ /  /_____/ _, _/___/ / ___ |")
	print ("/_/    \__,_/\___/_/|_|\___/_/        /_/ |_|/____/_/  |_|\n"+Fore.RESET)
	print (Fore.LIGHTCYAN_EX+"            [--Programado-por-BLY-]\n")
	print (Fore.LIGHTYELLOW_EX+"          Twitter: @bertrandlorent")
	print (Fore.LIGHTMAGENTA_EX+":)"+Fore.RESET)
	print ("----------------------------------------------------------")



def handler(signal,frame):
	print (Fore.LIGHTBLUE_EX+"[!] Saliendo...")
	exit(1)

signal.signal(signal.SIGINT, handler)

def uso():
	logo()
	print ("\n[!] USO: ./FuckerRSA.py id_rsa diccionario.txt")



def hack():

	if len(sys.argv) == 3:
		id_rsa = sys.argv[1]
		wordlist = sys.argv[2]

		#print (id_rsa + ' ' + wordlist)

		global test

		f = open(wordlist,"r")
		progreso=log.progress("Aplicando fuerza bruta\n")
		time.sleep(1)

		try:

			for word in f:

				test= (comando + ' -y -f ' + id_rsa + ' -P ' + word + '>/dev/null 2>&1')
				e=test.replace("\n"," ")
				resultado = os.system(e)
				#print(resultado)
				progreso.status("Intentando -> "+ word)

				if resultado == 0:
					progreso.success("La contraseña ha sido encontrada -> "+Fore.RED+word)
					break

			if resultado == 65280:
				progreso.failure("La contraseña no ha sido encontrada")


		except:

			pass
			exit(1)

	else:
		uso()

if __name__ == '__main__':

	logo()
	hack()
