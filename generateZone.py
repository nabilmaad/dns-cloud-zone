import gspread
import getpass
import socket

while True:
    # Ask user to login
    username = raw_input("Enter your Drive email address: ")
    password = getpass.getpass("Enter Password: ")

    try:
        # Authenticate user
        gc = gspread.login(username, password)
        break;
    except gspread.exceptions.AuthenticationError:
        print ">> Login failed! Try again...\n"

# OR replace everything above with below (uncommented)
# using your email address and password explicitely

# gc = gspread.login(email_address, password)

# Open the required spreadsheet
sheet = gc.open("focil.ciscoscience.net").sheet1

# Scan for SOA to get default TTL
defaultTtl = ''
for x in range(2, len(sheet.get_all_values())+1):
    # Fetch row
    row = sheet.row_values(x)
    print "Checking",row[0]

    # Check if record type is SOA
    if(row[3] == "SOA"):
        defaultTtl = row[1]
        break

# Create the zone file and start writing to it
zone = open('zone.txt', 'w')

for y in range(2, len(sheet.get_all_values())+1):
    # Fetch row
    row = sheet.row_values(y)

    # Check RR TTL
    rrTtl = defaultTtl if row[1] is None else row[1]

    print "Gonna write",row[0]
    # Write RR to zone file
    zone.write(row[0] + "\t" + rrTtl + "\t" + row[2] + "\t" + row[3] + "\t" + row[4] + "\n")

zone.close()
