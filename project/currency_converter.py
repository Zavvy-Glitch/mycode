#!/usr/bin/python3

""" TLG Cohort D23 | CChea
    Final Project: Currency Exchange """

import tkinter as tk
from tkinter import ttk
from tkinter import Label, Entry, StringVar, Button, mainloop
import re
import requests


class RTConverter:
    """ Class for Conversion """
    def __init__(self, rturl):
        """ Retrieves Data from URL"""
        try:
            self.data = requests.get(rturl).json()
            # data checkpoint: print(self.data['date'], self.data['time_last_updated'])
            # entry point of data needed: "rates": <- everything before credits
            self.currency = self.data['rates']
        except Exception as error:
            print(f' caught {type(error)}: error')

    def converter(self, from_currency, to_currency, amount):
        """ Converts specified currencies """
        # Takes in arguments
        # - from_currency: from which currency you will want to convert
        # - to_currency: which currency you will want to convert to
        # - amount: how much currency you will want to convert

        # Will want to convert currency type to USD, if not already USD.
        if from_currency != 'USD':
            amount = amount / self.currency[from_currency]

        # Limit on decimal place
        amount = round(amount * self.currency[to_currency], 4)
        return amount


class ConverterUi(tk.Tk):
    """ Interface to query conversions by:
        https://api.exchangerate-api.com/v4/latest/[AOA] or [USD]
        Default: USD """
    def __init__(self, uiconverter):
        """ Initiates GUI """
        tk.Tk.__init__(self)
        self.title = "CURRENCY EXCHANGE"
        self.curr_converter = uiconverter
        self.count = " "

        # create converter display
        self.geometry("500x200")

        # Labeling
        self.intro_label = Label(self,
                                 text='Currency Converter',
                                 fg='black',
                                 relief=tk.RIDGE,
                                 borderwidth=3)

        self.intro_label.config(font=('Sans-Serif', 15, 'bold'))

        self.date_label = Label(self,
                                text=f"1 Czech Koruna = "
                                     f"{self.curr_converter.converter('CZK', 'USD', 1)} "
                                     f"USD \n "f"Date : "
                                     f"{self.curr_converter.data['date']}",
                                relief=tk.RIDGE,
                                borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=160, y=50)

        # Building UI Features

        # Entry box
        valid = (self.register(self.restrict_number_only), '%d', '%P')
        # restrict_number_only is further down
        # restrict_number_only is used to filter to only accept numerical values
        self.amount_field = Entry(self,
                                  bd=3,
                                  relief=tk.RIDGE,
                                  justify=tk.CENTER,
                                  validate='key',
                                  validatecommand=valid)

        self.converted_amount_field_label = Label(self,
                                                  text='',
                                                  fg='black',
                                                  bg='white',
                                                  relief=tk.RIDGE,
                                                  justify=tk.CENTER,
                                                  width=17,
                                                  borderwidth=3)

        # dropdown menu #1
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("CZK")  # default value

        # drop down menu #2
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD")  # default value

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self,
                                                   textvariable=self.from_currency_variable,
                                                   values=list(self.curr_converter.currency.keys()),
                                                   font='Sans-Serif',
                                                   state='readonly',
                                                   width=12,
                                                   justify=tk.CENTER)

        self.to_currency_dropdown = ttk.Combobox(self,
                                                 textvariable=self.to_currency_variable,
                                                 values=list(self.curr_converter.currency.keys()),
                                                 font='Sans-Serif',
                                                 state='readonly',
                                                 width=12,
                                                 justify=tk.CENTER)

        # dimensional formatting
        self.from_currency_dropdown.place(x=30, y=120)
        self.amount_field.place(x=36, y=150)
        self.to_currency_dropdown.place(x=340, y=120)
        self.converted_amount_field_label.place(x=346, y=150)

        # Conversion button
        self.convert_button = Button(self,
                                     text="Convert",
                                     fg="black",
                                     command=self.perform)

        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=225, y=135)

    def perform(self, ):
        """ Takes input from amount_field and converts amount """
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.curr_converter.converter(from_curr, to_curr, amount)
        # will round the decimal places to 2 decimal places
        converted_amount = round(converted_amount, 2)
        # will output converted amount as string inside convert amount[field_label]
        self.converted_amount_field_label.config(text=str(converted_amount))

    def restrict_number_only(self):
        """ restricts numbers to only convert when integers are used """
        regex = re.compile(r'[0-9,]*?(\.)?[0-9,]*$')
        result = str(regex.match(self))
        return self == "" or (self.count <= "1" and result is not None)


if __name__ == '__main__':
    URL = 'https://api.exchangerate-api.com/v4/latest/USD'
    CONVERTER = RTConverter(URL)
    ConverterUi(CONVERTER)
    mainloop()
