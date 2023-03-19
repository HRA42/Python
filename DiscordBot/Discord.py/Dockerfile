FROM python:alpine3.15

WORKDIR /usr/src/app

COPY /Discord.py/. .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./bot.py" ]