## Build and Run Code

1. Clone the repository from GitHub. (Alternatively, make a copy of the Google Colab Notebook: https://colab.research.google.com/drive/1DJZKTHTfPFTHcU7m-wpc7Qf1hPsOFaVX?usp=sharing)
2. Install the necessary dependencies (TensorFlow, Keras, etc.) using pip
3. run all python cells in the notebook, the non-python cells are there to demonstrate how to navigate google's file structure if this is being done through a Google Colab. 
4. The cell that defines the model is the one responsible for training the model and saving it in a persistent state. This cell is estimated to take 4.5 hours to run. If you wish to use a model that is already trained, you may load the `my_model.h5` file, which represents a pre-trained model saved to a persistent state. This file is too large to be uploaded to github so provided is a link to the file in google drive: https://drive.google.com/file/d/1EbFOAxo9UzGyF1PlQBDePGz2Wu7DX8Ra/view?usp=sharing 
5. The last cell represents the interaction with the user. The user should upload the image to the file system, specify its location within the cell, and run the cell. Upon execution the output will be a prediction - either "CAT" or "DOG" based on what the model predicts the image to be.

Tests for this interface are located in test_model.py and can be run using `pytest` on the command line