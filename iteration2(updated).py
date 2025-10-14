import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- Main Rehabilitation Assistant App --------------------
class RehabApp:
    def __init__(self):
        self.user_data = {}

        # Shared styles
        self.BG1 = "#4bc3eb"
        self.BG2 = "#A0DD4C"
        self.BG3 = "#f69f4d"
        self.BG4 = "#f64f92"
        self.FONT_HEADER = ("Helvetica", 14, "bold")
        self.FONT_BODY = ("Helvetica", 11)

        # Start the first window
        self.launch_user_info()

    # Launches each class-based window
    def launch_user_info(self):
        UserInfoWindow(self)

    def launch_pain_window(self):
        PainLevelWindow(self)

    def launch_bodypart_window(self):
        BodyPartWindow(self)

    def launch_final_recommendations(self):
        FinalRecommendationWindow(self)


# -------------------- Class 1: User Info Window --------------------
class UserInfoWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Tk()
        self.window.title("Step 1: Student Info")
        self.window.geometry("350x200")
        self.window.config(bg=self.app.BG1)

        tk.Label(self.window, text="Welcome to Rehabilitation Assistant", font=self.app.FONT_HEADER, bg=self.app.BG1, fg="black").pack(pady=5)
        tk.Label(self.window, text="Enter your name:", bg=self.app.BG1, fg="black", font=self.app.FONT_BODY).pack()
        self.name_entry = tk.Entry(self.window, fg="white")
        self.name_entry.pack()

        tk.Label(self.window, text="Select your year level:", bg=self.app.BG1, fg="black", font=self.app.FONT_BODY).pack(pady=5)
        self.year_var = tk.StringVar()
        year_dropdown = ttk.Combobox(self.window, textvariable=self.year_var, values=[f"Yr{n}" for n in range(9, 14)], state="readonly")
        year_dropdown.set("Select Year")
        year_dropdown.pack()

        tk.Button(self.window, text="Next", command=self.next_step, fg="black").pack(pady=10)
        self.window.mainloop()

    def next_step(self):
        name = self.name_entry.get()
        year = self.year_var.get()

        if not name or year == "Select Year":
            messagebox.showerror("Missing Info", "Please enter your name and select a year level.")
            return

        self.app.user_data["name"] = name
        self.app.user_data["year"] = year
        self.window.destroy()
        self.app.launch_pain_window()


# -------------------- Class 2: Pain Level Window --------------------
class PainLevelWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Tk()
        self.window.title("Step 2: Pain Level")
        self.window.geometry("350x150")
        self.window.config(bg=self.app.BG2)

        tk.Label(self.window, text="On a scale from (0–10) rate how painful your body is feeling right now:",
                 font=self.app.FONT_BODY, bg=self.app.BG2, fg="black").pack(pady=10)
        self.pain_entry = tk.Entry(self.window, fg="white")
        self.pain_entry.pack()

        tk.Button(self.window, text="Next", command=self.next_step, fg="black").pack(pady=10)
        self.window.mainloop()

    def next_step(self):
        try:
            pain = int(self.pain_entry.get())
            if 0 <= pain <= 10:
                self.app.user_data["pain_level"] = pain
                self.window.destroy()
                self.app.launch_bodypart_window()
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid", "Pain level must be a number from 0–10.")


# -------------------- Class 3: Body Part Window --------------------
class BodyPartWindow:
    def __init__(self, app):
        self.app = app
        self.window = tk.Tk()
        self.window.title("Step 3: Affected Area")
        self.window.geometry("350x160")
        self.window.config(bg=self.app.BG3)

        tk.Label(self.window, text="Which part of your body hurts?", font=self.app.FONT_BODY, bg=self.app.BG3, fg="black").pack(pady=10)
        self.area_var = tk.StringVar()
        area_dropdown = ttk.Combobox(
            self.window,
            textvariable=self.area_var,
            values=["Knee", "Shoulder", "Back", "Wrist", "Ankle", "Thigh", "Head", "Neck", "Hand", "Hamstring", "Face", "Chest"],
            state="readonly"
        )
        area_dropdown.set("Select Area")
        area_dropdown.pack()

        tk.Button(self.window, text="Next", command=self.next_step, fg="black").pack(pady=10)
        self.window.mainloop()

    def next_step(self):
        area = self.area_var.get()
        if not area or area == "Select Area":
            messagebox.showerror("Missing Info", "Please select the body part which is causing the pain.")
            return

        self.app.user_data["body_area"] = area
        self.window.destroy()
        self.app.launch_final_recommendations()


# -------------------- Class 4: Final Recommendation Window --------------------
class FinalRecommendationWindow:
    def __init__(self, app):
        self.app = app
        user = self.app.user_data

        name = user["name"]
        year = user["year"]
        pain = user["pain_level"]
        area = user["body_area"]

        if pain <= 3:
            status = "Minor"
            rec_exercise = f"Gentle stretches and walking; light yoga targeting the {area.lower()}"
            diet = "Hydration, anti-inflammatory snacks, light protein"
            tips = "Stay lightly active, monitor any discomfort, sleep well"
        elif pain <= 7:
            status = "Moderate"
            rec_exercise = f"Controlled physio for {area.lower()}, resistance band work"
            diet = "Add omega-3s, reduce sugar and sodium, eat leafy greens"
            tips = "Rest between exercises, track improvement, apply heat or ice"
        else:
            status = "Severe"
            rec_exercise = f"Limit movement of {area.lower()}, use support gear if needed"
            diet = "Turmeric, berries, green vegetables, herbal teas"
            tips = "Prioritize pain management, breathing routines, full rest"

        self.window = tk.Tk()
        self.window.title("Final Recommendations")
        self.window.geometry("420x350")
        self.window.config(bg=self.app.BG4)

        tk.Label(self.window, text=f"🧾 Rehab Report for {name} ({year})", font=self.app.FONT_HEADER, bg=self.app.BG4, fg="black").pack(pady=10)
        tk.Label(self.window, text=f"Pain Level: {pain} ({status})", font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack()
        tk.Label(self.window, text=f"Affected Area: {area}", font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack(pady=5)

        tk.Label(self.window, text="🏃‍♀️ Recommended Exercises:", font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack()
        tk.Label(self.window, text=rec_exercise, wraplength=380, bg=self.app.BG4, fg="black").pack()

        tk.Label(self.window, text="🥗 Diet Tips:", font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack(pady=5)
        tk.Label(self.window, text=diet, wraplength=380, bg=self.app.BG4, fg="black").pack()

        tk.Label(self.window, text="🛌 Recovery Advice:", font=self.app.FONT_BODY, bg=self.app.BG4, fg="black").pack(pady=5)
        tk.Label(self.window, text=tips, wraplength=380, bg=self.app.BG4, fg="black").pack()

        tk.Button(self.window, text="Close", command=self.window.destroy, fg="black").pack(pady=15)
        self.window.mainloop()


# -------------------- Program Entry Point --------------------
if __name__ == "__main__":
    RehabApp()

