import numpy as np


class Exercise:

    def __init__(self):
        pass

    @staticmethod
    def np_version():
        """打印版本号"""
        return np.__version__

    @staticmethod
    def np_two():
        """创建从0到9的一维数字数组"""
        arr = np.arange(10)
        return arr

    @staticmethod
    def np_three():
        """元素值全为True（真）的数组"""
        arr = np.full((3, 3), True, dtype=bool)
        return arr

    def np_four(self):
        """提取所有的奇数"""
        arr = self.np_two()
        return arr[arr % 2 == 1]

    def np_five(self):
        """所有奇数替换为-1"""
        arr = self.np_two()
        arr[arr % 2 == 1] = -1
        return arr

    def np_six(self):
        """所有奇数替换为-1，而不改变arr"""
        arr = self.np_two()
        new_arr = np.where(arr % 2 == 1, -1, arr)
        print(arr)
        return new_arr

    def np_seven(self):
        """将一维数组转换为2行的2维数组"""
        arr = self.np_two()
        new_arr = arr.reshape(2, -1)
        return new_arr

    @staticmethod
    def np_eight(index=1):
        """垂直堆叠数组a和数组b"""
        a = np.arange(10).reshape(2, -1)
        b = np.repeat(1, 10).reshape(2, -1)
        method_1 = np.concatenate([a, b], axis=0)
        method_2 = np.vstack([a, b])
        method_3 = np.r_[a, b]
        if index == 1:
            return method_1
        elif index == 2:
            return method_2
        else:
            return method_3

    @staticmethod
    def np_nine(index=1):
        """水平叠加两个数组"""
        a = np.arange(10).reshape(2, -1)
        b = np.repeat(1, 10).reshape(2, -1)
        method_1 = np.concatenate([a, b], axis=1)
        method_2 = np.hstack([a, b])
        method_3 = np.c_[a, b]
        if index == 1:
            return method_1
        elif index == 2:
            return method_2
        else:
            return method_3

    @staticmethod
    def np_ten():
        """只使用numpy函数和下面的输入数组a，生成numpy中的自定义序列"""
        a = np.array([1, 2, 3])
        arr = np.r_[np.repeat(a, 3), np.tile(a, 3)]
        return arr

    def np_eleven(self):
        """获取数组a和数组b之间的公共项"""
        a = self.np_two()
        b = np.array([3, 4, 6, 8, 0, 12, 34, 45])
        arr = np.intersect1d(a, b)
        return arr

    def np_twelve(self ):
        """从数组a中删除数组b中的所有项"""
        a = self.np_two()
        b = np.array([1, 2, 3, 4, 5])
        arr = np.setdiff1d(a, b)
        return arr

    def np_thirteen(self):
        """获取a和b元素匹配的位置"""
        a = self.np_two()
        b = np.array([1, 1, 2, 3, 4, 5, 5, 4, 3, 2])
        arr = np.where(a == b)
        return arr[0]

    def np_fourteen(self, index=1):
        """获取5到8之间的所有项目"""
        a = self.np_two()
        method_1 = a[np.where((a >= 5) & (a <= 8))]
        method_2 = a[np.where(np.logical_and(a >= 5, a <= 8))]
        method_3 = a[(a >= 5) & (a <= 8)]
        if index == 1:
            return method_1
        elif index == 2:
            return method_2
        else:
            return method_3

    @staticmethod
    def max_x(x, y):
        """获取两者的较大值"""
        if x >= y:
            return x
        else:
            return y

    def np_fifteen(self):
        """转换适用于两个标量的函数max_x，以处理两个数组"""
        pair_max = np.vectorize(self.max_x, otypes=[float])
        a = np.array([5, 7, 9, 8, 6, 4, 5])
        b = np.array([6, 3, 4, 8, 9, 7, 1])
        return pair_max(a, b)

    @staticmethod
    def np_sixteen():
        """在数组arr中交换列1和2"""
        arr = np.arange(9).reshape(3, 3)
        return arr[:, [1, 0, 2]]

    @staticmethod
    def np_seventeen():
        """交换数组arr中的第1和第2行"""
        arr = np.arange(9).reshape(3, 3)
        return arr[[1, 0, 2], :]

    @staticmethod
    def np_eighteen():
        """反转二维数组arr的行"""
        arr = np.arange(9).reshape(3, 3)
        return arr[::-1]

    @staticmethod
    def np_nineteen():
        """反转二维数组arr的列"""
        arr = np.arange(9).reshape(3, 3)
        return arr[:, ::-1]

    @staticmethod
    def np_twenty(index=1):
        """创建一个形状为5x3的二维数组，以包含5到10之间的随机十进制数"""
        rand_arr_1 = np.random.randint(low=5, high=10, size=(5, 3)) + np.random.random((5, 3))
        rand_arr_2 = np.random.uniform(5, 10, size=(5, 3))
        if index == 1:
            return rand_arr_1
        else:
            return rand_arr_2

    @staticmethod
    def np_twenty_one():
        """只打印或显示numpy数组rand_arr的小数点后3位"""
        rand_arr = np.random.random((5, 3))
        np.set_printoptions(precision=3)
        return rand_arr[:3]

    @staticmethod
    def np_twenty_two():
        """通过e式科学记数法来打印rand_arr（如1e10）"""
        np.set_printoptions(suppress=False)
        np.random.seed(100)
        rand_arr = np.random.random([3, 3])/1e3
        np.set_printoptions(suppress=True, precision=6)
        return rand_arr

    @staticmethod
    def np_twenty_three():
        """将numpy数组a中打印的项数限制为最多6个元素"""
        arr = np.arange(15)
        np.set_printoptions(threshold=6)
        return arr

    def np_twenty_four(self):
        """打印完整的numpy数组a而不截断"""
        """异常"""
        arr = self.np_twenty_three()
        # np.set_printoptions(threshold=np.nan)
        return arr

    @staticmethod
    def np_twenty_five(index=3):
        """导入数字和文本的数据集保持文本在numpy数组中完好无损"""
        url = "archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        arr = np.genfromtxt(url, delimiter=',', dtype='object')
        names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
        return arr[:index]

    def np_twenty_six(self):
        """如何从1维元组数组中提取特定列"""
        iris_1d = self.np_twenty_five(10)
        species = np.array([row[4] for row in iris_1d])
        return species[:5]

    def np_twenty_seven(self):
        """将1维元组数组转换为2维numpy数组"""
        arr = self.np_twenty_five()
        new_arr = np.array([row.tolist()[:4] for row in arr])
        return new_arr

    @staticmethod
    def np_twenty_eight():
        """计算numpy数组的均值，中位数，标准差"""
        url = 'archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
        # iris = np.genfromtxt(url, delimiter=',', dtype='object')
        sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
        mu, med, sd = np.mean(sepallength), np.median(sepallength), np.std(sepallength)
        return mu, med, sd


if __name__ == '__main__':
    e = Exercise()
    print(e.np_twenty_eight())


