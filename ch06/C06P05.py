# Hanoi Tower Problem

class Disk:

    # properties
    size = 0

    # constructor
    def __init__(self, size):
        self.size = size

    # getSize method
    def getSize(self):
        return self.size


class Rod:

    # properties
    pile = []

    # constructor
    def __init__(self, diskList):
        self.pile = diskList

    # add new Disk
    def push(self, disk):
        return self.pile.append(disk)

    def pop(self):
        lastElemnt = self.pile[-1]
        self.pile.pop()
        return lastElemnt

    def getElements(self):
        return self.pile


def gameSetup(diskNumber, rodNumber):

    pile1 = []
    pile2 = []
    pile3 = []
    # for i in reversed(range(1, diskNumber)) :
    for i in range(diskNumber, 0, -1):
        newDisk = Disk(i)
        pile1.append(newDisk)

    return [Rod(pile1), Rod(pile2), Rod(pile3)]

# Solution


def problem():

    diskNumber = 5
    rodNumber = 3
    rodListState = gameSetup(diskNumber, rodNumber)

    for i in rodListState:
        for j in i.getElements():
            print(j.getSize())


# Asserts
diskGreen = Disk(2)
print(diskGreen.getSize())
pile = []
pile.append(diskGreen)
# print(pile)
rod1 = Rod(pile)
for i in rod1.getElements():
    print(i.getSize())
# problem()

'''
Version recursiva
'''


def Hanoi(discos, TorreOrigen=1, TorreAuxiliar=2, TorreDestino=3):

    if discos == 1:
        print(TorreOrigen, "a", TorreDestino)

    else:
        Hanoi(discos - 1, TorreOrigen, TorreDestino, TorreAuxiliar)
        print(TorreOrigen, "a", TorreDestino)
        Hanoi(discos - 1, TorreAuxiliar, TorreOrigen, TorreDestino)
    return


# Lo probamos con 3 discos
Hanoi(3)
