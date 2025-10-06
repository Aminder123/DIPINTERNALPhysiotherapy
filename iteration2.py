import tkinter as tk
from tkinter import ttk, messagebox

# This app uses Tkinter to create a multi-step GUI for student physiotherapy support.
# It collects user info, pain level, and affected body part, then gives tailored advice.

user_data = {}  # Stores all user inputs across windows

# Theme colors and fonts used across all windows for consistency
BG1 = "#4bc3eb"
BG2 = "#A0DD4C"
BG3 = "#f69f4d"
BG4 = "#f64f92"
FONT_HEADER = ("Helvetica", 14, "bold")
FONT_BODY = ("Helvetica", 11)

# ---------------- Window 1: Name & Student Year ----------------
def launch_user_info():
    # First window: collects user's name and school year level

    def next_step():
        name = name_entry.get()
        year = year_var.get()
        
        if not name or year == "Select Year":
            messagebox.showerror("Missing Info", "Please enter your name and select a year level.")
            return
        user_data["name"] = name
        user_data["year"] = year
        window.destroy()
        launch_pain_window()

    # GUI setup for name and year input
    window = tk.Tk()
    window.title("Step 1: Student Info")
    window.geometry("350x200")
    window.config(bg=BG1)

    # Labels and input fields for name and year
    tk.Label(window, text="Welcome to Rehabilitation Assistant", font=FONT_HEADER, bg=BG1, fg="black").pack(pady=5)
    tk.Label(window, text="Enter your name:", bg=BG1, fg="black", font=FONT_BODY).pack()
    name_entry = tk.Entry(window, fg="white")
    name_entry.pack()

    # Dropdown for year level selection
    tk.Label(window, text="Select your year level:", bg=BG1, fg="black", font=FONT_BODY).pack(pady=5)
    year_var = tk.StringVar()
    year_dropdown = ttk.Combobox(window, textvariable=year_var, values=[f"Yr{n}" for n in range(9, 14)], state="readonly")
    year_dropdown.set("Select Year")
    year_dropdown.pack()

    # Button to proceed to next step
    tk.Button(window, text="Next", command=next_step, fg="black").pack(pady=10)
    window.mainloop()

# ---------------- Window 2: Pain Level Entry ----------------
def launch_pain_window():
    # Second window: asks user to rate their pain level from 0 to 10

    def next_step():
        try:
            pain = int(pain_entry.get())
            if 0 <= pain <= 10:
                user_data["pain_level"] = pain
                window.destroy()
                launch_bodypart_window()
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid", "Pain level must be a number from 0–10.")

    # GUI setup for pain level input
    window = tk.Tk()
    window.title("Step 2: Pain Level")
    window.geometry("350x150")
    window.config(bg=BG2)

    # Label and entry field for pain level
    tk.Label(window, text="On a scale from (0–10) rate how painful your body is feeling right now:", font=FONT_BODY, bg=BG2, fg="black").pack(pady=10)
    pain_entry = tk.Entry(window, fg="white")
    pain_entry.pack()

    # Button to proceed to next step
    tk.Button(window, text="Next", command=next_step, fg="black").pack(pady=10)
    window.mainloop()

# ---------------- Window 3: Body Area Selection ----------------
def launch_bodypart_window():
    # Third window: asks which part of the body is affected

    def next_step():
        area = area_var.get()
        if not area or area == "Select Area":
            messagebox.showerror("Missing Info", "Please select the body part which is causing the pain.")
            return
        user_data["body_area"] = area
        window.destroy()
        launch_final_recommendations()

    # GUI setup for body area selection
    window = tk.Tk()
    window.title("Step 3: Affected Area")
    window.geometry("350x160")
    window.config(bg=BG3)

    # Label and dropdown for body part selection
    tk.Label(window, text="Which part of your body hurts?", font=FONT_BODY, bg=BG3, fg="black").pack(pady=10)
    area_var = tk.StringVar()
    area_dropdown = ttk.Combobox(window, textvariable=area_var,
                                  values=["Knee", "Shoulder", "Back", "Wrist", "Ankle", "Thigh", "Head", "Neck", "Hand", "Hamstring", "Face", "Chest"],
                                  state="readonly")
    area_dropdown.set("Select Area")
    area_dropdown.pack()

    # Button to proceed to final recommendations
    tk.Button(window, text="Next", command=next_step, fg="black").pack(pady=10)
    window.mainloop()

# ---------------- Final Recommendation Window ----------------
def launch_final_recommendations():
    # Final window: shows tailored advice based on pain level and body part

    name = user_data["name"]
    year = user_data["year"]
    pain = user_data["pain_level"]
    area = user_data["body_area"]

    # Logic to generate advice based on pain severity
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

    # GUI setup to display final recommendations
    window = tk.Tk()
    window.title("Final Recommendations")
    window.geometry("420x350")
    window.config(bg=BG4)

    # Display user summary and advice
    tk.Label(window, text=f"🧾 Rehab Report for {name} ({year})", font=FONT_HEADER, bg=BG4, fg="black").pack(pady=10)
    tk.Label(window, text=f"Pain Level: {pain} ({status})", font=FONT_BODY, bg=BG4, fg="black").pack()
    tk.Label(window, text=f"Affected Area: {area}", font=FONT_BODY, bg=BG4, fg="black").pack(pady=5)

    # Display exercise, diet, and recovery tips
    tk.Label(window, text="🏃‍♀️ Recommended Exercises:", font=FONT_BODY, bg=BG4, fg="black").pack()
    tk.Label(window, text=rec_exercise, wraplength=380, bg=BG4, fg="black").pack()

    tk.Label(window, text="🥗 Diet Tips:", font=FONT_BODY, bg=BG4, fg="black").pack(pady=5)
    tk.Label(window, text=diet, wraplength=380, bg=BG4, fg="black").pack()

    tk.Label(window, text="🛌 Recovery Advice:", font=FONT_BODY, bg=BG4, fg="black").pack(pady=5)
    tk.Label(window, text=tips, wraplength=380, bg=BG4, fg="black").pack()

    # Button to close the app
    tk.Button(window, text="Close", command=window.destroy, fg="black").pack(pady=15)
    window.mainloop()

# ---------------- Program Entry Point ----------------
if __name__ == "__main__":
    launch_user_info()  # Starts the app from the first window
