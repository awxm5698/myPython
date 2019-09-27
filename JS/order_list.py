import datetime

order_list = {"statusCode":0,"statusDesc":"Successfully processed","tenantId":1,"countryCode":"US","ebuNbr":4969,"data":{"searchText":"stage","pageNbr":1,"pageSize":10,"totalOrderCnt":7,"orders":[{"oid":230998,"programTypeCd":10,"programType":"CPU","orderStatusCd":10,"orderStatus":"PICK-RDY-MIN","membershipNbr":"10134100011112222","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070209519","srcFulfillOid":"001","qtyOrdered":1,"qtyRemaining":1,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-03 09:00:00 -05:00","pickDueTs":"2019-07-03 08:30:00 -05:00","exceptions":[],"prepaidInd":False},{"oid":231017,"programTypeCd":10,"programType":"CPU","orderStatusCd":11,"orderStatus":"PICK-RDY-OPT","membershipNbr":"10134100011116666","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070209598","srcFulfillOid":"001","qtyOrdered":1,"qtyRemaining":1,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-03 09:00:00 -05:00","pickDueTs":"2019-07-03 08:30:00 -05:00","exceptions":[],"prepaidInd":False},{"oid":222208,"programTypeCd":10,"programType":"CPU","orderStatusCd":11,"orderStatus":"PICK-RDY-OPT","membershipNbr":"10134100011116666","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070203973","srcFulfillOid":"001","qtyOrdered":1,"qtyRemaining":1,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-03 11:00:00 -05:00","pickDueTs":"2019-07-03 10:30:00 -05:00","exceptions":[],"prepaidInd":False},{"oid":235562,"programTypeCd":10,"programType":"CPU","orderStatusCd":11,"orderStatus":"PICK-RDY-OPT","membershipNbr":"10134100011116666","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070213881","srcFulfillOid":"001","qtyOrdered":2,"qtyRemaining":2,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-03 13:00:00 -05:00","pickDueTs":"2019-07-03 12:30:00 -05:00","exceptions":[],"prepaidInd":False},{"oid":235639,"programTypeCd":10,"programType":"CPU","orderStatusCd":10,"orderStatus":"PICK-RDY-MIN","membershipNbr":"10134100011116666","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070213927","srcFulfillOid":"001","qtyOrdered":1,"qtyRemaining":1,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-03 13:00:00 -05:00","pickDueTs":"2019-07-03 12:30:00 -05:00","exceptions":[],"prepaidInd":False},{"oid":279502,"programTypeCd":10,"programType":"CPU","orderStatusCd":11,"orderStatus":"PICK-RDY-OPT","membershipNbr":"10134100011116666","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070410101","srcFulfillOid":"001","qtyOrdered":2,"qtyRemaining":2,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-05 10:00:00 -05:00","pickDueTs":"2019-07-05 09:30:00 -05:00","exceptions":[],"prepaidInd":False},{"oid":279515,"programTypeCd":10,"programType":"CPU","orderStatusCd":11,"orderStatus":"PICK-RDY-OPT","membershipNbr":"10134100011112222","custFirstName":"stage","custLastName":"automation","srcCustOid":"90070410143","srcFulfillOid":"001","qtyOrdered":1,"qtyRemaining":1,"qtyPicked":0,"pickingUserDisplay":[],"packingUserDisplay":[],"dispenseUserDisplay":[],"orderDueTs":"2019-07-05 10:00:00 -05:00","pickDueTs":"2019-07-05 09:30:00 -05:00","exceptions":[],"prepaidInd":False}]}}


def get_date(order_data):
    order_data = order_data[0:-7]
    d = datetime.datetime.strptime(order_data, '%Y-%m-%d %H:%M:%S')
    d0 = d.strftime('%Y-%m-%d')
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    tomorrow = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    if d0 == today:
        d1 = 'Today'
    elif d0 == tomorrow:
        d1 = 'Tomorrow'
    else:
        d1 = d.strftime('%a %b %d,')
    d2 = d.strftime('%I:%M %p').lower()
    return '{} {}'.format(d1,d2)


def print_order_list():
    count = order_list.get('data').get('totalOrderCnt')
    print('{} {}'.format(count,'result' if count <= 1 else 'results'))
    orders = order_list.get('data').get('orders')
    print('='*40)
    for order in orders:
        customer_name = '{} {}'.format(order.get('custFirstName').upper(),
                                       order.get('custLastName').upper())
        show_date = get_date(order.get('orderDueTs'))
        line = """{} {}
Order {}
@ {} # {}{}""".format(customer_name.ljust(20, ' '),
                      show_date,
                      order.get('srcCustOid'),
                      order.get('qtyOrdered'),
                      str(order.get('qtyPicked')).ljust(28, ' '),
                      '' if len(order.get('pickingUserDisplay')) == 0 else order.get('pickingUserDisplay')[0])
        print(line)
        print('-'*40)


print_order_list()

