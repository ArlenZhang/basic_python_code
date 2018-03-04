"""
    描述符类：将某种特殊类型的类的实例指派给另一个类的属性
    __get__(self,instance,owner) 访问属性
    __set__(self,instance,value) 设置属性
    __delete__(self,instance)	 删除属性 的时候调用

    property实际上就是描述符类~
"""

class Desc:
    def __get__(self, instance, owner):
        print('getting ', self, instance, owner)  # 参数：描述类、被描述属性的对象实例、对象属类

    def __set__(self, instance, value):
        print('setting ', self, instance, value)

    def __delete__(self, instance):
        print('deleting ', self, instance)

class A:
    val = Desc()  # 上面的类就是当前属性的描述符


a = A()
a.val  # 访问

a.val = 'arlen'

del a.val

'''
问题描述：
    定义一个温度类，定义两个描述符类分别描述摄氏度和华氏度两个属性，要求两个属性能自动
转换，华氏度的值得变化随着社制度的值得变化而变化，关键在于外度对象对摄氏度数据的访问。
'''


class Celsius:
    def __init__(self, value=20.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fatrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8


class Temperature:
    cel = Celsius()
    fah = Fatrenheit()


t = Temperature()
t.cel = 35  # 摄氏35度
print(t.fah)

t.fah = 95
print(t.cel)
