import string

def process_captions(filename):
    string = _load_doc(filename)
    captions_dict = _all_image_captions(string)
    cleaned = _clean_text(captions_dict)
    vocabulary = _text_vocabulary(cleaned)
    _save_captions('text/cleaned_captions.txt',cleaned)
    return cleaned,vocabulary


def _load_doc(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text


def _all_image_captions(loaded_doc):
    captions_dict = {}
    lines = loaded_doc.strip().split('\n')
    for line in lines:
        image_id, caption = line.split('\t')
        image_name = image_id.split('#')[0]
        if image_name not in captions_dict:
            captions_dict[image_name] = []
        captions_dict[image_name].append(caption.strip())
    return captions_dict

def _clean_text(captions_dict):
    return _remove_punctuation(_convert_to_lowercase(captions_dict))

def _convert_to_lowercase(captions_dict):
    for image_name in captions_dict:
        captions_dict[image_name] = [caption.lower() for caption in captions_dict[image_name]]
    return captions_dict

def _remove_punctuation(captions_dict):
    for image_name in captions_dict:
        captions_dict[image_name] = [caption.translate(str.maketrans('', '', string.punctuation)) for caption in captions_dict[image_name]]
    return captions_dict

def _text_vocabulary(captions_dict):
    vocabulary = set()
    for image_name in captions_dict:
        for caption in captions_dict[image_name]:
            vocabulary.update(caption.split())
    return vocabulary

def _save_captions(filename,captions):
    with open(filename, 'w') as file:
        for image_name in captions:
            for caption in captions[image_name]:
                file.write(f"{image_name}\t{caption}\n")