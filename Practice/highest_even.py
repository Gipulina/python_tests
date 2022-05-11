def highest_even(li):
    evens = []
    for item in li:
        evens.append(item)
    # return evens
    return max (evens)


print(highest_even([9,8,14,5,35]))