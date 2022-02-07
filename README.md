 Project RAIDAR
# Script2Service Example
This repository is meant to showcase how to turn a python script in which an ML
workflow is implemented, into a web service that allows exploiting this 
workflow from a third party component.

## Pre-requisites:
1. docker
2. python
3. optionally, a virtual env in which to run the original script

## What is the workflow exemplified here:

This is a simple ML workflow using scikit learn, that takes a collection of
documents, does tokenization and vectorization on them, and then performs 
text classification using a Support Vector Machine.

### The idea:

Is to take this script, learn how to extract from it the models needed for 
production, and build a web API for them


### Steps:

1. Take a look at the `Script` directory. There you will find the baseline 
   script, which we will convert to a web API. The script itself, and the 
   pipeline implemented therein is not so amazing.
   
2. Checkout the branch "service" of this repo, to see how this is later 
   implemented into a web API based on the FastAPI library. 
   
The reason there are two branches is to allow for the service to be 
constructed step by step during a workshop.