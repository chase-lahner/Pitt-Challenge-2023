# Import the beautifulsoup 
# and request libraries of python.
import requests
import bs4

def get_headlines(text):
        # Combine two strings with default google search URL
        # 'https://google.com/search?q=' and
        # our customized search keyword parameter.
        # Concatenate them
        url = 'https://google.com/search?q=' + text

        # Fetch the URL data using requests.get(url),
        # store it in a variable, request_result.
        request_result=requests.get( url )
        
        # Creating soup from the fetched request
        soup = bs4.BeautifulSoup(request_result.text,
                                "html.parser")
        # soup.find.all( h3 ) to grab 
        # all major headings of our search result,
        heading_object=soup.find_all( 'h3' )
        
        # Iterate through the object 
        # and add it to the list
        headlines = []
        for info in heading_object:
            headlines.append(info.getText())

        return headlines

        