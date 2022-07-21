import requests
import pandas as pd

#search criteria
term = input("What type of cuisine do you want ")
location = input("What city and state? ")
SEARCH_LIMIT = 10
# defining variables
clientId = "NJIVdjU7-8vVZuVvkdGdBg"
apiKey = "cxt68BFcIE0oso3ZtPSSySd3PO0RuzGpdPUM5KkwCxaFaCHTbrU2tiD_bJ1ZfS-OVU2b8NM9Sokd5nrSPLDMqRp4iug9gojYQDgH4cqpyljodcqq2yoKVtfepGrMYnYx"

url = 'https://api.yelp.com/v3/businesses/search'

headers = {
        'Authorization': 'Bearer {}'.format(apiKey),
    }
url_params = {
                'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'limit': SEARCH_LIMIT
            }
print(url_params)
response = requests.get(url, headers=headers, params=url_params)
print(response.text)
df = pd.DataFrame.from_dict(response.json()['businesses'])
print(len(df)) #Print how many rows
print(df.columns) #Print column names
# dfnames = df(df.name ==)
df.head()
df1 = df.sample()
print(df1)
# make a reroll method
def decisionreroll():
    reroll = input("Would you like to pick a new restaurant? ")

    while reroll != "no":
        df2 = df.sample()
        if reroll == 'yes':
            print(df2)
            reroll
            print("hellp")
        else:
            return "helo"

print(decisionreroll())