base_url = "https://codefirstgirls.com/"
current_url = base_url

while True:
    print("You are currently on the URL", current_url)
    print("Where are you clicking?")

    if current_url == base_url:
        print("Options: Courses, Opportunities")
        user_input = input("User Input: ")

        if user_input == "Courses":
            current_url = base_url + "courses"
        elif user_input == "Opportunities":
            current_url = base_url + "opportunities"

    elif current_url == base_url + "courses":
        print("Options: CFGDegree, Back")
        user_input = input("User Input: ")

        if user_input == "CFGDegree":
            current_url = base_url + "courses/cfgdegree"
        elif user_input == "Back":
            current_url = base_url

    elif current_url == base_url + "courses/cfgdegree":
        print("Options: Back")
        user_input = input("User Input: ")

        if user_input == "Back":
            current_url = base_url + "courses"

    elif current_url == base_url + "opportunities":
        print("Options: Ambassadors, Back")
        user_input = input("User Input: ")

        if user_input == "Ambassadors":
            current_url = base_url + "opportunities/ambassadors"
        elif user_input == "Back":
            current_url = base_url

    elif current_url == base_url + "opportunities/ambassadors":
        print("Options: Back")
        user_input = input("User Input: ")

        if user_input == "Back":
            current_url = base_url + "opportunities"

    print()
    if user_input == "Exit":
        break
        
"""
PART B
Assumptions:
1.Fixed number of URL links 
2.The options for after clicking on each link is predefined and will not change
3.Error Handling is not needed

Time ans space complexity is O(1)
"""
