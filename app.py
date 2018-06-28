from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/hooks',methods=['POST'])
def hello_world():
	data = json.loads(request.data)
	sma = data['binance']['ADA/BTC']['informants']['sma'][0]
	ema = data['binance']['ADA/BTC']['informants']['ema'][0]
	app.logger.info("*** sma - ema = %f", sma['sma'] - ema['ema'])
	#app.logger.info('here is the raw data : %s', data)
	return "hola"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)