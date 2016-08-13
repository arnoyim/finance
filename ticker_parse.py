tickers = []

def parsing():
  try:
    read_file = open('rus3000.txt', 'r').read()
    split_file = read_file.split('\n')
    for line in split_file:
      split_line = line.split(' ')
      ticker = split_line[-1]
      if ticker != '':
        tickers.append(ticker)
  except Exception, e:
      print str(e)

parsing()
