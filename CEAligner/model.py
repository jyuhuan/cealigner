from util import ParallelCorpus, printDictionary


class Aligner(object):
    transProbOfTargetGivenSource = {}
    countOfTargetGivenSource = {}
    totalCountOfSource = {}
    normalizationForTarget = {}
    
    def __init__(self, corpus):
        
        # obtain corpus
        corpus = ParallelCorpus()
        targetWordCount = corpus.getTargetLanguageWordCount()
        
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
                    self.transProbOfTargetGivenSource[(tgtWord, srcWord)] = 1.0 / targetWordCount
                    # set count(target|source) to zeros
                    self.countOfTargetGivenSource[(tgtWord, srcWord)] = 0;
                # set total(source) to zeros
                self.totalCountOfSource[srcWord] = 0;
        ''' END: INITIALIZATION '''
                
        ''' ============================================================================== '''
        ''' BEGIN: EM ITERATION '''
        ''' ============================================================================== '''
        for i in range(0, 10):
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
                        self.totalCountOfSource[srcWord] += self.transProbOfTargetGivenSource[(tgtWord, srcWord)] / self.normalizationForTarget[tgtWord];
                        
            
            uniqueSrcWords = corpus.getAllSourceLanguageWords()
            uniqueTgtWords = corpus.getAllTargetLanguageWords()
            
            for srcWord in uniqueSrcWords:
                for tgtWord in uniqueTgtWords:
                    safeCountOfTagetGivenSource = 0.0;
                    if self.countOfTargetGivenSource.has_key((tgtWord, srcWord)):
                        safeCountOfTagetGivenSource = self.countOfTargetGivenSource[(tgtWord, srcWord)]
                    
                    self.transProbOfTargetGivenSource[(tgtWord, srcWord)] = safeCountOfTagetGivenSource / self.totalCountOfSource[srcWord]
                    
        ''' END: EM ITERATION '''
        
                
                    
        print self.transProbOfTargetGivenSource
        print self.countOfTargetGivenSource
        print self.totalCountOfSource
        print self.normalizationForTarget
        
      
    def train(self):
        return

    