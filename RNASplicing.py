RNA_CODON_TABLE = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

#read input file and generate the mRNA
def processInput():
    inputFile = open('C:/Users/sweta/Documents/ComputationalBiology/Rosalin/rosalind_splc.txt')
    sequences = inputFile.readlines()
    i=1
    tempString=''
    inputStrings =[]
    while(i<len(sequences)):
        if(sequences[i].__contains__('>')):
            inputStrings.append(tempString)
            tempString=''
            i+=1
        elif(i==len(sequences)-1):
            inputStrings.append(sequences[i])
            i+=1
        else:
            tempString +=sequences[i]
            i+=1
    inputStrings[0] = inputStrings[0].replace('\n', '')
    i=1
    while (i < len(inputStrings)):
        inputStrings[i] = inputStrings[i].replace('\n','')
        inputStrings[0] = removeIntrons(inputStrings[0],inputStrings[i])
        i+=1
    inputStrings[0] = inputStrings[0].replace('T','U')
    return inputStrings[0]


def removeIntrons(dnaSequence, intron):
    dnaSequence = dnaSequence.replace(intron, '')
    return dnaSequence


def replaceCodons(rnasequence):
    i = 0
    protein = ""
    rnasequence = rnasequence.replace("\n","")
    while (i < len(rnasequence)):
        if(RNA_CODON_TABLE[rnasequence[i:i+3]]== 'STOP'):
            break
        protein += RNA_CODON_TABLE[rnasequence[i:i + 3]]
        i += 3
    protein = protein.replace('STOP','')
    print(protein)

replaceCodons(processInput())