import gspread
from google.oauth2.service_account import Credentials

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
    Get the work-in-progress data of bolts from user
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

def update_wip_worksheet(wip):
    """
    Update WIP worksheet, add new row with the list data provided
    """
    print("Updating wip worksheet...\n")
    wip_worksheet = SHEET.worksheet("WIP")
    wip_worksheet.append_row(wip)
    print("WIP worksheet updated successfully.\n")


wip = get_wip_user()
wip_data = [int(num) for num in wip]
update_wip_worksheet((wip_data))


