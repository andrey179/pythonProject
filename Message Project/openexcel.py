from datetime import datetime
import openpyxl as xl

def main():
    wb = xl.load_workbook('PhoneData.xlsx')
    sheet = wb['Sheet1']
    # open workbook
    for row in range(2, sheet.max_row + 1):

        cell = sheet.cell(row, 2)
        phone_num = "+972"
        phone_num += str(cell.value)
        print(phone_num)

        cell = sheet.cell(row, 3)
        message = cell.value
        print(message)

        last_sent = sheet.cell(row, 6)
        print_date = f"{datetime.now().day}/{datetime.now().month}-{datetime.now().hour}:{datetime.now().minute}"
        last_sent.value = print_date
        print(last_sent.value)

    # save
    wb.save('PhoneData.xlsx')


if __name__ == '__main__':
    main()
