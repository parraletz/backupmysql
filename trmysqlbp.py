import argparse
import os
import subprocess
from datetime import date
import time
import gzip
import logging

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


### Configuracion de logs
logger = logging.getLogger('trbackup')
hdlr = logging.FileHandler('/var/log/'+tea+'_trbackup'+hoy+'.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


def MakeDump():
	
	logger.info('Se comienza con el backup de la base de datos ' + database + 'de la ' + tea )
	try:
		outputfile = open('/backups/db/'+filename, 'w') # Crea el archivo donde se volcara la base de datos 
		try:
			if tea == 'tea601':
				subprocess.Popen(['/usr/local/mysql/bin/mysqldump', '-u'+username, '-p'+password, '--single-transaction', '--ignore-table=TEA.SUBSCRIBERS_MARKETING_20_8_9', database], stdout=outputfile) 
			else :
				subprocess.Popen(['/usr/local/mysql/bin/mysqldump', '-u'+username, '-p'+password, '--single-transaction', database], stdout=outputfile) # Se crear el dump
		except OSError:
			logger.error("El comando no existe en el sistema operativo y/o no esta en la ruta correcta, favor de verificar")
		outputfile.close()
	except:
		logger.error('No fue posible crear el archivo donde se volcara la base de datos, favor de verificar que el directorio no sea de solo lectura')

	time.sleep(15)

	f_in = open('/backups/db/'+filename, 'rb')# Se crea el archivo comprimido
	f_out = gzip.open('/backups/db/'+filename+'.gz','wb')
	f_out.writelines(f_in)
	f_out.close()
	f_in.close()

	logger.info('Se ha terminado satisfactoriamente el respaldo de la base de datos el archivo se encuentra en /backups/db/'+filename)

MakeDump()
