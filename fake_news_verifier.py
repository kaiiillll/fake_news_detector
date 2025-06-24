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