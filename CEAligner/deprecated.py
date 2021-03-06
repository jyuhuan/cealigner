# -*- coding: utf-8 -*-
from collections import defaultdict
from util import printDictionary, tryGetDoubleValueByKeyFromDic,\
    tryIncDoubleValueAtKeyInDic, printTopResultsInDic
import gc
import time




''' tgt = target '''
''' src = source '''
''' cur = current '''
''' lang = language '''


class NaiveAligner(object):
    epoch = 100
    
    transProbOfTargetGivenSource = {}
    countOfTargetGivenSource = {}
    countOfSourceWordOccurrence = {}
    normalizationForTarget = {}
    
    def __init__(self, corpus):
        
        tgtLangWordCount = corpus.getTargetLanguageWordCount()
        
        ''' ============================================================================== '''
        ''' BEGIN: INITIALIZATION '''
        ''' ============================================================================== '''
        # iterate through the sentence pairs in the corpus
        for x in range(0, corpus.getEntryCount()):
            # get the current sentence pair
            curPair = corpus.getEntryAt(x)
            
            # split both sentences into words
            srcWords = curPair[0].split()
            tgtWords = curPair[1].split()
            
            # initializations
            for srcWord in srcWords:
                for tgtWord in tgtWords:
                    # uniformly assign values to the translation probabilities of target words given source words, i.e. t(target|source)
                    self.transProbOfTargetGivenSource[(tgtWord, srcWord)] = 1.0 / tgtLangWordCount
                    # set count(target|source) to zeros
                    self.countOfTargetGivenSource[(tgtWord, srcWord)] = 0;
                # set total(source) to zeros
                self.countOfSourceWordOccurrence[srcWord] = 0;
        ''' END: INITIALIZATION '''
                
        ''' ============================================================================== '''
        ''' BEGIN: EM ITERATION '''
        ''' ============================================================================== '''
        for i in range(0, self.epoch):
            for x in range(0, corpus.getEntryCount()):
                # get the current sentence pair
                curPair = corpus.getEntryAt(x)
                
                # split both sentences into words
                srcWords = curPair[0].split()
                tgtWords = curPair[1].split()
                
                # calculate the normalization term
                for tgtWord in tgtWords:
                    self.normalizationForTarget[tgtWord] = 0
                    for srcWord in srcWords:
                        self.normalizationForTarget[tgtWord] += self.transProbOfTargetGivenSource[(tgtWord, srcWord)];
                        
                # collect counts
                for tgtWord in tgtWords:
                    for srcWord in srcWords:
                        self.countOfTargetGivenSource[(tgtWord, srcWord)] += self.transProbOfTargetGivenSource[(tgtWord, srcWord)] / self.normalizationForTarget[tgtWord];
                        self.countOfSourceWordOccurrence[srcWord] += self.transProbOfTargetGivenSource[(tgtWord, srcWord)] / self.normalizationForTarget[tgtWord];
                        
                # TODO: I don't know why the following block affects the result
                uniqueSrcWords = corpus.getAllSourceLanguageWords()
                uniqueTgtWords = corpus.getAllTargetLanguageWords()
                
        for srcWord in uniqueSrcWords:
            for tgtWord in uniqueTgtWords:
                safeCountOfTagetGivenSource = 0.0;
                if self.countOfTargetGivenSource.has_key((tgtWord, srcWord)):
                    safeCountOfTagetGivenSource = self.countOfTargetGivenSource[(tgtWord, srcWord)]
                
                self.transProbOfTargetGivenSource[(tgtWord, srcWord)] = safeCountOfTagetGivenSource / self.countOfSourceWordOccurrence[srcWord]
                    
        ''' END: EM ITERATION '''
        
                
                    
        '''print self.transProbOfTargetGivenSource
        print self.countOfTargetGivenSource
        print self.countOfSourceWordOccurrence
        print self.normalizationForTarget'''
        
        printDictionary(self.transProbOfTargetGivenSource)
      
    def train(self):
        return







class IBM2Aligner:
    
    # parameters
    t = {}  # key: (srcWordIdx, tgtWordIdx). This represents t(tgtWordIdx|srcWordIdx)
    q = {}  # key: (srcWordIdx, tgtWordIdx, srcSentenceLength, tgtSentenceLength). This represents t(srcWordIdx|tgtWordIdx,srcSentenceLength,tgtSentenceLength)
    
    # counts
    srcTgtTransCounts = {}      # key: (srcWord, tgtWord). This represents c(source,target)
    srcOccurCounts = {}         # key: (srcWord). This represents c(source)
    srcTgtAlignCounts = {}      # key: (srcWordIdx, tgtWordIdx, lengthOfSrcSentence, lengthOfTgtSentence). This represents c(source-index|target-index, source-length, target-length)
    sentenceCoocurCounts = {}   # key: (tgtWordIdx, lengthOfSrcSentence, lengthOfTgtSentence). This represents c(target-index, source-length, target-length)
    
    epoch = 100
    
    
    def calcInc(self, tgtWordIdx, srcWordIdx, tgtWords, srcWords, tgtSentenceLength, srcSentenceLength):
        numerator = self.q[(srcWordIdx, tgtWordIdx, srcSentenceLength, tgtSentenceLength)] * self.t[(srcWords[srcWordIdx], tgtWords[tgtWordIdx])];
        denominator = 0.0;
        for j in range(0, srcSentenceLength):
            denominator += self.q[(j, tgtWordIdx, srcSentenceLength, tgtSentenceLength)] * self.t[(srcWords[j], tgtWords[tgtWordIdx])];
        return numerator / denominator
    
    def __init__(self, corpus):
        
        ''' INITIALIZATION: ALL PARAMETERS TO RANDOM VALUES '''
        for pairIdx in range(0, corpus.getEntryCount()):
            # get the current sentence pair
            curPair = corpus.getEntryAt(pairIdx)
            
            # split both sentences into words
            srcWords = curPair[0].split()
            tgtWords = curPair[1].split()
            
            # initializations
            for srcWordIdx in range(0, len(srcWords)):
                for tgtWordIdx in range(0, len(tgtWords)):
                    
                    self.t[(srcWords[srcWordIdx], tgtWords[tgtWordIdx])] = 0.5
                    self.q[(srcWordIdx, tgtWordIdx, len(srcWords), len(tgtWords))] = 0.5
        
        for epochIdx in range(0, self.epoch):
            
            ''' INITIALIZATION: SET ALL COUNTS TO ZEROS '''
            for pairIdx in range(0, corpus.getEntryCount()):
                # get the current sentence pair
                curPair = corpus.getEntryAt(pairIdx)
                
                # split both sentences into words
                srcWords = curPair[0].split()
                tgtWords = curPair[1].split()
                
                # initializations
                for srcWordIdx in range(0, len(srcWords)):
                    for tgtWordIdx in range(0, len(tgtWords)):
                        self.srcTgtTransCounts[(srcWords[srcWordIdx], tgtWords[tgtWordIdx])] = 0.0
                        self.srcOccurCounts[srcWords[srcWordIdx]] = 0.0
                        self.srcTgtAlignCounts[(srcWordIdx, tgtWordIdx, len(srcWords), len(tgtWords))] = 0.0
                        self.sentenceCoocurCounts[(tgtWordIdx, len(srcWords), len(tgtWords))] = 0.0
                                        
            ''' ITERATE THROUGH ALL SENTENCE PAIRS '''
            for pairIdx in range(0, corpus.getEntryCount()):
                # get the current sentence pair
                curPair = corpus.getEntryAt(pairIdx)
                
                # split both sentences into words
                srcWords = curPair[0].split()
                tgtWords = curPair[1].split()
                
                # inspect every combination of words from each sentence
                for tgtWordIdx in range(0, len(tgtWords)):
                    for srcWordIdx in range(0, len(srcWords)):
                        inc = self.calcInc(tgtWordIdx, srcWordIdx, tgtWords, srcWords, len(tgtWords), len(srcWords))
                        self.srcTgtTransCounts[(srcWords[srcWordIdx], tgtWords[tgtWordIdx])] += inc
                        self.srcOccurCounts[srcWords[srcWordIdx]] += inc
                        self.srcTgtAlignCounts[srcWordIdx, tgtWordIdx, len(srcWords), len(tgtWords)] += inc
                        self.sentenceCoocurCounts[tgtWordIdx, len(srcWords), len(tgtWords)] += inc
                        
        
        uniqueSrcWords = corpus.getAllSourceLanguageWords()
        uniqueTgtWords = corpus.getAllTargetLanguageWords()
        
        for srcWord in uniqueSrcWords:
            for tgtWord in uniqueTgtWords:
                srcTgtTransCounts_safe = 0.0;
                srcOccurCounts_safe = 0.0;
                
                if self.srcTgtTransCounts.has_key((srcWord, tgtWord)):
                    srcTgtTransCounts_safe = self.srcTgtTransCounts[(srcWord, tgtWord)]
                
                if self.srcOccurCounts.has_key(srcWord):
                    srcOccurCounts_safe = self.srcOccurCounts[srcWord]
                
                self.t[(srcWord, tgtWord)] = srcTgtTransCounts_safe / srcOccurCounts_safe
        
        printDictionary(self.t)



class IBMModel1:
    t = defaultdict()
    srcTgtProbs = defaultdict()    # t(e|f)
    srcTgtCounts = defaultdict()   # count(e|f)
    tgtNormTerms = defaultdict()   # s-total(e)
    srcCounts = defaultdict()      # total(f)
    
    def __init__(self, corpus):
        gc.disable()
        tgtLangVocabCount = corpus.getTargetLanguageWordCount()
        srcLangCount = corpus.getSourceLanguageWordCount()
        
        ''' INIT: translation probabilities '''
        for pairIdx in range(0, corpus.getEntryCount()):
            curPair = corpus.getEntryAt(pairIdx)
            srcWords = curPair[0].split()
            tgtWords = curPair[1].split()
            
            for srcWord in srcWords:
                for tgtWord in tgtWords:
                    self.srcTgtProbs[(srcWord, tgtWord)] = 1.0 / tgtLangVocabCount;
        
        ''' LOOP: epochs '''
        uniqueWordsInSrcVocab = corpus.getAllSourceLanguageWords()
        uniqueWordsInTgtVocab = corpus.getAllTargetLanguageWords()
        
        print "Number of unique source words = " + str(len(uniqueWordsInSrcVocab))
        print "Number of unique target words = " + str(len(uniqueWordsInTgtVocab))
        
        print "loop start"
        t1 = time.time()
        for srcWord in uniqueWordsInSrcVocab:
            for tgtWord in uniqueWordsInTgtVocab:
                self.srcTgtCounts[(srcWord, tgtWord)] = 0.0
                self.srcCounts[srcWord] = 0.0
        print "loop end"
        t2 = time.time()
        print str(t2 - t1) + "\n"
        
        for epochIdx in range(0, 10):  # this loop is run until convergence
            ''' initialize both counts '''            
            for srcWord in uniqueWordsInSrcVocab:
                for tgtWord in uniqueWordsInTgtVocab:
                    self.srcTgtCounts[(srcWord, tgtWord)] = 0.0
                    self.srcCounts[srcWord] = 0.0
            
            t3 = time.time()
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
            t4 = time.time()
            print str(epochIdx) + "th epoch ran for " + str(t4 - t3) + "\n"
            
            t5 = time.time()        
            print "now estimating trans probs"
            ''' estimate trans probs '''
            for srcWord in uniqueWordsInSrcVocab:
                for tgtWord in uniqueWordsInTgtVocab:
                    self.srcTgtProbs[(srcWord, tgtWord)] = self.srcTgtCounts[(srcWord, tgtWord)] / self.srcCounts[srcWord]
            print "estimation done"  
            t6 = time.time()
            print str(t6 - t5) + "\n"
        printTopResultsInDic(self.srcTgtProbs, 0.09)