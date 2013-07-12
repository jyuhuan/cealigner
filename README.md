cealigner
=========

A Chinese-English parallel corpus aligner. 

### Project file description:

1.  **main.py**: the main function. This is where you should test and run the model.
2.  **model.py**: contains classes for all models, including IBM Models and their optimized versions. Currently, this file contains:

    1.   *class* **NaiveAligner**: a model that considers only lexical translation probabilities (regardless of alignments or distortions)
    2.   *class* **IBM2Aligner**: an IBM Model 2 implementation.
    
    
3.  **util.py**: helper classes and functions. Currently, this file contains:
    
    1.   *class* **ParallelCorpus**: a class that provides access to data in a parallel corpus. 
    2.   *function* **printDictionary**: a helper function that prints dictionary vertically. This provides a clearer view than that invoked by the `print` command.
