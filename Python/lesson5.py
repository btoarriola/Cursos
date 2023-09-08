# Ejercicio 1
def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False

def has_lucky_number(nums):
    n=0
    for num in nums:
        if ((num % 7) == 0):
            n=n+1
    if n>=1:
        return True
    else:
        return False

# Ejercicio 2
def elementwise_greater_than(L, thresh):
    nl=[]
    for li in L:
        if li>thresh:
            nl.append(True)
        else:
            nl.append(False)
        
    return nl
    pass

# Ejercicio 3
def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False
    pass

# Ejercicio 4
def estimate_average_slot_payout(n_runs):
    payouts = [play_slot_machine()-1 for i in range(n_runs)] 
    avg_payout = sum(payouts) / n_runs
    return avg_payout
    pass
print(estimate_average_slot_payout(100000000))