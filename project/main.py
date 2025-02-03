from captions import load_doc,all_image_captions,clean_text
# testing functions manually
string = load_doc('text/Flickr8k.token.txt')
# print(string)
# print(len(string))

captions_dict = all_image_captions(string)
# for image_name, captions in captions_dict.items():
#     print(f"{image_name}: {captions}")

cleaned_captions_dict = clean_text(captions_dict)
# for image_name, captions in captions_dict.items():
#     print(f"{image_name}: {captions}")

    
