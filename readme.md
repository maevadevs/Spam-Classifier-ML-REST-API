# Spam Classifier ML REST API

This is a Machine Learning project for building a custom Spam Classifier Model that classifies a tweet into *Spam* or *Not Spam*. The Model is built using Keras and Scikit-Learn. Then, we put this ML Model into production as a REST API using FastAPI and Cassandra.

## Primary Dependencies

Library | Purpose
:-|:-
Keras | Python Machine Learning library
Scikit-Learn | Python Machine Learning library
FastAPI | Python REST API Framework
Cassandra DB | NoSQL Database
Astra DB | Cloud-Service for Cassandra DB

## Configuration

- Conda Env: `ml_as_api_proj`
  - Python 3.9
  - Requirements: `python -m pip install -r requirements.txt`

## Datasets

- [SMS Spam Collection Data Set](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- [YouTube Spam Collection Data Set](https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection)

Dataset handling is done using the helper function `custom_funcs.datasets_funcs.get_and_unpack_dataset()`
