from captions import load_doc,all_image_captions,clean_text,text_vocabulary,save_captions

source_text_file = "text/Flickr8k.token.txt"
target_text_file = "text/cleaned_captions.txt"

string = load_doc(source_text_file)
captions_dict = all_image_captions(string)
print("Lenght of captions dict: ",len(captions_dict))

cleaned = clean_text(captions_dict)

vocabulary = text_vocabulary(cleaned)
print("Lenght of vocabulary: ",len(vocabulary))

save_captions(target_text_file,cleaned)