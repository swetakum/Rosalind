def processInput():
    inputFile = open('C:/Users/sweta/Documents/ComputationalBiology/Rosalin/rosalind_corr.txt')
    sequences = inputFile.readlines()
    i = 1
    tempString = ''
    inputStrings = []
    while (i < len(sequences)):
        if (sequences[i].__contains__('>')):
            # print("tempstring = ", tempString)
            tempString =tempString.replace('\n','')
            inputStrings.append(tempString)
            tempString = ''
            i+=1
        elif (i == len(sequences) - 1):
            tempString+=sequences[i]
            tempString =tempString.replace('\n','')
            inputStrings.append(tempString)
            i += 1
        else:
            tempString += sequences[i]
            i += 1

    return inputStrings


def isOneHammingDistance(str1, str2):
    count = 0
    index = -1
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count +=1
        if count ==1 and index ==-1:
            index = i
        if count >1:
            return False

    if count ==1:
        # print("Before = ",str1, str2)
        str1 = list(str1)
        str1[index] = str2[index]
        str1 = ''.join(str1)
        # print("After = ", str1, str2)
        return str1
    return False

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

def findErrorReads(reads):
    incorrect = []
    correct = []
    for i in range(len(reads)):
        if reads.count(reads[i]) + reads.count(complement(reads[i])) >= 2:
            correct.append(reads[i])
        else:
            incorrect.append(reads[i])
    print(correct)
    print(incorrect)
    hammcount = 0
    corrections = []
    for item in incorrect:
        for corrects in correct:
            # print("Correct item = ", corrects)
            if isOneHammingDistance(item, corrects) != False:
                print(isOneHammingDistance(item,corrects))
                corrections.append(item + '->' +isOneHammingDistance(item,corrects))
                hammcount+=1
                break;
            if isOneHammingDistance(item, complement(corrects)) != False:
                hammcount+=1
                corrections.append(item + '->' +isOneHammingDistance(item,complement(corrects)))
                break;

    print(corrections)

findErrorReads(processInput())


