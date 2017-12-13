#Problem Code - dbru

def constructGraph(inputList):
    inputSet = set()
    print("List:", inputList)
    for item in inputList:
        rev = complement(item)
        inputSet.add(item)
        inputSet.add(rev)
    print("Set:", inputSet)
    #Because reads are of equal length
    length = len(inputList[0])
    edgelist =[]
    for item in inputSet:
        left = item[0:length-1]
        right = item[1:length]
        edgelist.append((left,right))

    return edgelist


def complement(read):
    comp = ''
    for i in read:
        if i == 'A':
            comp += 'T'
        if i == 'C':
            comp += 'G'
        if i == 'G':
            comp += 'C'
        if i == 'T':
            comp += 'A'

    return comp[::-1]

inputList = ['TGAT','CATG','TCAT','ATGC','CATC','CATC']
print(constructGraph(inputList))