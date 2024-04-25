class MobileTracker:
    """
    A class to track the mobile number of a lost or stolen SIM card or phone.

    Attributes:
    - owner_name (str): The name of the owner of the mobile number.
    - mobile_number (str): The mobile number to be tracked.
    - is_lost (bool): Flag to indicate if the mobile number is lost or stolen.
    """

    def __init__(self, owner_name, mobile_number):
        """
        Initialize the MobileTracker with owner's name and mobile number.

        Args:
        - owner_name (str): The name of the owner.
        - mobile_number (str): The mobile number to be tracked.
        """
        self.owner_name = owner_name
        self.mobile_number = mobile_number
        self.is_lost = False

    def report_lost(self):
        """
        Report the mobile number as lost or stolen.
        """
        self.is_lost = True
        print(f"Mobile number {self.mobile_number} reported as lost/stolen.")

    def find_mobile(self):
        """
        Find the mobile number if it is lost or stolen.
        """
        if self.is_lost:
            print(f"Mobile number {self.mobile_number} is currently lost/stolen. Please contact authorities.")
        else:
            print(f"Mobile number {self.mobile_number} is safe with {self.owner_name}.")

# Example Usage
# Create a MobileTracker instance
my_mobile = MobileTracker("John Doe", "123-456-7890")

# Report the mobile number as lost
my_mobile.report_lost()

# Find the mobile number status
my_mobile.find_mobile()
