# -*- coding: utf-8 -*-
"""
Created on Thu May 26 10:34:23 2022

@author: Sascha

Daily Coding Problem #17 (Google)

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory 
subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 
contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path 
to a file within our file system. For example, in the second example above, 
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length
 is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the 
length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

# def longest_path(file_system_string):
#     file_system_split = file_system_string.split("/")
#     current_directory = [file_system_split[0]]
#     current_depth = []
#     file_system_split.pop(file_system_split[0])
    
#     for substring in file_system_split[1:]:
#         if substring == 'n' or substring == 't':
#             current_depth.append(substring)
            
            
#         if file_system_split[]
#         current_directory.append(substring)
        
    
file_system_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" 

def string_to_list(file_system_string):
    '''
    the idea here is to transform the string into a format I can personally
        work better with. the string gets converted into a list of all files
        and directories with their respective level of depth, so that I can
        then generate paths to all "dead ends" of the whole directory tree

    Parameters
    ----------
    file_system_string : string
        the raw string to all directories

    Returns
    -------
    directory_list : list
        a list of all files and subdirectories, with their respective level
            of depth in the file system

    '''
    current_substring = ''
    current_depth = 0
    directory_list = []
    
    for letter in file_system_string:
        # this loop loops over every letter in the original string, builds up
        # the names of the current folder or file letter by letter, and appends
        # it to directory_list once a line folding or a space occurs
        if letter == '\n' or letter == '\t':
            if current_substring != '':
                # if a line folding or space occurs, and if the current 
                # substring contains something (the name of a folder or a file),
                # it gets appended to the directory list
                directory_list.append([current_depth, current_substring])
                current_substring = ''
                current_depth = 0
            current_depth += 1
            # counts at which level of depth the directory is at, i.e. how many
            # \n or \t have been looped over in a row
            
            
        if letter != '\n' and letter != '\t':
            current_substring += letter
    
    directory_list.append([current_depth, current_substring])
    return directory_list

def all_paths(directory_list):
    '''
    

    Parameters
    ----------
    directory_list : list
        a list, which results from the function string_to_list. a list in which
            every folder and file of the directory is stored, together with at
            which level of depth it is stored at

    Returns
    -------
    path_list : list
        returns a list of all paths to a "dead end" in the file directory. e.g.
            to individual files, or to a subdirectory which contains nothing

    '''
    path_list = []
    current_depth = -1
    current_directory = ''
    
    for entry in directory_list:
        # this loop loops over every entry in the directory_list, which is a 
        # result of the function string_to_list
        # it appends the current folder or file to current_directory, if the
        # level of depth is above that of the current_entry.
        # if the level of depth is not above the current_entry, it recognizes
        # that it is at a "dead end", stores the current path in path_list, 
        # deletes the entry that came before the current_entry, and calls itself
        # again
        if entry[0] <= current_depth:
            path_list.append(current_directory)
            directory_list.pop(directory_list.index(entry) - 1)
            path_list = all_paths(directory_list)
        if entry[0] > current_depth:
            current_depth = entry[0]
            current_directory += entry[1]
    path_list.append(current_directory)
    return path_list

def longest_path(path_list):
    '''
    

    Parameters
    ----------
    path_list : list
        a list which results from the function all_paths.
            a list of all paths to files or to empty subdirectories.

    Returns
    -------
    int
        the length of the longest absolute path to a file.

    '''
    file_list = []
    for entry in path_list:
        if '.' in entry:
            # if a path does not contain a '.', it does not point to a file, but
            # to an empty subdirectory, and should therefore not be considered
            file_list.append(entry)
    return len(max(file_list[:]))

directory_list = string_to_list(file_system_string)  
all_paths = all_paths(directory_list)
print(longest_path(all_paths))
        
        
        
    