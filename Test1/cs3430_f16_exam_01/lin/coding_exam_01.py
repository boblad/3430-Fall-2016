#!/usr/bin/python

## Bryant Oblad
## Your A01770171

import sys
import math
import operator
import os

### these strings are used in tests.

short_text_1 = 'ab cd'
short_text_2 = 'ab ab cde'
short_text_3 = "\n\
aaabb ccd\n\
ef ghi\n\
"

rumi_quote_1 = "The wound is the place where the Light enters you."
rumi_quote_2 = "\n\
Don\'t grieve.\n\
Anything you lose comes round\n\
in another form.\n\
"
rumi_quote_3 = "Sell your cleverness and buy bewilderment."
rumi_quote_4 = "\n\
Raise your words, not voice.\n\
It is rain that grows flowers, not thunder.\n\
"

## you may (or may not) use this tuple to compute char
## frequencies.
alphabet = ('a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z')



### -----------
### Problem 1
### -----------

def display_top_freq_chars(txt, size):

    alphabetDict = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
    }

    txt = txt.lower()
    print txt


    for letter in txt:
        if letter.isalpha():
            alphabetDict[letter] = alphabetDict[letter] + 1

    sortedLetters = sorted(alphabetDict.items(), key=operator.itemgetter(1), reverse=True)

    index = 0
    for key, value in sortedLetters:
        if index < size:
            print 'letter: {} count: {}'.format(key, value)
        index = index + 1




def unit_test_01():
  print 'top 3 chars in\n', short_text_1
  display_top_freq_chars(short_text_1, 3)
  print '------\n'
  print 'top 3 chars in\n', short_text_2
  display_top_freq_chars(short_text_2, 3)
  print '------\n'
  print 'top 5 chars in\n', short_text_3
  display_top_freq_chars(short_text_3, 5)
  print '------\n'
  print 'top 5 chars in\n', rumi_quote_1
  display_top_freq_chars(rumi_quote_1, 5)
  print '------\n'
  print 'top 7 chars in\n', rumi_quote_2
  display_top_freq_chars(rumi_quote_2, 7)
  print '------\n'
  print 'top 10 chars in\n', rumi_quote_3
  display_top_freq_chars(rumi_quote_3, 10)
  print '------\n'
  print 'top 10 chars in\n', rumi_quote_4
  display_top_freq_chars(rumi_quote_4, 7)
  print '------\n'

def word_code(word):
    total = [ ord(charactor) for charactor in word]
    charactor_sum = 0
    for i in total:
        charactor_sum = charactor_sum + total
    return charactor_sum

### -----------
### Problem 2
### -----------

def display_top_word_codes(txt, n):
  alpha_list = []
  for charactor in txt:
      if charactor.isalpha():
          alpha_list.append(charactor)

   print word_code(alpha_list)

def unit_test_02():
  print 'top 3 word codes in\n', short_text_1
  display_top_word_codes(short_text_1, 3)
  print '------\n'
  print 'top 3 word codes in\n', short_text_2
  display_top_word_codes(short_text_2, 3)
  print '------\n'
  print 'top 5 word codes in\n', short_text_3
  display_top_word_codes(short_text_3, 5)
  print '------\n'
  print 'top 5 word codes in\n', rumi_quote_1
  display_top_word_codes(rumi_quote_1, 5)
  print '------\n'
  print 'top 7 word codes in\n', rumi_quote_2
  display_top_word_codes(rumi_quote_2, 7)
  print '------\n'
  print 'top 10 word codes in\n', rumi_quote_3
  display_top_word_codes(rumi_quote_3, 10)
  print '------\n'
  print 'top 10 word codes in\n', rumi_quote_4
  display_top_word_codes(rumi_quote_4, 7)
  print '------\n'

### -----------
### Problem 3
### -----------

def get_mean_celcius(entries):

    import ipdb; ipdb.set_trace()
    total = 0.0
    for date, temp in entries:
        total = int(temp) + total
        print 'total: {}'.format(total)
    return total / len(entries)

def get_highest_temp(entries):
    return max(entries, key=operator.itemgetter(1))[0]

def get_lowest_temp(entries):
    return min(entries, key=operator.itemgetter(1))[0]

def get_std_dev_of_temps(entries):
    total = 0.0
    mean = get_mean_celcius(entries)
    for date, temp in entries:
        total = (int(temp) - mean)**2 + total
        print 'total in std dev: {}'.format(total)
    return math.sqrt(total / len(entries))


def display_temp_stats(temp_file):
    file_path = os.path.abspath(temp_file)
    current_file = open(file_path, 'r')
    lines = current_file.readlines()
    fixed_lines = []
    for line in lines:
        fixed_lines.append(line.split())

    print 'length of records {}'.format(len(fixed_lines))

    print 'The mean temperature {}'.format(get_mean_celcius(fixed_lines))
    print 'The Highest temperature {}'.format(get_highest_temp(fixed_lines))
    print 'The Lowest temperature {}'.format(get_lowest_temp(fixed_lines))
    print 'The Std Deviation {}'.format(get_std_dev_of_temps(fixed_lines))




lin_files = ['small_lin_temps.txt', 'small_lin_temps2.txt', 'lin_temps.txt']
win_files = ['small_win_temps.txt', 'small_win_temps2.txt', 'win_temps.txt']

def unit_test_lin_03():
  for lf in lin_files:
    print('STATS FOR %s:' % lf)
    display_temp_stats(lf)
    print('------')

def unit_test_win_03():
  for wf in win_files:
    display_temp_stats(wf)

### all unit tests
#
# if __name__ == '__main__':
#   #unit_test_01()
#   #unit_test_02()
#   #unit_test_lin_03()
#   #unit_test_win_03()

unit_test_02()
display_temp_stats('./lin_temps.txt')
