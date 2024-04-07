# Numbers in python
# int, float, complex, bool, decimal, fraction


x,y,z = 2,5,8
# print(x,y,x)
# print("gaurav")

a_repr = repr("gaurav")
b_str = str("gaurav")
c_list = list("gaurav")
d_tuple = tuple("gaurav")
e_set = set("gaurav")
f_frozenset = frozenset("gaurav")


# print("a_repr : ", a_repr, "type of a_repr : ", type(a_repr))
# print("b_str : ", b_str, "type of b_str : ", type(b_str))
# print("c_list : ", c_list, "type of c_list : ", type(c_list))
# print("d_tuple : ", d_tuple, "type of d_tuple : ", type(d_tuple))
# print("e_set : ", e_set, "type of e_set : ", type(e_set))
# print("f_frozenset : ", f_frozenset, "type of f_frozenset : ", type(f_frozenset))
import math
# print(math.floor(2.6))
# print(math.floor(-2.6))
# print(math.trunc(2.6))
# print(math.trunc(-2.6))

# # octal number
# print("octal 0o123", 0o123)
# # hexadecimal number
# print("hexadecimal 0x123", 0x123)
# # binary number
# print("binary 0b1010", 0b1010)


# bit wise operator

# print("5 << 3 : ", 5 << 3)
# print("5 | 3 : ", 5 | 3)
# print("5 & 3 : ", 5 & 3)

# random number
import random

# print("random.random : ", random.random())
# print("random.randint : ", random.randint(1,10))
# print("random.randrange : ", random.randrange(1,10))
# print("random.choice : ", random.choice([1,2,3,4,5]))
# print("random.choices : ", random.choices([1,2,3,4,5], k=2))
# print("random.shuffle : ", random.shuffle([1,2,3,4,5]))
# print("random.sample : ", random.sample([1,2,3,4,5], k=2))
# print("random.uniform : ", random.uniform(1,10))
# print("random.seed : ", random.seed(10))


# decimal number
# from decimal import Decimal
# print("Decimal('1.0') : ", Decimal('1.0'))
# print("Decimal('0.1') + Decimal('0.1') - Decimal('0.1')  ", Decimal('1.0') + Decimal('0.1') + Decimal('0.1') - Decimal('0.1')  )

# set 
a = {1,2,3}
b = {2,3,4}
print("a.union(b) : ", a.union(b))
print("a.intersection(b) : ", a.intersection(b))
print("a.difference(b) : ", a.difference(b))
print("a.symmetric_difference(b) : ", a.symmetric_difference(b))
print("a.issubset(b) : ", a.issubset(b))
print("a.issuperset(b) : ", a.issuperset(b))
print("a.isdisjoint(b) : ", a.isdisjoint(b))

# boolean

print("bool(0) : ", bool(0))
print("bool(1) : ", bool(1))
print("True == 1 : ", True == 1)
print("False == 0 : ", False == 0)
print("True + 1 : ", True + 1)
print("False + 1 : ", False + 1)
print("True * 1 : ", True * 1)
print("False * 1 : ", False * 1)
print("True / 1 : ", True / 1)
print("False / 1 : ", False / 1)
print("True - 1 : ", True - 1)
print("False - 1 : ", False - 1)



print("True and False : ", True and False)
print("True or False : ", True or False)
print("not True : ", not True)
print("not False : ", not False)
