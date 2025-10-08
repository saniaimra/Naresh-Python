class Stock:
    def __init__(self,name,price):
        self.name = name
        self.price_history = [price]

    def update_price(self,new_price):
        self.price_history.append(new_price)

    def get_current_price(self):
        return self.price_history[-1]
    
    def get_average_price(self):
        return sum(self.price_history)/len(self.price_history)
    
    def get_price_history(self):
        return self.price_history
    
class Trader:
    def __init__(self,name):
        self.name = name
        self.portfolio = {}
        self.transactions = []

    def buy_stock(self, stock: Stock, quantity: int):
            price = stock.get_current_price()
            self.portfolio[stock.name] = self.portfolio.get(stock.name, 0) + quantity
            self.transactions.append({
                "type": "BUY",
                "stock": stock.name,
                "quantity": quantity,
                "price": price
            })

    def sell_stock(self, stock: Stock, quantity: int):
        if self.portfolio.get(stock.name, 0) < quantity:
            print(f"Error: Not enough shares to sell for {stock.name}")
            return
        price = stock.get_current_price()
        self.portfolio[stock.name] -= quantity
        self.transactions.append({
            "type": "SELL",
            "stock": stock.name,
            "quantity": quantity,
            "price": price
        })

    def get_portfolio(self):
        return self.portfolio

    def get_transaction_history(self):
        return self.transactions
    
class StockMarket:
    def __init__(self):
        self.stocks = {}    # stock_name -> Stock object
        self.traders = {}   # trader_name -> Trader object
        self.total_transactions = 0

    def add_stock(self, stock_name, price):
        self.stocks[stock_name] = Stock(stock_name, price)

    def add_trader(self, trader_name):
        self.traders[trader_name] = Trader(trader_name)

    def update_stock_price(self, stock_name, new_price):
        if stock_name in self.stocks:
            self.stocks[stock_name].update_price(new_price)
        else:
            print(f"Stock '{stock_name}' not found.")

    def trader_buy_stock(self, trader_name, stock_name, quantity):
        if trader_name in self.traders and stock_name in self.stocks:
            self.traders[trader_name].buy_stock(self.stocks[stock_name], quantity)
            self.total_transactions += 1
        else:
            print("Trader or Stock not found.")

    def trader_sell_stock(self, trader_name, stock_name, quantity):
        if trader_name in self.traders and stock_name in self.stocks:
            self.traders[trader_name].sell_stock(self.stocks[stock_name], quantity)
            self.total_transactions += 1
        else:
            print("Trader or Stock not found.")

    def generate_report(self):
        market_cap = sum(stock.get_current_price() for stock in self.stocks.values())
        return {
            "Total Traders": len(self.traders),
            "Total Transactions": self.total_transactions,
            "Market Capitalization": market_cap
        }


market = StockMarket()


market.add_stock("AAPL", 150)      
market.add_stock("GOOGL", 2800)    


market.add_trader("Alice")
market.add_trader("Bob")


market.trader_buy_stock("Alice", "AAPL", 10)


market.trader_buy_stock("Bob", "GOOGL", 2)


market.trader_sell_stock("Alice", "AAPL", 5)


market.update_stock_price("AAPL", 160)


print("\nAlice's Portfolio:")
print(market.traders["Alice"].get_portfolio())

print("\nBob's Portfolio:")
print(market.traders["Bob"].get_portfolio())


print("\nAlice's Transactions:")
for txn in market.traders["Alice"].get_transaction_history():
    print(txn)

print("\nBob's Transactions:")
for txn in market.traders["Bob"].get_transaction_history():
    print(txn)

print("\nMarket Report:")
print(market.generate_report())
