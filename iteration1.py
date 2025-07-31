# Class to store user information such as their name and injury type
class User:
    def __init__(self, name, injury_type):
        # Initializes a new User object with a name and injury type
        self.name = name
        self.injury_type = injury_type

    def display_info(self):
        # Prints the user's name and injury information
        print(f"User: {self.name}, Injury: {self.injury_type}")

# Class representing an exercise used in rehabilitation
class Exercise:
    def __init__(self, name, target_area, description):
        # Initializes an Exercise object with its name, the body area it targets, and a short description
        self.name = name
        self.target_area = target_area
        self.description = description

    def show_details(self):
        # Displays the name, target area, and description of the exercise
        print(f"{self.name} – Targets: {self.target_area}\nDescription: {self.description}")

# Class representing a single rehabilitation session
class Session:
    def __init__(self, date, exercise, pain_level):
        # Initializes a session with a date, an Exercise object, and a pain level (from 0 to 10)
        self.date = date
        self.exercise = exercise
        self.pain_level = pain_level

    def display_session(self):
        # Displays session details including date, exercise name, and recorded pain level
        print(f"{self.date}: {self.exercise.name}, Pain Level: {self.pain_level}")

# Function to select an exercise – currently just returns a fixed exercise
def select_exercise():
    # Create two predefined exercise objects
    exercise1 = Exercise("Arm Circles", "Shoulder", "Rotate arms gently in circles.")
    exercise2 = Exercise("Leg Raises", "Thigh", "Lift leg while lying down.")
    
    # Right now, we always return exercise1 as a placeholder
    # In future versions, you could ask the user to choose between multiple options
    return exercise1

# Function to enter the user's pain level after doing the exercise
def enter_pain_level():
    try:
        # Ask the user to input a pain level from 0 to 10
        level = int(input("Enter pain level (0–10): "))
        if 0 <= level <= 10:
            # Valid input – return the pain level
            return level
        else:
            # If input is outside the valid range, show an error and retry
            print("Invalid – enter a number from 0 to 10.")
            return enter_pain_level()
    except ValueError:
        # If input is not a number, show an error and retry
        print("Invalid – please enter a number.")
        return enter_pain_level()

# Function to record and store a rehabilitation session for the user
def save_session(user, session_list):
    # Select an exercise (currently fixed to one predefined exercise)
    exercise = select_exercise()

    # Ask the user to input their pain level after doing the exercise
    pain = enter_pain_level()

    # Create a new Session object using today's date, the selected exercise, and entered pain level
    session = Session("2025-07-31", exercise, pain)

    # Add the new session to the session list
    session_list.append(session)

    # Confirm that the session has been saved
    print("Session saved.")

# Main program entry point (used for testing this code)
if __name__ == "__main__":
    # Create a sample user for demonstration
    user1 = User("Aminder", "Knee Strain")

    # Create an empty list to hold all the sessions for this user
    sessions = []

    # Save a session (this involves selecting an exercise and entering a pain level)
    save_session(user1, sessions)

    # Display the details of the first (and only) session saved
    sessions[0].display_session()
