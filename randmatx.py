import numpy as np
import random

#vetor = []

#while len(vetor) < 12:
#    x = random.randint(0,10)
#    vetor.append(x)

#print(np.array(vetor).reshape(3,4))

####################
import random
 
# Function to generate
# and append them 
# start = starting range,
# end = ending range
# num = number of 
# elements needs to be appended
def Rand(start, end, num):
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return (np.array(res).reshape(3,4))
 
# Driver Code
num = 12
start = 0
end = 20
print(Rand(start, end, num))

