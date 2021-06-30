def prim(b, a): 
      
    while (a) :
        if (not b[a]) :
            return False
          
        a //= 10
  
    return True
  
def maior_primo(c): 
  
    b = [True] * (c + 10) 
    b[0] = b[1] = False; 
    for i in range(2, c + 1) : 
        if (b[i]) : 
  
            for j in range(i * i, c + 1, i) : 
                b[j] = False
  
    while (True) :
        if (prim(b, c)):
            print(c)
            break
              
        else:
            c -= 1

                   
