# A simple script

based on scikit learn.

Steps: 
1. Get the dara from this kaggle: 
https://www.kaggle.com/hijest/genre-classification-dataset-imdb
   
2. Unzip it into the data folder

3. Change the separator from `:::` to `|` using, e.g.  `sed -i 's/:::/|/g' train_data.txt`

4. Remove the "short" from the `training_file` name in the script

