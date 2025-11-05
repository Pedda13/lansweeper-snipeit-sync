from ls_snipe_sync.config import Config
from ls_snipe_sync.core.filters import OUFilter
from ls_snipe_sync.core.mapper import Mapper
from ls_snipe_sync.core.sync_engine import SyncEngine
from ls_snipe_sync.datasources.lansweeper_sql import LansweeperSQL
from ls_snipe_sync.targets.snipeit_api import SnipeItAPI


cfg = Config("config.example.toml")


ds = LansweeperSQL(cfg.get("lansweeper", "connection_string"))
target = SnipeItAPI(cfg.get("snipeit", "base_url"), cfg.get("snipeit", "token"))
mapper = Mapper(cfg.data.get("mapping"))
filter_ou = OUFilter(cfg.data["filter"]["allowed_ous"])


engine = SyncEngine(ds, target, mapper, filter_ou, dry
