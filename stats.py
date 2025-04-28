def wordcount(text):
    return len(text.split())

def charcount(text):
    statdict = {}
    for char in text:
        lowchar = char.lower()
        if lowchar in statdict:
            statdict[lowchar] += 1
        else:
            statdict[lowchar] = 1
    
    return statdict

def sortedstats(statdict):
    sortlistdict = []
    for k, v in statdict.items():
        sortlistdict.append({"char": k, "num": v})
    
    def sort_on(d):
        return d["num"]
    
    sortlistdict.sort(reverse=True, key=sort_on)
    return sortlistdict
