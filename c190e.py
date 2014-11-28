''' Webscraping sentiments '''
import sys

happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst'] 

def scrape(N): 
   pass


def output(N,sentiment,numHappy,numSad,generalFeeling):
    ''' The output message'''
    print("From a sample size of "+str(N)+" persons.\n The sentiment is mostly"+sentiment
          +"\nIt contained "+str(numHappy)+" Happy keywords and "+str(numSad)
          +" Sad keywords\n The general feelings towards this video were "+generalFeeling)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python c190e.py <youtube-video-url>")
        sys.exit()
    url = sys.argv[1]
    