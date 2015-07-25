import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

if __name__ == "__main__":
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    ufile = drive.CreateFile({'id': '0B7Q6q7xIVnQUZVhWY3RZeFNaR2s'})
    ufile.SetContentFile('fedora_updater.py')
    ufile.Upload()
