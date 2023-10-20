#!/usr/bin/python3

x = ['NULL','START OF HEADING','START OF TEXT','END OF TEXT','END OF TRANSMISSION','ENQUIRY','ACKNOWLEDGE','BELL','BACKSPACE','HORIZONTAL TAB','LINE FEED','VERTICAL TAB','FORM FEED','CARRIAGE RETURN','SHIFT OUT','SHIFT IN','DATA LINK ESCAPE','DEVICE CONTROL 1','DEVICE CONTROL 2','DEVICE CONTROL 3','DEVICE CONTROL 4','NEGATIVE ACKNOWLEDGE','SYNCHRONOUS IDLE','END OF TRANS BLOCK','CANCEL','END OF MEDIUM','SUBSTITUTE','ESCAPE','FILE SEPARATOR','GROUP SEPARATOR','RECORD SEPARATOR','UNIT SEPARATOR']

def print_ascii_table_block(v):
    print(f"{v:>4}{hex(v)[2:]:>5}{chr(v):>4}|",end='')

def print_ascii_table():
    print(f"Dex Hex {'Chr':>20}| Dex Hex Chr | Dex Hex Chr | Dex Hex Chr |")
    for v1 in range(32):
        print(f"{v1:>3}{hex(v1)[2:]:>4}{x[v1]:>21}|",end='')
        print_ascii_table_block(v1+32)
        print_ascii_table_block(v1+64)
        print_ascii_table_block(v1+96)
        print()

print_ascii_table() 