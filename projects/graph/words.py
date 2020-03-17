from util import Stack, Queue  # These may come in handy
# Given two words (begin_word and end_word),
# and a dictionary's word list, return the shortest transformation
# sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.
# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None
# 2: Build the Graph
# Load words from dictionary
f = open('words.txt', 'r')
word_set = set(f.read().lower().split("\n"))
f.close()


def get_neighbors(word):
    '''
    Get all words that are one letter
    away from the given word
    '''
    # Get same length words first
    results = []
    list_word = list(word)
    # Go through each letter in the word
    for i in range(len(list_word)):
        # swap with each letter in the alphabet
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # If resulting word is in the word_set, add to results
            temp_word = list_word.copy()
            temp_word[i] = letter
            joined_word = "".join(temp_word)
            if joined_word in word_set and joined_word != word:
                results.append(joined_word)
    return results


def word_ladder(begin_word, end_word):
    # Create a queue
    q = Queue()
    # Enqueue a path to starting word
    q.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # While queue is not empty:
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab the last word from the path
        w = path[-1]
        # Check if it's our target word
        if w == end_word:
            # If so, return path
            return path
        # Check if it's been visited
        # If not, mark as visited
        if w not in visited:
            visited.add(w)
            # Enqueue path to each neighboring word
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)


print("HERE")
print(word_ladder("sail", "boat"))
print("END")
