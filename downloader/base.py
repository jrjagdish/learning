from abc import ABC, abstractmethod

class BaseDownloader(ABC):
    def __init__(self,url,save_path):
        self._url = url
        self._save_path = save_path

    @abstractmethod
    def download(self):
        pass

    def __str__(self):
        return f"<downloader url = {self._url} -> save = {self._save_path}"
        
        