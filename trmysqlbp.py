import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description="Realiza respaldo completo de la base de datos TEA", version="trBackup 1.0")
parser.add_argument( '-d','--database', dest='database', help='Nombre de la base de datos' )
parser.add_argument( '-u','--username', dest='username', help='Usuario de base de datos')
parser.add_argument( '-p','--password', dest='password',  help='Password')
args = parser.parse_args()


database = args.database
username = args.username
password = args.password




def MakeDump():
	def __init__():
		pass
	print username + " " + database + " " + password



