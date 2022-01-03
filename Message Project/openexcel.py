from datetime import datetime
import openpyxl as xl


wb = xl.load_workbook('PhoneData.xlsx')
sheet = wb['Sheet1']

for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 2)
    phone_num = cell.value
    print(phone_num)
    last_sent = sheet.cell(row, 6)
    print_date = f"{datetime.now().day}/{datetime.now().month}-{datetime.now().hour}:{datetime.now().minute}"
    last_sent.value = print_date
    print(last_sent.value)

wb.save('PhoneData.xlsx')




