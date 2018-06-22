FROM almir/webhook
RUN apk add --update -t curl
EXPOSE      9000
ENTRYPOINT  ["/usr/local/bin/webhook"]