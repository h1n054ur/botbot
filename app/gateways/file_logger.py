import json

class FileLogger:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def log(self, record: dict):
        with open(self.filepath, "a") as f:
            f.write(json.dumps(record) + "\n")
