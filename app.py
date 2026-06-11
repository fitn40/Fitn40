import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Branding
st.set_page_config(page_title="Fit N 40 Match Prediction", page_icon="⚽", layout="centered")

DATA_FILE = "data.csv"
current_date = datetime.now()
current_year = current_date.year

# Re-engineered Data Matrix: Pulled directly line-by-line from your exact attached CSV sheet
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
        {"Match_Num": 62, "Date_Str": "Jun 26", "Home_Team": "New Zealand", "Away_Team": "Belgium", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.55, "Actual_Result": "Pending"},
        {"Match_Num": 63, "Date_Str": "Jun 26", "Home_Team": "Cabo Verde", "Away_Team": "Saudi Arabia", "Home_Win_Odds": 3.2, "Draw_Odds": 3.2, "Away_Win_Odds": 2.3, "Actual_Result": "Pending"},
        {"Match_Num": 64, "Date_Str": "Jun 26", "Home_Team": "Uruguay", "Away_Team": "Spain", "Home_Win_Odds": 5.0, "Draw_Odds": 3.8, "Away_Win_Odds": 1.7, "Actual_Result": "Pending"},
        {"Match_Num": 65, "Date_Str": "Jun 26", "Home_Team": "Norway", "Away_Team": "France", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.6, "Actual_Result": "Pending"},
        {"Match_Num": 66, "Date_Str": "Jun 26", "Home_Team": "Senegal", "Away_Team": "Iraq", "Home_Win_Odds": 1.7, "Draw_Odds": 3.5, "Away_Win_Odds": 5.0, "Actual_Result": "Pending"},
        {"Match_Num": 67, "Date_Str": "Jun 27", "Home_Team": "Algeria", "Away_Team": "Austria", "Home_Win_Odds": 2.9, "Draw_Odds": 3.2, "Away_Win_Odds": 2.5, "Actual_Result": "Pending"},
        {"Match_Num": 68, "Date_Str": "Jun 27", "Home_Team": "Jordan", "Away_Team": "Argentina", "Home_Win_Odds": 12.0, "Draw_Odds": 6.5, "Away_Win_Odds": 1.25, "Actual_Result": "Pending"},
        {"Match_Num": 69, "Date_Str": "Jun 27", "Home_Team": "Colombia", "Away_Team": "Portugal", "Home_Win_Odds": 3.6, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1, "Actual_Result": "Pending"},
        {"Match_Num": 70, "Date_Str": "Jun 27", "Home_Team": "Congo DR", "Away_Team": "Uzbekistan", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8, "Actual_Result": "Pending"},
        {"Match_Num": 71, "Date_Str": "Jun 27", "Home_Team": "Panama", "Away_Team": "England", "Home_Win_Odds": 8.0, "Draw_Odds": 5.5, "Away_Win_Odds": 1.38, "Actual_Result": "Pending"},
        {"Match_Num": 72, "Date_Str": "Jun 27", "Home_Team": "Croatia", "Away_Team": "Ghana", "Home_Win_Odds": 2.1, "Draw_Odds": 3.3, "Away_Win_Odds": 3.5, "Actual_Result": "Pending"}
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

# File Handlers
def load_permanent_bets():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        df = pd.read_csv(DATA_FILE)
        df = df.fillna("")
        return df.to_dict(orient="records")
    except:
        return []

def save_all_bets_permanently(bets_list):
    if len(bets_list) == 0:
        df = pd.DataFrame(columns=["Bet_ID","Creator","Match_Num","Match_Name","Prediction","Points","Opponent_Payout","Opponent","Status","Is_Expired"])
    else:
        df = pd.DataFrame(bets_list)
    df.to_csv(DATA_FILE, index=False)

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

combined_bets = load_permanent_bets()

# Date Expiry Logic Engine
for bet in combined_bets:
    try:
        m_num = int(float(str(bet.get('Match_Num', 1)).strip()))
        match_lookup = match_data[match_data['Match_Num'] == m_num]
        if not match_lookup.empty:
            match_row = match_lookup.iloc[0]
            if current_date.date() > match_row['Match_Date_Obj']:
                bet["Is_Expired"] = True
            else:
                bet["Is_Expired"] = (str(bet.get("Is_Expired")).strip().lower() in ["true", "1"])
    except:
        bet["Is_Expired"] = False

# UI SCREEN 1: LOGIN
if st.session_state.current_page == "login":
    st.title("⚽ Fit N 40 Match Prediction")
    st.subheader("Join the Prediction Tournament Lounge")
    
    player_input = st.text_input("Enter Profile Name:", placeholder="e.g., Messi")
    
    if st.button("Enter Dashboard", use_container_width=True, type="primary"):
        cleaned_name = player_input.strip()
        if cleaned_name:
            st.session_state.player_name = cleaned_name
            st.session_state.current_page = "dashboard"
            st.rerun()

# UI SCREEN 2: DASHBOARD
elif st.session_state.current_page == "dashboard":
    st.title("🏆 Fit N 40 Match Prediction")
    st.write(f"Logged in as: **{st.session_state.player_name}**")
    
    if st.button("➕ Create & Add a New Bet Offer", use_container_width=True, type="primary"):
        st.session_state.current_page = "new_bet"
        st.rerun()
        
    st.markdown("---")
    
    open_bets = [b for b in combined_bets if str(b.get("Status", "Open")).strip().lower() == "open" and not b.get("Is_Expired", False)]
    live_bets = [b for b in combined_bets if str(b.get("Status", "")).strip().lower() == "matched" and not b.get("Is_Expired", False)]
    expired_bets = [b for b in combined_bets if b.get("Is_Expired", False)]
    
    is_admin = (st.session_state.player_name.lower() == "ashu")

    # 1. Open Bets Section
    st.subheader("📋 1. Open Bets Available")
    if not open_bets:
        st.info("No active open bets available.")
    else:
        for bet in open_bets:
            with st.container(border=True):
                st.markdown(f"**{bet.get('Creator')}** predicts **{bet.get('Prediction')}** in *{bet.get('Match_Name')}*")
                st.write(f"💰 Staked: {bet.get('Points')} | 🎁 Opponent Wins: {bet.get('Opponent_Payout')} pts")
                
                if str(bet.get('Creator', '')).lower() == st.session_state.player_name.lower():
                    st.caption("🔒 You created this offer")
                else:
                    if st.button(f"🤝 Match Bet #{bet.get('Bet_ID')}", key=f"match_{bet.get('Bet_ID')}", use_container_width=True):
                        st.session_state.selected_bet_to_match = bet
                        st.session_state.current_page = "confirm_match"
                        st.rerun()
                
                if is_admin or str(bet.get('Creator', '')).lower() == st.session_state.player_name.lower():
                    if st.button(f"🗑️ Delete Bet Offer #{bet.get('Bet_ID')}", key=f"del_open_{bet.get('Bet_ID')}", type="secondary", use_container_width=True):
                        updated_list = [b for b in combined_bets if int(b["Bet_ID"]) != int(bet["Bet_ID"])]
                        save_all_bets_permanently(updated_list)
                        st.toast(f"Bet Offer #{bet.get('Bet_ID')} removed selectively!", icon="🗑️")
                        st.rerun()

    st.markdown("---")
    
    # 2. Live Matched Bets Section
    st.subheader("🔥 2. Live Matched Bets (Locked)")
    if not live_bets:
        st.caption("No locked matched bets running currently.")
    else:
        for bet in live_bets:
            with st.container(border=True):
                st.markdown(f"🔒 **{bet.get('Creator')}** 🆚 **{bet.get('Opponent')}**")
                st.write(f"**Match:** {bet.get('Match_Name')} | **Prediction:** {bet.get('Creator')} chose *{bet.get('Prediction')}*")
                st.write(f"**Stakes:** Risking {bet.get('Points')} pts vs {bet.get('Opponent_Payout')} pts")
                
                if is_admin:
                    if st.button(f"🗑️ Delete Live Bet #{bet.get('Bet_ID')}", key=f"del_live_{bet.get('Bet_ID')}", type="secondary", use_container_width=True):
                        updated_list = [b for b in combined_bets if int(b["Bet_ID"]) != int(bet["Bet_ID"])]
                        save_all_bets_permanently(updated_list)
                        st.toast(f"Live Bet #{bet.get('Bet_ID')} deleted!", icon="🗑️")
                        st.rerun()

    st.markdown("---")
    
    # 3. Expired Bets Section
    st.subheader("🏁 3. Expired & Completed Bets")
    if not expired_bets:
        st.caption("No completed match history yet.")
    else:
        for bet in expired_bets:
            with st.container(border=True):
                st.write(f"🏆 **{bet.get('Match_Name')}**")
                if str(bet.get('Status', 'Open')).strip().lower() == "open":
                    st.error("❌ **Bet Expired Unmatched**")
                else:
                    st.success(f"🎉 Match date closed. Payout tracked between {bet.get('Creator')} and {bet.get('Opponent')}")
                
                if is_admin:
                    if st.button(f"🗑️ Purge Archive Entry #{bet.get('Bet_ID')}", key=f"del_exp_{bet.get('Bet_ID')}", type="secondary", use_container_width=True):
                        updated_list = [b for b in combined_bets if int(b["Bet_ID"]) != int(bet["Bet_ID"])]
                        save_all_bets_permanently(updated_list)
                        st.toast("Archive logs updated!", icon="🗑️")
                        st.rerun()

# UI SCREEN 3: CONFIRM MATCH
elif st.session_state.current_page == "confirm_match":
    bet = st.session_state.selected_bet_to_match
    st.title("🤝 Confirm Your Match")
    
    with st.container(border=True):
        st.write(f"**Bet Creator:** {bet.get('Creator')}")
        st.write(f"**Match Event:** {bet.get('Match_Name')}")
        st.write(f"**Their Prediction:** {bet.get('Prediction')}")
        st.markdown("---")
        st.write(f"🔴 If **{bet.get('Prediction')}** wins, you lose **{bet.get('Opponent_Payout')}** points.")
        st.write(f"🟢 If any other result occurs, you win **{bet.get('Points')}** points.")
        
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Confirm Bet", use_container_width=True, type="primary"):
            for b in combined_bets:
                if int(b["Bet_ID"]) == int(bet["Bet_ID"]):
                    b["Status"] = "Matched"
                    b["Opponent"] = st.session_state.player_name
            save_all_bets_permanently(combined_bets)
            st.success("Bet matched permanently!")
            st.session_state.current_page = "dashboard"
            st.rerun()
    with col2:
        if st.button("❌ Cancel", use_container_width=True):
            st.session_state.current_page = "dashboard"
            st.rerun()

# UI SCREEN 4: NEW BETS
elif st.session_state.current_page == "new_bet":
    st.title("🎲 Put Down a New Bet Offer")
    
    active_matches = match_data[match_data['Match_Date_Obj'] >= current_date.date()]
    match_options = active_matches['Match_Display'].tolist()
    selected_match_str = st.selectbox("👉 Group Match:", options=["-- Select League Match --"] + match_options)
    
    if selected_match_str != "-- Select League Match --":
        match_row = match_data[match_data['Match_Display'] == selected_match_str].iloc[0]
        prediction_options = [match_row['Home_Team'], match_row['Away_Team'], "Draw"]
        selected_prediction = st.selectbox("🔮 Predicted Winner Team:", options=["-- Choose Outcome --"] + prediction_options)
        
        if selected_prediction != "-- Choose Outcome --":
            points_to_bet = st.number_input("💰 Points to Bet:", min_value=1, max_value=5000, value=100, step=10)
            
            if selected_prediction == match_row['Home_Team']:
                odds = float(match_row['Home_Win_Odds'])
            elif selected_prediction == match_row['Away_Team']:
                odds = float(match_row['Away_Win_Odds'])
            else:
                odds = float(match_row['Draw_Odds'])
                
            opponent_payout = round(points_to_bet * (odds - 1), 2)
            st.metric(label="🎁 Opposing Bettor Payout (if you lose):", value=f"{opponent_payout} pts")
            
            if st.button("🚀 Submit Bet to Dashboard", use_container_width=True, type="primary"):
                next_id = 1 if len(combined_bets) == 0 else max([int(b.get("Bet_ID", 0)) for b in combined_bets]) + 1
                
                new_bet_entry = {
                    "Bet_ID": next_id,
                    "Creator": st.session_state.player_name,
                    "Match_Num": int(match_row['Match_Num']),
                    "Match_Name": f"{match_row['Home_Team']} vs {match_row['Away_Team']}",
                    "Prediction": selected_prediction,
                    "Points": points_to_bet,
                    "Opponent_Payout": opponent_payout,
                    "Opponent": "",
                    "Status": "Open",
                    "Is_Expired": False
                }
                combined_bets.append(new_bet_entry)
                save_all_bets_permanently(combined_bets)
                
                st.success("Bet registered permanently!")
                st.session_state.current_page = "dashboard"
                st.rerun()
                
    if st.button("⬅ Cancel & Back", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()
