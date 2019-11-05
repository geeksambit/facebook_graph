import requests

app_id = '131285656905938'
app_secret = '90342e5fcc7079d3474945079ddbeb7b'
user_short_token = 'EAAB3ZA1LxqNIBALXRgM21sC8cARo7a0MYwZC5dlNO3MFJ9q9Wqw4DqzlrCnBVVffohbD2Q2x9veSaFUKC00E4VgVEooqMAsJSDKunrHdhqOkikyuo3bIX6wWIOOFXmLLbmIg8LTmeY46I4l9WRErSZAzXvKwReQIwor9ZCW70jh9Ydj0DJ3gOMgyOo7YcW9gkkVtyc2wZCQZDZD'
access_token_url = "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}".format(app_id, app_secret, user_short_token)

r = requests.get(access_token_url)

access_token_info = r.json()
print(access_token_info)
exit()
user_long_token = access_token_info['access_token']

print(access_token_info)
