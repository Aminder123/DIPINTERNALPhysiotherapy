import tkinter as tk                      # Import Tkinter for GUI window creation
from tkinter import ttk, messagebox        # Import themed widgets and message boxes
import random                              # Import random for motivational quote selection


# -------------------- CLASS-BASED REHABILITATION ASSISTANT --------------------
class RehabApp:
    def __init__(self):
        # -------------------- Global Data --------------------
        self.user_data = {}  # Dictionary storing all user responses and info

        # -------------------- Modern Neutral Theme --------------------
        self.BG1 = "#322F2B"  # dark coffee brown
        self.BG2 = "#bba691"  # tan brown
        self.BG3 = "#9f9f9f"  # warm grey
        self.BG4 = "#85756d"  # darker brown
        self.FONT_HEADER = ("Arial", 14, "bold")
        self.FONT_BODY = ("Calibri", 11)
        self.BUTTON_BG = "#A0DD4C"
        self.BUTTON_FG = "black"
        self.ENTRY_BG = "#f4f1ee"
        self.ENTRY_FG = "black"

        # -------------------- Motivational Quotes --------------------
        self.MOTIVATIONAL_QUOTES = [
            "Small steps each day lead to big progress.",
            "Listen to your body — recovery takes time.",
            "Stay positive, healing is a journey.",
            "Consistency matters more than intensity.",
            "Every bit of effort helps!"
        ]

        # Start the app
        self.launch_intro_window()

    # -------------------- Progress Bar --------------------
    def update_progress(self, window, step, total_steps):
        progress = ttk.Progressbar(window, length=250, mode="determinate")
        progress["value"] = (step / total_steps) * 100
        progress.pack(pady=5)
        tk.Label(window, text=f"Step {step} of {total_steps}", bg=window["bg"], fg="white").pack()

    # -------------------- INTRO WINDOW --------------------
    def launch_intro_window(self):
        def start_new():
            window.destroy()
            self.launch_user_info()

        def close_app():
            window.destroy()

        window = tk.Tk()
        window.title("Rehabilitation Assistant - Introduction")
        window.geometry("420x520")
        window.config(bg=self.BG1)

        tk.Label(window, text="Welcome to the Rehabilitation Assistant!",
                 font=self.FONT_HEADER, bg=self.BG1, fg="white",
                 relief="ridge", bd=3, padx=5, pady=5).pack(pady=20)
        tk.Label(window, text="Your personal guide to recovery and progress tracking.",
                 bg=self.BG1, font=self.FONT_BODY, wraplength=360, fg="white").pack(pady=10)

        tk.Button(window, text="Start New Session", width=20, command=start_new,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)
        tk.Button(window, text="Close", width=20, command=close_app,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)
        window.mainloop()

    # -------------------- STEP 1: Student Info --------------------
    def launch_user_info(self):
        def next_step():
            name = name_entry.get()
            year = year_var.get()
            if not name or year == "Select Year":
                messagebox.showerror("Missing Info", "Please enter your name and select a year level.")
                return
            self.user_data["name"] = name
            self.user_data["year"] = year
            window.destroy()
            self.launch_pain_window()

        window = tk.Tk()
        window.title("Step 1: Student Info")
        window.geometry("420x520")
        window.config(bg=self.BG1)

        self.update_progress(window, 1, 4)

        tk.Label(window, text="Welcome to the Rehabilitation Assistant", font=self.FONT_HEADER,
                 bg=self.BG1, fg="white", relief="ridge", bd=3, padx=5, pady=5).pack(pady=5)
        tk.Label(window, text="Enter your name:", bg=self.BG1, font=self.FONT_BODY, fg="white").pack()
        name_entry = tk.Entry(window, bg=self.ENTRY_BG, fg=self.ENTRY_FG, relief="groove", bd=2)
        name_entry.pack(pady=5)

        tk.Label(window, text="Select your year level:", bg=self.BG1, font=self.FONT_BODY, fg="white").pack(pady=5)
        year_var = tk.StringVar()
        year_dropdown = ttk.Combobox(window, textvariable=year_var, values=[f"Yr{n}" for n in range(9, 14)], state="readonly")
        year_dropdown.set("Select Year")
        year_dropdown.pack()

        tk.Button(window, text="Next", command=next_step, bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)
        window.mainloop()

    # -------------------- STEP 2: Pain Level --------------------
    def launch_pain_window(self):
        def next_step():
            pain = pain_var.get()
            self.user_data["pain_level"] = pain
            window.destroy()
            self.launch_bodypart_window()

        window = tk.Tk()
        window.title("Step 2: Pain Level")
        window.geometry("420x520")
        window.config(bg=self.BG2)

        self.update_progress(window, 2, 4)

        tk.Label(window, text="Rate your pain (0–10):", font=self.FONT_BODY, bg=self.BG2, fg="white").pack(pady=10)
        pain_var = tk.IntVar(value=0)
        tk.Scale(window, from_=0, to=10, orient="horizontal", variable=pain_var,
                 bg=self.BG2, troughcolor="#d1c4b2", highlightbackground=self.BG2).pack(pady=5)
        tk.Button(window, text="Next", command=next_step, bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)
        window.mainloop()

    # -------------------- STEP 3: Body Area & Activity --------------------
    def launch_bodypart_window(self):
        def next_step():
            selected_areas = [area for area, var in body_areas.items() if var.get()]
            if not selected_areas:
                messagebox.showerror("Missing Info", "Please select at least one body area.")
                return
            activity = activity_var.get()
            if activity == "Select Activity":
                messagebox.showerror("Missing Info", "Please select your activity type.")
                return
            self.user_data["body_area"] = ", ".join(selected_areas)
            self.user_data["activity"] = activity
            window.destroy()
            self.launch_final_recommendations()

        window = tk.Tk()
        window.title("Step 3: Body Area & Activity")
        window.geometry("420x520")
        window.config(bg=self.BG3)

        self.update_progress(window, 3, 4)

        tk.Label(window, text="Which parts of your body hurt?", font=self.FONT_BODY, bg=self.BG3, fg="white").pack(pady=5)

        body_areas = {}
        for area in ["Knee", "Shoulder", "Back", "Wrist", "Ankle", "Thigh", "Neck", "Hand", "Hamstring"]:
            var = tk.BooleanVar()
            tk.Checkbutton(window, text=area, variable=var, bg=self.BG3, fg="white", selectcolor="#bba691").pack(anchor="w")
            body_areas[area] = var

        tk.Label(window, text="Select activity type:", font=self.FONT_BODY, bg=self.BG3, fg="white").pack(pady=10)
        activity_var = tk.StringVar()
        activity_dropdown = ttk.Combobox(window, textvariable=activity_var,
                                         values=["Sports Player", "Casual Exerciser", "Post-Injury Recovery"],
                                         state="readonly")
        activity_dropdown.set("Select Activity")
        activity_dropdown.pack()

        tk.Button(window, text="Next", command=next_step, bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=15)
        window.mainloop()

    # -------------------- STEP 4: Final Recommendations --------------------
    def launch_final_recommendations(self):
        name = self.user_data["name"]
        year = self.user_data["year"]
        pain = self.user_data["pain_level"]
        area = self.user_data["body_area"]
        activity = self.user_data["activity"]

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

        motivation = random.choice(self.MOTIVATIONAL_QUOTES)

motivation = random.choice(self.MOTIVATIONAL_QUOTES)

# -------------------- Save to Text File --------------------
with open("rehab_report.txt", "a") as file:
    file.write("----- Rehab Report -----\n")
    file.write(f"Name: {name}\n")
    file.write(f"Year Level: {year}\n")
    file.write(f"Pain Level: {pain} ({status})\n")
    file.write(f"Affected Area(s): {area}\n")
    file.write(f"Activity Type: {activity}\n")
    file.write(f"Recommended Exercises: {rec_exercise}\n")
    file.write(f"Diet Tips: {diet}\n")
    file.write(f"Recovery Advice: {tips}\n")
    file.write(f"Motivational Quote: {motivation}\n")
    file.write("------------------------\n\n")

window = tk.Tk()
window.title("Final Recommendations")
window.geometry("440x520")
window.config(bg=self.BG4)

self.update_progress(window, 4, 4)

tk.Label(window, text=f"🧾 Rehab Report for {name} ({year})", font=self.FONT_HEADER,
                 bg=self.BG4, fg="white", relief="ridge", bd=3, padx=5, pady=5).pack(pady=10)
tk.Label(window, text=f"Affected Area(s): {area}", font=self.FONT_BODY, bg=self.BG4, fg="white").pack()
tk.Label(window, text=f"Pain Level: {pain} ({status})", font=self.FONT_BODY, bg=self.BG4, fg=color).pack()
tk.Label(window, text=f"Activity: {activity}", font=self.FONT_BODY, bg=self.BG4, fg="white").pack(pady=5)

tk.Label(window, text="🏃‍♀️ Exercises:", font=self.FONT_BODY, bg=self.BG4, fg="white").pack()
tk.Label(window, text=rec_exercise, wraplength=380, bg=self.BG4, fg="white").pack()

tk.Label(window, text="🥗 Diet Tips:", font=self.FONT_BODY, bg=self.BG4, fg="white").pack(pady=5)
tk.Label(window, text=diet, wraplength=380, bg=self.BG4, fg="white").pack()

tk.Label(window, text="🛌 Recovery Advice:", font=self.FONT_BODY, bg=self.BG4, fg="white").pack(pady=5)
tk.Label(window, text=tips, wraplength=380, bg=self.BG4, fg="white").pack()

tk.Label(window, text=f"💡 Motivation: {motivation}", font=self.FONT_BODY,
                 bg=self.BG4, wraplength=380, fg="yellow").pack(pady=10)

tk.Button(window, text="Close", command=window.destroy,
                  bg=self.BUTTON_BG, fg=self.BUTTON_FG, relief="raised", bd=3).pack(pady=10)
window.mainloop()


# -------------------- Start the App --------------------
if __name__ == "__main__":
    RehabApp()
