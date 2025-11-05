# Lansweeper → Snipe-IT Sync (On-Prem to On-Prem)

A modular Python library and sync engine that automatically pulls assets from a **Lansweeper On-Premise SQL database** and synchronizes selected devices (typically laptops via OU filters) into **Snipe-IT On-Premise**.

This tool is designed for organizations that use:

✅ Lansweeper as their operational scanning and software inventory source  
✅ Snipe-IT as their asset ownership & lifecycle platform  
✅ Python as the integration layer  

---

## ✨ Features

- OU-based filtering (e.g. only laptops in specific OUs)
- Serial-number–based detection (create/update)
- MAC address aggregation (LAN/WLAN)
- Config-based field mapping
- Installed software export as text field
- Dry-run mode
- Modular architecture: datasource → mapper → filters → target
- Extendable (license reporting, compliance, custom fields)

---

## 📦 Installation

```bash
pip install -r requirements.txt
