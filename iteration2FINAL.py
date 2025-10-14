import tkinter as tk
from tkinter import ttk, messagebox

# ==============================================================
# Main App Class – controls navigation between windows and stores user info
# ==============================================================
class RehabApp:
    def __init__(self):
        # Dictionary to keep all user information gathered through the steps
        self.user_data = {}

        # Define colors and fonts for visual consistency
        self.BG1 = "#4bc3eb"  # blue for welcome screen
        self.BG2 = "#A0DD4C"  # green for pain level
        self.BG3 = "#f69f4d"  # orange for body area
        self.BG4 = "#f64f92"  # pink for final screen
        self.FONT_HEADER = ("Helvetica", 14, "bold")
        self.FONT_BODY = ("Helvetica", 11)

        # Start the application by opening the first window
        self.launch_user_info()

    # Each function launches a new step/window of the app
    def launch_user_info(self):
        UserInfoWindow(self)

    def launch_pain_window(self):
        PainLevelWindow(self)

    def launch_bodypart_window(self):
        BodyPartWindow(self)

    def launch_final_recommendations(self):
        FinalRecommendationWindow(self)


# ==============================================================
# STEP 1 – User Info Window: collects name and year level
# ==============================================================
class UserInfoWindow:
    def __init__(self, app):
        self.app = app  # connects this window to the main app so data can be shared
        self.window = tk.Tk()
        self.window.title("Step 1: Student Info")
        self.window.geometry("350x200")
        self.window.config(bg=self.app.BG1)

        # Display welcome message at the top
        tk.Label(self.window, text="Welcome to Rehabilitation Assistant",
                 font=self.app.FONT_HEADER, bg=self.app.BG1, fg="black").pack(pady=5)

        # Ask user for their name
        tk.Label(self.window, text="Enter your name:",
                 bg=self.app.BG1, fg="black", font=self.app.FONT_BODY).pack()
        self.name_entry = tk.Entry(self.window, fg="white")  # entry box to type name
        self.name_entry.pack()

        # Ask user to select year level from dropdown (Yr9–Yr13)
        tk.Label(self.window, text="Select your year level:",
                 bg=self.app.BG1, fg="black", font=self.app.FONT_BODY).pack(pady=5)
        self.year_var = tk.StringVar()
        year_dropdown = ttk.Combobox(self.window, textvariable=self.year_var,
                                     values=[f"Yr{n}" for n in range(9, 14)], state="readonly")
        year_dropdown.set("Select Year")  # default option
        year_dropdown.pack()

        # Button to continue to the next step
        tk.Button(self.window, text="Next", command=self.next_step, fg="black").pack(pady=10)

        # Keep window open until user interacts
        self.window.mainloop()

    def next_step(self):
        # Fetch user inputs from entry boxes
        name = self.name_entry.get()
        year = self.year_var.get()

        # Make sure both fields are filled before moving on
        if not name or year == "Select Year":
            messagebox.showerror("Missing Info", "Please enter your name and select a year level.")
            return

        # Save valid data into the shared user_data dictionary
        self.app.user_data["name"] = name
        self.app.user_data["year"] = year

        # Close current window and open the pain level screen
        self.window.destroy()
        self.app.launch_pain_window()


# ==============================================================
# STEP 2 – Pain Level Window: asks the user to rate pain (0–10)
# ==============================================================
class PainLevelWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Tk()
        self.window.title("Step 2: Pain Level")
        self.window.geometry("350x150")
        self.window.config(bg=self.app.BG2)

        # Instructional label explaining how to rate pain
        tk.Label(self.window, text="On a scale from (0–10) rate how painful your body feels right now:",
                 font=self.app.FONT_BODY, bg=self.app.BG2, fg="black").pack(pady=10)

        # Entry box for entering pain number
        self.pain_entry = tk.Entry(self.window, fg="white")
        self.pain_entry.pack()

        # Button to continue once user inputs a number
        tk.Button(self.window, text="Next", command=self.next_step, fg="black").pack(pady=10)
        self.window.mainloop()

    def next_step(self):
        # Try to convert input to integer to ensure it's a valid number
        try:
            pain = int(self.pain_entry.get())

            # Check if the number is in the valid range 0–10
            if 0 <= pain <= 10:
                self.app.user_data["pain_level"] = pain  # store pain value
                self.window.destroy()  # close window
                self.app.launch_bodypart_window()  # go to next step
            else:
                raise ValueError  # if outside range, trigger error message

        # If user enters non-number or out-of-range input
        except ValueError:
            messagebox.showerror("Invalid", "Pain level must be a number from 0–10.")


# ==============================================================
# STEP 3 – Body Part Window: user selects which body area hurts
# ==============================================================
class BodyPartWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Tk()
        self.window.title("Step 3: Affected Area")
        self.window.geometry("350x160")
        self.window.config(bg=self.app.BG3)

        # Label explaining what to do
        tk.Label(self.window, text="Which part of your body hurts?",
                 font=self.app.FONT_BODY, bg=self.app.BG3, fg="black").pack(pady=10)

        # Dropdown with multiple body part options
        self.area_var = tk.StringVar()
        area_dropdown = ttk.Combobox(
            self.window,
            textvariable=self.area_var,
            values=["Knee", "Shoulder", "Back", "Wrist", "Ankle", "Thigh",
                    "Head", "Neck", "Hand", "Hamstring", "Face", "Chest"],
            state="readonly"
        )
        area_dropdown.set("Select Area")
        area_dropdown.pack()

        # Button to continue after choosing an area
        tk.Button(self.window, text="Next", command=self.next_step, fg="black").pack(pady=10)
        self.window.mainloop()

    def next_step(self):
        # Get selected body part from dropdown
        area = self.area_var.get()

        # Ensure user actually selected something
        if not area or area == "Select Area":
            messagebox.showerror("Missing Info", "Please select the body part which is causing pain.")
            return

        # Save body area and move to final recommendations screen
        self.app.user_data["body_area"] = area
        self.window.destroy()
        self.app.launch_final_recommendations()


# ==============================================================
# STEP 4 – Final Recommendation Window: shows rehab plan
# ==============================================================
class FinalRecommendationWindow:
    def __init__(self, app):
        self.app = app
        user = self.app.user_data  # retrieve all stored info

        # Pull out each value from dictionary for clarity
        name = user["name"]
        year = user["year"]
        pain = user["pain_level"]
        area = user["body_area"]

        # Determine recovery category and advice based on pain severity
        if pain <= 3:
            status = "Minor"
            rec_exercise = f"Gentle stretches and walking; light yoga targeting the {area.lower()}."
            diet = "Drink water, eat anti-inflammatory foods and light protein."
            tips = "Stay lightly active, monitor any pain changes, and rest well."
        elif pain <= 7:
            status = "Moderate"
            rec_exercise = f"Controlled physio for {area.lower()} with resistance bands."
            diet = "Add omega-3 foods, reduce sugar/salt, include leafy greens."
            tips = "Rest between exercises, track progress, use heat/ice therapy."
        else:
            status = "Severe"
            rec_exercise = f"Limit movement of {area.lower()}, and use support gear if needed."
            diet = "Turmeric, berries, and greens to reduce inflammation."
            tips = "Prioritize rest, focus on breathing techniques, and seek advice."

        # Create window to display final report
        self.window = tk.Tk()
        self.window.title("Final Recommendations")
        self.window.geometry("420x350")
        self.window.config(bg=self.app.BG4)

        # Header summarizing user's inputs
        tk.Label(self.window, text=f"🧾 Rehab Report for {name} ({year})",
                 font=self.app.FONT_HEADER, bg=self.app.BG4, fg="black").pack(pady=10)

        # Display results (pain level, affected area, etc.)
        tk.Label(self.window, text=f"Pain Level: {pain} ({status})",
                 font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack()
        tk.Label(self.window, text=f"Affected Area: {area}",
                 font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack(pady=5)

        # Exercise advice section
        tk.Label(self.window, text="🏃‍♀️ Recommended Exercises:",
                 font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack()
        tk.Label(self.window, text=rec_exercise, wraplength=380,
                 bg=self.app.BG4, fg="black").pack()

        # Diet advice section
        tk.Label(self.window, text="🥗 Diet Tips:",
                 font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack(pady=5)
        tk.Label(self.window, text=diet, wraplength=380,
                 bg=self.app.BG4, fg="black").pack()

        # General recovery tips
        tk.Label(self.window, text="🛌 Recovery Advice:",
                 font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack(pady=5)
        tk.Label(self.window, text=tips, wraplength=380,
                 bg=self.app.BG4, fg="black").pack()

        # Close button to end program
        tk.Button(self.window, text="Close", command=self.window.destroy,
                  fg="black").pack(pady=15)

        # Keep window open until user closes it
        self.window.mainloop()


# ==============================================================
# Run the application
# ==============================================================
if __name__ == "__main__":
    RehabApp()
