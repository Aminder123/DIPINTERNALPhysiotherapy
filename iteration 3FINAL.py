import tkinter as tk                      # Import the Tkinter module for creating graphical user interfaces
from tkinter import ttk, messagebox        # Import themed widgets (ttk) and popup message boxes
import random                              # Import random module to randomly select motivational quotes


# -------------------- CLASS-BASED REHABILITATION ASSISTANT --------------------
class RehabApp:
    def __init__(self):
        # -------------------- Global Data --------------------
        self.user_data = {}  # Dictionary used to store user inputs across all steps (name, pain, etc.)

        # -------------------- Theme & UI Styling --------------------
        # Define background colors for different windows to maintain a consistent modern design
        self.BG1 = "#332F2C"  # Dark coffee brown background (used in intro and info windows)
        self.BG2 = "#bba691"  # Tan brown background (used in pain input window)
        self.BG3 = "#9f9f9f"  # Warm grey (used in body area selection window)
        self.BG4 = "#85756d"  # Darker brown (used in final recommendation screen)
        
        # Define fonts and widget colors for uniform styling
        self.FONT_HEADER = ("Arial", 14, "bold")   # Font for headers and titles
        self.FONT_BODY = ("Calibri", 11)           # Font for regular text and labels
        self.BUTTON_BG = "#A0DD4C"                 # Button background color (soft green)
        self.BUTTON_FG = "black"                   # Button text color
        self.ENTRY_BG = "#f4f1ee"                  # Entry field background (light beige)
        self.ENTRY_FG = "black"                    # Entry field text color

        # -------------------- Motivational Quotes --------------------
        # A list of positive reinforcement messages randomly shown at the end of the program
        self.MOTIVATIONAL_QUOTES = [
            "Small steps each day lead to big progress.",
            "Listen to your body — recovery takes time.",
            "Stay positive, healing is a journey.",
            "Consistency matters more than intensity.",
            "Every bit of effort helps!"
        ]

        # Start the app by showing the introduction screen first
        self.launch_intro_window()

    # -------------------- PROGRESS BAR FUNCTION --------------------
    def update_progress(self, window, step, total_steps):
        # Create a progress bar that visually shows how far along the user is in the 4-step process
        progress = ttk.Progressbar(window, length=250, mode="determinate")
        progress["value"] = (step / total_steps) * 100  # Calculate completion percentage
        progress.pack(pady=5)
        # Display the step number under the progress bar
        tk.Label(window, text=f"Step {step} of {total_steps}", bg=window["bg"], fg="white").pack()

    # -------------------- STEP 0: INTRO WINDOW --------------------
    def launch_intro_window(self):
        # Function to create and display the introductory screen of the application

        # Nested function to start the questionnaire (called when "Start New Session" button is clicked)
        def start_new():
            window.destroy()              # Close the current intro window
            self.launch_user_info()       # Move to the first question window

        # Nested function to close the entire app
        def close_app():
            window.destroy()

        # Create the main Tkinter window
        window = tk.Tk()
        window.title("Rehabilitation Assistant - Introduction")  # Set title bar text
        window.geometry("420x520")                               # Set fixed window size
        window.config(bg=self.BG1)                               # Apply theme background

        # Create title label
        tk.Label(window, text="Welcome to the Rehabilitation Assistant!",
                 font=self.FONT_HEADER, bg=self.BG1, fg="white",
                 relief="ridge", bd=3, padx=5, pady=5).pack(pady=20)

        # Create a short description under the title
        tk.Label(window, text="Your personal guide to recovery and progress tracking.",
                 bg=self.BG1, font=self.FONT_BODY, wraplength=360, fg="white").pack(pady=10)

        # Button to start a new session
        tk.Button(window, text="Start New Session", width=20, command=start_new,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)

        # Button to exit the application
        tk.Button(window, text="Close", width=20, command=close_app,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)

        window.mainloop()  # Keep window open until closed by user

    # -------------------- STEP 1: STUDENT INFO WINDOW --------------------
    def launch_user_info(self):
        # Function to collect user’s name and school year

        # Function called when "Next" button is clicked
        def next_step():
            name = name_entry.get()        # Get user name input
            year = year_var.get()          # Get selected year from dropdown
            # Validate that both fields are filled in
            if not name or year == "Select Year":
                messagebox.showerror("Missing Info", "Please enter your name and select a year level.")
                return
            # Store collected data
            self.user_data["name"] = name
            self.user_data["year"] = year
            # Close this window and open the next one
            window.destroy()
            self.launch_pain_window()

        # Create window
        window = tk.Tk()
        window.title("Step 1: Student Info")
        window.geometry("420x520")
        window.config(bg=self.BG1)

        # Add progress bar showing Step 1 of 4
        self.update_progress(window, 1, 4)

        # Labels and entry widgets
        tk.Label(window, text="Welcome to the Rehabilitation Assistant", font=self.FONT_HEADER,
                 bg=self.BG1, fg="white", relief="ridge", bd=3, padx=5, pady=5).pack(pady=5)

        tk.Label(window, text="Enter your name:", bg=self.BG1, font=self.FONT_BODY, fg="white").pack()
        name_entry = tk.Entry(window, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="groove", bd=2)
        name_entry.pack(pady=5)

        tk.Label(window, text="Select your year level:", bg=self.BG1, font=self.FONT_BODY, fg="white").pack(pady=5)
        year_var = tk.StringVar()
        # Dropdown menu for year selection
        year_dropdown = ttk.Combobox(window, textvariable=year_var,
                                     values=[f"Yr{n}" for n in range(9, 14)], state="readonly")
        year_dropdown.set("Select Year")
        year_dropdown.pack()

        # Button to move to next step
        tk.Button(window, text="Next", command=next_step,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)

        window.mainloop()

    # -------------------- STEP 2: PAIN LEVEL WINDOW --------------------
    def launch_pain_window(self):
        # Function to collect user's current pain level on a scale of 0–10

        def next_step():
            pain = pain_var.get()              # Get value from scale
            self.user_data["pain_level"] = pain  # Store pain level in dictionary
            window.destroy()                   # Close this window
            self.launch_bodypart_window()      # Move to next step

        window = tk.Tk()
        window.title("Step 2: Pain Level")
        window.geometry("420x520")
        window.config(bg=self.BG2)

        # Update progress bar to Step 2 of 4
        self.update_progress(window, 2, 4)

        # Instruction label
        tk.Label(window, text="Rate your pain (0–10):", font=self.FONT_BODY, bg=self.BG2, fg="white").pack(pady=10)

        # Horizontal scale for pain rating
        pain_var = tk.IntVar(value=0)
        tk.Scale(window, from_=0, to=10, orient="horizontal", variable=pain_var,
                 bg=self.BG2, troughcolor="#d1c4b2", highlightbackground=self.BG2).pack(pady=5)

        # Button to proceed
        tk.Button(window, text="Next", command=next_step,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)
        window.mainloop()

    # -------------------- STEP 3: BODY AREA & ACTIVITY --------------------
    def launch_bodypart_window(self):
        # Function to select affected body areas and type of physical activity

        def next_step():
            # Collect checked body areas
            selected_areas = [area for area, var in body_areas.items() if var.get()]
            # Validate that at least one is selected
            if not selected_areas:
                messagebox.showerror("Missing Info", "Please select at least one body area.")
                return

            # Get activity selection
            activity = activity_var.get()
            if activity == "Select Activity":
                messagebox.showerror("Missing Info", "Please select your activity type.")
                return

            # Store data
            self.user_data["body_area"] = ", ".join(selected_areas)
            self.user_data["activity"] = activity

            # Move to final recommendations
            window.destroy()
            self.launch_final_recommendations()

        window = tk.Tk()
        window.title("Step 3: Body Area & Activity")
        window.geometry("420x520")
        window.config(bg=self.BG3)

        # Update progress bar (Step 3 of 4)
        self.update_progress(window, 3, 4)

        # Label for body area selection
        tk.Label(window, text="Which parts of your body hurt?", font=self.FONT_BODY, bg=self.BG3, fg="white").pack(pady=5)

        # Dictionary to hold BooleanVars for each body area
        body_areas = {}
        for area in ["Knee", "Shoulder", "Back", "Wrist", "Ankle", "Thigh", "Neck", "Hand", "Hamstring"]:
            var = tk.BooleanVar()
            # Each area is represented as a checkbox
            tk.Checkbutton(window, text=area, variable=var, bg=self.BG3, fg="white", selectcolor="#bba691").pack(anchor="w")
            body_areas[area] = var  # Save variable in dictionary

        # Dropdown for activity type
        tk.Label(window, text="Select activity type:", font=self.FONT_BODY, bg=self.BG3, fg="white").pack(pady=10)
        activity_var = tk.StringVar()
        activity_dropdown = ttk.Combobox(window, textvariable=activity_var,
                                         values=["Sports Player", "Casual Exerciser", "Post-Injury Recovery"],
                                         state="readonly")
        activity_dropdown.set("Select Activity")
        activity_dropdown.pack()

        # Next button
        tk.Button(window, text="Next", command=next_step,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=15)
        window.mainloop()

    # -------------------- STEP 4: FINAL RECOMMENDATIONS --------------------
    def launch_final_recommendations(self):
        # Function to display personalized recommendations based on user inputs

        # Retrieve data from dictionary
        name = self.user_data["name"]
        year = self.user_data["year"]
        pain = self.user_data["pain_level"]
        area = self.user_data["body_area"]
        activity = self.user_data["activity"]

        # Generate recommendations based on pain level
        if pain <= 3:
            status = "Minor"
            rec_exercise = f"Gentle stretches (5–10 min) for {area.lower()}."
            diet = "Drink water and eat healthy snacks."
            tips = "Stay lightly active and rest well."
            color = "green"
        elif pain <= 7:
            status = "Moderate"
            rec_exercise = f"Light physio for {area.lower()} with breaks."
            diet = "Add omega-3 foods, reduce sugar and sodium."
            tips = "Take rest days and track your recovery."
            color = "orange"
        else:
            status = "Severe"
            rec_exercise = f"Rest and limit movement of {area.lower()}."
            diet = "Eat vegetables, fruits, and stay hydrated."
            tips = "Seek professional help if pain continues."
            color = "red"

        # Randomly select a motivational quote
        motivation = random.choice(self.MOTIVATIONAL_QUOTES)

        # Create final results window
        window = tk.Tk()
        window.title("Final Recommendations")
        window.geometry("440x520")
        window.config(bg=self.BG4)

        # Show completion progress
        self.update_progress(window, 4, 4)

        # Display the final personalized summary
        tk.Label(window, text=f"🧾 Rehab Report for {name} ({year})", font=self.FONT_HEADER,
                 bg=self.BG4, fg="white", relief="ridge", bd=3, padx=5, pady=5).pack(pady=10)

        # Show all calculated results and suggestions
        tk.Label(window, text=f"Pain Level: {pain} ({status})", font=self.FONT_BODY, bg=self.BG4, fg=color).pack()
        tk.Label(window, text=f"Affected Area(s): {area}", font=self.FONT_BODY, bg=self.BG4, fg="white").pack()
        tk.Label(window, text=f"Activity: {activity}", font=self.FONT_BODY, bg=self.BG4, fg="white").pack(pady=5)

        tk.Label(window, text="🏃‍♀️ Exercises:", font=self.FONT_BODY, bg=self.BG4, fg="white").pack()
        tk.Label(window, text=rec_exercise, wraplength=380, bg=self.BG4, fg="white").pack()

        tk.Label(window, text="🥗 Diet Tips:", font=self.FONT_BODY, bg=self.BG4, fg="white").pack(pady=5)
        tk.Label(window, text=diet, wraplength=380, bg=self.BG4, fg="white").pack()

        tk.Label(window, text="🛌 Recovery Advice:", font=self.FONT_BODY, bg=self.BG4, fg="white").pack(pady=5)
        tk.Label(window, text=tips, wraplength=380, bg=self.BG4, fg="white").pack()

        # Display motivational quote at the end
        tk.Label(window, text=f"💡 Motivation: {motivation}", font=self.FONT_BODY,
                 bg=self.BG4, wraplength=380, fg="yellow").pack(pady=10)

        # Button to close the program
        tk.Button(window, text="Close", command=window.destroy,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)

        window.mainloop()


# -------------------- MAIN PROGRAM ENTRY POINT --------------------
# If this script is executed directly (not imported), run the app
if __name__ == "__main__":
    RehabApp()  # Create an instance of the RehabApp class, starting the application
