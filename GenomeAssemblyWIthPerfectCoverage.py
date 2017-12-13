def constructGraph(inputList):
    edgelist =[]
    length = len(inputList[0])
    inputSet = set(inputList)
    for item in inputSet:
        left = item[0:length-1]
        right = item[1:length]
        edgelist.append([left,right])
    return edgelist


def genomeAssembly(edgelist):
    elem = edgelist[0]
    # print("Temp:", elem)
    superstring = elem[0][-1]
    # print("Cyclic ",superstring)
    i = 0
    while i<len(edgelist)-1:
        superstring+=elem[1][-1]
        for j in range(len(edgelist)):
            if elem[1] == edgelist[j][0]:
                next = j
                break
        elem = edgelist[next]
        # print(superstring)
        # print(elem)
        i+=1

    # Print and save the output.
    print(superstring)

k_mers = ['ATTAC','TACAG','GATTA','ACAGA','CAGAT','TTACA','AGATT']
genomeAssembly(constructGraph(k_mers))