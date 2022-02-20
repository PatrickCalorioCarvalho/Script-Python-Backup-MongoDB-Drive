from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import datetime
gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 
Database = "Burger"
NomeArquivo = Database +"-"+datetime.datetime.now().strftime("%d-%m-%Y") +".gz"
LocalArquivo  = '"'+os.getcwd() + "/" + NomeArquivo+'"'
os.system('mongodump --db '+ Database +' --gzip --archive >'+LocalArquivo+'')
gfile = drive.CreateFile({'parents': [{'id': 'COLOQUE_AQUI_SEU_FOLDERID'}]})
gfile.SetContentFile(NomeArquivo)
gfile.Upload()
os.system('rm '+LocalArquivo)