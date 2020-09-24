# Date printer

def date_printer(your_date):
    # split date string into list including month, day, year
    day, month, year = your_date.split("/")

    month = int(month)

    # list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    # match input month with months in list
    month = months[month - 1]

    # print the datetime
    print("The date is " + month + " " + day + ", " + year)


if __name__ == '__main__':
    # get the date
    your_date = input("Enter a date(dd/mm/yyyy): ")
    print(date_printer(your_date))
