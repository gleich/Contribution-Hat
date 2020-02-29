FROM arm32v7/python:3.7.6-stretch

# Fixing timezone:
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY /contribution-hat /contribution-hat

RUN pip3 install requests

WORKDIR /contribution-hat

CMD [ "python3", "main.py" ]
