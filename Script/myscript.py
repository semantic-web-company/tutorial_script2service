import csv
from os.path import join
import pickle

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import f1_score
from sklearn.model_selection import StratifiedKFold
from sklearn.svm import SVC as SVMC

from utils import remove_small_classes

data_directory = "../Data/Genre_Classification_Dataset"
training_file = join(data_directory, "train_data.txt")
output_model_file = "../Models/model_1.pkl"

class_size_threshold = 1000
max_classifier_iters = 200

raw_data = []
with open(training_file) as fin:
    reader = csv.DictReader(fin, delimiter="|",
                            fieldnames=["ID", "TITLE", "GENRE", "DESCRIPTION"])
    for row_dict in reader:
        raw_data.append(row_dict)

    text_data = [x["DESCRIPTION"].strip() for x in raw_data]
    class_data = [x["GENRE"].strip() for x in raw_data]

    text_data, class_data = remove_small_classes(text_data,
                                                 class_data,
                                                 class_size_threshold)

    all_classes = list(set(class_data))
    all_classes.sort()

    class2number = {cl: i for i, cl in enumerate(all_classes)}
    number2class = {i: cl for i, cl in enumerate(all_classes)}
    class_number = np.array([class2number[cl] for cl in class_data])

    # We split into 0.75 train 0.25 test, and I only take one split
    skf = StratifiedKFold(n_splits=4, shuffle=True)
    train_index, test_index = next(skf.split(text_data, class_data))

    text_train = [text_data[i] for i in train_index]
    y_train = [class_number[i] for i in train_index]
    text_test = [text_data[i] for i in test_index]
    y_test = [class_number[i] for i in test_index]

    # Converts text to vectors
    vectorizer = TfidfVectorizer(max_df=0.6, min_df=0.01)
    X_train = vectorizer.fit_transform(raw_documents=text_train)

    # Train classifier
    print("Shape of training data is:   ", X_train.shape)
    classifier = SVMC(max_iter=max_classifier_iters)
    classifier.fit(X=X_train, y=y_train)

    # Vectorize and classify test
    X_test = vectorizer.transform(raw_documents=text_test)
    y_test_predicted = classifier.predict(X_test)

    f1 = f1_score(y_test, y_test_predicted, average='weighted')
    print("Weighted f1 score was  ", f1)


    text = "Listening in to a conversation between his doctor and parents, 10-year-old Oscar learns what nobody has the courage to tell him. He only has a few weeks to live. Furious, he refuses to speak to anyone except straight-talking Rose, the lady in pink he meets on the hospital stairs. As Christmas approaches, Rose uses her fantastical experiences as a professional wrestler, her imagination, wit and charm to allow Oscar to live life and love to the full, in the company of his friends Pop Corn, Einstein, Bacon and childhood sweetheart Peggy Blue"
    vector = vectorizer.transform([text])
    predicted_class_number = classifier.predict(vector)
    predicted_class_name = number2class[predicted_class_number[0]]

    models = {"vectorizer" : vectorizer,
              "classifier": classifier,
              "classname_translator": number2class}

    with open(output_model_file, "wb") as fout:
        pickle.dump(models, fout)


