FROM alpine:latest
WORKDIR /app
RUN apk add tree
ADD ./run.sh ./run.sh
CMD [ "/bin/sh", "/app/run.sh" ] 
