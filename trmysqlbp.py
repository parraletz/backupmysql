import argparse
import os
import subprocess
from datetime import date

parser = argparse.ArgumentParser(description="Realiza respaldo completo de la base de datos MySQL", version="trBackup 1.0")
parser.add_argument( '-d','--database', dest='database', help='Nombre de la base de datos' )
parser.add_argument( '-u','--username', dest='username', help='Usuario de base de datos')
parser.add_argument( '-p','--password', dest='password',  help='Password')
parser.add_argument( '-m', '--host', dest='host', help='Hostname')
args = parser.parse_args()


database = args.database
username = args.username
password = args.password


outputfile = open('/backups/'+database+'-BACKUP.sql', 'w')
 
subprocess.Popen(['mysqldump', '-uUSERNAME', '-pPASSWORD', '--single-transaction', '--opt', database], stdout=outputfile)
 
outputfile.close()