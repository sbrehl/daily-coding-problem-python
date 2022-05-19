# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:05:33 2022

@author: Sascha

Daily Coding Problem #11 (Twitter)

Implement an autocomplete system. That is, given a query string s and a set of 
all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure 
to speed up queries.
"""

def autocomplete(query_string, possible_strings):
    '''
    Parameters
    ----------
    query_string : str
        the first part of a word, which is to be autocompleted
    possible_strings : list
        a set of all possible query strings

    Returns
    -------
    autocompletion: list
        a list of all strings in the set that have query_string as a prefix.

    '''
    autocompletion = []
    
    for string in possible_strings:
        # loops over all strings in the set
        if query_string in string:
            # checks if query_string is in string
            # if true, appends that string to 'autcompletion'
            autocompletion.append(string)
            
    return autocompletion

# problem: also returns all strings that don't just start with the query_string
# but also those, that contain query_string in the middle or in the end


#%%

def preprocess_set(set_of_strings):
    '''
    preprocesses the set of strings into a dictionary

    Parameters
    ----------
    set_of_strings : list
        the list of strings to be preprocessed.

    Returns
    -------
    autocomplete_dictionary : dictionary
        a dictionary which contains all possible query strings as keys, and the
        words of set_of_strings as values.

    '''
    autocomplete_dictionary = {}
    
    for string in set_of_strings:
        # loops over all the words in set_of_strings
        current_string = ''
        for letter in string:
            # loops over the letters in the current word
            current_string += letter
            # builds up the current_string by using every possible prefix of
            # the word; e.g. for deer: 'd', 'de', 'dee', 'deer'
            if current_string in autocomplete_dictionary:
                # if the current prefix is already present in the dictionary
                # the current word is appended to the prefix key
                autocomplete_dictionary[current_string].append(string)
            else:
                # if the current prefix is not present, it is created
                autocomplete_dictionary[current_string] = [string]
                
    return autocomplete_dictionary

s = ['dog', 'deer', 'deal']
q = 'dg'

dictionary_of_strings = preprocess_set(s)

def autocomplete2(query_string, dictionary_of_strings):
    '''
    takes the query_string, and looks if it is present in dictionary_of_strings
    if yes, returns the value associated with the prefix key
    if not, returns an empty list

    Parameters
    ----------
    query_string : string
        the first part of a word, which is to be autocompleted.
    dictionary_of_strings : dictionary
        a dictionary with the words in set_of_strings as values, and all
        possible prefixes of these words as keys.

    Returns
    -------
    type: list
        a list of all words the query can be autocompleted to.

    '''
    if query_string in dictionary_of_strings:
        return dictionary_of_strings[query_string]
    return []

print(autocomplete2(q,dictionary_of_strings))
