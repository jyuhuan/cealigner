# -*- coding: utf-8 -*-
from util import ParallelCorpus
from model import NaiveAligner, IBM2Aligner

def main():
    corpus = ParallelCorpus()
    #aligner = NaiveAligner(corpus)
    aligner = IBM2Aligner(corpus)

if __name__ == '__main__':
    main()