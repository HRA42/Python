# Use Python Image 
FROM python:bullseye

# select working directory according to documentation
WORKDIR /usr/src/app

# copy the the Hikari Folder to the working directory
COPY . .

# install the requirements for bot
RUN pip install -r requirements.txt

# run python script
CMD [ "python", "./bot.py" ]