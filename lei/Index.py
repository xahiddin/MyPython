# from calculator import Emel
#
# obj = Emel()
# obj.add()
import re

a = "18811484144"

result = re.match(r'^1[3 5 8](\d){9}$', a, re.M).group()
print(result)
