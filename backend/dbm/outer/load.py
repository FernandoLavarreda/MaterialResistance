# Fernando Lavarreda
# Read beams and materials from files

import openpyxl as xl

def read_xlsx(loctation:str, sheet:str, rows:list, columns:dict):
    wb = xl.load_workbook(loctation, True)
    file_sheet = wb[sheet]
    for row in rows:
        pass
    
