cealigner
=========

A Chinese-English parallel corpus aligner. 

### Project file description:

1.  **main.py**: the main function. This is where the code for model testing should be. Currently it does the following:

    1. Initializes a parallel corpus from two text files;
    2. Trains an IBM model with the corpus.

2.  **model.py**: contains classes for all models, including IBM Models and their optimized versions. Currently, this file contains:

    1.   *class* **ModelI**: an IBM Model I implementation
    
3.  **util.py**: helper classes and functions. Currently, this file contains:
    
    1.   *class* **ParallelCorpus**: a class that provides access to data in a parallel corpus. 
    2.   *function* **printDictionary**: a helper function that prints dictionary vertically. This provides a clearer view than that produced by the built-in `print` command.

4. **deprecated.py**: classes that contain past impelentations that are not used in the final release. I keep it here only because I sometimes need to review the code that I've written. this file contains:

    1.   *deprecated class* **NaiveAligner**: a model that considers only lexical translation probabilities (regardless of alignments or distortions)
    2.   *deprecated class* **IBM2Aligner**: an IBM Model II implementation.
    