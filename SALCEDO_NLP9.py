def createBigram(data):
   listOfBigrams = []
   bigramCounts = {}
   unigramCounts = {}
   for i in range(len(data)-1):
      if i < len(data) - 1 and data[i+1].islower():

         listOfBigrams.append((data[i], data[i + 1]))

         if (data[i], data[i+1]) in bigramCounts:
            bigramCounts[(data[i], data[i + 1])] += 1
         else:
            bigramCounts[(data[i], data[i + 1])] = 1

      if data[i] in unigramCounts:
         unigramCounts[data[i]] += 1
      else:
         unigramCounts[data[i]] = 1
   return listOfBigrams, unigramCounts, bigramCounts


def calcBigramProb(listOfBigrams, unigramCounts, bigramCounts):
    listOfProb = {}
    for bigram in listOfBigrams:
        word1 = bigram[0]
        word2 = bigram[1]
        listOfProb[bigram] = (bigramCounts.get(bigram))/(unigramCounts.get(word1))
    return listOfProb

def readData():
    data = ['He stepped out into the hall, was delighted to encounter a water brother.']
    toarray=[]
    for i in range(len(data)):
        for word in data[i].split():
            data.append(word)
    print('=========================================================================================================')
    print("The given sentence is:")
    print(data)
    return toarray


if __name__ == '__main__':
    data = readData()
    listOfBigrams, unigramCounts, bigramCounts = createBigram(data)
    print('=========================================================================================================')
    print("The Bigrams are ")
    print(listOfBigrams)
    print('=========================================================================================================')
    print("The frequency of Unigrams are: ")
    print(unigramCounts)
    print('=========================================================================================================')
    print("The frequency of Bigrams are:")
    print(bigramCounts)

    bigramProb = calcBigramProb(listOfBigrams, unigramCounts, bigramCounts)
    print('=========================================================================================================')
    print("The probability of each Bigrams")
    print(bigramProb)
    inputList="He stepped out into the hall, was delighted to encounter a water brother."
    splt=inputList.split()
    outputProb1 = 1
    bilist=[]
    bigrm=[]

    for i in range(len(splt) - 1):
        if i < len(splt) - 1:

            bilist.append((splt[i], splt[i + 1]))
    for i in range(len(bilist)):
        if bilist[i] in bigramProb:

            outputProb1 *= bigramProb[bilist[i]]
        else:

            outputProb1 *= 0
    print('=========================================================================================================')
    print('Probablility of sentence \"He stepped out into the hall, was delighted to encounter a water brother.\" = ' + str(outputProb1))