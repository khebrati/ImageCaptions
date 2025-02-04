from captions import load_doc,all_image_captions,cleaning_text,text_vocabulary
# testing functions manually
string = load_doc('text/Flickr8k.token.txt')
# print(string)
# print(len(string))

captions_dict = all_image_captions(string)

cleaned = cleaning_text(captions_dict)

vocabulary = text_vocabulary(cleaned)
for word in vocabulary:
    print(f"{word}")


    
