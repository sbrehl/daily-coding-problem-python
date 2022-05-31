# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:15:01 2022

@author: Sascha

Daily Coding Problem #22 (Microsoft)

Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list. If there is more than one possible 
reconstruction, return any of them. If there is no possible reconstruction, 
then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] 
or ['bedbath', 'and', 'beyond'].
"""

words1 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
words2 = ['bedbath', 'bed', 'bath', 'and', 'beyond']
words3 = ['bedbath', 'bed', 'bath', 'beyond']
sentence = "bedbathandbeyond"

def sentence_in_list(words, sentence):
    '''
    The general idea is to tag the words with the index at which they start in
        sentence, order them, and return them, while filtering out multiples.

    Parameters
    ----------
    words : list
        a list of words, that make up a sentence.
    sentence : string
        the sentence.

    Returns
    -------
    final_list : list
        a list of words, consisting of words occurring in "words", ordered in 
            the order in which they occur in sentence.

    '''
    
    words_with_index = []
    final_list = []
    
    for word in words:
        # this loop tags each word with the index, at which it starts in sentence
        words_with_index.append([sentence.index(word), word])
    
    words_with_index.sort()
    current_index = 0
    # current_index tracks at which point in the sentence final_list is currently
    # at. this helps filter out multiple variants (e.g. "bed" & "bath" / "bedbath")
    
    for index_and_word in words_with_index:
        if current_index == index_and_word[0]:
            # if the word to be considered at this iteration does not match the
            # current index, it is a multiple of what is already stored in
            # final_list and should not be considered
            final_list.append(index_and_word[1])
            current_index += len(index_and_word[1])
    
    if current_index != len(sentence):
        # if the length of all words in final_list combined does not match
        # the length of the sentence, there is no possible reconstruction
        return None
    
    return final_list

test1 = sentence_in_list(words1, sentence)
test2 = sentence_in_list(words2, sentence)
test3 = sentence_in_list(words3, sentence)