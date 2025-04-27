class Broker:
    stock_prices={'goog':400,'amzn':900,'tsla':350}

    def __init__(self,name,acc_no,money):
          self.name=name
          self.acc_no=acc_no
          self.wallet=money
          self.portfolio={}

    def get_portfolio(self):
        if self.portfolio!={}:
             for i,j in self.portfolio.items():
                  print(i,j)
        else:
             print('empty')
    def buy(self,stock_name):
        if stock_name in Broker.stock_prices.keys():
            price=Broker.stock_prices.get(stock_name)
            if self.wallet>=price:
                self.wallet-=price
                self.portfolio[stock_name]=price
                print(f'Bought {stock_name} for {price}, new balance: {self.wallet}')
            else:
                print(f'Not enough money, current balance{self.wallet}')

    def sell(self,stock_name):
        if stock_name in Broker.stock_prices.keys():
            price=Broker.stock_prices.get(stock_name)
            self.wallet+=price
            self.portfolio.pop(stock_name)
            print(f'Sold {stock_name} for {price}, new balance: {self.wallet}')
        else:
            print('Invalid stock name')
if __name__=="__main__":
    print("in file 1")