def powerset(lst):
    res = [[]]
    for x in lst:
        newset = [subset + [x] for subset in res]
        res.extend(newset)
    return res

def main():
    lst = [1,2,3]
    print powerset(lst)

main()