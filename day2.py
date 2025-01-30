l=[1,5,6,8,7,54,87]
l.sort()
print(l.count(9))
print(l)

k=[65,-20,97,94,66]
k.sort()
print(k)
def ascii(x):
    return ord(x)

m = ["A", -20, "a", 94, 66]
m.sort(key=lambda x: ord(x) if isinstance(x, str) else x)
print(m)













