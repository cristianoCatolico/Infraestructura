En cloud9 o localmente:

- Descargar el proyecto

`wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/DEV-AWS-MO-DevOps-C1/downloads/trivia-app.zip -O ~/trivia-app.zip`

- Descomprimir
 
`unzip -o ~/trivia-app.zip`

- Construir la aplicacion


`cd trivia-app`

`sam build`

`sam deploy --guided`

- Actualizar el frontend  en  `trivia-app/front-end-react/src/config.js`
- Establecer la version de node

`nvm install lts/gallium `

`nvm alias default lts/gallium`

- Hacer correr el frontend `npm install` y `npm run start`

- Desplegar el frontend en un s3

`aws s3 mb s3://<iniciales><edad>-trivia-app-bucket/`

`npm run build`

`aws s3 sync --acl public-read build s3://<iniciales><edad>-trivia-app-bucket/`

- Luego subir un repositio git

cd ~/environment/trivia-app/
`git init`

`git checkout -b main`

`git add .`

`git commit -m "initial commit"`

`git remote add origin codecommit://trivia-app`

`git push origin main`

