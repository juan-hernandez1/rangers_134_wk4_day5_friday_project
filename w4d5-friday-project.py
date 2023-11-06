class User:
    def __init__(self, name):
        self.properties = {}
        self.name = name

    def add_property(self, property_id, address):
        self.properties[property_id] = Property(property_id, address)

class Property:
    def __init__(self, property_id, address):
        self.property_id = property_id
        self.address = address
        self.expenses = {
            "Taxes": 0,
            "Insurance": 0,
            "Utilities": 0,
            "HOA": 0,
            "Lawn/Snow Removal": 0,
            "Vacancy": 0,
            "Repairs": 0,
            "CapEx": 0,
            "Property Management": 0,
            "Mortgage": 0
        }
        self.income = {
            "Rent": 0,
            "Laundry": 0,
            "Parking": 0,
            "Storage": 0,
            "Misc.": 0
        }
        self.investment = {
            "Down Payment": 0,
            "Closing Costs": 0,
            "Rehab Budget": 0,
            "Misc. Other": 0
            }
        self.roi = 0

    def calculate_roi(self):
        income = {}
        expenses = {}
        investment = {}
        
        for key in self.income:
            income[key] = float(input(f"What is your monthly income for {key}? $"))
        
        for key in self.expenses:
            expenses[key] = float(input(f"What are your monthly expenses for {key}? $"))
        
        for key in self.investment:
            investment[key] = float(input(f"What is your investment in this property for {key}? $"))
        
        monthly_income = sum(income.values())
        monthly_expenses = sum(expenses.values())
        total_investment = sum(investment.values())
        cash_flow = monthly_income - monthly_expenses
        self.roi = (cash_flow * 12) / total_investment
        print(f"ROI for property {self.property_id} at {self.address.title()} is: {self.roi}%")

class ROI:
    def __init__(self):
        self.users = {}
        self.current_user = None

    def add_user(self):
        username = input("Please create a username: ")
        if username in self.users:
            print("User with that name already exists. Please try again!")
        else:
            user = User(username)
            self.users[username] = user
            print(f"{user.name} has been created!")
        self.login_user()

    def login_user(self):
        username = input("To continue, log in with your username: ")
        if username in self.users:
            self.current_user = self.users[username]
            print(f"{self.current_user.name} has logged in")
        else:
            print("Username does not exist. Please create a username.")

    def change_user(self):
        if self.current_user:
            print(f"{self.current_user.name} has been logged out!")
            self.current_user = None
        else:
            print("No user is currently logged in.")

    def run(self):
        while True:
            menu = input("What would you like to do? Enter [a]to add user. Enter [c] to change user. Enter [l] to login user. Enter [p] to add a property. Enter [r] to calculate ROI. Enter [q] to quit: ")

            if menu.lower() == 'a':
                self.add_user()
                
            elif menu.lower() == 'c':
                self.change_user()

            elif menu.lower() == 'l':
                self.login_user()
               

            elif menu.lower() == 'p':
                if self.current_user:
                    property_id = int(input("Please enter your Property ID: "))
                    address = input(f"Please enter the address for Property ID: {property_id}: ").lower()
                    self.current_user.add_property(property_id, address)
                else:
                    print("Please log in as a user first.")

            elif menu.lower() == 'r':
                if self.current_user:
                    property_id = int(input("Please enter your Property ID: "))
                    property = self.current_user.properties.get(property_id)
                    if property:
                        property.calculate_roi()
                    else:
                        print(f"Property with ID: {property_id} not found in your properties. Please add it first.")
                else:
                    print("Please log in as a user first.")
           
            elif menu.lower() == 'q':
                print("Thanks for using the Rental Property Calculator!")
                break

roi = ROI()
roi.run()
