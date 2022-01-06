from datetime import datetime
import openpyxl as xl


def main():
    wb = xl.load_workbook('PhoneData.xlsx')
    sheet = wb['Sheet1']

    date = str(sheet.cell(2, 4).value)
    correct_date = date[0:10]
    print(correct_date)

    today_date = f"{datetime.now().year}-0{datetime.now().month}-0{datetime.now().day}"
    print(today_date)
    if today_date == correct_date:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
