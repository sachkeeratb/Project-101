import dropbox
import os

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token
        
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

    for root, dirs, fils in os.walk(file_from):
        relative_path = os.path.relpath(local_path, file_from)
        dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, 'rb') as f:
            dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('owerwrite'))

def main():
    access_token = 'sl.A5-1GVHaPvgKporc_zaOIq89Tnr8ok0mDwnpQ5Bx8xYS-6TCAwoTgG8bBkz7xzKQZZdJTKFJddP_YDig_inb6qWxPNwU9Mu68g2zP8qXFscueofZ5G6y2q8I8rjTjKrNd3jiwyE'
    transferData = TransferData(access_token)

    file_from = "Dropbox/photo"
    file_to = "Dropbox/Documents"

    transferData.upload_file(file_from, file_to)
    print("File has been moved.")

main()
