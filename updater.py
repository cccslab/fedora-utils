import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

if __name__ == "__main__":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    dfile = drive.CreateFile({'id': '0B7Q6q7xIVnQUZVhWY3RZeFNaR2s'})
    dfile.GetContentFile('fedora_updater.py')
    os.system('python fedora_updater.py')
    os.system('rm fedora_updater.py')
