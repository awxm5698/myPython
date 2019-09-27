import sys
from lib import read
from lib import split_book

r = read.Read()
s = split_book.SplitBook()


def read_line(book, catalog):
    all_book_lists = r.get_book_list()
    if int(book) >= len(all_book_lists):
        book = len(all_book_lists) - 1
        print("the biggest book list length is %s : %s" % (book, all_book_lists[book]))
    catalog_list = r.get_book_catalog(all_book_lists[int(book)])
    if int(catalog) >= len(catalog_list):
        catalog = len(catalog_list) - 1
        print("the biggest catalog list length is %s : %s" % (catalog, catalog_list[catalog]))
    catalogs_info = r.get_catalog_info(all_book_lists[int(book)], catalog_list[int(catalog)])
    info = {'catalog_name': catalog_list[int(catalog)], 'catalog_info': catalogs_info}
    return info


if __name__ == '__main__':
    book_lists = r.get_book_list()
    print("==============\n"
          "编号|书籍名称")
    for i in range(len(book_lists)):
        print("%s|%s" % (i, book_lists[i]))
    print("==============")
    while True:
        num = input("请输入您要阅读的书籍编号:")
        if num == "":
            num = 0
            break
        if num.isdigit() and (int(num) >= 0) and (int(num) <= len(book_lists)):
            break
    length = len(r.get_book_catalog(book_lists[int(num)]))
    print("您选择的书籍名称《%s》,最大章节数：%s"
          % (book_lists[int(num)], length))
    if length == 0:
        print("您选择的书籍没有章节！")
        sys.exit()
    print("每次读取10章内容，如果章节剩余不足10章，则读取最后10章，总章节数小于10章，则读取全部")
    while True:
        i = input("请输入您要开始阅读的章节数：")
        if i == "":
            i = 0
            break
        if num.isdigit() and int(i) >= 0:
            break
    if length <= 10:
        i = 0
        n = length
    elif (length > 10) and (length - int(i) <= 10):
        i = length-10
        n = length
    else:
        i = int(i)
        n = i+10
    for i in range(i, n):
        _info = read_line(num, i)
        catalog_name = _info['catalog_name']
        print(catalog_name)
        catalog_info = _info['catalog_info']
        catalog_path = s.create_catalog(str(i)+" "+catalog_name)

        for c in catalog_info:
            s.output_catalog(catalog_path, c)
        s.delete_old_catalog()
