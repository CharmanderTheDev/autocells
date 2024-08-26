class State:
    binary = [0,0,0,0,0,0,0,0]
    
    def __init__(self, num):
        for x in range(7,-1,-1):
            self.binary[7-x] = num//(2**x)
            num%=(2**x)
    
    def get(self, num):
        if(num>=0 and num<=7):
            return(self.binary[num])
        else:
            return(0)
    
def toNumber(binary):
    num = 0;
    for i in range(0, len(binary)):
        num+=(binary[i]*(2**(len(binary)-i-1)))
    return(num)


def iterate(state):
    nextbin = [0,0,0,0,0,0,0,0]
    for x in range(0,8):
        one = state.get(x-1)
        two = state.get(x)
        three = state.get(x+1)
        nextbin[x] = state.get(toNumber([one,two,three]))
    return(State(toNumber(nextbin)))
