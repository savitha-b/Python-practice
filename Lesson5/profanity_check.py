import urllib #module to access/work with webpages/urls

def read_text():
    quotes = open("C:\Python27\movie_quotes.txt") #opens a location on the computer
    contents_of_file = quotes.read() #reads contents from a location
    print(contents_of_file) #prints the variable
    quotes.close() #always use close along with open
    #open and close are not a part of the standard library but are independently present
    #these are a part of built-in functions

    check_profanity(contents_of_file) #calls this function within read-text function
    
def check_profanity(text_to_check):
    use = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    out = use.read() #reads content from use
    #print('response',out)
    use.close()
    if "true" in out:
        print("\n Profanity Alert!")
    elif "false" in out:
        print("\n This document has no curse words!")
    else:
        print("\n Unable to read document properly")

read_text()
