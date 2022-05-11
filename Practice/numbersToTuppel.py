#*args **kwargs

def super_func(*args, **kgwards):
    total = 0
    for items in kgwards.values():
        total += items
    return sum (args) + total

print(super_func(2,3,4,5, name = 4, passw =10))

#Rule: params, *args, devault parameters, **kwargs