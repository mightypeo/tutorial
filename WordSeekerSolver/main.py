import sys
from collections import Counter

if __name__ == "__main__":
    wanted = list( "reinl")
    wanted.sort()
    wls = ''.join( wanted)
    wls_set = set( wls)
    wls_dict = Counter(wanted)

    dict = {}
    words = []
    f = open( 'words.txt', 'r')
    for line in f:
        word = line.strip()
        letters = list( word)
        letters.sort()
        ls = ''.join(letters)
        ls_set = set( ls)
        ls_dict = Counter( letters)

        if len(word) < 6 and len(ls) > 2:
            if ls_set.issubset(wls_set):
                found = True
                for c in ls_set:
                    if ls_dict[ c] > wls_dict[ c]:
                        found = None
                        break
                if found:
                    print ( word)

