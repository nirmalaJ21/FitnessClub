import unittest
import datetime
from fitnesscenter import FitnessCenter, Club, SingleClubMember, MultiClubMember,Member


class TestMember_Finteness(unittest.TestCase):

    def setUp(self):
        # create a Club instance
        # create a Member instance
        self.club = Club("Test Club",'ClubA')
        self.member = SingleClubMember(1, "John Smith", self.club)
        self.club1 = Club(1, "Club 1")
        self.club2 = Club(2, "Club 2")
        self.member1 = MultiClubMember(1, "Anaye")
        self.fc = FitnessCenter()
    def test_check_in_Memeber(self):
        #Check in Memeber class check in method returns void/None
        self.assertEqual(Member.check_in(self,self.club), None)

    def test_check_in_correct_Single_club(self):
        # Test that member can check in to their own club
        self.assertTrue(self.member.check_in(self.club))

    def test_check_in_Single_wrong_club(self):
        # Test that member cannot check in to another club
        other_club = Club("Other Club",'Club B')
        expected_output = f"Alert! {self.member.name} is not a member of {other_club.name}.Please check in at your club{self.club.name}."
        with self.assertRaisesRegex(SystemExit, expected_output):
            self.member.check_in(other_club)

    def test_check_in_Multi_club(self):
        # Test initial membership points
        self.assertEqual(self.member1.membership_points, 0)
        # Test check-in at club 1
        self.assertTrue(self.member1.check_in(self.club1))
        self.assertEqual(self.member1.membership_points, 1)
        # Test check-in at club 1
        self.assertTrue(self.member1.check_in(self.club2))
        self.assertEqual(self.member1.membership_points, 2)
        # Test check-in at club 1 again
        self.assertTrue(self.member1.check_in(self.club1))
        self.assertEqual(self.member1.membership_points, 3)

    def test_club(self):
        # Test initialization of Club class
        club = Club("Chess Club", "123 Main St.")
        self.assertEqual(club.name, "Chess Club")
        self.assertEqual(club.address, "123 Main St.")

    def test_add_number(self):
        self.assertEqual(self.fc.add_member(), None)  # true because returns no member instance,
    def test_check_promotion_period(self):
        self.assertEqual((self.fc.is_promotion_period()), False)  # supposed to be True becuase promotion is set to today.
    def test_remove_member(self):
        self.assertIsNone(self.fc.remove_member())
    def test_display_member(self):
        self.assertEqual(self.fc.display_member_info(), None) # True because of ro return value
    def test_choose_club(self):
        self.assertEqual(self.fc.choose_club(), object) # choose club is storing the memory.
    def test_check_in(self):
        self.assertEqual(self.fc.check_in_member(), None) # true becuase function returns no value
    def test_generate_bill(self):
        self.assertEqual(self.fc.generate_bill(), None)  # True because no member instanced.
    def test_run(self):
        self.assertEqual(self.fc.run(), None)  # no return value, so true.


    if __name__ == '__main__':
     unittest.main()