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