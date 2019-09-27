# -*- coding: utf-8 -*-

import os
import re
from PIL import Image
from PIL import ImageChops
from .my_geometry import MyGeometry


class MyImage:

    def __init__(self):
        self.img_path = os.path.join(self.get_current_path(), 'Image')
        self.my_geometry = MyGeometry()

    @staticmethod
    def get_current_path():
        """
        获取当前文件夹上一层的绝对路径
        """
        current_path = os.path.split(os.path.realpath(__file__))[0]
        path = os.path.dirname(current_path)
        return path

    def get_img_file_path(self, name):
        """
        根据名称获取图片文件的绝对路径
        """
        path = os.path.join(self.img_path, '{}.png'.format(name))
        return path

    def take_quadrilateral_img(self, input_img_name, start_point, end_point, output_img_name=None):
        """
        根据输入的起点和终点坐标截取长方形
        """
        input_img_name_path = self.get_img_file_path(input_img_name)
        if output_img_name is None:
            output_img_name_path = self.get_img_file_path('{}_{}'.format(input_img_name, '_quadrilateral',))
        else:
            output_img_name_path = self.get_img_file_path('{}'.format(output_img_name))

        im = Image.open(input_img_name_path)
        im = im.crop((int(start_point[0]), int(start_point[1]), int(end_point[0]), int(end_point[1])))
        im.save(output_img_name_path)
        return output_img_name_path

    def take_square_img(self, input_img_name, start_point, side_length, output_img_name=None):
        """
        根据输入的起点和边长截取正方形
        """
        input_img_name_path = self.get_img_file_path(input_img_name)
        if output_img_name is None:
            output_img_name_path = self.get_img_file_path('{}_{}'.format(input_img_name, '_square'))
        else:
            output_img_name_path = self.get_img_file_path('{}'.format(output_img_name))

        im = Image.open(input_img_name_path)

        x = int(start_point[0])
        y = int(start_point[1])
        to_x = int(start_point[0]) + int(side_length)
        to_y = int(start_point[1]) + int(side_length)
        im = im.crop((x, y, to_x, to_y))

        im.save(output_img_name_path)
        return output_img_name_path

    def take_circular_img(self, input_img_name, center_point, radius, output_img_name=None):
        """
        根据输入的中心点和半径截取圆形
        """
        input_img_name_path = self.get_img_file_path(input_img_name)
        if output_img_name is None:
            output_img_name_path = self.get_img_file_path('{}_{}'.format(input_img_name, '_circular'))
        else:
            output_img_name_path = self.get_img_file_path('{}'.format(output_img_name))

        img_input = Image.open(input_img_name_path).convert("RGBA")
        width, height = img_input.size

        begin_x = center_point[0] - radius
        begin_y = center_point[1] - radius
        end_x = center_point[0] + radius
        end_y = center_point[1] + radius
        new_img_size = (radius*2, radius*2)
        new_img = Image.new('RGBA', new_img_size, (255, 255, 255, 0))

        for x in range(begin_x, end_x):
            for y in range(begin_y, end_y):
                distance = self.my_geometry.get_distance([(x, y), center_point])
                if distance <= radius:
                    if x < 0 or y < 0 or x > width or y > height:
                        s = (255, 255, 255, 0)
                    else:
                        s = img_input.getpixel((x, y))
                    new_img.putpixel((x - begin_x, y - begin_y), s)
        new_img.save(output_img_name_path)

    def take_triangular_img(self, input_img_name, point_one, point_two, point_three, output_img_name=None):
        """
        根据输入的三点坐标，截取三角形
        """
        is_triangular = self.my_geometry.check_is_triangular([point_one, point_two, point_three])
        if not is_triangular:
            return
        input_img_name_path = self.get_img_file_path(input_img_name)
        if output_img_name is None:
            output_img_name_path = self.get_img_file_path('{}_{}'.format(input_img_name, '_triangular'))
        else:
            output_img_name_path = self.get_img_file_path('{}'.format(output_img_name))

        img_input = Image.open(input_img_name_path).convert("RGBA")
        width, height = img_input.size

        area_location = self.my_geometry.get_min_area_location([point_one, point_two, point_three])

        new_start_x, new_start_y = area_location[0]
        new_end_x, new_end_y = area_location[1]
        if new_end_x > width:
            new_end_x = width
        if new_end_y > height:
            new_end_y = height

        new_width = int(new_end_x - new_start_x)
        new_height = int(new_end_y - new_start_y)
        new_img_size = (new_width, new_height)
        new_img = Image.new('RGBA', new_img_size, (255, 255, 255, 0))

        for x in range(new_start_x, new_end_x):
            for y in range(new_start_y, new_end_y):
                is_within_triangular = \
                    self.my_geometry.check_point_is_within_triangular((x, y), [point_one, point_two, point_three])
                if is_within_triangular:
                    s = img_input.getpixel((x, y))
                else:
                    s = (255, 255, 255, 0)
                new_img.putpixel((x - new_start_x, y - new_start_y), s)

        new_img.save(output_img_name_path)

    def compare_image(self, path_one, path_two):
        """
        比较两张图片是否相同
        """
        r = re.compile(r'png$')
        if not r.findall(path_one):
            path_one = self.get_img_file_path(path_one)
        if not r.findall(path_two):
            path_two = self.get_img_file_path(path_two)

        image_one = Image.open(path_one)
        image_two = Image.open(path_two)

        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            return True
        else:
            return False

    def compare_image_by_percent(self, file_image1, file_image2, percent=0.99, size=(256, 256), part_size=(64, 64)):
        """
        判断两种图片相似度（百分比）
        """
        r = re.compile(r'png$')
        if not r.findall(file_image1):
            file_image1 = self.get_img_file_path(file_image1)
        if not r.findall(file_image2):
            file_image2 = self.get_img_file_path(file_image2)

        image1 = Image.open(file_image1)
        image2 = Image.open(file_image2)

        img1 = image1.resize(size).convert("RGB")
        sub_image1 = self.split_image(img1, part_size)

        img2 = image2.resize(size).convert("RGB")
        sub_image2 = self.split_image(img2, part_size)

        sub_data = 0
        for im1, im2 in zip(sub_image1, sub_image2):
            sub_data += self.calculate(im1, im2)

        x = size[0] / part_size[0]
        y = size[1] / part_size[1]

        pre = round((sub_data / (x * y)), 6)
        if pre >= percent:
            return True
        else:
            return False

    @staticmethod
    def calculate(image1, image2):
        g = image1.histogram()
        s = image2.histogram()
        assert len(g) == len(s), "error"
        data = []
        for index in range(0, len(g)):
            if g[index] != s[index]:
                data.append(1 - abs(g[index] - s[index]) / max(g[index], s[index]))
            else:
                data.append(1)
        return sum(data) / len(g)

    @staticmethod
    def split_image(image, part_size):
        pw, ph = part_size
        w, h = image.size
        sub_image_list = []
        assert w % pw == h % ph == 0, "error"
        for i in range(0, w, pw):
            for j in range(0, h, ph):
                sub_image = image.crop((i, j, i + pw, j + ph)).copy()
                sub_image_list.append(sub_image)
        return sub_image_list

