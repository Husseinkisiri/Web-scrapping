import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_wikipedia():
    url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Locate the table containing the data
        table = soup.find("table", {"class": "wikitable"})

        if table:
            # Initialize lists to store data
            ranks = []
            company_names = []
            industries = []
            revenues = []
            revenue_growths = []
            headquarters = []

            # Loop through rows in the table
            for row in table.find_all("tr")[1:]:
                columns = row.find_all("td")

                # Extract data from each column
                rank = columns[0].text.strip()
                company_name = columns[1].text.strip()
                industry = columns[2].text.strip()
                revenue = columns[3].text.strip()
                revenue_growth = columns[4].text.strip()
                hq = columns[5].text.strip()

                # Append data to lists
                ranks.append(rank)
                company_names.append(company_name)
                industries.append(industry)
                revenues.append(revenue)
                revenue_growths.append(revenue_growth)
                headquarters.append(hq)

            # Organize data into a Pandas DataFrame
            data = {
                "Rank": ranks,
                "Company Name": company_names,
                "Industry": industries,
                "Revenue": revenues,
                "Revenue Growth": revenue_growths,
                "Headquarters": headquarters
            }

            df = pd.DataFrame(data)
            return df

        else:
            print("Unable to find the table on the page.")

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
    
    return None

if __name__ == "__main__":
    company_data_df = scrape_wikipedia()

    if company_data_df is not None:
        # Print the first few rows of the DataFrame
        print(company_data_df.head())
    else:
        print("Unable to fetch data.")
