### Download data





```
freqtrade download-data --exchange binance --pairs ETH/USDC BTC/USDC BNB/USDC SOL/USDC TRX/USDC AVAX/USDC ADA/USDC DOGE/USDC LTC/USDC BCH/USDC --timeframes 5m 1h --timerange 20210303-20260303
```

### Run backtest

```
freqtrade backtesting 
	--strategy Ema 
	--timerange 20240303-20260303 
	--timeframe 1h 
	--config config.spot.binance.json 
	--pairs ETH/USDC
```
