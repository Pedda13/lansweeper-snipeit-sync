class Mapper:
def __init__(self, mapping: dict):
self.mapping = mapping


def map_asset(self, ls_asset: dict) -> dict:
"""
Convert a Lansweeper asset dict → Snipe-IT format.
"""
payload = {}


for target_field, source_key in self.mapping.items():
payload[target_field] = ls_asset.get(source_key)


return payload
