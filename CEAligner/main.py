# -*- coding: utf-8 -*-

from util import ParallelCorpus
from model import ModelI#, ModelII
from collections import defaultdict


def main():
    #corpus = ParallelCorpus("/cs/guests/csgueste/Desktop/zh", "/cs/guests/csgueste/Desktop/en")
    #corpus = ParallelCorpus("/cs/natlang-data/Parallel_Corpora/cn-en/simp-chinese-training/train.all.tok.cn", "/cs/natlang-data/Parallel_Corpora/cn-en/simp-chinese-training/train.all.tok.en")
    #corpus = ParallelCorpus("/Users/Yuhuan/Desktop/zh.txt", "/Users/Yuhuan/Desktop/en.txt")
    #corpus = ParallelCorpus("/Volumes/Data/d/repos/dreamt/aligner/data/hansards.e", "/Volumes/Data/d/repos/dreamt/aligner/data/hansards.f")
    #corpus = ParallelCorpus("/Users/Yuhuan/Desktop/e", "/Users/Yuhuan/Desktop/f")
    #corpus = ParallelCorpus("/Volumes/Data/Download/zh-en/train.all.tok.cn", "/Volumes/Data/Download/zh-en/train.all.tok.en")
    #model = ModelI(corpus)
    
    
    #corpus = ParallelCorpus("c:/Users/Administrator/Desktop/f.txt", "c:/Users/Administrator/Desktop/e.txt")
    corpus = ParallelCorpus("E:/Users/Yuhuan/Desktop/e", "E:\Users\Yuhuan\Desktop\e");
    model1 = ModelI(corpus)
    #model2 = ModelII(model1, corpus)



if __name__ == '__main__':
    main()