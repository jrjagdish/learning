import requests
from base import BaseDownloader

class ImageDownloader(BaseDownloader):
    def download(self):
        response = requests.get(self._url)
        with open(self._save_path,'wb') as f:
            f.write(response.content)
        print("Image Downloaded:",self._save_path)

class TextDownloader(BaseDownloader):
    def download(self):
        response = requests.get(self._url)
        text = response.text
        with open(self._save_path,'w') as f:
            f.write(text) 
        print("Text file doenloaded:",self._save_path)           
