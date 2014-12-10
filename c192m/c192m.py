# http://www.reddit.com/r/dailyprogrammer/comments/2ovt2i/20141210_challenge_192_intermediate_markov_chain/

# input: wordlist

# 1. build occurrence matrix
# 2. for input word: predict using the occ matrix if word is misspelled

class MarkovChain(dict):
    ''' The Markov Chain used for validation '''
    def __init__(self):
        self.vocab = set([])
        self.size = 0
        dict.__init__(self)
        
    def __missing__(self,key):
        return 0
    
    def train(self,trainfile):
        ''' Expected format: 1 word per line '''
        with open(trainfile) as f:
            print("Starting training using file ",trainfile,"...")
            for line in f:
                self.addWord(line.strip())
            print("Done training markov chain....")
    
    def addWord(self,word):
        ''' Adds a word to the occurrence matrix '''
        for v,w in zip(word[:len(word)-1],word[1:len(word)]):
            self[(v,w)] += 1
            self.vocab.add(v)
            self.vocab.add(w)
            self.size += 1
    
    def getProbability(self, word):
        ''' returns the probability of the word '''
        prob = 1.0
        if len(word) == 0:
            return 0.0
        for v,w in zip(word[:len(word)-1],word[1:len(word)]):
            prob *= self[(v,w)]/self.size
        return prob
        
    def __str__(self):
        out = "\t"
        out += "\t".join(sorted(self.vocab))
        out +="\n"
        for v in sorted(self.vocab):
          out += v+"\t"
          for w in sorted(self.vocab):
              out += str(self[(v,w)])+"\t"
          out +="\n"
        return out

def test():
    ''' Test method '''
    mc = MarkovChain()
    mc.train('trainfile.txt')
    correct = "aardvark"
    wrong = "axrztog"
    print("Correct word ",correct,mc.getProbability(correct))
    print("Wrong word ", wrong, mc.getProbability(wrong))
    print(mc)
if __name__ == "__main__":
    test()
    