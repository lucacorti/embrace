eval $(docker-machine env default)
npm install -g ember-cli@2.13.1
cd embrace_ember
npm install
ember build -prod
cd ..
docker-compose build
