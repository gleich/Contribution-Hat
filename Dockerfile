FROM arm32v7/python:3.7-stretch

# Installing requirements
RUN pip3 install poetry
COPY pyproject.toml pyproject.toml
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-dev -n

COPY /contribution-hat /contribution-hat

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
