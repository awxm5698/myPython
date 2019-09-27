from SrcBarcode import my_barcode

if __name__ == '__main__':
    m = my_barcode.MyBarcode()
    p = ['code128', 'code39', 'ean', 'ean13', 'ean14', 'ean8', 'gs1', 'gs1_128', 'gtin',
         'isbn', 'isbn10', 'isbn13', 'issn', 'itf', 'jan', 'pzn', 'upc', 'upca']

    print(m.provided())
    # m.crate_barcode('code128', 'T-001')
    m.crate_barcode('code128', 'A-A1810')

