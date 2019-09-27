# -*- coding:utf-8 -*-
import os,re


class SplitBook:

    def __init__(self):
        self.path = os.path.join(self.get_path(), 'book_catalog')
        self.delete_old_catalog()

    def get_path(self):
        path = os.path.dirname(os.path.split(os.path.realpath(__file__))[0])
        return path

    def create_catalog(self, name):
        new_name = re.sub(r'[#]|[*]', "", name)
        catalog_path = os.path.join(self.path, new_name+".txt")
        if os.path.exists(catalog_path):
            os.remove(catalog_path)
        return catalog_path

    def output_catalog(self, catalog_name, catalog_info):
        f = open(catalog_name, 'a', encoding='utf-8')
        f.write(catalog_info + '\n')
        f.close()

    def delete_old_catalog(self):
        catalog_lists = os.listdir(self.path)
        catalog_lists.sort(key=lambda fn: os.path.getatime(os.path.join(self.path, fn)))
        if len(catalog_lists) > 10:
            os.remove(os.path.join(self.path,catalog_lists[0]))


if __name__ == '__main__':
    t = SplitBook()
    name = t.create_catalog("3**a")
    print(name)

