# Ejercicio 1
print("ejercicio 1------------")
def select_second(L):
    if(len(L)>1):
        return L[1]
    else: return None
    pass

# Ejercicio 2
print("ejercicio 2------------")
def losing_team_captain(teams):
    nlist=list(reversed(teams))
    
    return nlist[0][1]
    
    pass

# Ejercicio 3
print("ejercicio 3------------")
def purple_shell(racers):

    p1=racers[0]
    p2=racers[-1]
    racers[0]=p2
    racers[-1]=p1
    pass

# Ejercicio 4
print("ejercicio 4------------")
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

lengths = [3,2,0,2]

# Ejercicio 5
print("ejercicio 5------------")
def fashionably_late(arrivals, name):

    nlist=arrivals[round(len(arrivals)/2): len(arrivals)]
    if (arrivals[-1]==name):
        return False
    elif(name in nlist):
        return True
    
    else:
        return False
    pass