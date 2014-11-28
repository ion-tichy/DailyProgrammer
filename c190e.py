''' Webscraping sentiments '''
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python c190e.py <youtube-video-url>")
        sys.exit()
    url = sys.argv[1]
    