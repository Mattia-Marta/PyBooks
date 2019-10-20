#!Python 3
'''
Simple script to automatically launch the map in your browser using the contents of your clipboard.

• Gets a street address from the command line arguments or clipboard.
• Opens the web browser to the Google Maps page for the address.

This means your code will need to do the following:
• Read the command line arguments from sys.argv.
• Read the clipboard contents.
• Call the webbrowser.open() function to open the web browser
'''
import sys, webbrowser, clipboard

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
else:
    address = clipboard.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
