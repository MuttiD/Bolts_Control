import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bolts_control')

def get_wip_user():
    """
    Get the work-in-progress data of super bolts from user
    Add a while loop to collect a valid string of data from the user
    via the ternminal, that must be a string of 6 integer numbers separated
    by commas. The loop will keep repeating til it gets the correct set of numbers
    """
    while True:   
        print("Please provide WIP data from today's work: ")
        print("Data should be six numbers, separated by commas.")
        print("Example: 21,23,10,54,20,36")

        data_str = input("Enter your WIP here: ")
        wip_data = data_str.split(",")
        
        if validate_data(wip_data):
            print("This data is valid! Thank you")

            break 

    return wip_data

def validate_data(values):
    """
    This function will convert all string values into integers.
    Raising ValueError if strings cannot be converted into it,
    or if there aren't exactly six values
    """
    print(values)
    try:
        [int(value) for value in values]            # this will convert any string in values' list
        if len(values) != 6:
            raise ValueError(
                f"It is required 6 values, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def update_worksheet(wip, worksheet):
    """
    This function will receives a list of integers (WIP)
    And it will update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(wip)
    print(f"{worksheet} worksheet updated successfully.\n")


def calculate_inventory_data(wip_row):
    """
    The inventory is defined as the work-in-progress less the scrapped bolts.
    - positive scrap are bolts being left to recover
    - negative scrap are bolts recovered
    """
    print("Calculating inventory....\n")
    scrap = SHEET.worksheet("scrap").get_all_values()
    scrap_row = scrap[-1]                       # -1 last row in the sheet
    
    inventory_data = []

    for scrap, wip in zip(scrap_row, wip_row):
        inventory = wip - int(scrap)
        inventory_data.append(inventory)
    
    return inventory_data


def main():
    """
    Running all program functions
    """
    wip = get_wip_user()
    wip_data = [int(num) for num in wip]
    update_worksheet(wip_data, "WIP")
    new_inventory_data = calculate_inventory_data(wip_data)
    update_worksheet(new_inventory_data, "inventory")
    


print("")
print("       **** Welcome to the Bolts Control Programm **** \n")
main()

