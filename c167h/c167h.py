class Matrix(dict):
    def __init__(self,size=0):
        self.size = size

    def addEntry(self, row,col,value):
        if row > self.size or row < 0:
            raise ValueError('Invalid row index!')
        if col > self.size or col < 0:
            raise ValueError('Invalid column index!')
        self[(row,col)] = value

    def __missing__(self,key):
        return -1
        
    def degree(self,vertex):
        return len([ k for k in self if k[0] == vertex and self[k] != -1])

        
def getAlphaIndex(num):
    if 0<= num and num < 26:
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[num]   
        
def getCellAlphaIndex(coord):
    return (getAlphaIndex(coord[0]),getAlphaIndex(coord[1]))

def loadMatrix(filename):
    with open(filename) as f:
        lines = f.readlines()
        size = int(lines[0].strip())
        m = Matrix(size)
      
        for i,l in enumerate(lines[1:]):
            row = l.strip().split(',')
            print("Adding row ",row)
            for j in range(0, size):
                print("Adding entry",i,j,"=>",row[j])
                m.addEntry(i,j,int(row[j]))
                  
        return m                    


def checkRoute(matrix):
    odd_nodes = [i for i in range(0,matrix.size) if matrix.degree(i) % 2 != 0]
    print("We have ",len(odd_nodes),"odd degree nodes")
    if len(odd_nodes) == 0:
        print("Any")
        return
    
    # check paths starting in odd nodes
    for node in odd_nodes:
        start = node
        end = node
        # check distance to nearest neighbours
        
        
if __name__ == "__main__":

    filename1 = "example1matrix.txt"
    filename2 = "example2matrix.txt"
    filename3 = 'challengematrix.txt'
    m = loadMatrix(filename2)
    for i in range(0,m.size):
      print(i,[m[i,j] for j in range(0,m.size)])
      
    checkRoute(m)
    