FROM python:3.9

RUN pip install rasa
RUN rasa --version

RUN pip install transformers
RUN apt-get update -y && apt-get upgrade -y && apt-get install npm -y

WORKDIR /app
COPY ./ /app
RUN npm install
RUN npm run build

CMD ["npm", "run", "start"] 