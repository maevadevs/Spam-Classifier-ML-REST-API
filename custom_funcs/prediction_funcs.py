# Dependencies
import numpy as np
# For uniforming our token vectors
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Define functions
def predict(model, text_str, int_to_labels_mapping, tokenizer = None, max_sequence_length = 280):
    """
    Wrapper function for model.predict() for predicting on new data.
    
    Arguments:
    - model <Keras_Model>: Required. A pre-trained Keras Model.
    - text_str <string>: Required. The string of text to predict on.
    - int_to_labels_mapping <object>: Required. Maps the integer value to the actual string prediction value.
    - tokenizer <Tokenizer>: The tokenizer instance to use for tokenizing the text.
    - max_sequence_length <integer>: The maximum of sequence to use for the prediction.
    """
    
    try:
        # Argument check
        assert "<class 'keras." in str(type(model)), "'model' argument should be a Keras model"
        assert type(text_str) == str and len(text_str) >= 5, "'text_str' argument is required and must be at least 5 characters"
    
        # No result if there is no tokenizer
        if not tokenizer:
            return None

        # Create the sequences and the inputs: Make sure to pad
        sequences = tokenizer.texts_to_sequences([text_str])
        x_input = pad_sequences(sequences, maxlen = max_sequence_length)
        
        # Run prediction
        y_output = model.predict(x_input) # => [0.93, 0.07] -> ham: 93%, spam: 7%, value depending on y_train
        top_y_index = np.argmax(y_output)
 
        # Get the results of the prediction
        preds = y_output[top_y_index]
        labeled_preds = [{f"{int_to_labels_mapping[i]}": x} for i, x in enumerate(preds)]
        
        # Return predictions
        return labeled_preds
    
    except Exception as e:
        return e #f"Error: {e}"