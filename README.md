## Sg Case Statements

[St. Gallen, Stiftsbibliothek, Cod. Sang. 673](https://www.e-codices.unifr.ch/en/csg/0673)

### Stage 1

(31 December 2018)

- [x] install wdiff-1.2.2 in /usr/local/bin
---
Save Sg Hypothetical.docx as Plain Text (.txt),\
Text encoding: Other encoding: Western (ASCII),\
End lines with: CR/LF
```
% vim Sg_Hypothetical.txt
:set fileformat=unix
:w
```

### Stage 1a

(Add Causa Prima and C.1)

### Stage 2

(Create Friedberg-spelling version of text)

### Reminders:

```
git diff -U0 --word-diff
```
```
:%s/\s\+/\r/g
```
```
:%s/\n/\ /g
```
but remember to remove the trailing space this leaves behind!
```
:g/\<quae\>/s//que/gp
```

