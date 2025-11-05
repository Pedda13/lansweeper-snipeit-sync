

![status](https://img.shields.io/badge/status-work_in_progress-orange?style=for-the-badge)



# Lansweeper → Snipe-IT Sync (On-Prem to On-Prem)

A modular Python library and sync engine that pulls assets from a **Lansweeper On-Premise SQL database** and synchronizes selected devices (typically laptops via OU filters) into **Snipe-IT On-Premise**.

This tool is for teams that use:

- **Lansweeper** as the operational scanning & software inventory source  
- **Snipe-IT** as the ownership & lifecycle platform  
- **Python** as the integration layer

> **Scope:** We intentionally sync **end-user devices (laptops/PCs)**. Servers/VMs/network gear are kept in Lansweeper only. Installed software is exported as **text** to the asset; license management can remain in Lansweeper.

---

## ✨ Features

- **OU-based filtering** (e.g. only laptops in specific OUs)
- **Idempotent upsert** via **serial number** (create/update)
- **MAC address aggregation** (LAN/WLAN; multiple adapters)
- **Config-based field mapping** (no code changes required)
- **Installed software → text** on the asset (simple, low-maintenance)
- **Dry-run mode** and request throttling
- **Modular architecture**: datasource → filters → mapper → target
- Ready to extend (warranty, custom fields, compliance, alerts)

---

## 🧩 Requirements

- Python **3.10+**
- Microsoft **ODBC Driver 17/18 for SQL Server**
- Access to:
  - Lansweeper SQL (`lansweeperdb`) **read-only**
  - Snipe-IT API (token with hardware read/write)
- Network: SQL port (1433 or custom), HTTPS to Snipe-IT

Install dependencies:

```bash
pip install -r requirements.txt
```

Minimal `requirements.txt`:

```
pyodbc
requests
toml
```

---

## 🔧 Configuration

Copy the example config and adjust it to your environment:

```bash
cp examples/config.example.toml config.toml
```

**`examples/config.example.toml`**
```toml
[lansweeper]
connection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=YOUR-SERVER;DATABASE=lansweeperdb;UID=sqluser;PWD=sqlpassword;Encrypt=no"

[snipeit]
base_url   = "https://snipe-it.local"
token      = "YOUR_SNIPEIT_API_TOKEN"
verify_ssl = false
dry_run    = true
delay      = 0.2

[filter]
allowed_ous = ["OU=Laptops,DC=corp,DC=local"]

[mapping]
name         = "AssetName"
serial       = "SerialNumber"
asset_tag    = "AssetTag"
manufacturer = "Manufacturer"
model        = "Model"
notes        = "IPAddress"
mac_addresses = "MacAddress"
```

---

## 🚀 Usage

Dry-run:

```bash
python -m ls_snipe_sync --config config.toml --dry-run
```

Full sync:

```bash
python -m ls_snipe_sync --config config.toml
```

---

## 📁 Project Structure

```
src/
  ls_snipe_sync/
    core/
    datasources/
    targets/
    utils/
examples/
tests/
README.md
LICENSE
pyproject.toml
```

---

## 🧪 Testing

```bash
pytest -v
```

---

## 🛠️ Roadmap

- [ ] Installed software aggregation → asset notes/custom field  
- [ ] Snipe-IT lookups/caches  
- [ ] Robust retries & error classification  
- [ ] Rotating logs & metrics  
- [ ] Warranty sync  
- [ ] CLI subcommands  
- [ ] Dockerfile

---

## 🤝 Contributing

Contributions are welcome.  
Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines before opening issues or pull requests.


---

## 📄 License

MIT License
