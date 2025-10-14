# -----------------------------
# Class to store user information
# -----------------------------
class User:
    def __init__(self, name, injury_type):
        # Constructor: runs automatically when a new User object is created
        # 'name' = user's name, 'injury_type' = description of user's injury
        self.name = name
        self.injury_type = injury_type

    def display_info(self):
        # Prints user details in a formatted way
        print(f"User: {self.name}, Injury: {self.injury_type}")


# -----------------------------
# Class for an exercise
# -----------------------------
class Exercise:
    def __init__(self, name, target_area, description):
        # Stores details about an exercise
        # 'name' = exercise name, e.g., "Arm Circles"
        # 'target_area' = body part worked on, e.g., "Shoulder"
        # 'description' = short explanation of how to do the exercise
        self.name = name
        self.target_area = target_area
        self.description = description

    def show_details(self):
        # Displays exercise details nicely formatted
        print(f"{self.name} – Targets: {self.target_area}\nDescription: {self.description}")


# -----------------------------
# Class to store one rehabilitation session
# -----------------------------
class Session:
    def __init__(self, date, exercise, pain_level):
        # Stores details for a single rehab session
        # 'date' = when the session occurred
        # 'exercise' = which Exercise object was used
        # 'pain_level' = user’s self-reported pain level (0–10)
        self.date = date
        self.exercise = exercise
        self.pain_level = pain_level

    def display_session(self):
        # Displays key details of the session
        print(f"{self.date}: {self.exercise.name}, Pain Level: {self.pain_level}")


# -----------------------------
# Function to select an exercise
# -----------------------------
def select_exercise():
    # Create two example exercises (can be expanded later)
    exercise1 = Exercise("Arm Circles", "Shoulder", "Rotate arms gently in circles.")
    exercise2 = Exercise("Leg Raises", "Thigh", "Lift leg while lying down.")
    
    # Currently always returns exercise1 – this is a placeholder
    # Later, you can add logic to let the user choose between multiple exercises
    return exercise1


# -----------------------------
# Function to enter pain level with input validation
# -----------------------------
def enter_pain_level():
    try:
        # Ask the user to input their pain level (integer expected)
        level = int(input("Enter pain level (0–10): "))
        
        # Check if the entered number is within the valid range
        if 0 <= level <= 10:
            return level  # Valid input – return it
        else:
            # If the number is outside the range, print a warning and re-ask
            print("Invalid – enter a number from 0 to 10.")
            return enter_pain_level()  # Recursive call to re-prompt user

    except ValueError:
        # Handles case when user enters something that’s not a number (e.g., text)
        print("Invalid – please enter a number.")
        return enter_pain_level()  # Re-prompt user again


# -----------------------------
# Function to save a session
# -----------------------------
def save_session(user, session_list):
    # Allows recording one new rehab session for a user
    
    # Step 1: Select an exercise
    exercise = select_exercise()
    
    # Step 2: Ask user to enter pain level with validation
    pain = enter_pain_level()
    
    # Step 3: Create a new Session object
    # (In a full program, the date could be set automatically using datetime.today())
    session = Session("2025-07-31", exercise, pain)
    
    # Step 4: Add this session to the session list
    session_list.append(session)
    
    # Step 5: Confirm to the user that the session was saved
    print("Session saved.")


# -----------------------------
# Main program run logic (for testing)
# -----------------------------
if __name__ == "__main__":
    # Create a user with name and injury type
    user1 = User("Aminder", "Knee Strain")
    
    # Create an empty list to hold all session data
    sessions = []
    
    # Save one session (calls select_exercise + enter_pain_level)
    save_session(user1, sessions)
    
    # Display the first saved session to confirm it worked
    sessions[0].display_session()
