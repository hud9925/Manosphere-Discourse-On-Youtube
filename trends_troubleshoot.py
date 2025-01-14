from pytrends.request import TrendReq
import pandas as pd
import time 
from trendspy import Trends



tr = Trends()
try:
    related_queries = tr.related_queries("Red Pill", headers={'referer': 'https://www.google.com/'})
    # overcome api quota
    if related_queries:
        print("Related Queries:")
        for query in related_queries:
            print(f"{query['query']} - Value: {query['value']}")

        # Convert to DataFrame for further analysis
        df = pd.DataFrame(related_queries)
        print("\nDataframe of Related Queries:")
        print(df)

        # Save to CSV
        df.to_csv("redpill_related_queries.csv", index=False)
        print("\nSaved related queries to 'redpill_related_queries.csv'.")
    else:
        print("No related queries found for 'Red Pill'.")
except Exception as e:
    print(f"Error fetching related queries for 'Red Pill': {e}")



# pytrends = TrendReq()

# pytrends.related_queries()
# def fetch_related_queries(base_term, geo="US", timeframe="today 5-y", gprop=""):
#     """
#     Fetch related queries for a given term from Google Trends.
    
#     Args:
#         base_term (str): The term to search for.
#         geo (str): Geographic region (default: US).
#         timeframe (str): Timeframe for the query (default: last 5 years).
#         gprop (str): Google property to filter by (default: general web searches).
    
#     Returns:
#         dict: A dictionary with 'top' and 'rising' related queries.
#     """
#     try:
#         # Build the payload
#         pytrends.build_payload([base_term], geo=geo, timeframe=timeframe, gprop=gprop)
        
#         # Fetch related queries
#         related_queries = pytrends.related_queries()
        
#         # Check if the base term exists in the response
#         if base_term in related_queries and related_queries[base_term]:
#             top_queries = related_queries[base_term].get('top', pd.DataFrame())
#             rising_queries = related_queries[base_term].get('rising', pd.DataFrame())
            
#             return {"top": top_queries, "rising": rising_queries}
#         else:
#             print(f"No related queries found for '{base_term}' with parameters geo={geo}, timeframe={timeframe}, gprop={gprop}.")
#             return {"top": pd.DataFrame(), "rising": pd.DataFrame()}
#     except Exception as e:
#         print(f"Error fetching related queries for '{base_term}': {e}")
#         return {"top": pd.DataFrame(), "rising": pd.DataFrame()}

# # Example Usage
# search_term = "fitness"
# results = fetch_related_queries(search_term, geo="US", timeframe="2018-01-01 2023-12-31")

# # Print the results
# if not results["top"].empty:
#     print("Top Related Queries:")
#     print(results["top"])
# else:
#     print("No top related queries found.")

# if not results["rising"].empty:
#     print("\nRising Related Queries:")
#     print(results["rising"])
# else:
#     print("No rising related queries found.")
