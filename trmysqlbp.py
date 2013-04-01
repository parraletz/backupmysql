import argparse
import os
import subprocess
from datetime import date
import gzip


parser = argparse.ArgumentParser(description="Realiza respaldo completo de la base de datos MySQL", version="trBackup 1.0")
parser.add_argument( '-d','--database', dest='database', help='Nombre de la base de datos' )
parser.add_argument( '-u','--username', dest='username', help='Usuario de base de datos')
parser.add_argument( '-p','--password', dest='password',  help='Password')
parser.add_argument( '-t','--tea', dest='tea',  help='Nombre de la TEA ')
args = parser.parse_args()

database = args.database
username = args.username
password = args.password
tea = args.tea

fecha = date.today()
hoy= fecha.strftime("%d%m%Y")
filename = database + '_' + hoy + '_BACKUP.sql'

class Backup():

	def MakeDump():
		
		outputfile = open('/backups/db/'+filename, 'w')
		subprocess.Popen(['mysqldump', '-u'+username, '-p'+password, '--single-transaction', '--opt', database], stdout=outputfile)
		outputfile.close()


	def makeGzip():
		f_in = open('/backups/db/'+filename, 'rb')
		f_out = gzip.open('/backups/db/'+filename+'.gz','wb')
		f_out.writelines(f_in)
		f_out.close()
		f_in.close()


	def sendMail():
	    sendmail_location = "/usr/sbin/sendmail" 
	    p = os.popen("%s -t" % sendmail_location, "w")
	    p.write("From: %s\n" % "parra@tralix.com")
	    p.write("To: %s\n" % "soporte@tralix.com")
	    p.write("Subject: Se ha creado el respaldo de la base de datos de la TEA " + tea + " del dia " + hoy + "\n")
	    p.write("\n") 
	    p.write("Se ha creado correctamente el respaldo de la base de datos " + database + "correspondiente al dia " + hoy + "el archivo se encuentra en la ruta " + filename )
	    status = p.close()
	    if status != 0:
	           print "Sendmail exit status", status


	MakeDump()
	makeGzip()
	sendMail()