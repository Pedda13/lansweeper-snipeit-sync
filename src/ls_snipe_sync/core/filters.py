class OUFilter:
def __init__(self, allowed_ous: list[str]):
self.allowed = [ou.lower() for ou in allowed_ous]


def match(self, asset: dict) -> bool:
ou = (asset.get("OU") or "").lower()
return any(ou.startswith(a) for a in self.allowed)
