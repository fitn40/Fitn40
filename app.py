import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Branding
st.set_page_config(page_title="Fit N 40 Match Prediction", page_icon="⚽", layout="centered")

DATA_FILE = "data.csv"
current_date = datetime.now()
current_year = current_date.year

# Complete 72 Matches Matrix Data
@st.cache_data
def get_match_data(year):
    raw_data = [
        {"Match_Num": 1, "Date_Str": "Jun 11", "Home_Team": "Mexico", "Away_Team": "South Africa", "Home_Win_Odds": 1.55, "Draw_Odds": 3.8, "Away_Win_Odds": 5.5, "Actual_Result": "Pending"},
        {"Match_Num": 2, "Date_Str": "Jun 11", "Home_Team": "Korea Republic", "Away_Team": "Czechia", "Home_Win_Odds": 2.1, "Draw_Odds": 3.2, "Away_Win_Odds": 3.5, "Actual_Result": "Pending"},
        {"Match_Num": 3, "Date_Str": "Jun 12", "Home_Team": "Canada", "Away_Team": "Bosnia & Herz.", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8, "Actual_Result": "Pending"},
        {"Match_Num": 4, "Date_Str": "Jun 13", "Home_Team": "Qatar", "Away_Team": "Switzerland", "Home_Win_Odds": 3.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1, "Actual_Result": "Pending"},
        {"Match_Num": 5, "Date_Str": "Jun 13", "Home_Team": "Brazil", "Away_Team": "Morocco", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5, "Actual_Result": "Pending"},
        {"Match_Num": 6, "Date_Str": "Jun 13", "Home_Team": "Haiti", "Away_Team": "Scotland", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.75, "Actual_Result": "Pending"},
        {"Match_Num": 7, "Date_Str": "Jun 12", "Home_Team": "USA", "Away_Team": "Paraguay", "Home_Win_Odds": 1.8, "Draw_Odds": 3.5, "Away_Win_Odds": 4.5, "Actual_Result": "Pending"},
        {"Match_Num": 8, "Date_Str": "Jun 13", "Home_Team": "Australia", "Away_Team": "Türkiye", "Home_Win_Odds": 2.8, "Draw_Odds": 3.2, "Away_Win_Odds": 2.6, "Actual_Result": "Pending"},
        {"Match_Num": 9, "Date_Str": "Jun 14", "Home_Team": "Germany", "Away_Team": "Curaçao", "Home_Win_Odds": 1.12, "Draw_Odds": 8.0, "Away_Win_Odds": 22.0, "Actual_Result": "Pending"},
        {"Match_Num": 10, "Date_Str": "Jun 14", "Home_Team": "Côte d'Ivoire", "Away_Team": "Ecuador", "Home_Win_Odds": 2.2, "Draw_Odds": 3.3, "Away_Win_Odds": 3.3, "Actual_Result": "Pending"},
        {"Match_Num": 11, "Date_Str": "Jun 14", "Home_Team": "Netherlands", "Away_Team": "Japan", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5, "Actual_Result": "Pending"},
        {"Match_Num": 12, "Date_Str": "Jun 14", "Home_Team": "Sweden", "Away_Team": "Tunisia", "Home_Win_Odds": 1.7, "Draw_Odds": 3.5, "Away_Win_Odds": 5.0, "Actual_Result": "Pending"},
        {"Match_Num": 13, "Date_Str": "Jun 15", "Home_Team": "Belgium", "Away_Team": "Egypt", "Home_Win_Odds": 1.6, "Draw_Odds": 3.7, "Away_Win_Odds": 5.8, "Actual_Result": "Pending"},
        {"Match_Num": 14, "Date_Str": "Jun 15", "Home_Team": "IR Iran", "Away_Team": "New Zealand", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2, "Actual_Result": "Pending"},
        {"Match_Num": 15, "Date_Str": "Jun 15", "Home_Team": "Spain", "Away_Team": "Cabo Verde", "Home_Win_Odds": 1.18, "Draw_Odds": 7.0, "Away_Win_Odds": 16.0, "Actual_Result": "Pending"},
        {"Match_Num": 16, "Date_Str": "Jun 15", "Home_Team": "Saudi Arabia", "Away_Team": "Uruguay", "Home_Win_Odds": 3.2, "Draw_Odds": 3.2, "Away_Win_Odds": 2.3, "Actual_Result": "Pending"},
        {"Match_Num": 17, "Date_Str": "Jun 16", "Home_Team": "France", "Away_Team": "Senegal", "Home_Win_Odds": 1.5, "Draw_Odds": 4.0, "Away_Win_Odds": 7.0, "Actual_Result": "Pending"},
        {"Match_Num": 18, "Date_Str": "Jun 16", "Home_Team": "Iraq", "Away_Team": "Norway", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.8, "Actual_Result": "Pending"},
        {"Match_Num": 19, "Date_Str": "Jun 16", "Home_Team": "Argentina", "Away_Team": "Algeria", "Home_Win_Odds": 1.3, "Draw_Odds": 5.0, "Away_Win_Odds": 10.0, "Actual_Result": "Pending"},
        {"Match_Num": 20, "Date_Str": "Jun 16", "Home_Team": "Austria", "Away_Team": "Jordan", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5, "Actual_Result": "Pending"},
        {"Match_Num": 21, "Date_Str": "Jun 17", "Home_Team": "Portugal", "Away_Team": "Congo DR", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0, "Actual_Result": "Pending"},
        {"Match_Num": 22, "Date_Str": "Jun 17", "Home_Team": "Uzbekistan", "Away_Team": "Colombia", "Home_Win_Odds": 3.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1, "Actual_Result": "Pending"},
        {"Match_Num": 23, "Date_Str": "Jun 17", "Home_Team": "England", "Away_Team": "Croatia", "Home_Win_Odds": 1.6, "Draw_Odds": 3.8, "Away_Win_Odds": 5.8, "Actual_Result": "Pending"},
        {"Match_Num": 24, "Date_Str": "Jun 17", "Home_Team": "Ghana", "Away_Team": "Panama", "Home_Win_Odds": 1.95, "Draw_Odds": 3.3, "Away_Win_Odds": 4.0, "Actual_Result": "Pending"},
        {"Match_Num": 25, "Date_Str": "Jun 18", "Home_Team": "Czechia", "Away_Team": "South Africa", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2, "Actual_Result": "Pending"},
        {"Match_Num": 26, "Date_Str": "Jun 18", "Home_Team": "Mexico", "Away_Team": "Korea Republic", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.5, "Actual_Result": "Pending"},
        {"Match_Num": 27, "Date_Str": "Jun 18", "Home_Team": "Switzerland", "Away_Team": "Bosnia & Herz.", "Home_Win_Odds": 1.75, "Draw_Odds": 3.5, "Away_Win_Odds": 4.8, "Actual_Result": "Pending"},
        {"Match_Num": 28, "Date_Str": "Jun 18", "Home_Team": "Canada", "Away_Team": "Qatar", "Home_Win_Odds": 1.55, "Draw_Odds": 3.7, "Away_Win_Odds": 6.0, "Actual_Result": "Pending"},
        {"Match_Num": 29, "Date_Str": "Jun 19", "Home_Team": "Brazil", "Away_Team": "Haiti", "Home_Win_Odds": 1.2, "Draw_Odds": 6.5, "Away_Win_Odds": 16.0, "Actual_Result": "Pending"},
        {"Match_Num": 30, "Date_Str": "Jun 19", "Home_Team": "Scotland", "Away_Team": "Morocco", "Home_Win_Odds": 3.6, "Draw_Odds": 3.3, "Away_Win_Odds": 2.1, "Actual_Result": "Pending"},
        {"Match_Num": 31, "Date_Str": "Jun 19", "Home_Team": "USA", "Away_Team": "Australia", "Home_Win_Odds": 1.7, "Draw_Odds": 3.6, "Away_Win_Odds": 5.0, "Actual_Result": "Pending"},
        {"Match_Num": 32, "Date_Str": "Jun 19", "Home_Team": "Türkiye", "Away_Team": "Paraguay", "Home_Win_Odds": 2.2, "Draw_Odds": 3.3, "Away_Win_Odds": 3.3, "Actual_Result": "Pending"},
        {"Match_Num": 33, "Date_Str": "Jun 20", "Home_Team": "Germany", "Away_Team": "Côte d'Ivoire", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5, "Actual_Result": "Pending"},
        {"Match_Num": 34, "Date_Str": "Jun 20", "Home_Team": "Ecuador", "Away_Team": "Curaçao", "Home_Win_Odds": 1.35, "Draw_Odds": 4.8, "Away_Win_Odds": 9.0, "Actual_Result": "Pending"},
        {"Match_Num": 35, "Date_Str": "Jun 20", "Home_Team": "Netherlands", "Away_Team": "Sweden", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.5, "Actual_Result": "Pending"},
        {"Match_Num": 36, "Date_Str": "Jun 20", "Home_Team": "Tunisia", "Away_Team": "Japan", "Home_Win_Odds": 3.3, "Draw_Odds": 3.2, "Away_Win_Odds": 2.2, "Actual_Result": "Pending"},
        {"Match_Num": 37, "Date_Str": "Jun 21", "Home_Team": "Belgium", "Away_Team": "IR Iran", "Home_Win_Odds": 1.45, "Draw_Odds": 4.2, "Away_Win_Odds": 7.5, "Actual_Result": "Pending"},
        {"Match_Num": 38, "Date_Str": "Jun 21", "Home_Team": "New Zealand", "Away_Team": "Egypt", "Home_Win_Odds": 3.8, "Draw_Odds": 3.2, "Away_Win_Odds": 2.0, "Actual_Result": "Pending"},
        {"Match_Num": 39, "Date_Str": "Jun 21", "Home_Team": "Spain", "Away_Team": "Saudi Arabia", "Home_Win_Odds": 1.3, "Draw_Odds": 5.0, "Away_Win_Odds": 10.0, "Actual_Result": "Pending"},
        {"Match_Num": 40, "Date_Str": "Jun 21", "Home_Team": "Uruguay", "Away_Team": "Cabo Verde", "Home_Win_Odds": 1.5, "Draw_Odds": 3.8, "Away_Win_Odds": 7.0, "Actual_Result": "Pending"},
        {"Match_Num": 41, "Date_Str": "Jun 22", "Home_Team": "France", "Away_Team": "Iraq", "Home_Win_Odds": 1.15, "Draw_Odds": 8.0, "Away_Win_Odds": 18.0, "Actual_Result": "Pending"},
        {"Match_Num": 42, "Date_Str": "Jun 22", "Home_Team": "Norway", "Away_Team": "Senegal", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8, "Actual_Result": "Pending"},
        {"Match_Num": 43, "Date_Str": "Jun 22", "Home_Team": "Argentina", "Away_Team": "Austria", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0, "Actual_Result": "Pending"},
        {"Match_Num": 44, "Date_Str": "Jun 22", "Home_Team": "Jordan", "Away_Team": "Algeria", "Home_Win_Odds": 3.0, "Draw_Odds": 3.2, "Away_Win_Odds": 2.4, "Actual_Result": "Pending"},
        {"Match_Num": 45, "Date_Str": "Jun 23", "Home_Team": "Portugal", "Away_Team": "Uzbekistan", "Home_Win_Odds": 1.22, "Draw_Odds": 6.5, "Away_Win_Odds": 14.0, "Actual_Result": "Pending"},
        {"Match_Num": 46, "Date_Str": "Jun 23", "Home_Team": "Colombia", "Away_Team": "Congo DR", "Home_Win_Odds": 1.7, "Draw_Odds": 3.5, "Away_Win_Odds": 5.0, "Actual_Result": "Pending"},
        {"Match_Num": 47, "Date_Str": "Jun 23", "Home_Team": "England", "Away_Team": "Ghana", "Home_Win_Odds": 1.35, "Draw_Odds": 4.8, "Away_Win_Odds": 9.0, "Actual_Result": "Pending"},
        {"Match_Num": 48, "Date_Str": "Jun 23", "Home_Team": "Panama", "Away_Team": "Croatia", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.8, "Actual_Result": "Pending"},
        {"Match_Num": 49, "Date_Str": "Jun 24", "Home_Team": "Czechia", "Away_Team": "Mexico", "Home_Win_Odds": 3.8, "Draw_Odds": 3.4, "Away_Win_Odds": 2.0, "Actual_Result": "Pending"},
        {"Match_Num": 50, "Date_Str": "Jun 24", "Home_Team": "South Africa", "Away_Team": "Korea Republic", "Home_Win_Odds": 3.2, "Draw_Odds": 3.3, "Away_Win_Odds": 2.3, "Actual_Result": "Pending"},
        {"Match_Num": 51, "Date_Str": "Jun 24", "Home_Team": "Switzerland", "Away_Team": "Canada", "Home_Win_Odds": 2.4, "Draw_Odds": 3.2, "Away_Win_Odds": 3.0, "Actual_Result": "Pending"},
        {"Match_Num": 52, "Date_Str": "Jun 24", "Home_Team": "Bosnia & Herz.", "Away_Team": "Qatar", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2, "Actual_Result": "Pending"},
        {"Match_Num": 53, "Date_Str": "Jun 24", "Home_Team": "Scotland", "Away_Team": "Brazil", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.55, "Actual_Result": "Pending"},
        {"Match_Num": 54, "Date_Str": "Jun 24", "Home_Team": "Morocco", "Away_Team": "Haiti", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0, "Actual_Result": "Pending"},
        {"Match_Num": 55, "Date_Str": "Jun 25", "Home_Team": "Türkiye", "Away_Team": "USA", "Home_Win_Odds": 4.0, "Draw_Odds": 3.5, "Away_Win_Odds": 1.95, "Actual_Result": "Pending"},
        {"Match_Num": 56, "Date_Str": "Jun 25", "Home_Team": "Paraguay", "Away_Team": "Australia", "Home_Win_Odds": 2.7, "Draw_Odds": 3.2, "Away_Win_Odds": 2.7, "Actual_Result": "Pending"},
        {"Match_Num": 57, "Date_Str": "Jun 25", "Home_Team": "Curaçao", "Away_Team": "Côte d'Ivoire", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.6, "Actual_Result": "Pending"},
        {"Match_Num": 58, "Date_Str": "Jun 25", "Home_Team": "Ecuador", "Away_Team": "Germany", "Home_Win_Odds": 5.0, "Draw_Odds": 3.8, "Away_Win_Odds": 1.7, "Actual_Result": "Pending"},
        {"Match_Num": 59, "Date_Str": "Jun 25", "Home_Team": "Japan", "Away_Team": "Sweden", "Home_Win_Odds": 2.6, "Draw_Odds": 3.2, "Away_Win_Odds": 2.8, "Actual_Result": "Pending"},
        {"Match_Num": 60, "Date_Str": "Jun 25", "Home_Team": "Tunisia", "Away_Team": "Netherlands", "Home_Win_Odds": 5.5, "Draw_Odds": 3.8, "Away_Win_Odds": 1.65, "Actual_Result": "Pending"},
        {"Match_Num": 61, "Date_Str": "Jun 26", "Home_Team": "Egypt", "Away_Team": "IR Iran", "Home_Win_Odds": 2.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.9, "Actual_Result": "Pending"},
