FROM arm32v7/python:3.8-stretch


RUN pip3 install poetry

COPY pyproject.toml .

RUN poetry install --no-root --no-dev -n

COPY /contribution-hat /contribution-hat

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
