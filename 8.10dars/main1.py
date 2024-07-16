#   https://www.codewars.com/kata/56f399b59821793533000683/train/python


def sort_cards(cards):
    order = 'A23456789TJQK'

    rank_to_position = {rank: index for index, rank in enumerate(order)}

    sorted_cards = sorted(cards, key=lambda card: rank_to_position[card])

    return sorted_cards


cards = ['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K']
print(sort_cards(cards))  

