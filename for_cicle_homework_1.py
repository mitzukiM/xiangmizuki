words = ['природо-знавство', 'символ', 'корисна енергія']


def takes_the_words(words):
    words_10 = []
    for word in words:
        if len(word) > 10:
            words_10.append(word)
    return words_10


sample = takes_the_words(words)
print(sample)
