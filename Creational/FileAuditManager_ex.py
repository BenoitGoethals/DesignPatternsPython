import threading
from abc import ABCMeta
from datetime import datetime


class FileAuditManager:
    _instance = {}
    lock = threading.Lock()

    def __init__(self, path: str | None = None):
        if not hasattr(self, 'path'):
            self.path = path

    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if cls not in cls._instance:
                cls._instance[cls] = super().__new__(cls)
            return cls._instance[cls]
 
        
    def audit(self,action:str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.path,"a") as f:
            f.write(f"{timestamp} {action}\n")
            
            
FileAuditManager(path="audit.log").audit("Test audit")
FileAuditManager().audit("Test audit 2")

            
            

        
        