# Zadanie 3 - Dominika Maciąg
# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right
# włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną 

list = ["a","b","c","d","e","f"]
print("lista: ",list)

def odwracanie(L, left, right): # wersja iteracyjna
    while left < right:
        var = L[left]
        L[left]=L[right]
        L[right]=var
        left+=1
        right-=1
    return L

def recursion(L, left, right): # wersja rekurencyjna
    if left < right:
        var = L[left]
        L[left]=L[right]
        L[right]=var
        recursion(L,left+1,right-1)
    return L

odwracanie(list, 0, len(list)-1)
print("iteracyjnie: ",list) # odwrócona lista

recursion(list, 0, len(list)-1) 
print("rekurencyjnie: ",list) # ponownie odwrócona lista (wraca do początkowego stanu)