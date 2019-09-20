from copy import deepcopy

def main():
    m1 = [[6, 6], [3, 1]]
    m2 = [[1, 2], [3, 4]]
    print(add(m1, m2))
    print m1


def add(*args):
    argCount = len(args)
    if argCount == 0:
        return
    arr = deepcopy(args[0])
    for elem in args[1:]:
        for elem_inside in range(len(elem)):
            if len(arr) -1 < elem_inside:
                arr.append(elem[elem_inside])
            else:
                for item in range(len(elem[elem_inside])):
                    if len(arr[elem_inside]) -1 < item:
                        arr[elem_inside].append(elem[elem_inside][item])
                    else:
                        arr[elem_inside][item] += elem[elem_inside][item]
    return arr

if __name__ == "__main__":
    main()
