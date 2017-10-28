def processInput():
    inputFile = open('C:/Users/sweta/Documents/ComputationalBiology/Rosalin/rosalind_long.txt')
    sequences = inputFile.readlines()
    i = 1
    tempString = ''
    inputStrings = []
    while (i < len(sequences)):
        if (sequences[i].__contains__('>')):
            inputStrings.append(tempString)
            tempString = ''
            i+=1
        elif (i == len(sequences) - 1):
            inputStrings.append(tempString)
            i += 1
        else:
            tempString += sequences[i]
            i += 1

    i = 0
    while (i < len(inputStrings)):
        inputStrings[i] = inputStrings[i].replace('\n', '')
        i += 1
    return (inputStrings)


def overlap(str1, str2):

    if str2 in str1:
        return str1
    elif str1 in str2:
        return str2

    ll = min(len(str1), len(str2))
    end = int(ll/2) -1
    for i in range(ll,end, -1):
        if str1[0:i] == str2[-i:]:
            return str2 + str1[i:]

    for i in range(ll, end, -1):
        if str2[0:i] == str1[-i:]:
            return str1 + str2[i:]

    return ""

def find(inp):
    l = len(inp)
    mstr = ""
    str=""
    br=False
    for i in range(0, l):
        if br:
            break
        for j in range(i+1, l):
            str = overlap(inp[i], inp[j])
            if str:
                mstr = str
                ii = inp[i]
                jj = inp[j]
                inp.remove(ii)
                inp.remove(jj)
                br = True
                break

    l = len(inp)
    while len(inp):
        for i in range(0, len(inp)):
            str = overlap(mstr, inp[i])
            if str:
                mstr = str
                ii = inp[i]
                inp.remove(ii)
                break

    return mstr
print (find(processInput()))
