# API = https://www.boredapi.com/api/activity?participants=1

# imports 
import requests

# printTheActivity
def printTheActivity(do:str, for_participants:int, type_of_activity:str):
    print("************************")
    print()
    print(f"Do : {do}")
    print()
    print(f"For Participants : {for_participants}")
    print()
    print(f"Type of Activity: {type_of_activity}")
    print()
    print("************************")

if __name__ == "__main__":
    # Ask how many participants are there
    participants = input("How many participants you are?")

    # Url which returns a dictionary
    url = f"https://www.boredapi.com/api/activity?participants={participants}"

    # The activity
    activity = requests.get(url).json() 

    # Taking the Properties from participants dictionary
    do = activity["activity"]
    for_participants = activity["participants"]
    type_of_activity = activity["type"]
    
    printTheActivity(do, for_participants, type_of_activity)