# -*- coding: utf-8 -*-
class ParallelCorpus():
    
    '''data = [
                ["here are some chinese words", "这里 有 一些 中文 词语"],
                ["i am a chinese", "我 是 中国人"],
                ["i do not have a computer", "我 没 有 电脑"],
                ["you should come to china some time in the future", "将来 你 应该 来 中国 看 看"],
                ["the weather in canada is awesome", "加拿大 的 天气 太 好 了"],
                ["i love you", "我 爱 你"],
                ["i adore you", "我 喜欢 你"]
                ];'''
    
    '''data = [
            ["das Haus", "the house"],
            ["das Buch", "the book"],
            ["ein Buch", "a book"]
            ];'''
    
    '''data = [
            ["wo ai ni", "i love you"],
            ["ni ai wo", "you love me"],
            ["gei wo yi ben shu", "give me a book"],
            ["ni bu shi xuesheng", "you are not a student"],
            ["wo mei you ni de bi", "I do not have your pen"]
            ];'''
    data = []
    
    srcLines = []
    tgtLines = []

    curIdx = -1

    def __init__(self, sourceLangFilePath, targetLangFilePath):
        print "Opening files... "
        srcF = open(sourceLangFilePath, "r")
        tgtF = open(targetLangFilePath, "r")
        print "Files are now in memory. Now splitting the lines... "
        self.srcLines = srcF.read().splitlines()
        self.tgtLines = tgtF.read().splitlines()
        self.srcLines = self.srcLines[1:1000]
        self.tgtLines = self.tgtLines[1:1000]
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
        return len(self.getAllSourceLanguageWords())


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