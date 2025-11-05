class SyncEngine:
def __init__(self, datasource, target, mapper, ou_filter=None, dry_run=True):
self.datasource = datasource
self.target = target
self.mapper = mapper
self.ou_filter = ou_filter
self.dry_run = dry_run


def run(self):
assets = self.datasource.fetch_assets()


for asset in assets:
if self.ou_filter and not self.ou_filter.match(asset):
continue


payload = self.mapper.map_asset(asset)


if self.dry_run:
print("[DRY RUN] Would sync:", payload)
else:
self.target.upsert_asset(payload)
