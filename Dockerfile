FROM arm32v7/python:3.7.6-stretch

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY /contribution-hat /contribution-hat

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
