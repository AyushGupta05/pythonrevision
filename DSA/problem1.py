## alice has some cards with numbers on them. she arranges card in decreasing order. and she lays them out face down in a sequence on a table.
## she challenges bob to pick out the card contaitning a given number by turning over as few cards as possible
## write a fucntion to help bob locate the card 

def locate_card(cards, query):
    pass 

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

locate_card(test['input']['cards'], test['input']['query']) == test['output']

locate_card (**test['input']) == test ['output']

## general case, all that 
## nested dictionaries
#represent test case as dictionaries.

