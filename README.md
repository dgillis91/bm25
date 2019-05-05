# BM25 Scoring

## Description
Simple, and non-production worthy implementation of BM25
scoring. The database is maintained in a csv file, and read
with pandas. For this task, pandas is a good choice - it's 
SQL like, and doesn't require concurrency. For a production 
implementation in python, I would:

- Use an ORM library like SQLAlchemy with a robust database. 
  Another option is to use a document database.
- Handle requests using connecion & flask.

## Install
Clone the repo, I've included a conda environment. To setup, 
run:

``conda env create -f environment.yml``

Note that you may need to change ``prefix`` to point to 
your conda directory.

Then activate it with:

``conda activate bm25``

## Run

Once activated, you can run with:

``python source/bm25.py``

