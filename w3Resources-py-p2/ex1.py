lst = [2,6,4,7,12,77,55,34,7]
name = ["abc","asd","asd"]
sameNumber = True


# sets function don't allowed duplicated data in a lists
#lists can
#so we use sets and list so that to compare the length of each lists


def checkList(item):
    if len(item)== len(set(item)):
        return True
    else:
        return False


print(checkList(lst))

