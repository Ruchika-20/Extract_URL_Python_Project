import re

url_count = {} 
with open("./my_text_file.txt") as file:
    content = file.read() 

    # Regular expression to find all the urls in the text file which matches the given pattern
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',content)

    for url in urls:
        try:
            url_count[url] += 1
        except:
            url_count[url] = 1
    
    for url in url_count:
        print( "Occcurence Found : ", url_count[url],end=' ')
        print("First Occurence :" , url)