FROM python:3.8
ADD main.py .
RUN pip install seaborn numpy
CMD [ "python", "./main.py" ]