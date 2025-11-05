import pyodbc


class LansweeperSQL:
def __init__(self, connection_string: str):
self.connection_string = connection_string


def _connect(self):
return pyodbc.connect(self.connection_string)


def fetch_assets(self):
query = """
SELECT
a.AssetID,
a.AssetName,
a.IPAddress,
ad.OU,
cs.SerialNumber,
cs.Manufacturer,
cs.Model,
mac.MacAddress
FROM tblAssets a
LEFT JOIN tblComputersystem cs ON a.AssetID = cs.AssetID
LEFT JOIN tblADComputers ad ON a.AssetID = ad.AssetID
LEFT JOIN tblNetwork n ON a.AssetID = n.AssetID
LEFT JOIN tblMacAddress mac ON n.NetworkID = mac.NetworkID
"""


with self._connect() as conn:
cursor = conn.cursor()
rows = cursor.execute(query).fetchall()


columns = [column[0] for column in cursor.description]


return [dict(zip(columns, row)) for row in rows]
