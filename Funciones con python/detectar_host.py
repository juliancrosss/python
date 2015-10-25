# -*- coding: utf-8 -*-
import os
import subprocess

DONT_OUTPUT = open(os.devnul, "w")

def ping(ip):
	response = subprocess.call(["ping", "-c", "2", ip], stdout=DONT_OUTPUT, stderr=subprocess.STDOUT)
	if response == 0:
		print("La Maquina esta respondiendo")
	else:
		print("La Maquina no esta respondiendo")

print("Digite la IP(Digite 'hecho' si no quiere conectarse)")

while True:
	ip = input("> ")

	if ip == 'hecho':
		break
	ping(ip)
		continue