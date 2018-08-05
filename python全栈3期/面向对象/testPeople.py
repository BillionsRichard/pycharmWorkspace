from People import People
from pprint import pprint as pp

p = People(123, 'alex', 10000000)

p.get_id()

pp(People.__dict__)
print(p.__dict__)
print(p._People__star)