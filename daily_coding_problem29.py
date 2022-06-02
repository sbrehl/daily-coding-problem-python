# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:45:56 2022

@author: Sascha

Daily Coding Problem #29 (Amazon)

Run-length encoding is a fast and simple method of encoding strings. The basic 
idea is to represent repeated successive characters as a single count and 
character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be 
encoded have no digits and consists solely of alphabetic characters. You can 
assume the string to be decoded is valid.
"""

def run_length_encoding(string):
    count = 1
    encoded_string = ""
    last_letter = string[0]
    string = string[1:]
    
    while string:
        if string[0] == last_letter:
            count += 1
            string = string[1:]
        else:
            encoded_string = encoded_string + str(count) + last_letter 
            count = 1
            last_letter = string[0]
            string = string[1:]
    
    encoded_string = encoded_string + last_letter + str(count)
      
    return encoded_string

def run_length_decoding(string):
    decoded_string = ""
    while string:
        decoded_string = decoded_string + string[1] * int(string[0])
        string = string[2:]
    
    return decoded_string

encoded_string = "4A3B2C1D2A"
decoded_string = "AAAABBBCCDAA"

print(run_length_encoding(decoded_string))
print(run_length_decoding(encoded_string))