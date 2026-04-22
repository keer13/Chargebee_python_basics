# ================================
# OOPS
# ================================
class First:
    a = 20

    def method1(self):
        print("hiii")


o1 = First()
print(o1.a)

o1.a = 90
print(o1.a)

o1.method1()


# ================================
# INHERITANCE
# ================================
class Second(First):
    b = 60

    def method2(self):
        print("byee")


s1 = Second()
print(s1.b)
print(s1.a)


class Animal:
    def eat(self):
        print("eating")


class Dog(Animal):
    def sleep(self):
        print("sleeping")


d = Dog()
d.eat()
d.sleep()


# ================================
# MODULES
# ================================
# (Make sure cal.py exists in same folder)

import cal as k

k.add(2, 3)

from cal import *

add(5, 7)
sub(5, 7)
div(5, 7)
mul(5, 7)
