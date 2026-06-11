import streamlit as st
import pandas as pd
from datetime import datetime

# -------------------------------------------------------------
# 🔴 ENTER YOUR SPREADSHEET ID HERE
# -------------------------------------------------------------
SPREADSHEET_ID = "1jdOVGRpHKiuipDrW_dLc87qGYDBInScY-KZJ8mr3xmc"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/gviz/tq?tqx=out:csv&sheet=bets"

# Page Branding
st.set_page_config(page_title="Fit N 40 Match Prediction", page_icon="⚽", layout="centered")

# Get current system time parameters globally
current_date = datetime.now()
current_year = current_date.year

# Core Data Structure Pack (All 72 Matches with original schedule dates)
@st.cache_data
def get_match_data(year):
    raw_data = [
        {"Match_Num": 1, "Date_Str": "Jun 11", "Home_Team": "Mexico", "Away_Team": "South Africa", "Home_Win_Odds": 1.55, "Draw_Odds": 3.8, "Away_Win_Odds": 5.5, "Actual_Result": "Pending"},
        {"Match_Num": 2, "Date_Str": "Jun 11", "Home_Team": "Korea Republic", "Away_Team": "Czechia", "Home_Win_Odds": 2.1, "Draw_Odds": 3.2, "Away_Win_Odds": 3.5, "Actual_Result": "Pending"},
        {"Match_Num": 3, "Date_Str": "Jun 12", "Home_Team": "Canada", "Away_Team": "Bosnia & Herz.", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8, "Actual_Result": "Pending"},
        {"Match_Num": 4, "Date_Str": "Jun 13", "Home_Team": "Qatar", "Away_Team": "Switzerland", "Home_Win_Odds": 3.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1, "Actual_Result": "Pending"},
        {"Match_Num": 5, "Date_Str": "Jun 11", "Home_Team": "Spain", "Away_Team": "Cameroon", "Home_Win_Odds": 1.35, "Draw_Odds": 4.6, "Away_Win_Odds": 9.5, "Actual_Result": "Pending"},
        {"Match_Num": 6, "Date_Str": "Jun 12", "Home_Team": "USA", "Away_Team": "Morocco", "Home_Win_Odds": 2.4, "Draw_Odds": 3.2, "Away_Win_Odds": 3.0, "Actual_Result": "Pending"},
        {"Match_Num": 7, "Date_Str": "Jun 13", "Home_Team": "Uruguay", "Away_Team": "Panama", "Home_Win_Odds": 1.42, "Draw_Odds": 4.3, "Away_Win_Odds": 8.0, "Actual_Result": "Pending"},
        {"Match_Num": 8, "Date_Str": "Jun 13", "Home_Team": "Japan", "Away_Team": "Saudi Arabia", "Home_Win_Odds": 1.45, "Draw_Odds": 4.2, "Away_Win_Odds": 7.5, "Actual_Result": "Pending"},
        {"Match_Num": 9, "Date_Str": "Jun 13", "Home_Team": "Italy", "Away_Team": "Chile", "Home_Win_Odds": 1.7, "Draw_Odds": 3.6, "Away_Win_Odds": 5.25, "Actual_Result": "Pending"},
        {"Match_Num": 10, "Date_Str": "Jun 14", "Home_Team": "Croatia", "Away_Team": "Iraq", "Home_Win_Odds": 1.25, "Draw_Odds": 5.5, "Away_Win_Odds": 12.0, "Actual_Result": "Pending"},
        {"Match_Num": 11, "Date_Str": "Jun 14", "Home_Team": "Belgium", "Away_Team": "Algeria", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0, "Actual_Result": "Pending"},
        {"Match_Num": 12, "Date_Str": "Jun 14", "Home_Team": "Germany", "Away_Team": "New Zealand", "Home_Win_Odds": 1.14, "Draw_Odds": 7.5, "Away_Win_Odds": 19.0, "Actual_Result": "Pending"},
        {"Match_Num": 13, "Date_Str": "Jun 15", "Home_Team": "France", "Away_Team": "Angola", "Home_Win_Odds": 1.18, "Draw_Odds": 6.5, "Away_Win_Odds": 15.0, "Actual_Result": "Pending"},
        {"Match_Num": 14, "Date_Str": "Jun 15", "Home_Team": "Sweden", "Away_Team": "Ecuador", "Home_Win_Odds": 2.4, "Draw_Odds": 3.2, "Away_Win_Odds": 3.0, "Actual_Result": "Pending"},
        {"Match_Num": 15, "Date_Str": "Jun 16", "Home_Team": "Ukraine", "Away_Team": "Peru", "Home_Win_Odds": 2.2, "Draw_Odds": 3.2, "Away_Win_Odds": 3.4, "Actual_Result": "Pending"},
        {"Match_Num": 16, "Date_Str": "Jun 16", "Home_Team": "Argentina", "Away_Team": "Honduras", "Home_Win_Odds": 1.12, "Draw_Odds": 8.0, "Away_Win_Odds": 21.0, "Actual_Result": "Pending"},
        {"Match_Num": 17, "Date_Str": "Jun 17", "Home_Team": "Netherlands", "Away_Team": "Curaçao", "Home_Win_Odds": 1.08, "Draw_Odds": 9.5, "Away_Win_Odds": 26.0, "Actual_Result": "Pending"},
        {"Match_Num": 18, "Date_Str": "Jun 17", "Home_Team": "England", "Away_Team": "Jamaica", "Home_Win_Odds": 1.16, "Draw_Odds": 7.0, "Away_Win_Odds": 16.0, "Actual_Result": "Pending"},
        {"Match_Num": 19, "Date_Str": "Jun 17", "Home_Team": "Austria", "Away_Team": "Mali", "Home_Win_Odds": 1.95, "Draw_Odds": 3.3, "Away_Win_Odds": 4.0, "Actual_Result": "Pending"},
        {"Match_Num": 20, "Date_Str": "Jun 18", "Home_Team": "Ecuador", "Away_Team": "Scotland", "Home_Win_Odds": 2.05, "Draw_Odds": 3.3, "Away_Win_Odds": 3.7, "Actual_Result": "Pending"},
        {"Match_Num": 21, "Date_Str": "Jun 18", "Home_Team": "Portugal", "Away_Team": "Tunisia", "Home_Win_Odds": 1.45, "Draw_Odds": 4.2, "Away_Win_Odds": 7.5, "Actual_Result": "Pending"},
        {"Match_Num": 22, "Date_Str": "Jun 18", "Home_Team": "Colombia", "Away_Team": "Uzbekistan", "Home_Win_Odds": 1.22, "Draw_Odds": 6.0, "Away_Win_Odds": 13.0, "Actual_Result": "Pending"},
        {"Match_Num": 23, "Date_Str": "Jun 19", "Home_Team": "England", "Away_Team": "Croatia", "Home_Win_Odds": 1.75, "Draw_Odds": 3.5, "Away_Win_Odds": 4.8, "Actual_Result": "Pending"},
        {"Match_Num": 24, "Date_Str": "Jun 19", "Home_Team": "Ghana", "Away_Team": "Panama", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2, "Actual_Result": "Pending"},
        {"Match_Num": 25, "Date_Str": "Jun 18", "Home_Team": "Czechia", "Away_Team": "South Africa", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2, "Actual_Result": "Pending"},
        {"Match_Num": 26, "Date_Str": "Jun 18", "Home_Team": "Mexico", "Away_Team": "Korea Republic", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.5, "Actual_Result": "Pending"},
        {"Match_Num": 27, "Date_Str": "Jun 18", "Home_Team": "Switzerland", "Away_Team": "Bosnia & Herz.", "Home_Win_Odds": 1.75, "Draw_Odds": 3.5, "Away_Win_Odds": 4.8, "Actual_Result": "Pending"},
        {"Match_Num": 28, "Date_Str": "Jun 18", "Home_Team": "Canada", "Away_Team": "Qatar", "Home_Win_Odds": 1.55, "Draw_Odds": 3.7, "Away_Win_Odds": 6.0, "Actual_Result": "Pending"},
        {"Match_Num": 29, "Date_Str": "Jun 19", "Home_Team": "Spain", "Away_Team": "Uruguay", "Home_Win_Odds": 2.15, "Draw_Odds": 3.2, "Away_Win_Odds": 3.5, "Actual_Result": "Pending"},
        {"Match_Num": 30, "Date_Str": "Jun 19", "Home_Team": "Cameroon", "Away_Team": "Panama", "Home_Win_Odds": 2.1, "Draw_Odds": 3.2, "Away_Win_Odds": 3.6, "Actual_Result": "Pending"},
        {"Match_Num": 31, "Date_Str": "Jun 20", "Home_Team": "Japan", "Away_Team": "USA", "Home_Win_Odds": 1.95, "Draw_Odds": 3.3, "Away_Win_Odds": 4.0, "Actual_Result": "Pending"},
        {"Match_Num": 32, "Date_Str": "Jun 20", "Home_Team": "Saudi Arabia", "Away_Team": "Morocco", "Home_Win_Odds": 3.8, "Draw_Odds": 3.3, "Away_Win_Odds": 2.0, "Actual_Result": "Pending"},
        {"Match_Num": 33, "Date_Str": "Jun 20", "Home_Team": "Italy", "Away_Team": "Belgium", "Home_Win_Odds": 2.6, "Draw_Odds": 3.1, "Away_Win_Odds": 2.8, "Actual_Result": "Pending"},
        {"Match_Num": 34, "Date_Str": "Jun 21", "Home_Team": "Chile", "Away_Team": "Algeria", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.75, "Actual_Result": "Pending"},
        {"Match_Num": 35, "Date_Str": "Jun 21", "Home_Team": "Germany", "Away_Team": "Croatia", "Home_Win_Odds": 1.75, "Draw_Odds": 3.6, "Away_Win_Odds": 4.6, "Actual_Result": "Pending"},
        {"Match_Num": 36, "Date_Str": "Jun 21", "Home_Team": "New Zealand", "Away_Team": "Iraq", "Home_Win_Odds": 2.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.88, "Actual_Result": "Pending"},
        {"Match_Num": 37, "Date_Str": "Jun 22", "Home_Team": "France", "Away_Team": "Ukraine", "Home_Win_Odds": 1.48, "Draw_Odds": 4.2, "Away_Win_Odds": 6.8, "Actual_Result": "Pending"},
        {"Match_Num": 38, "Date_Str": "Jun 22", "Home_Team": "Angola", "Away_Team": "Peru", "Home_Win_Odds": 4.33, "Draw_Odds": 3.4, "Away_Win_Odds": 1.87, "Actual_Result": "Pending"},
        {"Match_Num": 39, "Date_Str": "Jun 22", "Home_Team": "Argentina", "Away_Team": "Sweden", "Home_Win_Odds": 1.5, "Draw_Odds": 4.2, "Away_Win_Odds": 6.5, "Actual_Result": "Pending"},
        {"Match_Num": 40, "Date_Str": "Jun 23", "Home_Team": "Honduras", "Away_Team": "Ecuador", "Home_Win_Odds": 5.5, "Draw_Odds": 3.8, "Away_Win_Odds": 1.62, "Actual_Result": "Pending"},
        {"Match_Num": 41, "Date_Str": "Jun 23", "Home_Team": "Netherlands", "Away_Team": "Austria", "Home_Win_Odds": 1.55, "Draw_Odds": 4.0, "Away_Win_Odds": 6.0, "Actual_Result": "Pending"},
        {"Match_Num": 42, "Date_Str": "Jun 23", "Home_Team": "Curaçao", "Away_Team": "Mali", "Home_Win_Odds": 6.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.53, "Actual_Result": "Pending"},
        {"Match_Num": 43, "Date_Str": "Jun 24", "Home_Team": "England", "Away_Team": "Ecuador", "Home_Win_Odds": 1.57, "Draw_Odds": 3.9, "Away_Win_Odds": 5.8, "Actual_Result": "Pending"},
        {"Match_Num": 44, "Date_Str": "Jun 24", "Home_Team": "Jamaica", "Away_Team": "Scotland", "Home_Win_Odds": 4.5, "Draw_Odds": 3.5, "Away_Win_Odds": 1.8, "Actual_Result": "Pending"},
        {"Match_Num": 45, "Date_Str": "Jun 24", "Home_Team": "Portugal", "Away_Team": "Uzbekistan", "Home_Win_Odds": 1.25, "Draw_Odds": 5.5, "Away_Win_Odds": 11.0, "Actual_Result": "Pending"},
        {"Match_Num": 46, "Date_Str": "Jun 24", "Home_Team": "Colombia", "Away_Team": "Congo DR", "Home_Win_Odds": 1.3, "Draw_Odds": 5.0, "Away_Win_Odds": 10.0, "Actual_Result": "Pending"},
        {"Match_Num": 47, "Date_Str": "Jun 25", "Home_Team": "England", "Away_Team": "Ghana", "Home_Win_Odds": 1.45, "Draw_Odds": 4.2, "Away_Win_Odds": 7.0, "Actual_Result": "Pending"},
        {"Match_Num": 48, "Date_Str": "Jun 25", "Home_Team": "Panama", "Away_Team": "Croatia", "Home_Win_Odds": 5.25, "Draw_Odds": 3.6, "Away_Win_Odds": 1.67, "Actual_Result": "Pending"},
        {"Match_Num": 49, "Date_Str": "Jun 24", "Home_Team": "Czechia", "Away_Team": "Mexico", "Home_Win_Odds": 3.8, "Draw_Odds": 3.4, "Away_Win_Odds": 2.0, "Actual_Result": "Pending"},
        {"Match_Num": 50, "Date_Str": "Jun 24", "Home_Team": "South Africa", "Away_Team": "Korea Republic", "Home_Win_Odds": 3.2, "Draw_Odds": 3.3, "Away_Win_Odds": 2.3, "Actual_Result": "Pending"},
        {"Match_Num": 51, "Date_Str": "Jun 24", "Home_Team": "Switzerland", "Away_Team": "Canada", "Home_Win_Odds": 2.2, "Draw_Odds": 3.1, "Away_Win_Odds": 3.4, "Actual_Result": "Pending"},
        {"Match_Num": 52, "Date_Str": "Jun 24", "Home_Team": "Bosnia & Herz.", "Away_Team": "Qatar", "Home_Win_Odds": 1.85, "Draw_Odds": 3.4, "Away_Win_Odds": 4.35, "Actual_Result": "Pending"},
        {"Match_Num": 53, "Date_Str": "Jun 24", "Home_Team": "Panama", "Away_Team": "Spain", "Home_Win_Odds": 9.0, "Draw_Odds": 4.8, "Away_Win_Odds": 1.36, "Actual_Result": "Pending"},
        {"Match_Num": 54, "Date_Str": "Jun 24", "Home_Team": "Cameroon", "Away_Team": "Uruguay", "Home_Win_Odds": 4.5, "Draw_Odds": 3.4, "Away_Win_Odds": 1.83, "Actual_Result": "Pending"},
        {"Match_Num": 55, "Date_Str": "Jun 25", "Home_Team": "Morocco", "Away_Team": "Japan", "Home_Win_Odds": 3.2, "Draw_Odds": 3.2, "Away_Win_Odds": 2.3, "Actual_Result": "Pending"},
        {"Match_Num": 56, "Date_Str": "Jun 25", "Home_Team": "Saudi Arabia", "Away_Team": "USA", "Home_Win_Odds": 4.0, "Draw_Odds": 3.4, "Away_Win_Odds": 1.91, "Actual_Result": "Pending"},
        {"Match_Num": 57, "Date_Str": "Jun 25", "Home_Team": "Algeria", "Away_Team": "Italy", "Home_Win_Odds": 6.5, "Draw_Odds": 3.9, "Away_Win_Odds": 1.53, "Actual_Result": "Pending"},
        {"Match_Num": 58, "Date_Str": "Jun 25", "Home_Team": "Chile", "Away_Team": "Belgium", "Home_Win_Odds": 4.33, "Draw_Odds": 3.5, "Away_Win_Odds": 1.83, "Actual_Result": "Pending"},
        {"Match_Num": 59, "Date_Str": "Jun 25", "Home_Team": "Iraq", "Away_Team": "Germany", "Home_Win_Odds": 15.0, "Draw_Odds": 6.5, "Away_Win_Odds": 1.18, "Actual_Result": "Pending"},
        {"Match_Num": 60, "Date_Str": "Jun 25", "Home_Team": "New Zealand", "Away_Team": "Croatia", "Home_Win_Odds": 9.0, "Draw_Odds": 4.8, "Away_Win_Odds": 1.35, "Actual_Result": "Pending"},
        {"Match_Num": 61, "Date_Str": "Jun 26", "Home_Team": "Peru", "Away_Team": "France", "Home_Win_Odds": 8.0, "Draw_Odds": 4.5, "Away_Win_Odds": 1.4, "Actual_Result": "Pending"},
        {"Match_Num": 62, "Date_Str": "Jun 26", "Home_Team": "Angola", "Away_Team": "Ukraine", "Home_Win_Odds": 5.25, "Draw_Odds": 3.6, "Away_Win_Odds": 1.67, "Actual_Result": "Pending"},
        {"Match_Num": 63, "Date_Str": "Jun 26", "Home_Team": "Ecuador", "Away_Team": "Argentina", "Home_Win_Odds": 6.5, "Draw_Odds": 4.2, "Away_Win_Odds": 1.5, "Actual_Result": "Pending"},
        {"Match_Num": 64, "Date_Str": "Jun 26", "Home_Team": "Honduras", "Away_Team": "Sweden", "Home_Win_Odds": 8.0, "Draw_Odds": 4.5, "Away_Win_Odds": 1.4, "Actual_Result": "Pending"},
        {"Match_Num": 65, "Date_Str": "Jun 26", "Home_Team": "Mali", "Away_Team": "Netherlands", "Home_Win_Odds": 10.0, "Draw_Odds": 5.25, "Away_Win_Odds": 1.3, "Actual_Result": "Pending"},
        {"Match_Num": 66, "Date_Str": "Jun 26", "Home_Team": "Curaçao", "Away_Team": "Austria", "Home_Win_Odds": 12.0, "Draw_Odds": 5.5, "Away_Win_Odds": 1.25, "Actual_Result": "Pending"},
        {"Match_Num": 67, "Date_Str": "Jun 27", "Home_Team": "Scotland", "Away_Team": "England", "Home_Win_Odds": 6.0, "Draw_Odds": 4.0, "Away_Win_Odds": 1.55, "Actual_Result": "Pending"},
        {"Match_Num": 68, "Date_Str": "Jun 27", "Home_Team": "Jamaica", "Away_Team": "Ecuador", "Home_Win_Odds": 5.5, "Draw_Odds": 3.75, "Away_Win_Odds": 1.63, "Actual_Result": "Pending"},
        {"Match_Num": 69, "Date_Str": "Jun 27", "Home_Team": "Colombia", "Away_Team": "Portugal", "Home_Win_Odds": 3.1, "Draw_Odds": 3.2, "Away_Win_Odds": 2.35, "Actual_Result": "Pending"},
        {"Match_Num": 70, "Date_Str": "Jun 27", "Home_Team": "Congo DR", "Away_Team": "Uzbekistan", "Home_Win_Odds": 2.2, "Draw_Odds": 3.2, "Away_Win_Odds": 3.4, "Actual_Result": "Pending"},
        {"Match_Num": 71, "Date_Str": "Jun 27", "Home_Team": "Panama", "Away_Team": "England", "Home_Win_Odds": 8.5, "Draw_Odds": 4.6, "Away_Win_Odds": 1.38, "Actual_Result": "Pending"},
        {"Match_Num": 72, "Date_Str": "Jun 27", "Home_Team": "Croatia", "Away_Team": "Ghana", "Home_Win_Odds": 1.8, "Draw_Odds": 3.4, "Away_Win_Odds": 4.5, "Actual_Result": "Pending"}
    ]
    df = pd.DataFrame(raw_data)
    df = df.sort_values(by="Match_Num").reset_index(drop=True)
    df['Match_Display'] = "Match " + df['Match_Num'].astype(str) + " (" + df['Date_Str'] + "): " + df['Home_Team'] + " vs " + df['Away_Team']
    
    # Pre-parse text string dates into clean objects for drop-down calculation
    dates_list = []
    for idx, row in df.iterrows():
        try:
            dates_list.append(datetime.strptime(f"{row['Date_Str']} {year}", "%b %d %Y").date())
        except:
            dates_list.append(datetime.now().date())
    df['Match_Date_Obj'] = dates_list
    return df

match_data = get_match_data(current_year)

# Database syncing utilities
def load_bets_from_sheet():
    try:
        df = pd.read_csv(SHEET_URL)
        df.columns = [c.strip() for c in df.columns]
        df = df.fillna("")
        return df.to_dict(orient="records")
    except:
        return []

# Initialize state structures
if "current_page" not in st.session_state:
    st.session_state.current_page = "login"
if "player_name" not in st.session_state:
    st.session_state.player_name = ""
if "local_backup_bets" not in st.session_state:
    st.session_state.local_backup_bets = []

# Fetch active cloud database rows
all_bets = load_bets_from_sheet()
combined_bets = all_bets + st.session_state.local_backup_bets

# 📅 REAL-TIME AUTO-EXPIRY TRACKER FOR MAIN BOARD SHOWS
for bet in combined_bets:
    match_row = match_data[match_data['Match_Num'] == int(bet['Match_Num'])].iloc[0]
    if current_date.date() > match_row['Match_Date_Obj']:
        bet["Is_Expired"] = True

# INTERFACE SCREEN 1: LOGIN
if st.session_state.current_page == "login":
    st.title("⚽ Fit N 40 Match Prediction")
    st.subheader("Join the Prediction Tournament Lounge")
    
    player_input = st.text_input("Enter Profile Name:", placeholder="e.g., Ashu")
    
    if st.button("Enter Dashboard", use_container_width=True, type="primary"):
        cleaned_name = player_input.strip()
        if cleaned_name:
            st.session_state.player_name = cleaned_name
            st.session_state.current_page = "dashboard"
            st.rerun()
        else:
            st.warning("Please enter a valid profile name.")

# INTERFACE SCREEN 2: MAIN DASHBOARD
elif st.session_state.current_page == "dashboard":
    st.title("🏆 Fit N 40 Match Prediction")
    
    col_user, col_logout = st.columns([3, 1])
    with col_user:
        st.write(f"Logged in as: **{st.session_state.player_name}**")
    with col_logout:
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.player_name = ""
            st.session_state.current_page = "login"
            st.rerun()
    
    if st.button("➕ Create & Add a New Bet Offer", use_container_width=True, type="primary"):
        st.session_state.current_page = "new_bet"
        st.rerun()
        
    st.markdown("---")
    
    open_bets = [b for b in combined_bets if b["Status"] == "Open" and not b["Is_Expired"]]
    live_bets = [b for b in combined_bets if b["Status"] == "Matched" and not b["Is_Expired"]]
    expired_bets = [b for b in combined_bets if b["Is_Expired"]]
    
    # 1. Open Bets Section
    st.subheader("📋 1. Open Bets Available")
    if not open_bets:
        st.info("No active open bets to take right now. Click the button above to add one!")
    else:
        for bet in open_bets:
            with st.container(border=True):
                st.markdown(f"**{bet['Creator']}** predicts **{bet['Prediction']}** will win in *{bet['Match_Name']}*")
                st.write(f"💰 **Staked Points:** {bet['Points']} | 🎁 **Opponent Wins:** {bet['Opponent_Payout']} pts")
                
                if str(bet['Creator']).lower() == st.session_state.player_name.lower():
                    st.caption("🔒 You created this offer line")
                else:
                    if st.button(f"🤝 Match Bet Offer #{bet['Bet_ID']}", key=f"match_{bet['Bet_ID']}", use_container_width=True):
                        st.session_state.selected_bet_to_match = bet
                        st.session_state.current_page = "confirm_match"
                        st.rerun()

    st.markdown("---")
    
    # 2. Live Matched Bets Section
    st.subheader("🔥 2. Live Matched Bets (Locked)")
    if not live_bets:
        st.caption("No locked matched bets running currently.")
    else:
        for bet in live_bets:
            with st.container(border=True):
                st.markdown(f"🔒 **{bet['Creator']}** 🆚 **{bet['Opponent']}**")
                st.write(f"**Match:** {bet['Match_Name']} | **Prediction:** {bet['Creator']} chose *{bet['Prediction']}*")
                st.write(f"**Stakes:** Creator risks {bet['Points']} pts vs Opponent risks {bet['Opponent_Payout']} pts")

    st.markdown("---")
    
    # 3. Expired Bets Section
    st.subheader("🏁 3. Expired & Completed Bets")
    if not expired_bets:
        st.caption("No completed match history yet.")
    else:
        for bet in expired_bets:
            with st.container(border=True):
                st.write(f"🏆 **{bet['Match_Name']}**")
                match_info = match_data[match_data['Match_Num'] == int(bet['Match_Num'])].iloc[0]
                actual_outcome = match_info['Actual_Result']
                
                if bet['Status'] == "Open":
                    st.error("❌ **Bet Expired Unmatched**")
                else:
                    creator_won = (bet['Prediction'] == actual_outcome)
                    if creator_won:
                        winner, loser, points_won = bet['Creator'], bet['Opponent'], bet['Opponent_Payout']
                    else:
                        winner, loser, points_won = bet['Opponent'], bet['Creator'], bet['Points']
                    
                    if actual_outcome == "Pending":
                        st.warning(f"⏳ Match date reached! Awaiting official results input.")
                        st.write(f"**Stakes Set:** {bet['Creator']} vs {bet['Opponent']}")
                    else:
                        st.success(f"🎉 **{winner}** won **{points_won}** points from **{loser}**")

# INTERFACE SCREEN 3: CONFIRM MATCH
elif st.session_state.current_page == "confirm_match":
    bet = st.session_state.selected_bet_to_match
    st.title("🤝 Confirm Your Match")
    
    with st.container(border=True):
        st.write(f"**Bet Creator:** {bet['Creator']}")
        st.write(f"**Match Event:** {bet['Match_Name']}")
        st.write(f"**Their Prediction:** {bet['Prediction']}")
        st.markdown("---")
        st.write(f"🔴 If **{bet['Prediction']}** wins, you lose **{bet['Opponent_Payout']}** points.")
        st.write(f"🟢 If any other result occurs, you win **{bet['Points']}** points.")
        
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Confirm Bet", use_container_width=True, type="primary"):
            for b in st.session_state.local_backup_bets:
                if b["Bet_ID"] == bet["Bet_ID"]:
                    b["Status"] = "Matched"
                    b["Opponent"] = st.session_state.player_name
            st.success("Bet locked in successfully!")
            st.session_state.current_page = "dashboard"
            st.rerun()
    with col2:
        if st.button("❌ Cancel", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()

# INTERFACE SCREEN 4: ADD NEW BET OFFERS
elif st.session_state.current_page == "new_bet":
    st.title("🎲 Put Down a New Bet Offer")
    
    # 📅 REQ UPDATE: Filter out past entries from dropdown display selection lists
    active_matches = match_data[match_data['Match_Date_Obj'] >= current_date.date()]
    match_options = active_matches['Match_Display'].tolist()
    
    selected_match_str = st.selectbox("👉 Group Match:", options=["-- Select League Match --"] + match_options)
    
    if selected_match_str != "-- Select League Match --":
        match_row = match_data[match_data['Match_Display'] == selected_match_str].iloc[0]
        home = match_row['Home_Team']
        away = match_row['Away_Team']
        
        prediction_options = [home, away, "Draw"]
        selected_prediction = st.selectbox("🔮 Predicted Winner Team:", options=["-- Choose Outcome --"] + prediction_options)
        
        if selected_prediction != "-- Choose Outcome --":
            points_to_bet = st.number_input("💰 Points to Bet:", min_value=1, max_value=5000, value=100, step=10)
            
            if selected_prediction == home:
                odds = float(match_row['Home_Win_Odds'])
            elif selected_prediction == away:
                odds = float(match_row['Away_Win_Odds'])
            else:
                odds = float(match_row['Draw_Odds'])
                
            opponent_payout = round(points_to_bet * (odds - 1), 2)
            st.metric(label="🎁 Opposing Bettor Payout (if you lose):", value=f"{opponent_payout} pts")
            
            if st.button("🚀 Submit Bet to Dashboard", use_container_width=True, type="primary"):
                next_id = len(combined_bets) + 1
                new_bet_entry = {
                    "Bet_ID": next_id,
                    "Creator": st.session_state.player_name,
                    "Match_Num": int(match_row['Match_Num']),
                    "Match_Name": f"{home} vs {away}",
                    "Prediction": selected_prediction,
                    "Points": points_to_bet,
                    "Opponent_Payout": opponent_payout,
                    "Opponent": "",
                    "Status": "Open",
                    "Is_Expired": False
                }
                st.session_state.local_backup_bets.append(new_bet_entry)
                st.session_state.current_page = "dashboard"
                st.rerun()
                
    if st.button("⬅ Cancel & Back", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()
