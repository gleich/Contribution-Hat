FROM arm32v7/python:3.7-stretch

# Installing requirements
RUN pip3 install poetry

COPY pyproject.toml pyproject.toml

RUN poetry install --no-dev

COPY /contribution-hat /contribution-hat

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
