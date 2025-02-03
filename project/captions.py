def load_doc(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text



def all_image_captions(loaded_doc):
    captions_dict = {}
    lines = loaded_doc.strip().split('\n')
    for line in lines:
        image_id, caption = line.split('\t')
        image_name = image_id.split('#')[0]
        if image_name not in captions_dict:
            captions_dict[image_name] = []
        captions_dict[image_name].append(caption.strip())
    return captions_dict

def clean_text(captions_dict):
    for image_name in captions_dict:
        captions_dict[image_name] = [caption.lower() for caption in captions_dict[image_name]]
    return captions_dict

def convert_to_lowercase():

    pass
