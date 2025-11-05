import requests


class SnipeItAPI:
def __init__(self, base_url: str, token: str):
self.url = base_url.rstrip("/")
self.token = token
self.headers = {"Authorization": f"Bearer {self.token}"}


def upsert_asset(self, payload: dict):
print("[SYNC] Would send to Snipe-IT:", payload)
# API interaction TODO
