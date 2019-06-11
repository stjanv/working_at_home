import math
from line import line


# class Figure(object):
#     def __init__(self, sides):
#         self.sides = sides
#
#     def perimeter(self):
#         raise NotImplementedError('U must init def Per... ')
#
#     def area(self):
#         raise NotImplementedError('U must init def Area ')
#
#
# class Triangle(Figure):
#     def __init__(self, sides):
#         if len(sides) != 3:
#             raise Exception('Is\'nt a Triangle')
#         super().__init__(sides)
#
#     def perimeter(self):
#         p = sum(self.sides)
#         return f'Triangle perimeter = {p}'
#
#     def area(self):
#         p = sum(self.sides) / 2
#         s = math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
#         return f'Triangle area = {s}'

#
# t = Triangle([3, 4, 5])
# print(t.perimeter())
# print(t.area())
#
#
# class Rectangle(Figure):
#     def __init__(self, sides):
#         if len(sides) == 2 or len(sides) == 4:
#             super().__init__(sides)
#         else:
#             raise NotImplementedError('Is\nnt a Rectanle')
#
#     def perimeter(self):
#         if len(self.sides) == 2:
#             p = sum(self.sides) * 2
#         elif len(self.sides) == 4:
#             p = sum(self.sides)
#         return f'Rectangle perimeter = {p}'
#
#     def area(self):
#         s = self.sides[0] * self.sides[1]
#         return f'Rectangle area = {s}'
#
#
# print(line)
# r = Rectangle([5, 10])
# print(r.perimeter())
# print(r.area())
#

# class Circle(object):
#     def __init__(self, radius):
#         if radius < 0: radius = abs(radius)
#         self.radius = radius
#
#     def perimeter(self):
#         p = 2 * math.pi * self.radius
#         return f'circle len = {p}'
#
#     def area(self):
#         s = math.pi * self.radius ** 2
#         return f'circle area = {s}'


# print(line)
# c = Circle(5)
# print(c.perimeter())
# print(c.area())


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def segment_len(point1, point2):
        segment = math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
        return f'Segment len = {segment}'

    @staticmethod
    def area_duwn_segment(point1, point2):
        left_side = abs(point1.y)
        right_side = abs(point2.y)
        top_side = abs(math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2))
        bottom_side = abs(point1.x - point2.x)
        area = bottom_side * min(left_side, right_side) + abs(left_side - right_side) * bottom_side / 2
        return f'Left Side len = {left_side}\nRight Side len = {right_side} ' \
            f'\nTop Side len = {top_side}\nBottom Side len = {bottom_side}' \
            f'\nArea down the segment = {area}'


point1 = Point(5, 7)
point2 = Point(9, 14)
print(line)
print(point1.segment_len(point1, point2))
print(line)
print(point1.area_duwn_segment(point1, point2))
#
# class Singleton(object):
#     def __init__(self, cls):
#         self.cls = cls
#         self.cache = {}
#
#     def __call__(self, *args, **kwargs):
#         if self.cls.__name__ in self.cache:
#             return 'Just called once'
#         else:
#             res = self.cls(*args, **kwargs)
#             self.cache[self.cls.__name__] = (res)
#             return res
#
#
# @Singleton
# class ToTry(object):
#     def __init__(self, n):
#         self.n = n ** 2
#
#     def __str__(self):
#         return f'{self.n}'
#
#
# print(line)
# print(ToTry(5))
# print(line)
# print(ToTry(5))
# print(line)
#
#
# class ConnectToNetworkNode(object):
#     def __init__(self, unit_name, mac_address, ip_address, login, password):
#         self.__unit_name = unit_name
#         self.__mac_address = mac_address
#         self.__ip_address = ip_address
#         self.__login = login
#         self.__password = password
#
#     @property
#     def Unit_name(self):
#         return f'unit_name = {self.__unit_name}'
#
#     @property
#     def Mac_address(self):
#         return f'mac_address = {self.__mac_address}'
#
#     @property
#     def Ip_address(self):
#         return f'ip_address = {self.__ip_address}'
#
#     @property
#     def Login(self):
#         return f'login = {self.__login}'
#
#     @property
#     def Password(self):
#         return f'password = {self.__password}'
#
#     @Unit_name.setter
#     def Unit_name(self, new_unit_name):
#         self.__unit_name = new_unit_name
#
#     @Mac_address.setter
#     def Mac_address(self, new_mac_address):
#         self.__mac_address = new_mac_address
#
#     @Ip_address.setter
#     def Ip_address(self, new_ip_address):
#         self.__ip_address = new_ip_address
#
#     @Login.setter
#     def Login(self, new_login):
#         self.__login = new_login
#
#     @Password.setter
#     def Password(self, new_password):
#         self.__password = new_password
#
#     @Unit_name.deleter
#     def Unit_name(self):
#         self.__unit_name = None
#
#     @Mac_address.deleter
#     def Mac_address(self):
#         self.__mac_address = None
#
#     @Ip_address.deleter
#     def Ip_address(self):
#         self.__ip_address = None
#
#     @Login.deleter
#     def Login(self):
#         self.__login = None
#
#     @Password.deleter
#     def Password(self):
#         self.__password = None
#
#
# new_connection = ConnectToNetworkNode('switch1', 'E2:23:4D:DA:06', '192.168.0.123', 'admin', 'admin')
# print(new_connection.Unit_name)
# print(new_connection.Mac_address)
# print(new_connection.Ip_address)
# print(new_connection.Login)
# print(new_connection.Password)
# print(line)
# new_connection.Unit_name = 'switch2'
# print(new_connection.Unit_name)
# print(new_connection.Mac_address)
# print(new_connection.Ip_address)
# print(new_connection.Login)
# print(new_connection.Password)
# print(line)
# del new_connection.Ip_address
# print(new_connection.Unit_name)
# print(new_connection.Mac_address)
# print(new_connection.Ip_address)
# print(new_connection.Login)
# print(new_connection.Password)
# print(line)


point1 = Point(5, 7)
point2 = Point(9, 14)
point3 = Point(8, 19)
point4 = Point(11, 24)
point5 = Point(4, 12)
point_list = [point1, point2, point3, point4, point5]
print(point_list)


class Polygon(object):
    def __init__(self, point_list):
        self.point_list = point_list


    def segment_len(self,flag):
        self.flag = flag
        listX = []
        listY = []
        if flag == 'right':
            for i in self.point_list:
                listX.append(i.x)
                listY.append(i.y)
            a = (max(listX)-min(listX))/2+min(listX)
            b = (max(listY)-min(listY))/2+min(listY)

        return (a,b)

polygon = Polygon(point_list)
print(polygon.segment_len('right'))
