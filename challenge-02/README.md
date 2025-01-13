# Challenge 03 Docker With Go Application

This contains 2 files dockerfile and docker-compose.yaml

the dockerfile is where we are creating 2 directory first builder to get image and second minimal image which lightweight image which copies the server binary file from builder image and file-dev or prod text files.

also we are setting ENV here by default DEV 

Second is docker-compose.yaml were we mention the port , environment details. along side a sheel script command which copies the respective env files into file.txt and runs ./server command.

commands ran to build and start

docker-compose build --build-arg ENV=DEV or PROD

docker-compose up -d 