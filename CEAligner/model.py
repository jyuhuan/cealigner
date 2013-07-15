from collections import defaultdict
from util import printTopResultsInDic

class ModelI:
    t = defaultdict()
    srcTgtProbs = defaultdict()    # t(e|f)
    srcTgtCounts = defaultdict()   # count(e|f)
    tgtNormTerms = defaultdict()   # s-total(e)
    srcCounts = defaultdict()      # total(f)
    
    def __init__(self, corpus):
        tgtLangVocabCount = corpus.getTargetLanguageWordCount()
        
        ''' INIT: translation probabilities '''
        for pairIdx in range(0, corpus.getEntryCount()):
            curPair = corpus.getEntryAt(pairIdx)
            srcWords = curPair[0].split()
            tgtWords = curPair[1].split()
            
            for srcWord in srcWords:
                for tgtWord in tgtWords:
                    self.srcTgtProbs[(srcWord, tgtWord)] = 1.0 / tgtLangVocabCount;
        
        uniqueWordsInSrcVocab = corpus.getAllSourceLanguageWords()
        uniqueWordsInTgtVocab = corpus.getAllTargetLanguageWords()
        
        print "Number of unique source words = " + str(len(uniqueWordsInSrcVocab))
        print "Number of unique target words = " + str(len(uniqueWordsInTgtVocab))
        
        for srcWord in uniqueWordsInSrcVocab:
            for tgtWord in uniqueWordsInTgtVocab:
                self.srcTgtCounts[(srcWord, tgtWord)] = 0.0
                self.srcCounts[srcWord] = 0.0
        
        ''' LOOP: epochs '''
        for epochIdx in range(0, 10):  # this loop is run until convergence
            ''' initialize both counts '''            
            for srcWord in uniqueWordsInSrcVocab:
                for tgtWord in uniqueWordsInTgtVocab:
                    self.srcTgtCounts[(srcWord, tgtWord)] = 0.0
                    self.srcCounts[srcWord] = 0.0
            
            ''' examine each pair in the corpus '''
            for pairIdx in range(0, corpus.getEntryCount()):
                curPair = corpus.getEntryAt(pairIdx)
                srcWords = curPair[0].split()
                tgtWords = curPair[1].split()
                
                ''' calc normalization term '''
                for tgtWord in tgtWords:
                    self.tgtNormTerms[tgtWord] = 0
                    for srcWord in srcWords:
                        self.tgtNormTerms[tgtWord] += self.srcTgtProbs[(srcWord, tgtWord)]
                
                ''' collect count '''
                for tgtWord in tgtWords:
                    for srcWord in srcWords:
                        inc = self.srcTgtProbs[(srcWord, tgtWord)] / self.tgtNormTerms[tgtWord]
                        self.srcTgtCounts[(srcWord, tgtWord)] += inc
                        self.srcCounts[srcWord] += inc
            
            print "now estimating trans probs"
            ''' estimate trans probs '''
            for srcWord in uniqueWordsInSrcVocab:
                for tgtWord in uniqueWordsInTgtVocab:
                    self.srcTgtProbs[(srcWord, tgtWord)] = self.srcTgtCounts[(srcWord, tgtWord)] / self.srcCounts[srcWord]
            print "estimation done"  
        printTopResultsInDic(self.srcTgtProbs, 0.5)
        
        ''' DECODING '''
        alignments = []
        for pairIdx in range(0, corpus.getEntryCount()):
            curPair = corpus.getEntryAt(pairIdx)
            srcWords = curPair[0].split()
            tgtWords = curPair[1].split()
            
            alignmentInCurPair = []
            
            for srcWordIdx in range(0, len(srcWords)):
                bestTgtWordIdx = 0
                bestSrcTgtProb = 0
                for tgtWordIdx in range(0, len(tgtWords)):
                    transProb = self.srcTgtProbs[(srcWords[srcWordIdx], tgtWords[tgtWordIdx])]
                    if transProb > bestSrcTgtProb:
                        bestSrcTgtProb = transProb
                        bestTgtWordIdx = tgtWordIdx
                alignmentInCurPair.append([srcWordIdx, bestTgtWordIdx])
            alignments.append(alignmentInCurPair)
        print alignments
        
        outputStr = ""
        for sentence in alignments:
            for word in sentence:
                outputStr += str(word[0]) + "-" + str(word[1]) + " "
            outputStr += "\n"
        outputFile = open("c:/Users/Administrator/Desktop/a.txt", "w")
        outputFile.write(outputStr)
            




        ''' DECODING '''
        alignmentsText = []
        for pairIdx in range(0, corpus.getEntryCount()):
            curPair = corpus.getEntryAt(pairIdx)
            srcWords = curPair[0].split()
            tgtWords = curPair[1].split()
            
            alignmentInCurPair = []
            
            for srcWord in srcWords:
                bestTgtWord = ""
                bestSrcTgtProb = 0.0
                for tgtWord in tgtWords:
                    transProb = self.srcTgtProbs[(srcWord, tgtWord)]
                    if transProb > bestSrcTgtProb:
                        bestSrcTgtProb = transProb
                        bestTgtWord = tgtWord
                alignmentInCurPair.append([srcWord, bestTgtWord])
            alignmentsText.append(alignmentInCurPair)
        print alignmentsText
        
        outputStr2 = ""
        for sentence in alignmentsText:
            for word in sentence:
                outputStr2 += word[0] + "-" + word[1] + " "
            outputStr2 += "\n"
        outputFile = open("c:/Users/Administrator/Desktop/a.str.txt", "w")
        outputFile.write(outputStr2)