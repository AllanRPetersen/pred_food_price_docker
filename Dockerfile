FROM python:3.8.6-buster
COPY fast_app.py /fast_app.py
COPY requirements.txt /requirements.txt
COPY raw_data/neural_network_v1.h5 raw_data/neural_network_v1.h5
COPY raw_data/preprocessor_v1.joblib raw_data/preprocessor_v1.joblib
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn fast_app:app --host 0.0.0.0 --port $PORT
