from captions import load_doc,all_image_captions,cleaning_text
# testing functions manually
string = load_doc('text/Flickr8k.token.txt')
# print(string)
# print(len(string))

captions_dict = all_image_captions(string)

cleaned = cleaning_text(captions_dict)
for image_name, captions in cleaned.items():
    print(f"{image_name}: {captions}")



    
