from typing import Counter
from macro import macro 

counter = int(input("Enter 1 for GDP at MP using income method and 2 for GDP at MP using Expenditure Method : "))

obj = macro(counter)


nti = 500
y =  obj.GDPatFC(NetIndirectTax=nti)
print(y)