1.Download all the necessary libraries from requirements.txt

2. Download the entire dataset (zip) from https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria and unzip to any location.

3. Open Jupyterlab and run each cell of "malaria-cell-classification.ipynb". 
    Note: Make sure to change the paths of the dataset(that you downloaded) while reading it and anywhere else it's used in the entire code.

4. Save the tensorflow model using "tf.keras.models.save_model(model,'mymodel.hdf5')" in a hdf5 format so that it can be accessed by the streamlit app later.

5. Run the streamlit app code and a "app.py" file will be created.
    Note: Load the hdf5 model in the load_model() function by selecting it's path from the earlier downloaded file.

6. You can verify the accuracy of the model using "Test the Model" block and selecting cell image files from test_images.

7. Open Anaconda Prompt and change directory to where the "app.py" file is located.

8. Type streamlit run app.py and a seperate tab will open in your browser for the dashboard with localhost 8501

9. Test the images in "test_images" folder and see the accuracy of prediction of the model.