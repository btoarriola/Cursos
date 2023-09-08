# Ejercicio 1
def sign(n):
    if(n>0):
        return 1
    elif(n<0):
        return -1
    else:return 0
    
sign(0)

# Ejercicio 2
def to_smash(total_candies):
    print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)

# Ejercicio 2

def to_smash(total_candies):
    if(total_candies>1):
        print("Splitting", total_candies, "candies")
        return total_candies % 3
    else:
        print("Splitting", total_candies, "candy")
        return total_candies % 3

to_smash(91)
to_smash(1)

# Ejercicio 3
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    return have_umbrella or rain_level < 5 and have_hood or not (rain_level > 0 and is_workday)


have_umbrella = False
rain_level = 0.0
have_hood = False
is_workday = False

actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Ejercicio 4
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    return (True if number<0 else False)
    pass 

# Ejercicio 5


def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return(True if (ketchup==True and mustard == True and onion==True) else False)
    pass
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return(True if (ketchup==False and mustard == False and onion==False) else False)
    pass
    
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    if(ketchup and mustard):
        return False
    elif(ketchup or mustard):
        return True
    return False
    pass

# Ejercicio 5

def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    if(ketchup and not mustard and not onion):
        print ("entro 1")
        return True
    elif(mustard and not onion ):
        print ("entro 2")
        return True
    elif(onion and not ketchup and not mustard):
        print ("entro 3")
        return True
    else: 
        print ("entro 4") 
        return False
        
    pass

exactly_one_topping(True, True, True)