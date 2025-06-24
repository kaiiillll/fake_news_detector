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