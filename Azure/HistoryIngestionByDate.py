# REQUIREMENTS
#! pip install azure-mgmt-resource
#! pip install azure-mgmt-datalake-store
#! pip install azure-datalake-store

from azure.datalake.store import core, lib, multithread
import os
import fnmatch
import zipfile

tenant_id = "XXXXXXXXXXXXXXXX"
store_name = "DATALAKE"
token = lib.auth(tenant_id, username=None, password=None, client_id='XXXXXXXXXXXXXXXXXXXX',
client_secret = "XXXXXXXXXXXXXXXXXXXX=", resource='https://management.core.windows.net/',
                 require_2fa=False, authority=None)
adl = core.AzureDLFileSystem(token, store_name=store_name)

LOCAL_PATH = "\\PROD\\Shared\\Archives\\"
UNZIPPED_PATH = "C:\\Unzippedfiles\\"
INGESTION_DATALAKE_PATH = '/RAW/'
TARGETED_ZIP_FILE = 'prediction*.zip'
TARGETED_FILE = 'Detailed.csv'


def upload_one_shot():
	for dirName in os.listdir(LOCAL_PATH):
		partionnedDirName = dirName[:4] + '/' + dirName[4:]
		partionnedDirName = partionnedDirName[:7] + '/' + partionnedDirName[7:]
		print(partionnedDirName)
		adl.mkdir(INGESTION_DATALAKE_PATH + partionnedDirName)
		for filename in os.listdir(LOCAL_PATH + dirName):
			if fnmatch.fnmatch(filename, TARGETED_ZIP_FILE):
				zipFileRef = zipfile.ZipFile(LOCAL_PATH + dirName + "\\" + filename)
				CSVFilePath = zipFileRef.extract( TARGETED_FILE,UNZIPPED_PATH)
				multithread.ADLUploader(adl, lpath=CSVFilePath, rpath=INGESTION_DATALAKE_PATH + partionnedDirName, overwrite=True)
				os.remove(UNZIPPED_PATH + TARGETED_FILE)
				print('ingesting successful of : ' + partionnedDirName)

upload_one_shot()
