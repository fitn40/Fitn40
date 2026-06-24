import streamlit as st
import pandas as pd
import os
from datetime import datetime
from github import Github

# Page Branding Setup
st.set_page_config(page_title="Fit N 40 Match Prediction", page_icon="⚽", layout="centered")

DATA_FILE = "data.csv"
current_date = datetime.now()
current_year = current_date.year

# 📋 Official 72-Match Matrix (Wrapped for Mobile)
@st.cache_data
def get_match_data(year):
    raw_data = [
        {"Match_Num": 1, "Date_Str": "Jun 11", "Home_Team": "Mexico", "Away_Team": "South Africa", "Home_Win_Odds": 1.55, "Draw_Odds": 3.8, "Away_Win_Odds": 5.5},
        {"Match_Num": 2, "Date_Str": "Jun 11", "Home_Team": "Korea Republic", "Away_Team": "Czechia", "Home_Win_Odds": 2.1, "Draw_Odds": 3.2, "Away_Win_Odds": 3.5},
        {"Match_Num": 3, "Date_Str": "Jun 12", "Home_Team": "Canada", "Away_Team": "Bosnia & Herz.", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8},
        {"Match_Num": 4, "Date_Str": "Jun 13", "Home_Team": "Qatar", "Away_Team": "Switzerland", "Home_Win_Odds": 3.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1},
        {"Match_Num": 5, "Date_Str": "Jun 13", "Home_Team": "Brazil", "Away_Team": "Morocco", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5},
        {"Match_Num": 6, "Date_Str": "Jun 13", "Home_Team": "Haiti", "Away_Team": "Scotland", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.75},
        {"Match_Num": 7, "Date_Str": "Jun 12", "Home_Team": "USA", "Away_Team": "Paraguay", "Home_Win_Odds": 1.8, "Draw_Odds": 3.5, "Away_Win_Odds": 4.5},
        {"Match_Num": 8, "Date_Str": "Jun 13", "Home_Team": "Australia", "Away_Team": "Türkiye", "Home_Win_Odds": 2.8, "Draw_Odds": 3.2, "Away_Win_Odds": 2.6},
        {"Match_Num": 9, "Date_Str": "Jun 14", "Home_Team": "Germany", "Away_Team": "Curaçao", "Home_Win_Odds": 1.12, "Draw_Odds": 8.0, "Away_Win_Odds": 22.0},
        {"Match_Num": 10, "Date_Str": "Jun 14", "Home_Team": "Côte d'Ivoire", "Away_Team": "Ecuador", "Home_Win_Odds": 2.2, "Draw_Odds": 3.3, "Away_Win_Odds": 3.3},
        {"Match_Num": 11, "Date_Str": "Jun 14", "Home_Team": "Netherlands", "Away_Team": "Japan", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5},
        {"Match_Num": 12, "Date_Str": "Jun 14", "Home_Team": "Sweden", "Away_Team": "Tunisia", "Home_Win_Odds": 1.7, "Draw_Odds": 3.5, "Away_Win_Odds": 5.0},
        {"Match_Num": 13, "Date_Str": "Jun 15", "Home_Team": "Belgium", "Away_Team": "Egypt", "Home_Win_Odds": 1.6, "Draw_Odds": 3.7, "Away_Win_Odds": 5.8},
        {"Match_Num": 14, "Date_Str": "Jun 15", "Home_Team": "IR Iran", "Away_Team": "New Zealand", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2},
        {"Match_Num": 15, "Date_Str": "Jun 15", "Home_Team": "Spain", "Away_Team": "Cabo Verde", "Home_Win_Odds": 1.18, "Draw_Odds": 7.0, "Away_Win_Odds": 16.0},
        {"Match_Num": 16, "Date_Str": "Jun 15", "Home_Team": "Saudi Arabia", "Away_Team": "Uruguay", "Home_Win_Odds": 3.2, "Draw_Odds": 3.2, "Away_Win_Odds": 2.3},
        {"Match_Num": 17, "Date_Str": "Jun 16", "Home_Team": "France", "Away_Team": "Senegal", "Home_Win_Odds": 1.5, "Draw_Odds": 4.0, "Away_Win_Odds": 7.0},
        {"Match_Num": 18, "Date_Str": "Jun 16", "Home_Team": "Iraq", "Away_Team": "Norway", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.8},
        {"Match_Num": 19, "Date_Str": "Jun 16", "Home_Team": "Argentina", "Away_Team": "Algeria", "Home_Win_Odds": 1.3, "Draw_Odds": 5.0, "Away_Win_Odds": 10.0},
        {"Match_Num": 20, "Date_Str": "Jun 16", "Home_Team": "Austria", "Away_Team": "Jordan", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5},
        {"Match_Num": 21, "Date_Str": "Jun 17", "Home_Team": "Portugal", "Away_Team": "Congo DR", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0},
        {"Match_Num": 22, "Date_Str": "Jun 17", "Home_Team": "Uzbekistan", "Away_Team": "Colombia", "Home_Win_Odds": 3.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1},
        {"Match_Num": 23, "Date_Str": "Jun 17", "Home_Team": "England", "Away_Team": "Croatia", "Home_Win_Odds": 1.6, "Draw_Odds": 3.8, "Away_Win_Odds": 5.8},
        {"Match_Num": 24, "Date_Str": "Jun 17", "Home_Team": "Ghana", "Away_Team": "Panama", "Home_Win_Odds": 1.95, "Draw_Odds": 3.3, "Away_Win_Odds": 4.0},
        {"Match_Num": 25, "Date_Str": "Jun 18", "Home_Team": "Czechia", "Away_Team": "South Africa", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2},
        {"Match_Num": 26, "Date_Str": "Jun 18", "Home_Team": "Mexico", "Away_Team": "Korea Republic", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.5},
        {"Match_Num": 27, "Date_Str": "Jun 18", "Home_Team": "Switzerland", "Away_Team": "Bosnia & Herz.", "Home_Win_Odds": 1.75, "Draw_Odds": 3.5, "Away_Win_Odds": 4.8},
        {"Match_Num": 28, "Date_Str": "Jun 18", "Home_Team": "Canada", "Away_Team": "Qatar", "Home_Win_Odds": 1.55, "Draw_Odds": 3.7, "Away_Win_Odds": 6.0},
        {"Match_Num": 29, "Date_Str": "Jun 19", "Home_Team": "Brazil", "Away_Team": "Haiti", "Home_Win_Odds": 1.2, "Draw_Odds": 6.5, "Away_Win_Odds": 16.0},
        {"Match_Num": 30, "Date_Str": "Jun 19", "Home_Team": "Scotland", "Away_Team": "Morocco", "Home_Win_Odds": 3.6, "Draw_Odds": 3.3, "Away_Win_Odds": 2.1},
        {"Match_Num": 31, "Date_Str": "Jun 19", "Home_Team": "USA", "Away_Team": "Australia", "Home_Win_Odds": 1.7, "Draw_Odds": 3.6, "Away_Win_Odds": 5.0},
        {"Match_Num": 32, "Date_Str": "Jun 19", "Home_Team": "Türkiye", "Away_Team": "Paraguay", "Home_Win_Odds": 2.2, "Draw_Odds": 3.3, "Away_Win_Odds": 3.3},
        {"Match_Num": 33, "Date_Str": "Jun 20", "Home_Team": "Germany", "Away_Team": "Côte d'Ivoire", "Home_Win_Odds": 1.65, "Draw_Odds": 3.6, "Away_Win_Odds": 5.5},
        {"Match_Num": 34, "Date_Str": "Jun 20", "Home_Team": "Ecuador", "Away_Team": "Curaçao", "Home_Win_Odds": 1.35, "Draw_Odds": 4.8, "Away_Win_Odds": 9.0},
        {"Match_Num": 35, "Date_Str": "Jun 20", "Home_Team": "Netherlands", "Away_Team": "Sweden", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.5},
        {"Match_Num": 36, "Date_Str": "Jun 20", "Home_Team": "Tunisia", "Away_Team": "Japan", "Home_Win_Odds": 3.3, "Draw_Odds": 3.2, "Away_Win_Odds": 2.2},
        {"Match_Num": 37, "Date_Str": "Jun 21", "Home_Team": "Belgium", "Away_Team": "IR Iran", "Home_Win_Odds": 1.45, "Draw_Odds": 4.2, "Away_Win_Odds": 7.5},
        {"Match_Num": 38, "Date_Str": "Jun 21", "Home_Team": "New Zealand", "Away_Team": "Egypt", "Home_Win_Odds": 3.8, "Draw_Odds": 3.2, "Away_Win_Odds": 2.0},
        {"Match_Num": 39, "Date_Str": "Jun 21", "Home_Team": "Spain", "Away_Team": "Saudi Arabia", "Home_Win_Odds": 1.3, "Draw_Odds": 5.0, "Away_Win_Odds": 10.0},
        {"Match_Num": 40, "Date_Str": "Jun 21", "Home_Team": "Uruguay", "Away_Team": "Cabo Verde", "Home_Win_Odds": 1.5, "Draw_Odds": 3.8, "Away_Win_Odds": 7.0},
        {"Match_Num": 41, "Date_Str": "Jun 22", "Home_Team": "France", "Away_Team": "Iraq", "Home_Win_Odds": 1.15, "Draw_Odds": 8.0, "Away_Win_Odds": 18.0},
        {"Match_Num": 42, "Date_Str": "Jun 22", "Home_Team": "Norway", "Away_Team": "Senegal", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8},
        {"Match_Num": 43, "Date_Str": "Jun 22", "Home_Team": "Argentina", "Away_Team": "Austria", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0},
        {"Match_Num": 44, "Date_Str": "Jun 22", "Home_Team": "Jordan", "Away_Team": "Algeria", "Home_Win_Odds": 3.0, "Draw_Odds": 3.2, "Away_Win_Odds": 2.4},
        {"Match_Num": 45, "Date_Str": "Jun 23", "Home_Team": "Portugal", "Away_Team": "Uzbekistan", "Home_Win_Odds": 1.22, "Draw_Odds": 6.5, "Away_Win_Odds": 14.0},
        {"Match_Num": 46, "Date_Str": "Jun 23", "Home_Team": "Colombia", "Away_Team": "Congo DR", "Home_Win_Odds": 1.7, "Draw_Odds": 3.5, "Away_Win_Odds": 5.0},
        {"Match_Num": 47, "Date_Str": "Jun 23", "Home_Team": "England", "Away_Team": "Ghana", "Home_Win_Odds": 1.35, "Draw_Odds": 4.8, "Away_Win_Odds": 9.0},
        {"Match_Num": 48, "Date_Str": "Jun 23", "Home_Team": "Panama", "Away_Team": "Croatia", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.8},
        
        # 👇 Lines wrapped shorter below so they safely copy on phones:
        {"Match_Num": 49, "Date_Str": "Jun 24", "Home_Team": "Czechia", 
         "Away_Team": "Mexico", "Home_Win_Odds": 3.6, "Draw_Odds": 3.9, "Away_Win_Odds": 1.91},
        {"Match_Num": 50, "Date_Str": "Jun 24", "Home_Team": "South Africa", 
         "Away_Team": "Korea Republic", "Home_Win_Odds": 5.0, "Draw_Odds": 3.9, "Away_Win_Odds": 1.67},
        {"Match_Num": 51, "Date_Str": "Jun 24", "Home_Team": "Switzerland", 
         "Away_Team": "Canada", "Home_Win_Odds": 2.3, "Draw_Odds": 3.2, "Away_Win_Odds": 3.25},
        {"Match_Num": 52, "Date_Str": "Jun 24", "Home_Team": "Bosnia & Herz.", 
         "Away_Team": "Qatar", "Home_Win_Odds": 1.4, "Draw_Odds": 5.0, "Away_Win_Odds": 7.5},
        {"Match_Num": 53, "Date_Str": "Jun 24", "Home_Team": "Scotland", 
         "Away_Team": "Brazil", "Home_Win_Odds": 8.5, "Draw_Odds": 5.25, "Away_Win_Odds": 1.33},
        {"Match_Num": 54, "Date_Str": "Jun 24", "Home_Team": "Morocco", 
         "Away_Team": "Haiti", "Home_Win_Odds": 1.18, "Draw_Odds": 7.0, "Away_Win_Odds": 13.0},
        {"Match_Num": 55, "Date_Str": "Jun 25", "Home_Team": "Türkiye", 
         "Away_Team": "USA", "Home_Win_Odds": 3.7, "Draw_Odds": 3.9, "Away_Win_Odds": 1.91},
        {"Match_Num": 56, "Date_Str": "Jun 25", "Home_Team": "Paraguay", 
         "Away_Team": "Australia", "Home_Win_Odds": 2.2, "Draw_Odds": 3.1, "Away_Win_Odds": 3.1},
        {"Match_Num": 57, "Date_Str": "Jun 25", "Home_Team": "Curaçao", 
         "Away_Team": "Côte d'Ivoire", "Home_Win_Odds": 17.0, "Draw_Odds": 8.0, "Away_Win_Odds": 1.17},
        {"Match_Num": 58, "Date_Str": "Jun 25", "Home_Team": "Ecuador", 
         "Away_Team": "Germany", "Home_Win_Odds": 3.7, "Draw_Odds": 4.1, "Away_Win_Odds": 1.9},
        {"Match_Num": 59, "Date_Str": "Jun 25", "Home_Team": "Japan", 
         "Away_Team": "Sweden", "Home_Win_Odds": 1.9, "Draw_Odds": 3.4, "Away_Win_Odds": 4.33},
        {"Match_Num": 60, "Date_Str": "Jun 25", "Home_Team": "Tunisia", 
         "Away_Team": "Netherlands", "Home_Win_Odds": 23.0, "Draw_Odds": 8.0, "Away_Win_Odds": 1.12},
        {"Match_Num": 61, "Date_Str": "Jun 26", "Home_Team": "Egypt", 
         "Away_Team": "IR Iran", "Home_Win_Odds": 1.5, "Draw_Odds": 3.8, "Away_Win_Odds": 6.5},
        {"Match_Num": 62, "Date_Str": "Jun 26", "Home_Team": "New Zealand", 
         "Away_Team": "Belgium", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.55},
        {"Match_Num": 63, "Date_Str": "Jun 26", "Home_Team": "Cabo Verde", 
         "Away_Team": "Saudi Arabia", "Home_Win_Odds": 1.55, "Draw_Odds": 3.5, "Away_Win_Odds": 5.5},
        {"Match_Num": 64, "Date_Str": "Jun 26", "Home_Team": "Uruguay", 
         "Away_Team": "Spain", "Home_Win_Odds": 4.5, "Draw_Odds": 3.8, "Away_Win_Odds": 1.55},
        {"Match_Num": 65, "Date_Str": "Jun 26", "Home_Team": "Norway", 
         "Away_Team": "France", "Home_Win_Odds": 3.0, "Draw_Odds": 3.4, "Away_Win_Odds": 2.0},
        {"Match_Num": 66, "Date_Str": "Jun 26", "Home_Team": "Senegal", 
         "Away_Team": "Iraq", "Home_Win_Odds": 1.65, "Draw_Odds": 3.2, "Away_Win_Odds": 5.5},
        {"Match_Num": 67, "Date_Str": "Jun 27", "Home_Team": "Algeria", 
         "Away_Team": "Austria", "Home_Win_Odds": 2.8, "Draw_Odds": 3.2, "Away_Win_Odds": 2.5},
        {"Match_Num": 68, "Date_Str": "Jun 27", "Home_Team": "Jordan", 
         "Away_Team": "Argentina", "Home_Win_Odds": 8.5, "Draw_Odds": 5.0, "Away_Win_Odds": 1.25},
        {"Match_Num": 69, "Date_Str": "Jun 27", "Home_Team": "Colombia", 
         "Away_Team": "Portugal", "Home_Win_Odds": 2.3, "Draw_Odds": 3.2, "Away_Win_Odds": 4.5},
        {"Match_Num": 70, "Date_Str": "Jun 27", "Home_Team": "Congo DR", 
         "Away_Team": "Uzbekistan", "Home_Win_Odds": 1.53, "Draw_Odds": 3.9, "Away_Win_Odds": 6.5},
        {"Match_Num": 71, "Date_Str": "Jun 27", "Home_Team": "Panama", 
         "Away_Team": "England", "Home_Win_Odds": 8.0, "Draw_Odds": 5.5, "Away_Win_Odds": 1.2},
        {"Match_Num": 72, "Date_Str": "Jun 27", "Home_Team": "Croatia", 
         "Away_Team": "Ghana", "Home_Win_Odds": 1.6, "Draw_Odds": 3.2, "Away_Win_Odds": 5.5}
    ]
    df = pd.DataFrame(raw_data)
    df = df.sort_values(by="Match_Num").reset_index(drop=True)
    df['Match_Display'] = "Match " + df['Match_Num'].astype(str) + " (" + df['Date_Str'] + "): " + df['Home_Team'] + " vs " + df['Away_Team']
    
    dates_list = []
    for idx, row in df.iterrows():
        try:
            dates_list.append(datetime.strptime(f"{row['Date_Str']} {year}", "%b %d %Y").date())
        except:
            dates_list.append(datetime.now().date())
    df['Match_Date_Obj'] = dates_list
    return df

match_data = get_match_data(current_year)

# 🔄 AUTOMATIC PERMANENT STORAGE HOOKS (Ensures data survives refreshes and syncs globally)
def get_github_repo():
    try:
        gh = Github(st.secrets["GITHUB_TOKEN"])
        return gh.get_repo(st.secrets["REPO_NAME"])
    except:
        return None

def sync_from_github():
    repo = get_github_repo()
    if repo:
        try:
            content = repo.get_contents(DATA_FILE)
            raw_data = content.decoded_content.decode('utf-8')
            with open(DATA_FILE, "w") as f:
                f.write(raw_data)
        except:
            pass

def load_permanent_bets():
    sync_from_github()
    if os.path.exists(DATA_FILE):
        try:
            df = pd.read_csv(DATA_FILE)
            return df.fillna("").to_dict(orient="records")
        except:
            return []
    return []

def save_all_bets_permanently(bets_list):
    df = pd.DataFrame(bets_list) if len(bets_list) > 0 else pd.DataFrame(columns=["Bet_ID","Creator","Match_Num","Match_Name","Match_Date","Prediction","Points","Opponent_Payout","Opponent","Status","Is_Expired"])
    df.to_csv(DATA_FILE, index=False)
    repo = get_github_repo()
    if repo:
        try:
            csv_string = df.to_csv(index=False)
            contents = repo.get_contents(DATA_FILE)
            repo.update_file(contents.path, "🔄 Live Bets Auto-Sync", csv_string, contents.sha)
        except:
            pass
            
def execute_backend_deletion(bet_id_to_remove):
    # Filter out the targeted bet ID from the master list
    updated_bets = [b for b in combined_bets if int(b.get("Bet_ID", 0)) != int(bet_id_to_remove)]
    save_all_bets_permanently(updated_bets)
    st.success(f"🗑️ Bet #{bet_id_to_remove} deleted successfully from backend!")
    st.rerun()
    

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

if "user" in st.query_params and st.session_state.player_name == "":
    st.session_state.player_name = st.query_params["user"].strip()
    st.session_state.current_page = "dashboard"

combined_bets = load_permanent_bets()

# Auto Expiry Processing Loop
for bet in combined_bets:
    try:
        m_lookup = match_data[match_data['Match_Num'] == int(bet['Match_Num'])]
        if not m_lookup.empty:
            bet["Is_Expired"] = current_date.date() > m_lookup.iloc[0]['Match_Date_Obj']
    except:
        bet["Is_Expired"] = False

is_admin = (st.session_state.player_name == "Fifa@2026")

# ==========================================
# ⚽ UI SCREEN 1: LOGIN LOUNGE
# ==========================================
if st.session_state.current_page == "login":
    st.title("⚽ Fit N 40 Match Prediction")
    st.subheader("Welcome to the Lounge")
    player_input = st.text_input("Profile Handle Name:")
    if st.button("Enter Dashboard", use_container_width=True, type="primary"):
        if player_input.strip():
            st.session_state.player_name = player_input.strip()
            st.query_params["user"] = player_input.strip()
            st.session_state.current_page = "dashboard"
            st.rerun()

# ==========================================
# 🏆 UI SCREEN 2: MAIN USER APP INTERFACE
# ==========================================
elif st.session_state.current_page == "dashboard":
    st.title("🏆 Fit N 40 Dashboard")
    st.write(f"Logged in as: **{st.session_state.player_name}**")
    
    if is_admin:
        col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    else:
        col_n1, col_n2, col_n4 = st.columns([1, 1, 1])

    with col_n1:
        if st.button("➕ Open New Bet", use_container_width=True, type="primary"):
            st.session_state.current_page = "new_bet"
            st.rerun()
    with col_n2:
        if st.button("📊 Current Standings", use_container_width=True):
            st.session_state.current_page = "view_excel"
            st.rerun()
    if is_admin:
        with col_n3:
            if st.button("⚙️ Dev Storage", use_container_width=True):
                st.session_state.current_page = "view_db"
                st.rerun()
    with col_n4:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.player_name = ""
            st.query_params.clear()
            st.session_state.current_page = "login"
            st.rerun()
            
    st.markdown("---")
    
    # Pull directly from your permanent data.csv rows
    open_bets = [b for b in combined_bets if b.get("Status", "Open") == "Open" and not b.get("Is_Expired", False)]
    live_bets = [b for b in combined_bets if b.get("Status") == "Matched" and not b.get("Is_Expired", False)]

    # 🔄 CHRONOLOGICAL DATE-SORTING ENGINE
    def get_bet_sort_date(b):
        try:
            m_num = int(b.get("Match_Num", 0))
            match_row = match_data[match_data['Match_Num'] == m_num]
            if not match_row.empty:
                return match_row.iloc[0]['Match_Date_Obj']
        except:
            pass
        return current_date.date()

    # Sort both lists so the earliest matches appear at the top
    open_bets = sorted(open_bets, key=get_bet_sort_date)
    live_bets = sorted(live_bets, key=get_bet_sort_date)

    
    # 📋 1. Unmatched Open Block
    st.subheader("📋 1. Active Open Offers")
    if not open_bets:
        st.info("No open offers available.")
    else:
        for bet in open_bets:
            with st.container(border=True):
                # 🔍 1. Background lookup to grab original market baseline payout
                try:
                    m_lookup = match_data[match_data['Match_Num'] == int(bet.get('Match_Num'))].iloc[0]
                    prediction_type = bet.get('Prediction')
                    
                    if prediction_type == m_lookup['Home_Team']:
                        m_odds = m_lookup['Home_Win_Odds']
                    elif prediction_type == m_lookup['Away_Team']:
                        m_odds = m_lookup['Away_Win_Odds']
                    else:
                        m_odds = m_lookup['Draw_Odds']
                    
                    # Calculate what the market payout would have been for this risk amount
                    b_pts = float(bet.get('Points', 100))
                    market_payout = float(round(b_pts * (m_odds - 1), 1))
                    market_str = f"Market Odds - {market_payout} pts"
                except:
                    market_str = "Market Odds - N/A"

                # 📊 2. Read current offer numbers
                b_creator = bet.get('Creator')
                b_pred = bet.get('Prediction')
                b_match = bet.get('Match_Name')
                b_risk = float(bet.get('Points', 0))
                b_payout = float(bet.get('Opponent_Payout', 0))

                # 📱 3. Render the Name-Specific Layout
                st.markdown(f"🗓️ **{b_creator}** backs **{b_pred}**")
                st.write(f"📅 **Date:** {bet.get('Match_Date')} | Fixture: {b_match}")
                st.markdown(f"🔹 **{b_creator} Risks:** {b_risk} pts to win {b_payout} pts")
                st.markdown(f"🔸 **You Must Risk:** {b_payout} pts to win {b_risk} pts *({market_str})*")
    
                is_bet_creator = bet.get('Creator').lower() == st.session_state.player_name.lower()
                
                if is_admin or is_bet_creator:
                    if st.button(f"🗑️ Delete Offer #{bet.get('Bet_ID')}", key=f"del_open_{bet.get('Bet_ID')}", use_container_width=True, type="secondary"):
                        execute_backend_deletion(bet.get('Bet_ID'))
                
                if not is_bet_creator:
                    if st.button(f"🤝 Match Offer #{bet.get('Bet_ID')}", key=f"m_{bet.get('Bet_ID')}", use_container_width=True):
                        st.session_state.selected_bet_to_match = bet
                        st.session_state.current_page = "confirm_match"
                        st.rerun()

    # 🔥 2. Live Matched Locked Block
    st.subheader("🔥 2. Live Matched Bets (Locked)")
    if not live_bets:
        st.caption("No matched transactions are locked right now.")
    else:
        for bet in live_bets:
            with st.container(border=True):
                st.markdown(f"🔒 **{bet.get('Creator')}** 🆚 **{bet.get('Opponent')}**")
                st.write(f"📅 **Kickoff Date:** {bet.get('Match_Date')} | **Match:** {bet.get('Match_Name')}")
                
                risk_pts = bet.get('Points', 100)
                win_pts = bet.get('Opponent_Payout', 55)
                st.write(f"📢 **{bet.get('Creator')}** bet on **{bet.get('Prediction')}** (Risking: {risk_pts} pts / Winning: {win_pts} pts) with **{bet.get('Opponent')}**.")
                
                if is_admin:
                    if st.button(f"🚨 Admin Override: Force Delete #{bet.get('Bet_ID')}", key=f"del_live_{bet.get('Bet_ID')}", use_container_width=True, type="secondary"):
                        execute_backend_deletion(bet.get('Bet_ID'))
                        

# ==========================================
# 📊 UI SCREEN: TOURNAMENT BOARD (LIVE EXCEL)
# ==========================================
elif st.session_state.current_page == "view_excel":
    st.title("📊 Live Tournament Board")
    st.write("This table updates dynamically whenever results are committed to the backend repository.")
    
    import os
    if os.path.exists("results.xlsx"):
        try:
            df_excel = pd.read_excel("results.xlsx")
            st.dataframe(df_excel, use_container_width=True, hide_index=True)
        except Exception as e:
            st.error("⚠️ Found results.xlsx but could not read its formatting. Ensure it is a standard data grid layout!")
    else:
        st.info("📢 Standings spreadsheet is currently being updated. Check back shortly or view your WhatsApp group chat for the latest scores!")
        
    st.markdown("---")
    if st.button("⬅ Back to Dashboard", use_container_width=True, type="secondary"):
        st.session_state.current_page = "dashboard"
        st.rerun()

# ==========================================
# 🤝 UI SCREEN: CONFIRM TO MATCH OFFER
# ==========================================
elif st.session_state.current_page == "confirm_match":
    st.title("🤝 Confirm Your Match Selection")
    
    bet = st.session_state.get("selected_bet_to_match", {})
    if not bet:
        st.error("No bet selected.")
        if st.button("⬅ Return to Dashboard", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()
    else:
        # 🔍 Look up original market odds for reference summary
        try:
            m_lookup = match_data[match_data['Match_Num'] == int(bet.get('Match_Num'))].iloc[0]
            prediction_type = bet.get('Prediction')
            if prediction_type == m_lookup['Home_Team']:
                m_odds = m_lookup['Home_Win_Odds']
            elif prediction_type == m_lookup['Away_Team']:
                m_odds = m_lookup['Away_Win_Odds']
            else:
                m_odds = m_lookup['Draw_Odds']
            
            b_pts = float(bet.get('Points', 100))
            market_payout = float(round(b_pts * (m_odds - 1), 1))
            market_str = f"{market_payout} pts"
        except:
            market_str = "N/A"

        # 📊 Extract exact stakes values
        creator_name = bet.get('Creator')
        match_title = bet.get('Match_Name')
        prediction = bet.get('Prediction')
        creator_risk = float(bet.get('Points', 0))
        your_risk = float(bet.get('Opponent_Payout', 0))

        # 📋 Summary Breakdown Card Display
        with st.container(border=True):
            st.subheader("📊 Bet Transaction Summary")
            st.write(f"📅 **Match Date:** {bet.get('Match_Date')}")
            st.write(f"⚽ **Fixture:** {match_title}")
            st.write(f"🔮 **{creator_name}’s Prediction:** Backing **{prediction}**")
            st.markdown("---")
            st.write(f"💵 **Your Risk Amount:** {your_risk} pts *(Amount you lose if {prediction} wins)*")
            st.write(f"💰 **Your Potential Payout:** {creator_risk} pts *(Amount you win if {prediction} loses/draws)*")
            
            # 🏛️ Calculate and show the market odds equivalent (Opponent Risk / Opponent Win)
            try:
                # market_payout is what the market says the opponent's risk SHOULD be for the creator's stake
                st.write(f"📊 **Market odds for the bet is:** {market_payout} (you lose) / {creator_risk} (you win)")
            except:
                st.write(f"📊 **Market odds for the bet is:** N/A")


        st.warning("⚠️ Once confirmed, this transaction is locked and cannot be deleted by either player.")

        # 🛑 Execution Buttons
        if st.button("✅ Confirm & Lock Bet", use_container_width=True, type="primary"):
            for b in combined_bets:
                if int(b.get("Bet_ID", 0)) == int(bet.get("Bet_ID", 0)):
                    b["Status"] = "Matched"
                    b["Opponent"] = str(st.session_state.player_name)
            
            save_all_bets_permanently(combined_bets)
            st.success("🔒 Bet matched and locked into ledger permanently!")
            st.session_state.current_page = "dashboard"
            st.rerun()

        if st.button("⬅ Cancel & Go Back", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()

# ==========================================
# 🎲 UI SCREEN: CREATE NEW BET OFFERS
# ==========================================
elif st.session_state.current_page == "new_bet":
    st.title("🎲 Create New Prediction Offer")
    active_fixtures = match_data[match_data['Match_Date_Obj'] >= current_date.date()]
    selected_match_str = st.selectbox("👉 Target Match Fixture:", options=["-- Select --"] + active_fixtures['Match_Display'].tolist())
    
    if selected_match_str != "-- Select --":
        match_row = match_data[match_data['Match_Display'] == selected_match_str].iloc[0]
        selected_prediction = st.selectbox("🔮 Outcome Selection:", options=["-- Select --", match_row['Home_Team'], match_row['Away_Team'], "Draw"])
        
        if selected_prediction != "-- Select --":
        # 💰 UNLOCKED RISK & WIN SELECTION EXCHANGE
            points = st.number_input("Points You Want to Risk:", min_value=1, value=100, step=5)
            
            # Use the matrix odds to calculate a smart initial recommendation
            odds = float(match_row['Home_Win_Odds'] if selected_prediction == match_row['Home_Team'] else (match_row['Away_Win_Odds'] if selected_prediction == match_row['Away_Team'] else match_row['Draw_Odds']))
            default_payout = int(round(points * (odds - 1), 0))
            
            # Fully unlocked win input box with adjusters (+ / -)
            payout = st.number_input("Points You Want to Win (Adjustable):", min_value=1, value=default_payout, step=5)
            
            # Display information layout for the player
            custom_odds = round((payout / points) + 1, 2) if points > 0 else 0
            st.caption(f"💡 Implied custom odds layout: {custom_odds}x (Your opponent risks {payout} pts to win {points} pts)")

            if st.button("🚀 Publish Offer to Board", use_container_width=True, type="primary"):
                if not combined_bets:
                    next_id = 1
                else:
                    try:
                        next_id = max([int(b["Bet_ID"]) for b in combined_bets]) + 1
                    except:
                        next_id = len(combined_bets) + 1
                        
                combined_bets.append({
                    "Bet_ID": int(next_id), "Creator": str(st.session_state.player_name), "Match_Num": int(match_row['Match_Num']),
                    "Match_Name": f"{match_row['Home_Team']} vs {match_row['Away_Team']}", "Match_Date": str(match_row['Date_Str']),
                    "Prediction": str(selected_prediction), "Points": float(points), "Opponent_Payout": float(payout), "Opponent": "", "Status": "Open", "Is_Expired": False
                })
                save_all_bets_permanently(combined_bets)
                st.session_state.current_page = "dashboard"
                st.rerun()
                
    if st.button("⬅ Cancel", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()

# ==========================================
# ⚙️ UI SCREEN: MASTER DATABASE LOOKOVER
# ==========================================
elif st.session_state.current_page == "view_db":
    st.title("📊 Running Memory Dump Instance")
    st.dataframe(pd.DataFrame(combined_bets), use_container_width=True, hide_index=True)
    if st.button("⬅ Back", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()
