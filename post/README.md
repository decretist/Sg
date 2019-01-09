# Postprocessing and Analysis

`hamming.py` was an attempt to use Hamming distance (as opposed to regular expressions) as a way of identifying pairs of words that differed by one character. Not as useful in practice as I had hoped, but worth keeping the code for future reference.

```pylint --extension-pkg-whitelist=Levenshtein hamming.py```
