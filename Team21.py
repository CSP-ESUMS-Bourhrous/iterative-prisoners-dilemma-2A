team_name = 'Team21'
strategy_name = 'Betray 90% unless Colluded within last 10 rounds.'
strategy_description = strategy_name

import random


def move(my_history, their_history, my_score, their_score):

    if 'c' in their_history[-10:]: 
        return 'c'               
    else:
        if random.random()<0.1: 
            return 'c'         
        else:
            return 'b'         
