FROM python:3.6
COPY ./requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN apt-get update
RUN apt-get install sudo
RUN sudo apt-get install -y mecab mecab-ipadic-utf8 libmecab-dev
RUN sudo apt-get install -y mecab mecab-ipadic-utf8 libmecab-dev swig
RUN pip install -r requirements.txt
RUN chmod 644 app.py
CMD python app.py