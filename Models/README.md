Add your models here.
They must be pickles with this structure:

```
    models = {"vectorizer" : vectorizer,
              "classifier": classifier,
              "classname_translator": number2class}


```
Where
 * `vectorizer` exposes a `transform` method from strings to numpy vectors.
 * `classifier` exposes a `predict` method from vectors to integers
 * `classname_translator` is a dictionary from integers to strings

They will then be hooked in a call like this
```
    def classify(text : str):
        vector = vectorizer.transform([text])
        predicted_class_number = classifier.predict(vector)
        predicted_class_name = classname_translator[
            predicted_class_number[0]]
```

Notice this fits well with sickit learn classes.