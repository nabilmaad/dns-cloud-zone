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

# Get default TTL from SOA
defaultTtl = sheet.acell('B2').value

# Create the zone file and start writing to it
zone = open('zone.txt', 'w')

for x in range(2, len(sheet.get_all_values())+1):
    # Fetch row
    row = sheet.row_values(x)

    # Check RR TTL
    rrTtl = defaultTtl if row[1] is None else row[1]

    # Data validation
    if(row[3] == "A"):
        try:
            socket.inet_aton(row[4])
        except socket.error:
            sheet.update_cell(x, 7, 'Wrong IPv4 format!')

    elif(row[3] == "AAAA"):
        try:
            socket.inet_pton(socket.AF_INET6, row[4])
        except socket.error:
            sheet.update_cell(x, 7, 'Wrong IPv6 format!')

    print "Gonna write",row[0]
    # Write RR to zone file
    zone.write(row[0] + "\t" + rrTtl + "\t" + row[2] + "\t" + row[3] + "\t" + row[4] + "\n")

zone.close()
