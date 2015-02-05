dns-cloud-zone
==============

Create DNS zone files (bind acceptable) from a Google Spreadsheet, using Python and gspread.

Requirements:
- Python (2.6+ or 3+)
- [gspread library](https://github.com/burnash/gspread)

Use:
- Authenticate through the command line or by typing your email address and password directly in the code (see comments inside "generateZone.py").
- Pick the name of the document using its title, and the sheet.
- A "zone.txt" file will be created based on the format of [this sheet](https://docs.google.com/a/ciscofederal.net/spreadsheets/d/1aaECBBJ9KnZqEGpQZ7X1umabGPURU4nEzjTrQcKmLSM/edit#gid=0)
