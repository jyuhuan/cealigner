# -*- coding: utf-8 -*-


from util import ParallelCorpus
from model import Aligner

def main():
    corpus = ParallelCorpus()
    aligner = Aligner(corpus)
    
    print "".join(["asdf", "中文"])
    print "".join(["中文"])
    print "中文"
    

if __name__ == '__main__':
    main()