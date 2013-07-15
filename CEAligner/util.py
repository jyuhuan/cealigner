# -*- coding: utf-8 -*-
class ParallelCorpus():
    srcLines = []
    tgtLines = []

    def __init__(self, sourceLangFilePath, targetLangFilePath):
        print "Opening files... "
        srcF = open(sourceLangFilePath, "r")
        tgtF = open(targetLangFilePath, "r")
        print "Files are now in memory. Now splitting the lines... "
        self.srcLines = srcF.read().splitlines()
        self.tgtLines = tgtF.read().splitlines()
        print "Files are now splitted into lines. "
        print "Corpus ready. "
        return
    
    def getEntryCount(self):
        return len(self.srcLines)
      
    def getEntryAt(self, idx):
        return [self.srcLines[idx], self.tgtLines[idx]]
    
    def getAllSourceLanguageWords(self):
        allWords = set()
        for line in self.srcLines:
            words = line.split()
            for word in words:
                allWords.add(word)
        return allWords
    
    def getSourceLanguageWordCount(self):
        return len(self.getAllSourceLanguageWords())
    
    def getAllTargetLanguageWords(self):
        allWords = set()
        for line in self.tgtLines:
            words = line.split()
            for word in words:
                allWords.add(word)
        return allWords
    
    def getTargetLanguageWordCount(self):
        return len(self.getAllTargetLanguageWords())


def printDictionary(dic):
    for key in dic.keys():
        keysStr = ""
        for i in range(0, len(key)):
            keysStr += str(key[i]) + ", "
        keysStr = keysStr[:-2]
        print "".join(keysStr) + " = " + str(dic[key])

def tryGetDoubleValueByKeyFromDic(key, dic):
    result = 0.0
    if dic.has_key(key):
        result = dic[key]
    return result

def tryIncDoubleValueAtKeyInDic(key, dic, val):
    if dic.has_key(key):
        dic[key] += val
    else:
        dic[key] = val
    return

def printTopResultsInDic(dic, threshold):
    for key in dic.keys():
        if dic[key] >= threshold:
            keysStr = ""
            for i in range(0, len(key)):
                keysStr += str(key[i]) + ", "
            keysStr = keysStr[:-2]
            print "".join(keysStr) + " = " + str(dic[key])
    return


