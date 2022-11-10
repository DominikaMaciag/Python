# 1. Napisz program, który będzie dodawał element do najbardziej zagnieżdżonej listy 


list=[1,2,[3,4,[5,6],5],3,[4,5]]

def mostNestedList(l,n):
    while l and isinstance(l[-1], list):
       l = l[-1]
    l.append(n)
    return l

mostNestedList(list, 7)
print(list)

# Niestety nie udało mi się poprawnie wykonać tego zadania.