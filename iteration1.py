# Class to store user information
class User:
    def __init__(self, name, injury_type):
        self.name = name
        self.injury_type = injury_type

    def display_info(self):
        print(f"User: {self.name}, Injury: {self.injury_type}")

# Class for an exercise
class Exercise:
    def __init__(self, name, target_area, description):
        self.name = name
        self.target_area = target_area
        self.description = description

    def show_details(self):
        print(f"{self.name} – Targets: {self.target_area}\nDescription: {self.description}")

# Class to store one rehabilitation session
class Session:
    def __init__(self, date, exercise, pain_level):
        self.date = date
        self.exercise = exercise
        self.pain_level = pain_level

    def display_session(self):
        print(f"{self.date}: {self.exercise.name}, Pain Level: {self.pain_level}")

# Function to select an exercise (simple return from list for now)
def select_exercise():
    exercise1 = Exercise("Arm Circles", "Shoulder", "Rotate arms gently in circles.")
    exercise2 = Exercise("Leg Raises", "Thigh", "Lift leg while lying down.")
    return exercise1  # Placeholder – can later let user choose

# Function to enter pain level with input validation
def enter_pain_level():
    try:
        level = int(input("Enter pain level (0–10): "))
        if 0 <= level <= 10:
            return level
        else:
            print("Invalid – enter a number from 0 to 10.")
            return enter_pain_level()
    except ValueError:
        print("Invalid – please enter a number.")
        return enter_pain_level()

# Function to save session to a simple list (later could be file/database)
def save_session(user, session_list):
    exercise = select_exercise()
    pain = enter_pain_level()
    session = Session("2025-07-31", exercise, pain)
    session_list.append(session)
    print("Session saved.")

# Main run logic (for testing)
if __name__ == "__main__":
    user1 = User("Aminder", "Knee Strain")
    sessions = []
    save_session(user1, sessions)
    sessions[0].display_session()
