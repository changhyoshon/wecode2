
list = []
def test():
    for i in range(51):
        if not i % 2:
            list.append(i)
    return list
print(test())
