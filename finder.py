import re
import numpy as np
def finder(searchin, look):
    """
    Finds a collection of strings inside a larger string, returns a dict of all matches

    Params:
    searchin: str to be searched for items in the look list
    look: str list of strings to be searched for.

    Returns a dict, key: str, value: indexes
    """
    lore = ""
    #import ipdb; ipdb.set_trace()
    for expr in look:
        lore += "("+expr+")|"
    lore = lore[:-1] # remove the last |
    p = re.compile(lore)
    rdict = {}
    for m in p.finditer(searchin):
        if m.group() in rdict:
            rdict[m.group()].append(m.start())
        else:
            rdict[m.group()] = [m.start()]
    return rdict

def word2i(searchin, look, offset, which = 0):
    """
    takes in a mass string and looks for values with names, storing the items after the names using an offset and a word selector
    args:
        searchin: a string to be search
        look: list of words to be searched
        offset: offset from the match index location to extract to do a split() to get numerical values
        which: which item to take in the split() object to obtain the value
    """
     rdict = finder(searchin, look)
     numdict = {}
     for key, value in rdict.items():
         for indexo in value:
             index = indexo +len(key)
             if key in numdict:
                 numdict[key].append(float(searchin[index: index + offset].split()[which]))
             else:
                 numdict[key] = [float(searchin[index: index + offset].split()[which])]
     return numdict
