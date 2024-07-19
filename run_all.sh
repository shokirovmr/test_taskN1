#!/bin/bash

echo "Running unit tests..."
python3 tests.py

echo "Running PySpark script..."
python3 pyspark_task.py