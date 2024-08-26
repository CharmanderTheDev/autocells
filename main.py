import matplotlib.pyplot as plt
import math

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

graphs = []
for x in range(256):
    state = State(x)
    graph = []
    for x in range(12):
        graph.append(toNumber(state.binary))
        state = iterate(state)
    graphs.append(graph)

x = []
for i in range(12):
    x.append(i+1)

fig = plt.figure(figsize = (20,16))
ax = fig.add_axes([.1,.1,.8,.8])
ax.set_xticks((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,12))
ax.set_yticks((0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240,256))
ax.tick_params(axis='both', which='major', labelsize=25)
plt.rcParams['figure.constrained_layout.use'] = True
plt.tight_layout(pad=0)

for i in range(256):
    rgb = [i%8, (i%16)/8, (i%32)/16]
    if(rgb!=[0,0,0]):
        rgb = [float(i)/sum(rgb) for i in rgb]

    plt.plot(x, graphs[i], linewidth = 1, markersize=2, color = (rgb[0],rgb[1],rgb[2]))

plt.title('autocell systems', fontsize = 40)
plt.savefig('colorplot.png')