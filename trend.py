from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq()

search_term = "Red Pill"
timeframe = "2019-01-01 2024-12-31"  # Last 4 years
geo = "US"

# Build payload and fetch data
pytrends.build_payload([search_term], timeframe=timeframe, geo=geo)
interest_over_time_df = pytrends.interest_over_time()


# finding related queries
# related_queries = pytrend.related_queries()
# related_queries.values()

# Ensure there's no 'isPartial' column if it exists
if 'isPartial' in interest_over_time_df.columns:
    interest_over_time_df = interest_over_time_df.drop(columns=['isPartial'])

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(interest_over_time_df.index, interest_over_time_df[search_term], label=search_term, color="blue", linewidth=2)
plt.title(f"Interest Over Time for '{search_term}'", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Interest", fontsize=12)
plt.grid(alpha=0.5)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()



