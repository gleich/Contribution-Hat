FROM arm32v7/python:3.7.6-stretch

COPY /contribution-hat /contribution-hat

RUN pip3 install requests

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
