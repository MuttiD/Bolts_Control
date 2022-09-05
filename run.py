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


def get_wip_scrap_user():
    """
    Get the work-in-progress data and srapped bolts data from user
    Add a while loop to collect a valid string of data from the user
    via the ternminal, that must be 6 integer numbers separated
    by commas. The loop will keep repeating til it gets the
    correct set of numbers
    """
    while True:
        print("""Please provide WIP and SCRAP data from today's work of 
                 the following metric-sized bolts respectively:
                 M10, M12, M16, M20, M24, M30""")
        print("Data should be six numbers, separated by commas.")
        print("In the SCRAP data, please be aware that: ")
        print("   - Positive scrap means bolts refused")
        print("   - Negative scrap means bolts repaired/recovered\n")
        print("Example: 21,23,10,54,20,36\n")

        data_str = input("Enter your WIP data here: ")
        wip_data = data_str.split(",")

        scrap_str = input("Enter the scrapped data here: ")
        scr_data = scrap_str.split(",")

        if validate_data(wip_data) and validate_data(scr_data):
            print("Data provided is valid! Thank you")

            wip_data = [int(w) for w in wip_data]
            scr_data = [int(s) for s in scr_data]

            break

    return (wip_data, scr_data)


def validate_data(values):
    """
    This function will convert all string values into integers.
    Raising ValueError if strings cannot be converted into it,
    or if there aren't exactly six values
    """
    try:
        # this will convert any string in values' list
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"It is required 6 values, you have provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_worksheet(values, worksheet):
    """
    This function will receives a list of integers (values)
    And it will update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")

    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(values)
    print(f"{worksheet} worksheet updated successfully.\n")


def calculate_inventory_data(wip_row):
    """
    The inventory is defined as the work-in-progress less the scrapped bolts.
    As a reminder:
    - positive scrap are bolts refused
    - negative scrap are bolts repaired/recovered
    """
    print("Calculating inventory....\n")
    scrap = SHEET.worksheet("scrap").get_all_values()
    scrap_row = scrap[-1]                       # -1 last row in the sheet

    inventory_data = []

    for scrap, wip in zip(scrap_row, wip_row):
        inventory = wip - int(scrap)
        inventory_data.append(inventory)

    return inventory_data


def main(show, sheet):
    """
    Running all program functions
    """
    wip = get_wip_scrap_user()

    wip_data = wip[0]
    scrap_data = wip[1]

    update_worksheet(wip_data, "WIP")
    update_worksheet(scrap_data, "scrap")

    new_inventory_data = calculate_inventory_data(wip_data)
    update_worksheet(new_inventory_data, "inventory")

    show = input("""Do you want to see calculated inventory? Press 'y'
                    Otherwise press Enter to restart the app: """)
    if show == "y":
        worksheet_to_get = SHEET.worksheet(sheet)
        list_of_dicts = worksheet_to_get.get_all_records()
        print(f"""The calculated inventory data for each bolt are:

             {list_of_dicts[-1]}\n""")
    else:
        main("n", "inventory")


main("n", "inventory")


print("")
print("       **** Welcome to the Bolts Control Programm **** \n")
main("n", "inventory")
