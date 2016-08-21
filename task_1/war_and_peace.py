# coding:utf8
import re
books = ['book1-2.txt', 'book3-4.txt']

words_frequency = dict()
text = ' '.join(open(path).read() for path in books)
for word in re.findall('\w+', text, re.UNICODE):
    if word in words_frequency:
        words_frequency[word] += 1
    else:
        words_frequency[word] = 1
for word in words_frequency:
    print("%s - %s" % (word, words_frequency[word]))