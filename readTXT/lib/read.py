# -*- coding: utf-8 -*-
import re
import os


class Read:

    def __init__(self):
        self.book_path = os.path.join(self.get_book_path(), "book_library")
        self.re_compile = r'.*[第].{1,4}[章|节|集|季|卷|篇|回|册][" "]'

    def get_book_path(self):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        print(path)
        return path

    def get_book_list(self):
        book_list = os.listdir(self.book_path)
        return book_list

    def get_book_catalog(self, book_name):
        book = os.path.join(self.book_path, book_name)
        f = open(book, "r", encoding="utf-8")
        book_catalog_list = []
        r = re.compile(self.re_compile)
        for ele in f.readlines():
            _info = ele.strip()
            if r.findall(_info):
                book_catalog_list.append(_info.split(';')[0])
        f.close()
        return book_catalog_list

    def get_catalog_info(self, book_name, catalog):
        book = os.path.join(self.book_path, book_name)
        f = open(book, "r", encoding="utf-8")
        all_catalog_info = []
        catalog_info = []
        r = re.compile(self.re_compile)
        for ele in f.readlines():
            _info = ele.strip()
            all_catalog_info.append(_info.split(';')[0])
        is_catalog_info = False
        all_lines = len(all_catalog_info)
        for i in range(all_lines):
            if all_catalog_info[i] == catalog:
                is_catalog_info = True
            if is_catalog_info:
                catalog_info.append(all_catalog_info[i])

            if i == all_lines-1:
                break
            elif is_catalog_info is True and r.findall(all_catalog_info[i+1]):
                break
        return catalog_info


if __name__ == "__main__":
    t = Read()
    t.get_book_path()
    book_name = t.get_book_list()[0]
    catalog_list = t.get_book_catalog(book_name)
    print(catalog_list)
    print(t.get_catalog_info(book_name, catalog_list[2]))
