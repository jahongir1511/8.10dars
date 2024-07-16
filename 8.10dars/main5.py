#https://www.codewars.com/kata/53da6a7e112bd15cbc000012/train/python


def sort_dict(d):
    sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return sorted_items

print(sort_dict({3: 1, 2: 2, 1: 3}))
print(sort_dict({1: 2, 2: 4, 3: 6})) 

