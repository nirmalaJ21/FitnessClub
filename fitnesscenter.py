
""" This is a simple Fitness membership app to help manage members and membership options."""

"""Member class is for storing member information, has two child class
  SingleClubMember and MultiClubMember"""
import os
import datetime
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name


    def check_in(self, Club ):

        return

class SingleClubMember(Member):
    def __init__(self, member_id, name, club):
        self.member_id = member_id
        self.name = name
        self.club = club
#The check_in method alerts the user if it’s not their club and prompts them again for the correct club or to cancel the check in process
    def check_in(self, club):
        if club.name != self.club.name:
            print(f"Alert! {self.name} is not a member of {club.name}. Please check in here: {club.name}.")
            return False
        else:
            print(f"Welcome {self.name} to {club.name}!")
            return True


class MultiClubMember(Member):
    def __init__(self, member_id, name, membership_points=0):
        self.member_id = member_id
        self.name = name
        self.membership_points = membership_points
#The check_in method adds to their membership points
    def check_in(self, club):
        self.membership_points += 1
        print(f"Welcome {self.name} to {club.name}! Membership points: {self.membership_points}")
        return True
# Club class that holds basic details about each fitness club
class Club():
    def __init__(self,Name,Address):
        self.name = Name
        self.address = Address


class FitnessCenter:
    def __init__(self):
        self.members = []
        self.clubs = [Club("Basketball Club", "100 Park Way"), Club("Golf Club", "102 Park Way"), Club("Tennis Club", "104 Park Way"),
                      Club("Tennis Club", "106 Park Way")]
        self.promotion_start_date = datetime.date(2023, 4, 1)
        self.promotion_end_date = datetime.date(2023, 4, 30)
#Add members (both kinds),
    def add_member(self):
        while True:
            name = input("Enter name of member: ")
            if not name:
                print("Name cannot be empty. Please try again.")
                continue
            break

        while True:
            membership_type = input("Enter membership type (Single/Multi): ").lower()
            if membership_type not in ("single", "multi"):
                print("Invalid membership type. Please enter 'single' or 'multi'.")
                continue
            break

        member_id = len(self.members) + 1
        if membership_type == "single":
            club = self.choose_club()
            member = SingleClubMember(member_id, name, club)
        else:
            member = MultiClubMember(member_id, name)
        if self.is_promotion_period():
            print("You have signed up during the promotion period!")
            if isinstance(member, SingleClubMember):
                cost = 40
            else:
                cost = 80
            print(f"You get discount of: ${cost}")
        else:
            print(f"{name} has been added as a {membership_type}-club member with ID {member_id}.")
            if isinstance(member, SingleClubMember):
                cost = 50
            else:
                cost = 100
            print(f"You get discount of: ${cost}")
        self.members.append(member)


    def is_promotion_period(self):
        today = datetime.date.today()
        return self.promotion_start_date <= today <= self.promotion_end_date
#Remove members (both kinds),
    def remove_member(self):
        while True:
            try:
                member_id = int(input("Enter ID of member to remove: "))
                if member_id <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid member ID. Please enter a positive integer.")
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member with ID {member_id} has been removed.")
                return
        print(f"No member found with ID {member_id}.")
#Display member information.
    def display_member_info(self):

        while True:
            try:
                member_id = int(input("Enter ID of member to display: "))
                if member_id <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid member ID. Please enter a positive integer.")
        for member in self.members:
            if member.member_id == member_id:
                print(f"Member ID: {member.member_id}")
                print(f"Name: {member.name}")
                if isinstance(member, SingleClubMember):
                    print(f"Membership Type: Single-Club")
                    print(f"Club: {member.club.name}")
                else:
                    print(f"Membership Type: Multi-Club")
                    print(f"Points: {member.membership_points}")
                return
        print(f"No member found with ID {member_id}.")
 #tMethod to select from  4 fitness center locations
    def choose_club(self):
     while True:
        print("Choose a club:")
        for i, club in enumerate(self.clubs):
            print(f"{i + 1}. {club.name} - {club.address}")
        choice = input()
        try:
            index = int(choice) - 1
            if index >= 0 and index < len(self.clubs):
                return self.clubs[index]
            else:
                print("Invalid choice. Please choose again.")
        except ValueError:
            print("Invalid choice. Please choose again.")
#Check a particular member in at a particular club. (Call the check_in method)
    def check_in_member(self):
        while True:
            try:
                member_id = int(input("Enter ID of member to check in: "))
                if member_id <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid member ID. Please enter a positive integer.")
        for member in self.members:
            if member.member_id == member_id:
                if isinstance(member, SingleClubMember):
                    club = self.choose_club()
                    member.check_in(club)
                else:
                    club = self.choose_club()
                    member.check_in(club)
                return
        print(f"No member found with ID {member_id}.")
#Select a member and generate a bill of fees.
    def generate_bill(self):

     while True:
         try:
             member_id = int(input("Enter ID of member to generate bill: "))
             if member_id <= 0:
                 raise ValueError
             break
         except ValueError:
             print("Invalid member ID. Please enter a positive integer.")
     for member in self.members:
        if member.member_id == member_id:
            #
            if self.is_promotion_period():
                if isinstance(member, SingleClubMember):
                    Dicost = 40
                else:
                    Dicost = 80
                print(f"You get discount of: ${Dicost}")
            else:
                if isinstance(member, SingleClubMember):
                    Dicost = 50
                else:
                    Dicost = 100
                print(f"You get discount of: ${Dicost}")
            #
            print(f"Member ID: {member.member_id}")
            print(f"Name: {member.name}")
            if isinstance(member, SingleClubMember):
                print(f"Membership Type: Single-Club")
                print(f"Club: {member.club.name}")
                cost = 500 # cost for single-club membership
            else:
                print(f"Membership Type: Multi-Club")
                print(f"Points: {member.membership_points}")
                cost = 800  # cost for multi-club membership
                if member.membership_points > 10:
                    discount = 0.1  # 10% discount for more than 10 points
                    cost *= (1 - discount)
                    print(f"You have received a extra 10% discount for having more than 10 points.")
            cost = cost -Dicost
            print(f"Total cost: ${cost}")
            return
     print(f"No member found with ID {member_id}.")
#Method to display main menu and carry out operations
    def run(self):
     print('WELCOME TO FITNESS CENTER')
     print("*"*50)
     while True:
        print("What would you like to do?")
        print("1. Add member")
        print("2. Remove member")
        print("3. Display member information")
        print("4. Check in member")
        print("5. Generate bill")
        print("6. Quit")
        choice = input()
        if choice == "1":
            self.add_member()
        elif choice == "2":
            self.remove_member()
        elif choice == "3":
            self.display_member_info()
        elif choice == "4":
            self.check_in_member()
        elif choice == "5":
            self.generate_bill()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")
if __name__ == "__main__":
    print("This file is not intended to be run as a main.")
