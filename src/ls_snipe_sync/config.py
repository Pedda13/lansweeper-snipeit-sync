import toml
from pathlib import Path


class Config:
def __init__(self, path: str):
self.path = Path(path)
self.data = toml.load(self.path)


def get(self, section: str, key: str, default=None):
return self.data.get(section, {}).get(key, default)
