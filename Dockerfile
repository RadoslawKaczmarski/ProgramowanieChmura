FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY wykres.py .
EXPOSE 5000
CMD python wykres.py