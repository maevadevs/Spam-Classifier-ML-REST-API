# Building Custom ML Model As A REST API

## Dependencies

Library | Purpose
:-|:-
Keras | Python Machine Learning library
FastAPI | Python REST API Framework
Cassandra DB | NoSQL Database
Astra DB | Cloud-Service for Cassandra DB

## Reference Code

- [Production Code (Updated Overtime)](https://github.com/codingforentrepreneurs/AI-as-an-API)
- [Course Reference (Course Specific)](https://github.com/codingforentrepreneurs/AI-as-an-API-Course-Reference)

## Configuration

- Conda Env: `ml_as_api_proj`
  - Python 3.9
- Requirements: `python -m pip install -r requirements.txt`

## Datasets

- [SMS Spam Collection Data Set](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)
- [YouTube Spam Collection Data Set](https://archive.ics.uci.edu/ml/datasets/YouTube+Spam+Collection)

Dataset handling is done using the helper function `custom_funcs.datasets_funcs.get_and_unpack_dataset()`
