from keras.api.applications.xception import Xception, preprocess_input

def extract_features(directory):
    """
    Use the Xception model to extranct image features in this directory.
    Features of each image is a vector with 2048 elements.
    """
    # TODO:
    # Define the xception model without considering the last layer
    # Resize and normalize each picture, then give it to the model so it can extract its features
    # call model.predict() and save the output in a dictionary

# TODO
# call extract_features on images directory
# save the features using pickle.dump() in features.p
# load the features again using pickle.load()