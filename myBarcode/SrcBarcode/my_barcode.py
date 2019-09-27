import os
import barcode


class MyBarcode:

    def __init__(self):
        self.img_path = os.path.join(self.get_current_path(), 'Img')

    @staticmethod
    def get_current_path():
        """
        获取当前文件夹上一层的绝对路径
        """
        current_path = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.dirname(current_path)
        return path

    def crate_barcode(self, provided, item):
        code = barcode.get_barcode_class(provided)
        bar = code(item, writer=barcode.writer.ImageWriter())
        bar.save(os.path.join(os.path.join(self.get_current_path(), 'Img'), provided+"_"+item))

    @staticmethod
    def provided():
        return barcode.PROVIDED_BARCODES

