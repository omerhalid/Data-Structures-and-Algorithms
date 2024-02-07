data = "2024-02-06 09:30:00, AAPL, 150, 100"

def parse_data(data):
    parts = data.split(",")
    date_and_hour = parts[0]
    date = date_and_hour.split(" ")[0]
    symbol = parts[1]
    price_per_share = parts[2]
    number_of_shares = parts[3]
    
    return {
        "date": date,
        "symbol": symbol,
        "price_per_share": price_per_share,
        "number_of_shares": number_of_shares,
    }

given_day = "2024-02-06"
transaction_volumes = {}

with open('trade_data.txt', 'r') as f:
    for line in f:
        trade_data = parse_data(line)
        print(trade_data)
        
        if trade_data["date"] == given_day:
            symbol = trade_data["symbol"]
            volume = trade_data["price_per_share"] * trade_data["number_of_shares"]
            
            if symbol in transaction_volumes:
                transaction_volumes[symbol] += volume
                
            else:
                transaction_volumes[symbol] = volume
                
# Find the symbol with the highest total transaction volume
max_volume_symbol = max(transaction_volumes, key=transaction_volumes.get)

print(f"the max is : {max_volume_symbol}")
        