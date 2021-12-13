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

