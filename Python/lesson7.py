# Ejercicio 1
print("ejercicio 1------------")
def prettify_graph(graph):
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")

graph = jimmy_slots.get_graph()
prettify_graph(graph)
graph

# Ejercicio 2
print("ejercicio 2------------")
def best_items(racers):
    winner_item_counts = {}
    for rango in range(len(racers)):
        racer = racers[rango]
        if racer['finish'] == 1:
            for item in racer['items']:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                rango+1, len(racers), racer['name'])
                 )
    return winner_item_counts

best_items(full_dataset)

# Ejercicio 3
print("ejercicio 3------------")
def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)

    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)
    pass