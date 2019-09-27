data = {"orderId":150846,"tenantId":1,"countryCd":"US","fulfillEbuNbr":4969,"orderStatus":"AUTH","customerOrderId":"10070118576","fulfillOrderId":"001","orderInfo":{"orderType":"TEST-TRAIN","programType":"CPU","fulfillType":"IN-CLUB","packType":"NONE","dispenseType":"PICKUP","dispenseLocation":"IN-CLUB"},"ageRestrictions":{"ageRestrHandle":0,"ageRestrSellBy":0,"ageRestrPurchase":0},"paymentInfo":{"prepaidInd":"Y","pymntAuthInd":"Y"},"shippingInfo":{"packageAsn":None,"trackingNbr":None,"shipCarrier":None,"carrierServiceMethod":None},"cartInfo":{"prepaidCartId":"3013f152-cbd0-4a96-8b9a-6357c85d2d5d","postpaidCardId":"f25d4ba0-d93b-4bb5-84bf-fc2635ce3cb0","prepaidPairingId":"4005049698210070118576998","postpaidPairingId":"4005049698210070118576001"},"orderDueInfo":{"orderDueDt":"2019-07-02","slotStartTs":"2019-07-02 18:00:00 -05:00","slotEndTs":"2019-07-02 19:00:00 -05:00","orderDueTs":"2019-07-02 18:00:00 -05:00","pickDueTs":"2019-07-02 17:30:00 -05:00"},"customerInfo":{"membershipNbr":"10134100011116666","customerFirstName":"KELI","customerLastName":"HE","customerEmail":"xiujun.he@samsclub.com","customerPrimaryPhoneNbr":"(123)456-7890","customerAlternatePhoneNbr":"1234567890"},"alternatePickupPerson":[{"alternateFirstName":"Aor","alternateLastName":"HE"}],"memberComments":[{"commentText":"This is a testing pickup order"}],"associateComments":None,"currentlyAssigned":None,"orderLineSummary":{"orderLineCnt":3,"totalOrderedQty":17,"totalPickedQty":None,"totalRemainingQty":None,"totalPickedAsOrderedQty":None,"totalNilPickedQty":None,"totalAddedQty":None},
        "orderLines":[{"orderLineNbr":1,"orderItemNbr":773603,"orderGtin":"00017641994971","cartLineId":"276bf91a-f4c9-4666-82c1-6743344b85ba","productType":"FROZEN","tempBand":"FROZEN","locationSeqId":"10-13-ZZZZ-99-99-13","srcOrderLineNbr":1,"locZoneId":None,"locAisleId":None,"locSectionId":None,"productWebDesc":None,"itemDesc1":"INDUSTRIAL SHELVING","itemDesc2":"6POLYPROLENEINLAYS","itemDesc3":None,"ageRestrHandle":None,"ageRestrSellBy":None,"ageRestrPurchase":None,"allowSubstituteInd":"N","orderByWeightInd":"N","orderUom":"EA","orderQty":7,"orderWeightAmt":0.00,"sellByWeightInd":"N","sellUom":"EA","minUnitWeightAmt":None,"maxUnitWeightAmt":None,"unitRetailAmt":99.98,"alternateLocations":None,"orderLineItems":[{"itemSeqNbr":1,"itemNbr":773603,"gtin":"00017641994971"},{"itemSeqNbr":2,"itemNbr":773603,"gtin":"00017641984965"},{"itemSeqNbr":3,"itemNbr":773603,"gtin":"00078742057361"}],"pickSummary":None,"pickDetails":None},
                      {"orderLineNbr":2,"orderItemNbr":637127,"orderGtin":"00611269991246","cartLineId":"6320195f-8619-4356-b8cf-e0a0e7c20f8b","productType":"AMBIENT","tempBand":"AMBIENT","locationSeqId":"10-23-M000-03-09-45","srcOrderLineNbr":2,"locZoneId":"M","locAisleId":"3","locSectionId":"9","productWebDesc":None,"itemDesc1":"RED BULL","itemDesc2":"24/84OZCANS","itemDesc3":None,"ageRestrHandle":None,"ageRestrSellBy":None,"ageRestrPurchase":None,"allowSubstituteInd":"N","orderByWeightInd":"N","orderUom":"EA","orderQty":6,"orderWeightAmt":0.00,"sellByWeightInd":"N","sellUom":"EA","minUnitWeightAmt":None,"maxUnitWeightAmt":None,"unitRetailAmt":33.98,"alternateLocations":[{"locZoneId":"M","locAisleId":"3","locSectionId":"9"}],"orderLineItems":[{"itemSeqNbr":1,"itemNbr":637127,"gtin":"00611269991246"}],"pickSummary":None,"pickDetails":None},
                      {"orderLineNbr":3,"orderItemNbr":980002151,"orderGtin":"00078742233949","cartLineId":"d6a49b41-4d69-4b08-a21c-0ce6ff659d1e","productType":"CHILLED","tempBand":"CHILLED","locationSeqId":"10-24-M000-04-15-08","srcOrderLineNbr":3,"locZoneId":"M","locAisleId":"4","locSectionId":"15","productWebDesc":None,"itemDesc1":"MM WATER 45/16.9 OZ","itemDesc2":"45/169OZ","itemDesc3":None,"ageRestrHandle":None,"ageRestrSellBy":None,"ageRestrPurchase":None,"allowSubstituteInd":"N","orderByWeightInd":"N","orderUom":"EA","orderQty":4,"orderWeightAmt":0.00,"sellByWeightInd":"N","sellUom":"EA","minUnitWeightAmt":None,"maxUnitWeightAmt":None,"unitRetailAmt":3.36,"alternateLocations":[{"locZoneId":"M","locAisleId":"7","locSectionId":"3"},{"locZoneId":"M","locAisleId":"4","locSectionId":"15"},{"locZoneId":"M","locAisleId":"7","locSectionId":"5"},{"locZoneId":"M","locAisleId":"7","locSectionId":"1"}],"orderLineItems":[{"itemSeqNbr":1,"itemNbr":980002151,"gtin":"00078742233949"}],"pickSummary":None,"pickDetails":None}],
        "containerDetails":[{"containerId":"t1200","tempBand":"AMB","containerType":"TOTE","location":None,"locationType":None,"trackingNumber":None,"items":[{"lineId":1,"itemSeqNbr":1,"gtin":"00078742233949","quantity":1}]},
                            {"containerId":"t1201","tempBand":"CHL","containerType":"TOTE","location":None,"locationType":None,"trackingNumber":None,"items":[{"lineId":3,"itemSeqNbr":1,"gtin":"00078742233949","quantity":2}]}],
        "dispenseDetails": None}


orderLines = data.get('orderLines')
containers = data.get('containerDetails')
details = {'AMBIENT': [], 'CHILLED': [], 'FROZEN': []}
container_temp = {'AMB': 'AMBIENT', 'CHL': 'CHILLED', 'FRZ': 'FROZEN'}
for line in orderLines:
    temp_band = line.get('tempBand')
    print(temp_band)
    temp_band_detail = details[temp_band]
    if containers is None:
        line_item = {'container_id': None,
                     'gtin': line.get('orderGtin'),
                     'orderItemNbr': line.get('orderItemNbr'),
                     'itemDesc1': line.get('itemDesc1'),
                     'pickedQty': 0,
                     'orderQty': line.get('orderQty'),
                     'aisle': '',
                     'bin': ''}
        if line['alternateLocations'] is not None:
            line_item['aisle'] = line['alternateLocations'][0]['locAisleId']
            line_item['bin'] = line['alternateLocations'][0]['locZoneId']

        temp_band_detail.append(line_item)

    if containers is not None:
        for container in containers:
            short_container_temp_band = container.get('tempBand')
            temp_band_detail = details.get(container_temp.get(short_container_temp_band))
            items = container.get('items')
            line_item = {'container_id': None,
                         'gtin': line.get('orderGtin'),
                         'orderItemNbr': line.get('orderItemNbr'),
                         'itemDesc1': line.get('itemDesc1'),
                         'pickedQty': 0,
                         'orderQty': line.get('orderQty'),
                         'aisle': '',
                         'bin': ''}
            if line['alternateLocations'] is not None:
                line_item['aisle'] = line['alternateLocations'][0]['locAisleId']
                line_item['bin'] = line['alternateLocations'][0]['locZoneId']

            for item in items:
                if item.get('gtin') == line.get('orderGtin'):
                    line_item['container_id'] = container.get('containerId')
                    line_item['pickedQty'] = item.get('quantity')

            temp_band_detail.append(line_item)

print(details)
for detail in details:
    if len(details[detail]) != 0:
        temp_band_container = []
        items = details[detail]
        for item in items:
            if item.get('container_id') is not None:
                temp_band_container.append(item.get('container_id'))
        print(temp_band_container)
        if len(temp_band_container) > 1:
            container_title = []
            for container in temp_band_container:
                print('='*33)
                title = '{}    {}'.format(detail, container)
                if title not in container_title:
                    container_title.append(title)
                    print(title)
                print('='*33)
                for item in items:
                    if item.get('container_id') == container:
                        print('{}    {}'.format(item['itemDesc1'].ljust(25, ' '), 'Qty'))
                        print('Item {}    {}/{}'.format(str(item['orderItemNbr']).ljust(20, ' '),
                                                        item['pickedQty'],
                                                        item['orderQty']))
                        print('Aisle {} Bin {}'.format(item['aisle'], item['bin']))
                        print('-'*33)
        else:
            print('='*33)
            if len(temp_band_container) == 1:
                print('{}    {}'.format(detail, item['container_id']))
            else:
                print(detail)
            print('='*33)
            for item in items:
                print('{}    {}'.format(item['itemDesc1'].ljust(25, ' '), 'Qty'))
                print('Item {}    {}/{}'.format(str(item['orderItemNbr']).ljust(20, ' '),
                                                item['pickedQty'],
                                                item['orderQty']))
                print('Aisle {} Bin {}'.format(item['aisle'], item['bin']))
                print('-'*33)

