from keras.preprocessing.text import Tokenizer
from pickle import dump

def dict_to_list(discriptions):
    values_list = list(discriptions.values())
    return values_list

def create_tokenizer(discriptions):

    values_list = dict_to_list(discriptions)

    # Step 1: Initialize the Tokenizer
    # Initializes a tokenizer that will keep only the top 1,000 most frequent words.
    tokenizer = Tokenizer(num_words=1000)  

    # Step 2: Fit the Tokenizer on the list of strings
    tokenizer.fit_on_texts(values_list)

    # Step 3: Save the Tokenizer to a .p file
    with open('tokenizer.p', 'wb') as file:
        dump(tokenizer, file)

def max_length(discriptions):
    captions = list(discriptions.values())
    # Calculate the maximum number of words
    max_words = max(len(caption.split()) for caption in captions)
    return max_words