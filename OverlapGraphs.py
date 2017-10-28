def processInput():
    tokens = dict()
    suffix = []
    prefix = []
    inputFile = open('C:/Users/sweta/Documents/ComputationalBiology/Rosalin/rosalind_grph.txt')
    inputStrings = inputFile.readlines()
    index = 0
    tempString =''
    i=0
    sequences =[]
    while i<len(inputStrings):
        if inputStrings[i].__contains__('>'):
            inputStrings[i] = inputStrings[i].replace('\n','')
            tokens[index] = inputStrings[i].replace('>','')
            index+=1
            if not tempString is '':
                tempString  = tempString.replace('\n','')
                sequences.append(tempString)
                tempString =''
            i+=1
            continue
        tempString += inputStrings[i]
        if(i==len(inputStrings)-1):
            tempString = tempString.replace('\n', '')
            sequences.append(tempString)

        i+=1
    for item in sequences:
        k = len(item) -3
        suffix.append(item[k:])
        prefix.append(item[:3])
    return suffix,prefix, tokens

def find_overlaps(suffix, prefix, tokens):
    adj_list =[]
    for i in range(len(suffix)):
        for j in range(len(prefix)):
            if(i==j):
                continue
            if(suffix[i]== prefix[j]):
                adj_list.append(tokens[i] + ' ' + tokens [j])

    print(adj_list)
    return adj_list

suffix, prefix, tokens = processInput()
find_overlaps(suffix, prefix, tokens)
