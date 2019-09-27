class MyGeometry:

    def __init__(self):
        pass

    @staticmethod
    def get_triangular_area(args):
        """
        计算三角形的面积（二维直角坐标系）
        :arg    ((0,1),(0,2),(0,3)) or [(0,1),(0,2),(0,3)]
        """
        x1, y1 = args[0]
        x2, y2 = args[1]
        x3, y3 = args[2]
        area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
        return area

    def check_point_is_within_triangular(self, point, args):
        """
        判断点是否在三角形内（二维直角坐标系）
        :arg    ((0,1),(1,2),(0,3)) or [(0,1),(1,2),(0,3)]
        """
        triangular_area = self.get_triangular_area([args[0], args[1], args[2]])
        area_a = self.get_triangular_area([point, args[0], args[1]])
        area_b = self.get_triangular_area([point, args[0], args[2]])
        area_c = self.get_triangular_area([point, args[1], args[2]])

        return triangular_area == area_a + area_b + area_c

    @staticmethod
    def get_min_area_location(args):
        """
        获取输入点的最小外包矩形（二维直角坐标系）
        :arg    ((0,1),(1,2),(0,3)) or [(0,1),(1,2),(0,3)]
        """
        ar_x = []
        ar_y = []
        for ar in args:
            ar_x.append(ar[0])
            ar_y.append(ar[1])
        location = [(min(ar_x), min(ar_y)), (max(ar_x), max(ar_y))]
        return location

    @staticmethod
    def get_distance(args):
        """
        计算两点的直线距离（二维直角坐标系）
        :arg    ((0,1),(1,2)) or [(0,1),(1,2)]
        """
        point_one = args[0]
        point_two = args[1]
        distance_x = abs(point_one[0] - point_two[0])   # 横坐标差
        distance_y = abs(point_one[1] - point_two[1])   # 纵坐标差
        distance = (pow(distance_x, 2) + pow(distance_y, 2)) ** 0.5    # 距离
        return distance

    def check_is_triangular(self, args):
        """
        判断三个点是否能组成三角形（二维直角坐标系）
        :arg    ((0,1),(1,2),(0,3)) or [(0,1),(1,2),(0,3)]
        """
        point_one = args[0]
        point_two = args[1]
        point_three = args[2]
        distance_one = self.get_distance([point_one, point_two])
        distance_two = self.get_distance([point_one, point_three])
        distance_three = self.get_distance([point_three, point_two])
        is_triangular = False
        if (distance_one+distance_two > distance_three
                or distance_one+distance_three > distance_two
                or distance_two+distance_three > distance_one):
            is_triangular = True
        return is_triangular

    def check_point_in_area(self, point, args):
        """
        判断点是否在区域内
        :param point: （x,y）
        :param args: [(x1,y1),(x2,y2),(x3,y3),...]   # 最少三个点
        :return:
        """
        if len(args) < 3:
            return False
        is_in_area = False
        min_area = self.get_min_area_location(args)
        min_x, min_y = min_area[0]
        max_x, max_y = min_area[1]
        point_x = point[0]
        point_y = point[1]
        if point_x < min_x or point_y < min_y or point_x > max_x or point_y > max_y:
            is_in_area = False
        elif point in args:
            is_in_area = True
        else:
            vertx = self.get_all_x_location(args)
            verty = self.get_all_y_location(args)
            nvert = len(args)

            for i in range(0, nvert-1):
                j = i+1
                if (((verty[i] > point_y) != (verty[j] > point_y)) and
                        (point_x < (vertx[j]-vertx[i]) * (point_y-verty[i]) / (verty[j]-verty[i]) + vertx[i])):
                    cross_time = cross_time + 1
            if cross_time % 2 != 0:
                is_in_area = True
        return is_in_area
        # elif point in args:
        #     is_in_area = True
        # else:
        #     args_x = self.get_all_x_location(args)
        #     args_y = self.get_all_y_location(args)
        #     cross_time = 0
        #     for i in range(len(args)):
        #         next_i = i+1
        #         if next_i == len(args):
        #             next_i = 0
        #         if self.check_cross(((point_x, point_y), (max_x, point_y)),
        #                             ((args_x[i], args_y[i]), (args_x[next_i], args_y[next_i]))):
        #             cross_time = cross_time + 1

    @staticmethod
    def get_all_x_location(args):
        """获取所有的x坐标的值"""
        args_x = []
        for arg in args:
            args_x.append(arg[0])
        return args_x

    @staticmethod
    def get_all_y_location(args):
        """获取所有的y坐标的值"""
        args_y = []
        for arg in args:
            args_y.append(arg[1])
        return args_y

    @staticmethod
    def compute_cross_product(point_one, point_two):
        """
        计算差乘
        """
        x1, y1 = point_one
        x2, y2 = point_two
        return x1*y2 - y1*x2

    @staticmethod
    def check_is_repeat(*args):
        """检查是否有重复项"""
        is_repeat = False
        new_args = sorted(args)
        for i in range(len(new_args)):
            if i < len(new_args)-2:
                if new_args[i] == new_args[i+1]:
                    is_repeat = True
        return is_repeat

    def check_cross(self, line_a, line_b):
        """判断两线段是否交叉"""
        is_cross = False
        a1, a2 = line_a
        b1, b2 = line_b
        if self.check_is_repeat(a1, a2, b1, b2):
            is_cross = True
        else:
            vector_a = self.compute_cross_product(a1, a2)
            vector_a1_b1 = self.compute_cross_product(a1, b1)
            vector_a1_b2 = self.compute_cross_product(a1, b2)
            vector_b = self.compute_cross_product(b1, b2)
            vector_b1_a1 = self.compute_cross_product(b1, a1)
            vector_b1_a2 = self.compute_cross_product(b1, a2)
            """计算向量乘积"""
            multiply_a = (vector_a * vector_a1_b1) * (vector_a * vector_a1_b2)
            multiply_b = (vector_b * vector_b1_a1) * (vector_b * vector_b1_a2)
            """如果两者相同并且乘积等于0，说明两者平行并且在一条直线上"""
            if multiply_a == multiply_b and vector_a*vector_a1_b1 == 0:
                len_a = self.get_distance([a1, a2])
                len_b = self.get_distance([b1, b2])
                len_a1b1 = self.get_distance([a1, b1])
                len_a1b2 = self.get_distance([a1, b2])
                len_a2b1 = self.get_distance([a2, b1])
                len_a2b2 = self.get_distance([a2, b2])
                """判断是否有重叠部分"""
                if max(len_a1b1, len_a1b2, len_a2b1, len_a2b2) < len_a+len_b:
                    is_cross = True
            """如果两者不相等并且都不大于0"""
            if (multiply_a <= 0) and (multiply_b <= 0) and (multiply_a != multiply_b):
                is_cross = True
        return is_cross


if __name__ == '__main__':
    g = MyGeometry()
    # a = g.check_cross([(0, 0), (2, 2)], [(4, 4), (-3, -3)])
    a = g.check_point_in_area((0, 1), [(0, 1), (1, 1), (1, 0), [0, 0]])
    print(a)

