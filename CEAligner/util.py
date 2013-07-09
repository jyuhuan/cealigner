
class ParallelCorpus():
    
    data = [
                ["here are some chinese words", "zheli you yixie zhongwen ciyu"],
                ["i am a chinese", "wo shi zhongguoren"],
                ["i do not have a computer", "wo mei you diannao"],
                ["you should come to china some time in the future", "jianglai ni yinggai lai zhongguo kankan"],
                ["the weather in canada is awesome", "jianada de tianqi tai bang le"],
                ["i love you", "wo ai ni"],
                ["i adore you", "wo xihuan ni"]
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
        