from line import line
# class Person:
#     def __init__(self, name, position, zp):
#         self.name = name
#         self.position = position
#         self.zp = zp
#
#     def __str__(self):
#         return 'Name: {},\nPosition: {},\nZp: {}'.format(self.name, self.position, self.zp)
#
#
# class Manager(Person):
#     def __init__(self, name, position, zp, proc):
#         super().__init__(name, position, zp)
#         self.proc = int(zp/proc)
#
#     def __str__(self):
#         return 'Name: {},\nPosition: {},\nZp: {},\nBonus: {}'.format(self.name, self.position, self.zp, self.proc)
#
#
# p = Person('Nick', 'Manager', 1500)
# m = Manager('Vova','Admin',300,10)
#
#
#
# print(p)
# print(line)
# print(m)

class ReadString:
    string_for_check = ['{', '}', '[', ']', '(', ')', '<', '>']
    string_for_check_right = ['{}', '[]', '()', '<>']
    def __init__(self, string='String is empty'):
        self.string = string

    def __str__(self):
        return 'Ur string is "{}"'.format(self.string)

    def check_in_string(self):
        boolean=True
        for symbol in self.string:
            if symbol not in ReadString.string_for_check:
                boolean=False
        if boolean:
            return ('String contains only from this items list: '
                    +str(ReadString.string_for_check)
                    )
        else:
            return 'Ur string is bad'

    def chec_for_good_or_bad(self):
        boolean = True
        for i in range(len(self.string)-1,2):
            if (self.string[i]+self.string[i+1]) in ReadString.string_for_check_right:
                boolean = True
            else:
                boolean = False
                break
        return boolean



s = ReadString(input())
print(s)
print(s.check_in_string())
print(s.chec_for_good_or_bad())