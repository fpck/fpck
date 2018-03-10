FROM node:9-slim

RUN npm install -g @vue/cli
RUN npm install -g @vue/cli-init

WORKDIR /srv
COPY ./ /srv
RUN npm install

