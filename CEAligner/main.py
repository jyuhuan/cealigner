# -*- coding: utf-8 -*-
from util import ParallelCorpus
from model import NaiveAligner, IBM2Aligner, IBMModel1

def main():
    #corpus = ParallelCorpus("/cs/guests/csgueste/Desktop/zh", "/cs/guests/csgueste/Desktop/en")
    #corpus = ParallelCorpus("/cs/natlang-data/Parallel_Corpora/cn-en/simp-chinese-training/train.all.tok.cn", "/cs/natlang-data/Parallel_Corpora/cn-en/simp-chinese-training/train.all.tok.en")
    corpus = ParallelCorpus("/Users/Yuhuan/Desktop/zh.txt", "/Users/Yuhuan/Desktop/en.txt")
    model = IBMModel1(corpus)

    
if __name__ == '__main__':
    main()