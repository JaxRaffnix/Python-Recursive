a = 2
n = 1
b = 2

def uparrow(a, n, b):
    print(a, n, b)
    if n == 1:
        return pow(a, b)
    else:
        while b >0:
            return uparrow(a, n - 1, uparrow(a, n, b - 1))
        else:
            return 1

print("UpArrow ist",uparrow(a, n, b))


x= 5

aber= "aber aber aber"

print ("füneff")