from util import ParallelCorpus
from model import Aligner

def main():
    corpus = ParallelCorpus()
    aligner = Aligner(corpus)

if __name__ == '__main__':
    main()