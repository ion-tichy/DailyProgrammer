import sys
import random
''' C189E: Simple CLI Hangman '''

def init(wordlist):
    ''' Read in words according to user specified difficulty '''
    diff_prompt = "Pick a difficulty: easy(0),medium(1),hard(2)\n >:"
    diff = input(diff_prompt)
    while diff not in ['0','1','2']:
        if diff == "":
            sys.exit()
        diff = input("Invalid Input!\n"+diff_prompt)
    dims = (7-float(diff)-1,
            15//(float(diff)+1))
    print("Initialized game, using words of length ",dims[0],"->",dims[1])
    with open(wordlist,'r') as f:
        return [w.strip() for w in f if len(w.strip()) <= dims[1] and len(w.strip()) >= dims[0]],int(diff)
           
def start(word,lives):
    ''' Start a round using #word and a certain amount of lives '''
    disp_word = " ".join(["_ " for w in word])
    disp_prompt = disp_word+"\nGuess letter:"
    guessed = set([])
    guess = input(disp_prompt+"("+str(lives)+" lives left):")
    while guess != "" and lives > 1:
        disp_word = ""
        if guess[0] in word:
            guessed.add(guess[0])
        else:
           lives -= 1
        disp_word = " ".join(w if (w in guessed) else "_" for w in word)
        if disp_word == word:        
            print("You win, the word was ",word)
            return    
        guess = input(disp_word+"\nGuess letter:"+"("+str(lives)+" lives left):")
    print("You loose, the word was:",word)              

if __name__ == "__main__":
    wlist = "enable1.txt"
    if len(sys.argv) > 2:
        print("Usage: python c189e.py (<your-word-list>)\n Will use enable1.txt on default.")
        sys.exit()
    if len(sys.argv) == 2:
        wlist = sys.argv[1]
        print("Enabling custom wordlist",wlist)
    wordlist,diff = init(wlist)
    start(random.sample(wordlist,1)[0],9 - 3*int(diff))