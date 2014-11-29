''' Webscraping sentiments '''
import sys
import urllib3

from html.parser import HTMLParser


YTPATH = "http://www.youtube.com/all_comments?v="

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__(self)
        self.sad = 0
        self.happy = 0
        
    def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)
        if tag == "div":
            for k,v in attrs:
               if k == "class":
                   print("class:"+v)
        
    def handle_startendtag(self,tag,attrs):
        pass
    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass
    def handle_data(self, data):
        pass

### /html/body/div[2]/div[3]/div/div[5]/div/div/div/div/div/div[2]/div/div[2]/div/div[3]/div[1]


##    <div class="comments embedded">
  ##     <div class="comment-item...">
     ##     <div class="content">
        ###     <div class="comment-text">
        ##       <div class="comment-text-content">
        ##           $Text
               
happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst'] 

def scrape(N): 
   http = urllib3.PoolManager()
   r = http.request('GET',YTPATH+"Kp1RALicgbQ")
   parser = MyHTMLParser()
   parser.feed(str(r.data))
   
    
def output(N,sentiment,numHappy,numSad,generalFeeling):
    ''' The output message'''
    print("From a sample size of "+str(N)+" persons.\n The sentiment is mostly "+sentiment
          +"\nIt contained "+str(numHappy)+" Happy keywords and "+str(numSad)
          +" Sad keywords\n The general feelings towards this video were "+generalFeeling)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python c190e.py <youtube-video-url>")
        sys.exit()
    url = sys.argv[1]
    scrape(0)
 #   output('All','Happy' if h>s else 'Sad',h,s,'unknown')