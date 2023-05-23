#This code allows users to search for UK Bank Holidays for a given Country & Year.
#import library
import requests

url = "https://www.gov.uk/bank-holidays.json"
countries = ["scotland", "england-and-wales", "northern-ireland"]

#created a function to check the data in the URL and fetch the data for a given country and year. Provide the results.
#This function has two parameters called country and year which is passed by the user.

def search_bank_holidays(country, year):
    response = requests.get(url)  # Send a request to the specified URL
    if response.ok:  # Check if the request was successful (connected to the URL)
        data = response.json()  # Fetch the data from the URL in JSON format

        events = data[country]["events"]  # First it goes into the data, then into the given country & gets the events for that country. Results placed in variable 'events'
        # The title and date of events are extracted so that they match the provided year
        data_from_events = [f"{events['title']}:{events['date']}" for events in events if events["date"].startswith(year)]

        if data_from_events:
            return "Bank Holidays:\n" + "\n".join(data_from_events)  # Returns the bank holiday data with paragraph spaces
        else:
            return "No Bank Holidays for the given year"  # Returns a message when there are no bank holidays for the given year

while True:
    country = input("Please enter scotland or england-and-wales or northern-ireland): ")  # Prompt the user to enter a country
    if not country:
        break
    while country.lower() not in countries:  # Validate the entered country against the available countries
        print("Sorry, wrong country name entered")
        country = input("Please enter scotland or england-and-wales or northern-ireland): ")

        if not country:
            break

    year = input("Please enter a year (e.g. 2023): ")  # Prompt the user to enter a year
    if not year:
        break  # Exit the loop if the user wants to quit

    results = search_bank_holidays(country.lower(), year)  # Call the function with the provided country and year
    print(results)

    choice = input("Would you like to perform another search? (yes/no): ")  # Ask the user if they want to continue searching
    if choice.lower() == "no":
        break  # #If no then end the loop/search.
    elif choice.lower() == "yes":
        continue  # Continue the search if the user chooses to do so

print("Thank you! from Sultana W ")  # Display the final message when the program ends
