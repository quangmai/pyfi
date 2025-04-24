import pandas as pd
import matplotlib as plt

# Set the index of listings to Stock Symbol
listings_ss = listings.set_index('Stock Symbol')

# Get ticker of the largest Consumer Services company
ticker = listings_ss.loc[listings_ss['Sector'] == 'Consumer Services', 'Market Capitalization'].idxmax()

# Set the start date
start = date(2015, 1, 1)

# Import the stock data
data = DataReader(ticker, data_source='yahoo', start = start)

# Plot close and volume
data[['close', 'volume']].plot(secondary_y='volume', title=ticker)

# Show the plot
plt.show()
