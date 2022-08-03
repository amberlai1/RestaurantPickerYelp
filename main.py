import requests
import pandas as pd
import tkinter as tk
from tkinter import ttk


#gui 
root = tk.Tk()
root.title("Restaurant Picker")
message = tk.Label(root, text="Welcome to the restaurant picker ")
message.pack()


#dimensions
window_width = 500
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# button 
def button_clicked():
    print('Button clicked')
button = ttk.Button(root, text='Click Me', command=button_clicked)
button.pack()


# making everything clear
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()

#executing loop 
root.mainloop()


# defining variables
clientId = "NJIVdjU7-8vVZuVvkdGdBg"
apiKey = "cxt68BFcIE0oso3ZtPSSySd3PO0RuzGpdPUM5KkwCxaFaCHTbrU2tiD_bJ1ZfS-OVU2b8NM9Sokd5nrSPLDMqRp4iug9gojYQDgH4cqpyljodcqq2yoKVtfepGrMYnYx"
url = 'https://api.yelp.com/v3/businesses/search'

print("Welcome to the Restaurant Picker! Answer a couple questions below to find the perfect restaurant for you!")

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
newdict = {}
df = pd.DataFrame.from_dict(response.json()['businesses'])
dataframeprice = df.loc[df['price'] <= pricerange]
df1 = dataframeprice[['name', 'url', 'price', 'location']].copy()
print(len(df1)) #Print how many rows
print(df1.columns) #Print column names

df2 = df1.sample()
newdict[df2] 
print(df2)

# make a reroll method
def decisionreroll():
    reroll = input("Would you like to pick a new restaurant? ")
    while reroll != "no":
        if df3 != newdict:
            df3 = df1.sample()
            newdict[df3]
            print(df3)
        else:
            df3 = df1.sample()
        reroll = input("Would you like to pick a new restaurant? ")

    return "Hope you enjoy your restaurant!" # , df3[['name']]

print(decisionreroll())

