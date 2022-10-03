import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "KWRFJJIHIUDIDAL0"
NEWS_API_KEY = "e4aa052b094049dba57a3cd0f1ddff48"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = "mambeInfo vs yours"
TOKEN = "mambeToken vs yours"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
# [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# Get the day before yesterday's closing stock price
day_before_yesterday_price = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_price["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.

difference = round(abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price)), 4)
print(difference)

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round(difference / float(yesterday_closing_price) * 100, 4)
print(diff_percent)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_percent > 4:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    ## STEP 2: https://newsapi.org/

    three_articles = articles[:3]
    print(three_articles)

    # # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 article's headline and description using list comprehension.
    "Headlines: {article title}. \nBrief: {articles description}"
    formatted_article = [f"Headlines: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

#Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TOKEN)

#Optional TODO: Format the message like this:
    for article in formatted_article:
        message = client.messages.create(
            body=article,
            from_="+19594008593",
            to="mambeNumber"
        )
"""
Release information about the share 
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

