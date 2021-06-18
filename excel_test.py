import xlrd
from datetime import date,datetime
tables = []
def read_excel():
    workbook = xlrd.open_workbook(r'/Users/echo/Desktop/618福袋活动实物发货-20200618-1.xlsx',encoding_override='utf-8')
    sheet = workbook.sheet_by_index(0)
    for rown in range(sheet.nrows):
        array = {'userId':'','kuaidi':'','logisticsOrder':''}
        array['userId'] = sheet.cell_value(rown,5)
        array['kuaidi'] = sheet.cell_value(rown,11)
        array['logisticsOrder'] = sheet.cell_value(rown,12)
        tables.append(array)
    print (tables)


if __name__ == "__main__":
    read_excel()