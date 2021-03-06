from yahoo_finance import Share

def get_data(ticker, start_date, end_date, num_days_per_point, traits):
  stock = Share(ticker)
  days = stock.get_historical(start_date, end_date)
  points = []
  cur_x, cur_y = [], 0
  num_traits = len(traits)
  limit = num_days_per_point*num_traits
  for day in days[1:]:
    if (len(cur_x) == limit):
      points.append((cur_x, float(days[cur_y]['Close'])))
      cur_x = cur_x[num_traits:]
      cur_y += 1
    for trait in traits:
      cur_x.append(float(day[trait]))
  return points

def get_point(ticker, start_date, end_date, traits):
  stock = Share(ticker)
  days = stock.get_historical(start_date, end_date)
  x = []
  for day in days:
    for trait in traits:
      x.append(float(day[trait]))
  return x

