from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import warnings
from imblearn.over_sampling import SMOTE

warnings.filterwarnings("ignore")

def training_knn_model(dataset):

    print("Starting steps to train your KNN model. 🤖")
    seed = 1
    smote_bal = SMOTE(random_state=seed)

    classification_df = dataset.select_dtypes(include=['number']).drop(columns=['ID'])
    classification_df['real_state'] = dataset['real_state']

    # Defining X e y
    print("Defining X e y")
    varX = classification_df.drop(columns=['encoded_state','real_state'])
    varY = classification_df['real_state']

    # Balancing the dataset
    print("This is umbalanced dataset. Balancing our data.")
    varX, varY = smote_bal.fit_resample(varX, varY)

    # Train test split
    print("Spliting data into train and test datasets")
    X_train, X_test, y_train, y_test = train_test_split(varX, varY, test_size=0.3, random_state=38)

    # Applying KNN
    print("Training the model.")
    neighbors = 5
    knn_model = KNeighborsClassifier(n_neighbors=neighbors)
    print("Your KNNClassifier Model is ready! ✅")
    return knn_model.fit(X_train, y_train)


def predict_knn_model(knn_model, paramns: list = [0, 0,0, 0, 0, 0]):
    """
    Inform a list with values to following parameters:
    'goal', 'pledged', 'backers',	'usd pledged',	'usd_pledged_real',	'usd_goal_real'.
    """
    return f"Based on given values, the project was '{knn_model.predict([paramns])[0]}'."
