# -*- coding: utf-8 -*-
class ParallelCorpus():
    
    data = [
                ["here are some chinese words", "这里 有 一些 中文 词语"],
                ["i am a chinese", "我 是 中国人"],
                ["i do not have a computer", "我 没 有 电脑"],
                ["you should come to china some time in the future", "将来 你 应该 来 中国 看 看"],
                ["the weather in canada is awesome", "加拿大 的 天气 太 好 了"],
                ["i love you", "我 爱 你"],
                ["i adore you", "我 喜欢 你"]
                ];
    
    '''data = [
            ["das haus", "the house"],
            ["das Buch", "the book"],
            ["ein Buch", "a book"]
            ];'''

    curIdx = -1

    def __init__(self):
        return
    
    def getEntryCount(self):
        return len(self.data)
      
    def getEntryAt(self, idx):
        return self.data[idx]
    
    def getAllSourceLanguageWords(self):
        allWords = set()
        for pair in self.data:
            wordsInCurPair = pair[0].split()
            for word in wordsInCurPair:
                allWords.add(word)
        return allWords
    
    def getSourceLanguageWordCount(self):
        return len(self.getAllSourceLanguageWords())
    
    def getAllTargetLanguageWords(self):
        allWords = set()
        for pair in self.data:
            wordsInCurPair = pair[1].split()
            for word in wordsInCurPair:
                allWords.add(word)
        return allWords
    
    def getTargetLanguageWordCount(self):
        return len(self.getAllSourceLanguageWords())


def printDictionary(dic):
    for key in dic.keys():
        keysStr = ""
        for i in range(0, len(key)):
            keysStr += key[i] + ", "
        keysStr = keysStr[:-2]
        print "".join(keysStr) + " = " + str(dic[key])
        