import pandas as pd

print("This will overwrite existing CSVs with excel contents, breakout if not desired!")
input()

excel_file = 'all-mso-config.xlsx'
all_sheets = pd.read_excel(excel_file, sheet_name=None)
sheets = all_sheets.keys()

for sheet_name in sheets:
    sheet = pd.read_excel(excel_file, sheet_name=sheet_name)
    sheet.to_csv("mso-config/%s.csv" % sheet_name, index=False)
