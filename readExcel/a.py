# -*- coding: utf-8 -*-
import xlrd
import xlwt
import numpy as np
from xlutils.copy import copy


def read_excel():
    f = xlrd.open_workbook('test.xls')
    # print(f.sheet_names())
    sheet = f.sheet_by_name('Sheet1')
    rows_num = sheet.nrows
    cols_num = sheet.ncols
    # rows = sheet.row_values(rows_num-1)    # 第三行内容
    # cols = sheet.col_values(cols_num-1)    # 第二列内容
    # print cols, rows
    # print(sheet.cell(1, 0).value.encode('utf-8'))
    # print(sheet.cell_value(1, 1).encode('utf-8'))
    # print(sheet.row(2)[3].value.encode('utf-8'))
    # print(sheet.cell(1, 4).ctype)
    ar = []
    for i in range(rows_num):
        for j in range(cols_num):
            ar.append(sheet.cell_value(i, j))
    n = np.array(ar)
    m = n.reshape(rows_num, cols_num)
    return m


def write_excel(item, name):
    if type(item) is not np.ndarray:
        return False
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('Sheet 1')
    sh = item.shape
    for i in range(sh[0]-1, -1, -1):
        worksheet.write(sh[0]-i-1, 0, label=item[i])
    workbook.save(name)


if __name__ == '__main__':
    d = ["Activity Log_details", "Payment Processing Visual Que", "Same day order visualization", "Home", "Forced Exit", "Associate Comments-v2", "Assets - colored icons - v2", "Location scan error ", "Dispensing - Reject bad scan", "Staging during picking - default container ", "Dispensing - happy path w check in ", "Dispensing - happy path_V2", "Staging to an existing location", " Staging (scan/manually enter) ", "Staging during picking ", "Dispensing - check in alert - no associate action", "Assets - colored icons (MVP)", "Add Container Label", "Dispensing - check in alert log ", "Dispensing - Member ID Other_V2", "Dispense - rejected item_V2", "Dispense complete - pre paid_V2", "Dispensing - restricted Items", "Pick - Add additional container + Move item + Default container ", "Staging - Add additional container + Move item", "Container management ", "Dispense Complete Modals ", "Dispense - rejected item cancel order ", "Dispensing - check in alert", "Dispense complete - pre paid - added item", "Dispense complete - post paid + added items ", "Dispense complete - post paid", "Nil pick item _ V2", "Picking from Item detail screen", "Three Dot Drop Down_V2", "Picking from item list", "Weighted item - over or under weight", "Weighted item ", "Dispensing - happy path 01", "Staging ", "Wrong Item picked", "Nil pick item ", "Add item V2", "Item Detail Screens", "Dispense - rejected item ", "Order detail - member inforamtion", "Order detail - member information", "Dispensing - Member ID Other", "Edit item", "Dispense complete - pre paid", "Associate logout", "Not Adding Container Label", "Three Dot Drop Down", "End pick walk ", "Container header states", "Add item ", "App Icon", "Cancel order", "Order detail ", "Artboard", "Dispensing - end dispense", "Staging - exit stage", "Order detail V3 ", "Assets - colored icons", "Dispensing - happy path", "Colors", "Edit item V2", "Order review ", "Partial pick", "Picking from item list V3", "Wrong Item picked _ V3", "Add Container Label  V2", "Refine V3", "UI explorations", "Picking from Item detail screen V2", "Cancel order_ V2", "Associate Comments", "Activity log", "Orders  V3", "Pick walk complete ", "Wrong Item picked _ V2", "Search V3", "Picking from item list - V2", "Progress indicator"]

    d_np = np.array(d)
    print(d_np)
    write_excel(d_np, 'QuickPick.xls')
    # f = xlrd.open_workbook('test.xls')
    # new_f = copy(f)
    # sheet = new_f.get_sheet('Sheet1')
    # sheet.write(3, 4, 'hello')
    # sheet.write(4, 4, 'world')
    # new_f.save('test.xls')


