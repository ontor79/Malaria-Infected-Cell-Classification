# Malaria-Infected-Cell-Classification

# This Deep Learning model shows how we can classify malaria infected cells from a bunch of images and deploy it in a simple dashboard.

Deep learning methods achieve impressive performance (even surpassing human-level performance) in several tasks over a wide spectrum of domains. However, in many domains like healthcare, reasoning the predictions of a model is vital. They are useful in evaluating the reliability and fairness of a model, and in effective data-driven decision making.

While being a generally black box approach, with modern techniques, deep learning methods can provide some explanations to their predictions. In the context of image classification, heat-maps on the image highlighting areas that highly influence the classification of the target can be generated.


# Objectives

1. Built a deep learning model to classify infected cells

2. Built a simple application using streamlit to classify a given image and highlight the hotspots in the image that influence the prediction
    - The hotspots has been overlayed on the image and displayed in the streamlit app
    - Included a video demo of the app using a screen recorder
    - Bonus: deployed the streamlit app on a cloud platform (eg: heroku)

3. Detailed approach and findings from the dataset in a 2-4 page technical report using a prefered format. Provided the necessary details to rationalize assumptions and choice of methods.


# Model used here : CNN (Convolutional Neural Network)

A convolutional neural network (CNN) is a type of artificial neural network used in image recognition and processing that is specifically designed to process pixel data.
CNNs are powerful image processing, artificial intelligence (AI) that use deep learning to perform both generative and descriptive tasks, often using machine vison that includes image and video recognition, along with recommender systems and natural language processing (NLP).


![1-4](https://user-images.githubusercontent.com/94853515/145634851-b625d049-15ff-4287-a77e-aec660a0d9cb.png)



# Steps to recreate the procedure of the entire task:

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

------------------------------------------------------------------------ # Thank You # ----------------------------------------------------------------------------------
