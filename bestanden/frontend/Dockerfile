FROM node

COPY package.json /

RUN npm install

COPY . /

RUN npm run build

CMD ["/bin/bash", "-c", "npm run start"]