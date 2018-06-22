# cryptosignal-webhook

Runs CryptoSignal in Docker with a webhook server, so you can define alerts the way you like.
Perhaps you can add some logic too ?

### Instructions
* Install Docker https://docs.docker.com/install/ then run these commands
* `git clone https://github.com/patrickpxp/cryptosignal-webhook`
* `cd cryptosignal-webhook`
* `docker-compose up`

Customize your CryptoSignal configuration file
Customize what happens when webhooks are triggered (no restart required!)  by editing hooks/telegram.sh
