# http://www.reddit.com/r/dailyprogrammer/comments/2ovt2i/20141210_challenge_192_intermediate_markov_chain/

# input: wordlist

# 1. build occurrence matrix
# 2. for input word: predict using the occ matrix if word is misspelled

class MarkovChain(dict):
    ''' The Markov Chain used for validation '''
    def __missing__(self,key):
        return 0
    
    def addWord(self,word):
        ''' Adds a word to the occurrence matrix '''
        pass
    
    def getProbability(self, word):
        ''' returns the probability of the word '''
        pass
        
        

def test():
    ''' Test method '''
    pass

if __name__ == "__main__":
    pass
    