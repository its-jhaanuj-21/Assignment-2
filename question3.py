# Accept any city from the user and display monument of the city.
def display_monument(city):
    if city == "Delhi":
        monument = "Red Fort"
        print("The monument in", city, "is", monument)
    elif city == "Agra":
        monument = "Taj Mahal"
        print("The monument in", city, "is", monument)
    elif city == "Jaipur":
        monument = "Jal Mahal"
        print("The monument in", city, "is", monument)
    else:
        print("Monument information not available for the given city.")
        
city = input("Enter the name of a city: ")
display_monument(city)
