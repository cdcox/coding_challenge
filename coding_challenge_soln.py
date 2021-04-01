# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:16:46 2021

@author: Conor
"""

import numpy as np

def poker_hand_problem():
    '''define a few functions for readability and code reuse then run problem near the end
    at the bottom'''
    #Rank dict, we can drop R flush as it's an instance of S Flush
    rank = {'High Card': 0,
            'One Pair': 1,
            'Two Pairs': 2,
            'Three of a Kind': 3,
            'Straight':4,
            'High CardFlush': 5, #For easier calling
            'Full House': 6,
            'Four of a Kind': 7,
            'StraightFlush': 8
            }
    
    def convert_faces(values):
        '''convert face cards to numbers for convenient ranking, note A has a weird
        exception handled in the straight checker.'''
        new_values = []
        for value in values:
            if value == 'T':
                new_values.append(10)
            elif value == 'J':
                new_values.append(11)
            elif value == 'Q':
                new_values.append(12)
            elif value == 'K':
                new_values.append(13)
            elif value == 'A':
                new_values.append(14)
            else:
                new_values.append(int(value))
        new_values = np.sort(new_values)
        return new_values           
    
    
    def test_for_straights_pairs(values):
        '''takes in values which ahve been converted to numbered list and tests for 
        various hands, straights sequentially increase by one, and other hands can
        be found by frequencies of repeated values returns ordered high cards
        formatted by hand type, and the string reprsentation of the hand '''  
        sequential = values[1:]-values[:-1]
        uniques,counts = np.unique(values, return_counts=True)
        uniques = uniques[::-1]
        counts = counts[::-1]
        if np.all(sequential==1):
            label = 'Straight'
            ordered_rest = list(uniques)        
        #one crazy straight called a 5 high straight    
        elif np.all(values == np.array([14,5,4,3,2])):
            label = 'Straight'
            ordered_rest = list[values[1:]] +[0]     
        elif 4 in counts:
            label = 'Four of a Kind'
            ordered_rest = list(uniques[counts==4])+list(uniques[counts!=4])
        elif 3 in counts and 2 in counts:
            label = 'Full House'
            ordered_rest = list(uniques[counts==3])+list(uniques[counts==2])
        elif 3 in counts:
            label = 'Three of a Kind'
            ordered_rest = list(uniques[counts==3])+list(uniques[counts!=3])
        elif sum(counts==2)==2:
            label = 'Two Pairs'
            ordered_rest = [np.max(uniques[counts==2])]+[np.min(uniques[counts==2])]
            ordered_rest = ordered_rest+ list(uniques[counts!=2])
        elif 2 in counts:
            label = 'One Pair'
            ordered_rest = list(uniques[counts==2])+list(uniques[counts!=2])
        else:
            label = 'High Card'
            ordered_rest = list(uniques)
        return label,ordered_rest
    
    
    def get_hand_label(hand):
        '''Takes in a hand splits value and suit. Uses suit to find flushes.
        Converts values to numerical representation and finds stratights and pairs.
        Returns ordered cards and label.'''    
        #seperate values and  suit
        values = [x[0] for x in hand]
        values = convert_faces(values)
        suit = [x[1] for x in hand]
        #test for flush
        flush_str = ''
        if len(set(suit))==1:
            flush_str = 'Flush'
        #test for straight and pairs
        pair_label,ordered_rest = test_for_straights_pairs(values)
        #combine
        full_label = pair_label+flush_str
        return full_label,ordered_rest
    
    def compare_hands(p1_hand, p2_hand,rank):
        '''takes the two hands, finds thier rank value and compares, if rank is 
        equivelent then compares the ordered card values to find the winner.
        Can also handle tie results though these are disallowed. Returns the winner'''
        p1_hand_label,p1_ordered_rest = get_hand_label(p1_hand)
        p2_hand_label,p2_ordered_rest =get_hand_label(p2_hand)        
        p1_hand_rank = rank[p1_hand_label]
        p2_hand_rank = rank[p2_hand_label]
        #Ccompare winner by rank then value
        if p1_hand_rank>p2_hand_rank:
            winner = 'p1'
        elif p1_hand_rank<p2_hand_rank:
            winner = 'p2'
        elif p1_ordered_rest == p2_ordered_rest:
            winner = 'tie'
        else:
            high_test = np.array(p1_ordered_rest) - np.array(p2_ordered_rest)
            winner_val = high_test[np.where(high_test!=0)[0][0]]
            if winner_val >0:
                winner = 'p1'
            if winner_val <0:
                winner ='p2'
        return winner

    '''runs poker hand comparison on a target file'''
    file_name = 'poker.txt'
    outcomes = []
    with open(file_name) as f:
        all_hands = f.readlines()
    all_hands = [x[:-1].split(' ') for x in all_hands]
    for hands in all_hands:
        p1_hand = hands[:5]
        p2_hand = hands[5:]
        winner = compare_hands(p1_hand, p2_hand,rank)
        outcomes.append(winner)   
    print(outcomes.count('p1'))
    
def fib_problem():
    '''Calculate a fibnonacci sequence and stops before the stop_val
    then recognizing that even numbers occuer every 3rd step strides that
    then sums'''
    stop_val = 4000000
    out_list = []
    past_current = 1
    current =1
    while current<stop_val:
        out_list.append(current)
        temp = current
        current = current+past_current
        past_current = temp
    print(sum(out_list[1::3]))

if __name__ == '__main__':
    poker_hand_problem()
    fib_problem()
    
    