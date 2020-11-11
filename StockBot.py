symbols = ["AAPL", "GOOGL", "AMZN", "FB", "MSFT", "NLFX"]

#TODO: Write a function that takes in a list of ticker symbols and acquires OHLCV values for each symbol
# returns True on success, False on failure
def acquireData(symbols):
    return False

#TODO: write  a function that takes in a ticker symbol and returns the predicted percent change for that symbol
def predict(symbol):
    return

#TODO: Write a function that, given a ticker symbol and number of shares, purchases that many shares of that symbol
# should return True on a succesful purchase and False otherwise
def purchase(symbol, num_shares):
    return False

#TODO: Write a function that, given a ticker symbol and number of shares, sells that many shares of that symbol
# should return True on a succesful sell and False otherwise
def sell(symbol, num_shares):
    return False

#TODO: Write a function that takes in a ticker symbol and returns True if StockBot owns any shares of that symbol, False otherwise
def weOwnShares(symbol):
    return False

def main():
    acquireData(symbols)
    predictions = []
    for symbol in symbols:
        # predictions[symbol] = predict(symbol)
        return

    for symbol in predictions:
        if (symbol.percent_change >= 5):
            #Purchase(symbol, 20 shares)
            return
        elif(symbol.percent_change <= -5 and weOwnShares(symbol)):
            #Sell(symbol, all.shares())

if (__name__ == '__main__'):
	main()