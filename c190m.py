# http://www.reddit.com/r/dailyprogrammer/comments/2nihz6/20141126_challenge_190_intermediate_words_inside/
winner = ""
with open('enable1.txt') as f:
    print("Parsing file...")
    # read out words from file and cache them
    words = {w.strip():0 for w in f}
    print("Read in ", len(words)," words") 
  
    [words[w].add(w[j:j+i]) for w in words for i in range(2,len(w)-1) for j in range(0,(len(w) - i+1))                        
                            if w[j:j+i] in words ]         
    print("Computing winner....")
    max = 0
    for w in words:
        # find the word with the most subwords
        if len(words[w]) > max:
            max,winner = len(words[w]),w

print("Most words:",winner)
print("Contais:",words[winner])