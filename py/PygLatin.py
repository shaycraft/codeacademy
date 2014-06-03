#!/usr/bin/python

def firstvowel(word):
    vowels = ['a','e','i','o','u']
    l = len(word)
    for x in range (0,l):
        if word[x] in vowels:
            return x

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    #print original
    word = original.lower()
    start = firstvowel(word)
    first = word[0:start]
    new_word = word + first + pyg
    #print 'Debug:  start = ' + str(start)
    new_word = new_word[start:len(new_word)]
    print new_word
else:
    print 'empty'
