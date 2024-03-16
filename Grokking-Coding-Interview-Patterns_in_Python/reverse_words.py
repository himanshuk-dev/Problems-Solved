def reverse_words(sentence):
    # First, split the sentence into words
    words = sentence.split()
    
    # Then, reverse the list of words
    words.reverse()
    
    # Finally, join the reversed list of words back into a string
    reversed_sentence = ' '.join(words)
    
    return reversed_sentence
