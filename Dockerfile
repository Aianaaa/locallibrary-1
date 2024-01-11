FROM python:3.9
WORKDIR /locallibrary
#COPY requirements.txt /locallibrary/requirements.txt
COPY . /locallibrary/
RUN pip install -r requirements.txt
CMD ./setup.sh
