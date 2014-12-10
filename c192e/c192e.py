# http://www.reddit.com/r/dailyprogrammer/comments/2onyoq/2014128_challenge_192_easy_carry_adding/
from functools import reduce
# attention with the carry, can be greater than 1 now (never greater than 9 tho)
def add(inp):
    ## format step: format numbers into lists of equal length ##
    print(inp+"=")
    numbers = inp.split("+")
    maxlen = max([len(n) for n in numbers])
    [print(n.rjust(maxlen -len(n)+1," ")) for n in numbers] 
    numbers = normalize(numbers,maxlen)
   
    ## calc step: add columns and update carry ###
    result = []
    carry = 0
    carrystr = ""

    for i in range(0,maxlen):
        sum = reduce(lambda x,y: x+y,[int(n[::-1][i]) for n in numbers])
        sum += carry
        result.append(sum%10)
        carry = sum//10
        carrystr += str(carry) if carry > 0 else " "
    
    if carry > 0:
        result.append(carry)       
    print(carrystr)
    print("".join(['-' for i in range(0,maxlen)]))    
    print("".join([str(x) for x in result[::-1]]),"\n")
            
    
def normalize(nums,maxlen):
    ''' Normalizes input numbers to maxlength.
        e.g.: maxlen=3: '1' becomes '001'
    '''        
    return  ["".join(['0' for i in range(0,maxlen - len(n))])+n if len(n)< maxlen else n for n in nums]

def test1():
    add("8765+305")
    add("12+34+56+78+90")
    add("999999+1")

    
if __name__ == "__main__":
     test1()