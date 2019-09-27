import os
import json

items_info = {'weight': [[477417, '21848000000', 'BD CHED4YRRESVCHUNK', '18/RW', 55, 'item_qty', 'EACH', 'Q', 9.98, 0, 9.98, 'Y', 'Y', 2, ''], [980140087, '22087300000', 'WHOLE BONELESS HAM', '712LBAVERAGE', 55, 'item_qty', 'EACH', 'Q', 2.98, 0, 2.98, 'Y', 'Y', 12, '']], 'amb': [[475326, '04900005846', 'COKE', '35/12OZCANS', 55, 'item_qty', 'EACH', 'Q', 12.1, 0, 12.1, 'Y', 'Y', 0, ''], [476704, '07800002170', 'DR PEPPER', '35/12OZCANS', 55, 'item_qty', 'EACH', 'Q', 12.1, 0, 12.1, 'Y', 'Y', 0, ''], [127733, '08526479012', 'JUMBO ICED HONEY BUN', '12/475OZ', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'Y', 0, ''], [980002151, '07874223394', 'MM WATER 45/16.9 OZ', '45/169OZ', 55, 'item_qty', 'EACH', 'Q', 3.44, 0, 3.44, 'Y', 'Y', 0, ''], [710500, '08526477050', 'CHERRY CHEESE DANISH', '12CT425OZ', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'Y', 0, ''], [845706, '08526479160', 'CREAM CHEESE DANISH', '12/4OZ', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'Y', 0, ''], [781149, '01200010010', 'PEPSI', '36/12OZCANS', 55, 'item_qty', 'EACH', 'Q', 9.98, 0, 9.98, 'Y', 'Y', 0, ''], [320930, '07800005210', 'A&amp;W ROOT BEER', '24/12OZCANS', 55, 'item_qty', 'EACH', 'Q', 6.48, 0, 6.48, 'Y', 'Y', 0, ''], [856858, '03800025919', 'STRAW PTART 18-2PKS', '182PKS', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'Y', 0, ''], [781184, '01200010049', 'MOUNTAIN DEW', '36/12OZCANS', 55, 'item_qty', 'EACH', 'Q', 9.98, 0, 9.98, 'Y', 'Y', 0, ''], [762043, '08526479002', 'BIG TEXAS CINNAMON', 'ROLL12CT48OZ', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'Y', 0, '']], 'frz': [[980094746, '07874226641', 'MM ORG TRIPLE BERRY', 'FIRESTONE', 55, 'item_qty', 'EACH', 'Q', 8.98, 0, 8.98, 'Y', 'N', 0, ''], [980094744, '07874226639', 'MM ORG BLUEBERRIES', 'FIRESTONE', 55, 'item_qty', 'EACH', 'Q', 8.98, 0, 8.98, 'Y', 'N', 0, ''], [980085888, '07120213719', 'SWEET CHERRIES', 'DOLE', 55, 'item_qty', 'EACH', 'Q', 8.48, 0, 8.48, 'Y', 'N', 0, ''], [980094609, '07874226638', 'MM ORG MANGO CHUNKS', 'FIRESTONE', 55, 'item_qty', 'EACH', 'Q', 7.98, 0, 7.98, 'Y', 'N', 0, ''], [78016, '01312008566', 'ORE-IDA TATER TOTS', '8LB', 55, 'item_qty', 'EACH', 'Q', 7.28, 0, 7.28, 'Y', 'N', 0, '']], 'chl': [[980133247, '01786980715', 'PANINO STICKS', 'FIORUCCI', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'N', 0, ''], [489811, '04610030224', 'LIGHT STRING 28 CT', '13125LB', 55, 'item_qty', 'EACH', 'Q', 7.98, 0, 7.98, 'Y', 'N', 0, ''], [534517, '07874216027', 'WHOLE MILK', '1GALLON', 55, 'item_qty', 'EACH', 'Q', 3.08, 0, 3.08, 'Y', 'N', 0, ''], [286560, '07342000110', 'SOUR CREAM', '5LB', 55, 'item_qty', 'EACH', 'Q', 6.98, 0, 6.98, 'Y', 'N', 0, ''], [372235, '07283000602', 'SHARP CHEDDAR CHEESE', '25LB', 55, 'item_qty', 'EACH', 'Q', 9.98, 0, 9.98, 'Y', 'N', 0, ''], [372221, '07283000613', 'PEPPER JACK CHEESE', '25LB', 55, 'item_qty', 'EACH', 'Q', 8.48, 0, 8.48, 'Y', 'N', 0, ''], [831428, '07874210444', 'SALTED BTR SOLIDS', '41LB', 55, 'item_qty', 'EACH', 'Q', 11.88, 0, 11.88, 'Y', 'N', 0, ''], [831421, '07874210442', 'SALTED BUTTER QTRS', '41LB', 55, 'item_qty', 'EACH', 'Q', 11.98, 0, 11.98, 'Y', 'N', 0, ''], [284479, '71575610026', 'BLACKBERRIES', '18OZ', 55, 'item_qty', 'EACH', 'Q', 7.98, 0, 7.98, 'Y', 'N', 0, ''], [749972, '01715620006', 'STRAWBERRIES 2LB', 'STRAWBERRIES2LB', 55, 'item_qty', 'EACH', 'Q', 4.98, 0, 4.98, 'Y', 'N', 0, '']]}


for item in items_info:
    print('{}:{}'.format(item, len(items_info.get(item))))


def get_order_data():
    file_path = 'order_detail.json'
    with open(file_path, 'r') as f:
        data = json.load(f)

    order_lines = data.get('orderLines')
    for line in order_lines:
        product_type = line.get('productType')
        if product_type == 'AMBIENT' and line.get('orderByWeightInd') == 'N' \
                and line.get('sellByWeightInd') == 'N':
            items = items_info.get('amb')
        if product_type == 'CHILLED' and line.get('orderByWeightInd') == 'N' \
                and line.get('sellByWeightInd') == 'N':
            items = items_info.get('chl')
        if product_type == 'FROZEN' and line.get('orderByWeightInd') == 'N' \
                and line.get('sellByWeightInd') == 'N':
            items = items_info.get('frz')
        if line.get('sellByWeightInd') == 'Y':
            items = items_info.get('weight')
        item = [line.get('orderItemNbr'),
                line.get('orderGtin')[2:-1],
                line.get('itemDesc1'),
                line.get('itemDesc2'),
                55,
                "item_qty",
                'EACH',
                'N',
                'Q',
                line.get('unitRetailAmt'),
                0,
                line.get('unitRetailAmt'),
                'Y',
                'N' if line.get('sellByWeightInd') == 'N' else 'Y',
                0 if line.get('maxUnitWeightAmt') is None else line.get('maxUnitWeightAmt'),
                '']
        if item not in items and len(items) < 10:
            items.append(item)
    print(items_info)


if __name__ == "__main__":
    get_order_data()

    for item in items_info:
        print('{}:{}'.format(item, len(items_info.get(item))))