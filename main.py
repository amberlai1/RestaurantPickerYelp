import requests
import pandas as pd
# from PyQt5.QtWidgets import QApplication, QWidget
# import sys
# # gui
# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
# #execute app
# app.exec()

# defining variables
clientId = "NJIVdjU7-8vVZuVvkdGdBg"
apiKey = "cxt68BFcIE0oso3ZtPSSySd3PO0RuzGpdPUM5KkwCxaFaCHTbrU2tiD_bJ1ZfS-OVU2b8NM9Sokd5nrSPLDMqRp4iug9gojYQDgH4cqpyljodcqq2yoKVtfepGrMYnYx"
url = 'https://api.yelp.com/v3/businesses/search'

print("Welcomes to the Restaurant Picker! Answer a couple questions below to find the perfect restaurant for you!")

#search criteria
term = input("What type of cuisine do you want ")
location = input("What city and state? ")
pricerange = input("How much are you willing to spend per person? ")
SEARCH_LIMIT = 50

headers = {
        'Authorization': 'Bearer {}'.format(apiKey),
    }
url_params = {
                'term': term.replace(' ', '+'),
                'location': location.replace(' ', '+'),
                'pricerange': pricerange.replace(' ', '+'),
                'limit': SEARCH_LIMIT
            }


print(url_params)
response = requests.get(url, headers=headers, params=url_params)
print(response.text)

#making a dataframe
df = pd.DataFrame.from_dict(response.json()['businesses'])
dataframeprice = df.loc[['price'] <= int(pricerange)]
df1 = dataframeprice[['name', 'url', 'price', 'location']].copy()
print(len(df)) #Print how many rows
print(df1.columns) #Print column names

#df.head()
df2 = df1.sample()
print(df2)

# make a reroll method

def decisionreroll():
    reroll = input("Would you like to pick a new restaurant? ")
    while reroll != "no":
        df3 = df1.sample()
        print(df3)
        reroll = input("Would you like to pick a new restaurant? ")

    print("Hope you enjoy your restaurant!") #, df3[['name']])

print(decisionreroll())