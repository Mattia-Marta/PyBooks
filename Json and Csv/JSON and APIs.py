'''
JavaScript Object Notation is a way to format data as a single, human-readable, string.
It resemples pprint() in python. 

Many sites offer JSON content as a way to interact with programs.
This is known as providing an "Application Programming Interface"(API).

You’ll have to find documentation for what URLs your program needs to request 
in order to get the data you want, as well as the general format of the JSON data structures
that are returned. 
This documentation should be provided by whatever site is offering the API; 
if they have a“Developers” page, look for the documentation there.
Using APIs, you could write programs that do the following:
    • Scrape raw data from websites. (Accessing APIs is often more convenient than parsing)
    • Automatically download new posts from one of your social network accounts 
      and post them to another account. 
      For example, you could take your Tumblr posts and post them to Facebook.
    • Create a “movie encyclopedia” for your personal movie collection 
      by pulling data from IMDb, Rotten Tomatoes, and Wikipedia and putting it 
      into a single text file on your computer.

------------------------Reading JSON with loads()------------------------
Translating a JSON string into py value requires to be passed to json.loads() function.

------------------------Writing JSON with dumps()------------------------
Is the reverse function of loads(), it changes py values to JSON-formatted data.

'''

