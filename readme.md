

## BUILD APP:

  - From directory home

    ` docker build -t <YOUR_USERNAME>/flask-dog-app . `



## Run image


      ` docker run -p 8080:5000 --name flask-dog-app YOUR_USERNAME/flask-dog-app `


      ` http://localhost:8080 `

      - Hit the Refresh button in the web browser to see a few more dog images.

## Push Image

      ` docker login `

      ` docker push YOUR_USERNAME/flask-dog-app `


## Stop and remove container

    ` docker stop flask-dog-app `

    ` docker rm flask-dog-app `

    ..didn't work....

    ` docker rmi <image-id> `
