#!/usr/bin/python3

import requests
from tkinter import *
import tkinter as tk
from tkinter  import ttk

URL = 'https://api.exchangerate-api.com/v4/latest/USD'

class RTConverter():
    def __init__(self, url):
        """Retrieves Data from URL"""
        self.data = requests.get(url).json()
        self.currency = self.data['rates']

    def converter(self, from_currency, to_currency, amount):
        """Converts specified currencies """
        ## Takes in arguments
        ## - from_currency: from which currency you will want to convert
        ## - to_currency: which currency you will want to convert to
        ## - amount: how much currency you will want to convert

        ## Will want to convert currency type to USD, if not already USD.
        initial_amount = amount
        if from_currency != 'USD' :
            amount = amount / self.currency[from_currency]
    
        # Limit on decimal place
        amount = round(amount * self.currency[to_currency], 4)
        return amount

converting = RTConverter(URL)
print(converting.converter('CZK','USD', 300))


class converterUI():
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = "CURRENCY EXCHANGE"
        self.curr_converter = converter
    
        # creating converter display
        self.geometry("800x500")
    
        # Labeling
        self.intro_label = Label(self, text = 'Real Time Currency Converter', fg = 'gray', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font = ('Sans-Serif', 20, 'bold'))

        self.date_label = Label(self, text = f"1 Czech Koruna = {self.curr_converter.convert('CZK', 'USD', 1)} USD \n Date : {self.curr_converter.data['date']}", relief = tk.GROOVE, borderwidth = 10)

        self.intro_label.place(x = 30, y = 15)
        self.date_label.place9(x = 510, y = 150)


