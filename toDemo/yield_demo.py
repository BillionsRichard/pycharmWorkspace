from pprint import pprint as pp

def yield_sth(i):
    for j in range(i):
        yield j

sth = yield_sth(10)
pp(type(sth))
pp(dir(sth))

for i in sth:
    pp(i)

