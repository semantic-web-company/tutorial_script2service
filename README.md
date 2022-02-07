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