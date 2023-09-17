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

# pittsburgh_headlines = get_headlines("pittsburgh")
# for text in pittsburgh_headlines:
#     print(text)

def get_drugs_for_imprint(imprint):
    url = f"https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&query={imprint}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the drug information section
        drug_info_section = soup.find("div", class_="section-text")
        
        # Extract drug names
        drug_names = []
        for item in drug_info_section.find_all("strong"):
            drug_names.append(item.get_text().strip())
        
        # Return up to 5 drug names
        return drug_names[:5]
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    imprint = input("Enter the pill imprint: ")
    drugs = get_drugs_for_imprint(imprint)
    
    if drugs:
        print("Possible drugs:")
        for i, drug in enumerate(drugs, start=1):
            print(f"{i}. {drug}")
    else:
        print("No drugs found for the given imprint.")
