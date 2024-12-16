import json
from datetime import date, datetime
from decimal import Decimal
from marshmallow import Schema, fields, post_load

class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock):
            return {
                "__type__": "Stock",
                "symbol": obj.symbol,
                "date": obj.date.isoformat(),
                "open": str(obj.open),
                "high": str(obj.high),
                "low": str(obj.low),
                "close": str(obj.close),
                "volume": obj.volume
            }
        elif isinstance(obj, Trade):
            return {
                "__type__": "Trade",
                "symbol": obj.symbol,
                "timestamp": obj.timestamp.isoformat(),
                "order": obj.order,
                "price": str(obj.price),
                "volume": obj.volume,
                "commission": str(obj.commission)
            }
        return super().default(obj)

def custom_decoder(dct):
    if "__type__" in dct:
        if dct["__type__"] == "Stock":
            return Stock(
                dct["symbol"],
                date.fromisoformat(dct["date"]),
                Decimal(dct["open"]),
                Decimal(dct["high"]),
                Decimal(dct["low"]),
                Decimal(dct["close"]),
                dct["volume"]
            )
        elif dct["__type__"] == "Trade":
            return Trade(
                dct["symbol"],
                datetime.fromisoformat(dct["timestamp"]),
                dct["order"],
                Decimal(dct["price"]),
                dct["volume"],
                Decimal(dct["commission"])
            )
    return dct

def deserialize_activity(json_string):
    """Deserialize a JSON string into an activity dictionary containing Stock and Trade objects."""
    data = json.loads(json_string, object_hook=custom_decoder)
    return {
        "quotes": [item for item in data["quotes"]],
        "trades": [item for item in data["trades"]]
    }

class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open_ = fields.Decimal(data_key="open", as_string=True, attribute="open")
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Int()

    @post_load
    def make_stock(self, data, **kwargs):
        #print(f"data: {data}, kwargs: {kwargs}")
        if 'open' in data:
            data['open_'] = data.pop('open')
        return Stock(**data)

class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    volume = fields.Int()
    commission = fields.Decimal(as_string=True)

    @post_load
    def make_trade(self, data, **kwargs):
        return Trade(**data)

def serialize_with_marshmallow(data):
    """Serialize data using Marshmallow.
    
    Args:
        data: Can be either a single Stock/Trade object or an activity dictionary
    Returns:
        str: JSON string representation of the serialized data
    """
    if isinstance(data, Stock):
        stock_schema = StockSchema()
        print (f"Stock data {data.open}")
        serialized = stock_schema.dump(data)
        print (f"Dump stock data {serialized}")
        if "open_" in serialized:
            serialized["open"] = serialized.pop("open_")
        return json.dumps(serialized)
    elif isinstance(data, Trade):
        trade_schema = TradeSchema()
        return json.dumps(trade_schema.dump(data))
    elif isinstance(data, dict) and "quotes" in data and "trades" in data:
        stock_schema = StockSchema(many=True)
        trade_schema = TradeSchema(many=True)
        quotes_data = stock_schema.dump(data["quotes"])
        for quote in quotes_data:
            if "open_" in quote:
                quote["open"] = quote.pop("open_")
        return json.dumps({
            "quotes": quotes_data,
            "trades": trade_schema.dump(data["trades"])
        })
    return json.dumps(data)

def deserialize_with_marshmallow(json_data, schema=None):
    """Deserialize JSON data into objects using Marshmallow.
    
    Args:
        json_data: Can be either a JSON string or a dictionary
        schema: Optional schema to use for deserialization
    """
    # Convert JSON string to dict if needed
    if isinstance(json_data, str):
        json_data = json.loads(json_data)
    
    print (f"Type of json_data {type(json_data)} {json_data}")
    if schema is not None:
        return schema.load(json_data)
    elif isinstance(json_data, dict):
        if "quotes" in json_data and "trades" in json_data:
            stock_schema = StockSchema(many=True)
            trade_schema = TradeSchema(many=True)
            return {
                "quotes": stock_schema.load(json_data["quotes"]),
                "trades": trade_schema.load(json_data["trades"])
            }
        elif "__type__" in json_data:
            schema = StockSchema() if json_data["__type__"] == "Stock" else TradeSchema()
            return schema.load(json_data)
    return json_data