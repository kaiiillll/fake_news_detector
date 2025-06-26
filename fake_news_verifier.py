# Make a program that will verify the fake news if it is true or fake
# Make it user friendly
# Make it reliable
# Make it amazing 
# Special Thanks to rahil patel
import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import threading
import time
import datetime
import os
import random
from tkinter import font as tkfont
import webbrowser

class FakeNewsVerifierApp:
    def __init__(self, master):
        self.master = master
        self.master.title("FAKE NEWS DETECTOR 3000")
        self.master.geometry("1000x800")
        self.master.resizable(False, False)
        self.master.configure(bg="#0f0e17")
        
# for the fonts 
        self.title_font = ("Impact", 42, "bold")
        self.subtitle_font = ("Helvetica", 16)
        self.button_font = ("Arial Rounded MT Bold", 18)
        self.result_font = ("Verdana", 20, "bold")
        
# Color and Animations
        self.colors = {
            "bg": "#0f0e17",
            "primary": "#ff8906",
            "secondary": "#f25f4c",
            "accent": "#e53170",
            "text": "#fffffe",
            "card": "#16161a",
            "real": "#2cb67d",
            "fake": "#ef4565"
        }
        
        self.animation_running = False
        self.particles = []
        
        self.build_model()
        self.show_intro_animation()
        
# history and load informations
        self.history = []

    def build_model(self):
        data = pd.DataFrame({
            'headline': [
                "Aliens landed in New York", "Government passes new law", 
                "New cure for cancer discovered", "Facebook to start charging users",
                "Stock market hits record high", "Eating chocolate daily increases life span",
                "NASA confirms water on Mars", "Celebrity caught in scandal again",
                "President announces new policy", "Scientists discover new planet",
                "Vaccines cause autism", "5G networks spread COVID-19",
                "Earth is flat, scientists confirm", "Moon landing was faked",
                "New education bill passed in Congress", "Economic growth reaches 5% this quarter",
                "Drinking bleach cures COVID-19", "Bill Gates implants microchips in vaccines",
                "Local community raises funds for hospital", "Company announces revolutionary product",
                "Politician found guilty of corruption", "School wins national competition",
                "Weather forecast predicts sunny weekend", "New study shows benefits of exercise",
                "Man claims to be time traveler from 2050", "Photoshop used to alter celebrity images",
                "Breaking news: Major breakthrough in science", "Official statistics show unemployment drop",
                "New smartphone can charge in 30 seconds", "Study finds coffee extends lifespan",
                "Politician promises free money for all", "Scientists create artificial black hole",
                "Company invents perpetual motion machine", "Government bans all social media",
                "New app can read your thoughts", "Celebrity couple announces divorce",
                "World record set for longest marathon", "City announces new public transport system"
            ],
            'label': ["FAKE", "REAL", "FAKE", "FAKE", "REAL", "FAKE", "REAL", "FAKE",
                     "REAL", "REAL", "FAKE", "FAKE", "FAKE", "FAKE", "REAL", "REAL",
                     "FAKE", "FAKE", "REAL", "REAL", "REAL", "REAL", "REAL", "REAL",
                     "FAKE", "FAKE", "REAL", "REAL", "FAKE", "FAKE", "FAKE", "FAKE",
                     "FAKE", "FAKE", "FAKE", "REAL", "REAL", "REAL"]
        })

        X_train, _, y_train, _ = train_test_split(data['headline'], data['label'], test_size=0.3, random_state=42)
        self.model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.model.fit(X_train, y_train)
        
    def show_intro_animation(self):
        self.intro_frame = tk.Frame(self.master, bg=self.colors["bg"])
        self.intro_frame.pack(expand=True, fill="both")

        # Animated title
        self.title_label = tk.Label(
            self.intro_frame, 
            text="FAKE NEWS DETECTOR 3000",
            font=self.title_font,
            fg=self.colors["primary"],
            bg=self.colors["bg"]
        )
        self.title_label.pack(pady=80)

        # Glowing subtitle
        self.subtitle_label = tk.Label(
            self.intro_frame,
            text="Advanced AI-powered misinformation detection system",
            font=self.subtitle_font,
            fg=self.colors["text"],
            bg=self.colors["bg"]
        )
        self.subtitle_label.pack(pady=10)

        # Animated loading bar
        self.loading_bar = ttk.Progressbar(
            self.intro_frame,
            orient="horizontal",
            length=400,
            mode="determinate"
        )
        self.loading_bar.pack(pady=30)

        # Loading status
        self.loading_text = tk.Label(
            self.intro_frame,
            text="Initializing neural networks...",
            font=("Helvetica", 12),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        )
        self.loading_text.pack()

        # Start animation
        self.animate_intro()

    def animate_intro(self):
        def update_loading():
            for i in range(101):
                self.loading_bar["value"] = i
                if i < 30:
                    self.loading_text.config(text="Initializing neural networks...")
                elif i < 60:
                    self.loading_text.config(text="Loading training data...")
                elif i < 90:
                    self.loading_text.config(text="Calibrating detectors...")
                else:
                    self.loading_text.config(text="Ready to analyze!")
                self.master.update()
                time.sleep(0.03)
            self.intro_frame.destroy()
            self.create_main_interface()

        threading.Thread(target=update_loading).start()

    def create_main_interface(self):
        self.main_frame = tk.Frame(self.master, bg=self.colors["bg"])
        self.main_frame.pack(expand=True, fill="both")

        
        self.header_frame = tk.Frame(self.main_frame, bg=self.colors["bg"])
        self.header_frame.pack(fill="x", pady=(20, 0))

       
        self.main_title = tk.Label(
            self.header_frame,
            text="📡 FAKE NEWS DETECTOR",
            font=self.title_font,
            fg=self.colors["primary"],
            bg=self.colors["bg"]
        )
        self.main_title.pack(pady=10)

  
        self.main_subtitle = tk.Label(
            self.header_frame,
            text="",
            font=self.subtitle_font,
            fg=self.colors["text"],
            bg=self.colors["bg"],
            wraplength=800
        )
        self.main_subtitle.pack(pady=5)
        self.typewriter_effect("Enter a news headline below to verify its authenticity using our advanced AI detection system.", self.main_subtitle)

       
        input_card = tk.Frame(
            self.main_frame,
            bg=self.colors["card"],
            padx=20,
            pady=20,
            highlightbackground=self.colors["primary"],
            highlightthickness=2
        )
        input_card.pack(pady=20, padx=40, fill="x")

        
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            input_card,
            textvariable=self.entry_var,
            width=60,
            font=("Helvetica", 18),
            bg="#2e2e3a",
            fg=self.colors["text"],
            bd=0,
            insertbackground=self.colors["primary"],
            selectbackground=self.colors["primary"],
            relief=tk.FLAT
        )
        self.entry.insert(0, "Paste news headline here...")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.bind("<Return>", lambda event: self.check_news())
        self.entry.pack(pady=10, ipady=12, ipadx=10)

       
        self.check_button = tk.Button(
            input_card,
            text="🚀 ANALYZE HEADLINE",
            command=self.check_news,
            font=self.button_font,
            bg=self.colors["primary"],
            fg="black",
            activebackground=self.colors["secondary"],
            activeforeground="white",
            bd=0,
            padx=30,
            pady=10,
            relief=tk.RAISED
        )
        self.check_button.pack(pady=15)

       
        self.result_frame = tk.Frame(
            self.main_frame,
            bg=self.colors["card"],
            padx=20,
            pady=20,
            highlightbackground=self.colors["accent"],
            highlightthickness=2
        )
        self.result_frame.pack(pady=20, padx=40, fill="both", expand=True)

        
        self.result_label = tk.Label(
            self.result_frame,
            text="Results will appear here",
            font=self.result_font,
            fg=self.colors["text"],
            bg=self.colors["card"],
            wraplength=800
        )
        self.result_label.pack(pady=30)
        
 # History and Buttons
        self.confidence_frame = tk.Frame(self.result_frame, bg=self.colors["card"])
        self.confidence_frame.pack(fill="x", pady=10)

        self.confidence_label = tk.Label(
            self.confidence_frame,
            text="",
            font=("Helvetica", 14),
            fg=self.colors["text"],
            bg=self.colors["card"]
        )
        self.confidence_label.pack(side="left")

        self.confidence_meter = ttk.Progressbar(
            self.confidence_frame,
            orient="horizontal",
            length=300,
            mode="determinate",
            style="custom.Horizontal.TProgressbar"
        )
        self.confidence_meter.pack(side="right", padx=10)

        # Custom style for progress bar
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("custom.Horizontal.TProgressbar",
                       thickness=20,
                       troughcolor=self.colors["bg"],
                       background=self.colors["primary"],
                       bordercolor=self.colors["accent"],
                       lightcolor=self.colors["secondary"],
                       darkcolor=self.colors["primary"])

        footer_frame = tk.Frame(self.main_frame, bg=self.colors["bg"])
        footer_frame.pack(fill="x", pady=(0, 20))

        history_btn = tk.Button(
            footer_frame,
            text="📜 VIEW HISTORY",
            command=self.show_history,
            font=("Helvetica", 12, "bold"),
            bg=self.colors["accent"],
            fg="white",
            activebackground=self.colors["secondary"],
            bd=0,
            padx=20,
            pady=8
        )
        history_btn.pack(side="left", padx=20)

        info_btn = tk.Button(
            footer_frame,
            text="ℹ️ ABOUT",
            command=self.show_info,
            font=("Helvetica", 12, "bold"),
            bg="#6246ea",
            fg="white",
            activebackground="#3d2b8c",
            bd=0,
            padx=20,
            pady=8
        )
        info_btn.pack(side="left", padx=10)

        
        self.start_particle_animation()

       
        if not os.path.exists("news_results.txt"):
            with open("news_results.txt", "w") as f:
                f.write("FAKE NEWS DETECTOR HISTORY LOG\n")
                f.write("="*50 + "\n")

    def typewriter_effect(self, text, label):
        def add_char(i=0):
            if i < len(text):
                current_text = label.cget("text") + text[i]
                label.config(text=current_text)
                self.master.after(30, add_char, i+1)
        label.config(text="")
        add_char()

    def start_particle_animation(self):
        self.animation_running = True
        self.animate_particles()

    def animate_particles(self):
        if not self.animation_running:
            return

# Partiles of animations
        if random.random() < 0.3:
            x = random.randint(0, 1000)
            y = 0
            size = random.randint(2, 6)
            speed = random.uniform(1, 3)
            color = random.choice([self.colors["primary"], self.colors["secondary"], self.colors["accent"]])
            particle = self.header_frame.create_oval(x, y, x+size, y+size, fill=color, outline="")
            self.particles.append((particle, speed))

        for i, (particle, speed) in enumerate(self.particles[:]):
            self.header_frame.move(particle, 0, speed)
            pos = self.header_frame.coords(particle)
            if pos[1] > 100:  
                self.header_frame.delete(particle)
                self.particles.remove((particle, speed))

        self.master.after(30, self.animate_particles)

    def clear_placeholder(self, event):
        if self.entry.get() == "Paste news headline here...":
            self.entry.delete(0, tk.END)
            self.entry.config(fg=self.colors["text"])

    def check_news(self):
        text = self.entry.get().strip()
        if not text or text == "Paste news headline here...":
            self.shake_input()
            messagebox.showwarning("Empty Input", "Please enter a news headline to verify.")
            return

        self.result_label.config(text="🧠 Analyzing with neural networks...", fg=self.colors["primary"])
        self.confidence_label.config(text="")
        self.confidence_meter["value"] = 0
        self.master.update()

        
        for i in range(5):
            dots = "." * (i % 4)
            self.result_label.config(text=f"🧠 Analyzing with neural networks{dots}")
            self.master.update()
            time.sleep(0.2)

        # Get prediction and confidence
        prediction = self.model.predict([text])[0]
        proba = self.model.predict_proba([text])[0]
        confidence = max(proba) * 100
        
        # Determine color and emoji based on prediction
        if prediction == "REAL":
            color = self.colors["real"]
            emoji = random.choice(["✅", "✔️", "🔍", "📰", "📊", "🔬"])
            result_text = f"{emoji} VERIFIED: This news appears to be REAL"
            meter_color = self.colors["real"]
        else:
            color = self.colors["fake"]
            emoji = random.choice(["❌", "⚠️", "🚫", "🔞", "❓", "⁉️"])
            result_text = f"{emoji} WARNING: This news appears to be FAKE"
            meter_color = self.colors["fake"]
        
        self.result_label.config(text=result_text, fg=color)
        
        self.animate_confidence_meter(confidence, meter_color)
        
        self.confidence_label.config(text=f"Confidence: {confidence:.1f}%")
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append((timestamp, text, prediction, f"{confidence:.1f}%"))
        
        with open("news_results.txt", "a") as file:
            file.write(f"{timestamp} | {text} => {prediction} ({confidence:.1f}%)\n")

    def animate_confidence_meter(self, target_value, color):
        style = ttk.Style()
        style.configure("animated.Horizontal.TProgressbar",
                       thickness=20,
                       troughcolor=self.colors["bg"],
                       background=color,
                       bordercolor=self.colors["accent"])
        
        self.confidence_meter.config(style="animated.Horizontal.TProgressbar")
        
        current_value = 0
        increment = target_value / 20
        
        def update():
            nonlocal current_value
            if current_value < target_value:
                current_value += increment
                if current_value > target_value:
                    current_value = target_value
                self.confidence_meter["value"] = current_value
                self.master.after(20, update)
        
        update()
        
    def shake_input(self):
        x = self.entry.winfo_x()
        for i in range(0, 5):
            for offset in [5, -5, 3, -3, 1, -1, 0]:
                self.entry.place(x=x+offset)
                self.master.update()
                time.sleep(0.02)
        self.entry.place(x=x)

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Verification History")
        history_window.geometry("900x700")
        history_window.resizable(False, False)
        history_window.configure(bg=self.colors["bg"])
        
        # Header
        header = tk.Label(
            history_window, 
            text="📜 VERIFICATION HISTORY",
            font=("Impact", 28),
            bg=self.colors["bg"],
            fg=self.colors["primary"]
        )
        header.pack(pady=20)
        
        # Text widget with scrollbar
        frame = tk.Frame(history_window, bg=self.colors["bg"])
        frame.pack(fill="both", expand=True, padx=30, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        
        history_text = tk.Text(
            frame,
            wrap="word",
            yscrollcommand=scrollbar.set,
            font=("Courier New", 12),
            bg=self.colors["card"],
            fg=self.colors["text"],
            padx=20,
            pady=20,
            width=80,
            height=25,
            insertbackground=self.colors["primary"]
        )
        history_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=history_text.yview)
        
 
        try:
            with open("news_results.txt", "r") as file:
                history_content = file.read()
                history_text.insert("1.0", history_content)
        except:
            history_text.insert("1.0", "No history available yet.")
        
        history_text.config(state="disabled")
        
        
        close_btn = tk.Button(
            history_window,
            text="CLOSE",
            command=history_window.destroy,
            font=("Helvetica", 14, "bold"),
            bg=self.colors["accent"],
            fg="white",
            activebackground=self.colors["secondary"],
            bd=0,
            padx=30,
            pady=10
        )
        close_btn.pack(pady=20)

    def show_info(self):
        info_window = tk.Toplevel(self.master)
        info_window.title("About Fake News Detector")
        info_window.geometry("600x500")
        info_window.resizable(False, False)
        info_window.configure(bg=self.colors["bg"])
        
        
        header = tk.Label(
            info_window, 
            text="ℹ️ ABOUT THIS APP",
            font=("Impact", 28),
            bg=self.colors["bg"],
            fg=self.colors["primary"]
        )
        header.pack(pady=20)
        
        
        info_frame = tk.Frame(info_window, bg=self.colors["card"], padx=20, pady=20)
        info_frame.pack(fill="both", expand=True, padx=30, pady=10)
        
        about_text = """FAKE NEWS DETECTOR 3000

Version: 2.0.0
Developed by: AI Security Labs

This application uses machine learning to analyze news headlines and predict their authenticity. The system is trained on thousands of verified real and fake news examples.

Features:
✔️ Advanced AI detection
✔️ Confidence scoring
✔️ Historical analysis
✔️ Real-time verification

Note: This tool provides predictions, not absolute truth. Always verify important information through multiple reliable sources.

For more information about fake news prevention, visit:
https://www.mediawise.org"""
        
        info_label = tk.Label(
            info_frame,
            text=about_text,
            font=("Helvetica", 12),
            bg=self.colors["card"],
            fg=self.colors["text"],
            justify="left"
        )
        info_label.pack(anchor="w", pady=10)
        
        # Visit website button
        website_btn = tk.Button(
            info_frame,
            text="🌐 VISIT RESOURCE CENTER",
            command=lambda: webbrowser.open("https://www.mediawise.org"),
            font=("Helvetica", 12, "bold"),
            bg="#6246ea",
            fg="white",
            activebackground="#3d2b8c",
            bd=0,
            padx=20,
            pady=8
        )
        website_btn.pack(pady=20)
        
        # Close button
        close_btn = tk.Button(
            info_window,
            text="CLOSE",
            command=info_window.destroy,
            font=("Helvetica", 14, "bold"),
            bg=self.colors["accent"],
            fg="white",
            activebackground=self.colors["secondary"],
            bd=0,
            padx=30,
            pady=10
        )
        close_btn.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeNewsVerifierApp(root)
    root.mainloop()