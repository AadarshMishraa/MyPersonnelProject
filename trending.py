# trending.py
from pytrends.request import TrendReq
import time

def get_google_trends(keyword):
    pytrend = TrendReq()
    pytrend.build_payload([keyword])
    time.sleep(2)  # Be polite to Google!
    return pytrend.interest_over_time()


def get_google_trends(keyword, timeframe='now 1-d'):
    pytrend = TrendReq(hl='en-US', tz=360)
    pytrend.build_payload(kw_list=[keyword], timeframe=timeframe)
    data = pytrend.interest_over_time()
    if not data.empty:
        latest_value = data[keyword].iloc[-1]
        return latest_value
    else:
        return None

if __name__ == "__main__":
    keyword = "content marketing"
    print(f"Trend value for '{keyword}':", get_google_trends(keyword))
