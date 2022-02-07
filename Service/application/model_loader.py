import pickle
from os import listdir
from os.path import isfile, join

from pathvalidate import ValidationError

from config import logger, data_dir


class ModelExistsException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class ModelNotFoundException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class EndToEndModel:
    def __init__(self, vectorizer, classifier, classname_translator):
        self.vectorizer = vectorizer
        self.classifier = classifier
        self.classname_translator = classname_translator

    def classify(self, text : str):
        vector = self.vectorizer.transform([text])
        predicted_class_number = self.classifier.predict(vector)
        predicted_class_name = self.classname_translator[
            predicted_class_number[0]]

        return predicted_class_name


class ModelLoader():

    def __init__(self):
        self.root_dir = data_dir
        logger.debug("Model Loader Initialized")
        self.models = {f[:-4]: None
                       for f in listdir(self.root_dir)
                       if isfile(join(self.root_dir, f))
                       and f.endswith(".pkl")}

    def _load_model(self, modelname: str) -> EndToEndModel:
        print(modelname)
        if ".." in modelname:
            raise ValidationError
        filepath = join(self.root_dir, modelname + ".pkl")
        if not isfile(filepath):
            raise ModelNotFoundException
        with open(filepath,"rb") as fin:
            a = pickle.load(fin)
            model = EndToEndModel(**a)
            self.models[modelname] = model

        return model

    def _save_model(self, modelname: str, model):
        if ".." in modelname:
            raise ValidationError
        filepath = join(self.root_dir, modelname + ".pkl")
        pickle.dump(model, filepath)
        return True

    def __getitem__(self, key) -> EndToEndModel:
        if key not in self.models.keys() or self.models[key] == None:
            self._load_model(key)
        return self.models[key]

    def __setitem__(self, key, value : EndToEndModel):
        if key in self.models.keys():
            raise ModelExistsException
        self.models[key] = value
        return self._save_model(modelname=key, model=value)
