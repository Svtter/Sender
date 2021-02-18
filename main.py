# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
Send to my phone
"""

import PySimpleGUI as Sg
import requests
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def main():
    Sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[Sg.Text('Some text on Row 1')],
              [Sg.Text('Send to my phone'), Sg.InputText()],
              [Sg.Button('Ok'), Sg.Button('Cancel')]]

    # Create the Window
    window = Sg.Window('Sender', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == Sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break
        print('You entered ', values[0])
        api_key = os.environ.get('API_KEY')
        url = f'https://api.day.app/{api_key}/{values[0]}'
        print(url)
        resp = requests.get(url)
        print(resp)

    window.close()


if __name__ == '__main__':
    main()





