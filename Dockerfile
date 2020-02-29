FROM mattgleich/sense-hat

COPY /contribution-hat /contribution-hat

RUN pip3 install -r requirements.txt

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
