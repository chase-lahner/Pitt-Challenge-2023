import requests

def find_drug_interactions(drug_name):
    # Replace with your OpenFDA API endpoint
    api_url = f"https://api.fda.gov/drug/label.json"

    # Parameters for the API request
    params = {
        "search": f"drug_interactions:\"{drug_name}\"",
        "limit": 1
    }

    try:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                interactions = data["results"][0].get("drug_interactions", [])
                if interactions:
                    text = "" + (f"Interactions for {drug_name}:")
                    for interaction in interactions:
                        text = "" + (interaction)
                else:
                    text = "" + (f"No drug interactions found for {drug_name}.")
            else:
                text = "" + (f"No information found for {drug_name}.")
        else:
            text = "" + (f"Failed to retrieve data from OpenFDA API. Status code: {response.status_code}")
    except Exception as e:
        text = "" + (f"An error occurred: {str(e)}")

    return text

# if __name__ == "__main__":
#     drug_name = input("Enter the name of the drug: ")
#     text = find_drug_interactions(drug_name)