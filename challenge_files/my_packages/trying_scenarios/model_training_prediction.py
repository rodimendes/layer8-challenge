from get_data import opening_pickle, to_pickle
from models.knn_classifier import training_knn_model, predict_knn_model


# Opening a file and Training KNNClassifier
cleaned_data = opening_pickle("cleaned_data")
my_knn = training_knn_model(cleaned_data)

# Saving the model as a pickle file.
to_pickle(my_knn, "my_knn_model")

# Predicting with KNN model
my_params = [1000, 100, 2000, 10, 150, 30000]
print(predict_knn_model(opening_pickle("my_knn_model"), my_params))
