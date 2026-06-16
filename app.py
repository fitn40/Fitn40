import streamlit as st
import pandas as pd
from datetime import datetime

# Page Branding Setup
st.set_page_config(page_title="Fit N 40 Match Prediction", page_icon="⚽", layout="centered")

# --- CONFIGURATION HUB ---
# Paste your public viewable Google Sheet link right here inside the quotation marks:
GOOGLE_SHEET_LINK = "https://docs.google.com/spreadsheets/d/10dSFKVVfOpPaRKut3au0FWfjWt3po530YdgmSstd6os/pubhtml"
# -------------------------

current_date = datetime.now()
current_year = current_date.year

# Fallback Local 72-Match Matrix Data for placing new bets
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
        {"Match_Num": 49, "Date_Str": "Jun 24", "Home_Team": "Czechia", "Away_Team": "Mexico", "Home_Win_Odds": 3.8, "Draw_Odds": 3.4, "Away_Win_Odds": 2.0},
        {"Match_Num": 50, "Date_Str": "Jun 24", "Home_Team": "South Africa", "Away_Team": "Korea Republic", "Home_Win_Odds": 3.2, "Draw_Odds": 3.3, "Away_Win_Odds": 2.3},
        {"Match_Num": 51, "Date_Str": "Jun 24", "Home_Team": "Switzerland", "Away_Team": "Canada", "Home_Win_Odds": 2.4, "Draw_Odds": 3.2, "Away_Win_Odds": 3.0},
        {"Match_Num": 52, "Date_Str": "Jun 24", "Home_Team": "Bosnia & Herz.", "Away_Team": "Qatar", "Home_Win_Odds": 1.9, "Draw_Odds": 3.3, "Away_Win_Odds": 4.2},
        {"Match_Num": 53, "Date_Str": "Jun 24", "Home_Team": "Scotland", "Away_Team": "Brazil", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.55},
        {"Match_Num": 54, "Date_Str": "Jun 24", "Home_Team": "Morocco", "Away_Team": "Haiti", "Home_Win_Odds": 1.4, "Draw_Odds": 4.5, "Away_Win_Odds": 8.0},
        {"Match_Num": 55, "Date_Str": "Jun 25", "Home_Team": "Türkiye", "Away_Team": "USA", "Home_Win_Odds": 4.0, "Draw_Odds": 3.5, "Away_Win_Odds": 1.95},
        {"Match_Num": 56, "Date_Str": "Jun 25", "Home_Team": "Paraguay", "Away_Team": "Australia", "Home_Win_Odds": 2.7, "Draw_Odds": 3.2, "Away_Win_Odds": 2.7},
        {"Match_Num": 57, "Date_Str": "Jun 25", "Home_Team": "Curaçao", "Away_Team": "Côte d'Ivoire", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.6},
        {"Match_Num": 58, "Date_Str": "Jun 25", "Home_Team": "Ecuador", "Away_Team": "Germany", "Home_Win_Odds": 5.0, "Draw_Odds": 3.8, "Away_Win_Odds": 1.7},
        {"Match_Num": 59, "Date_Str": "Jun 25", "Home_Team": "Japan", "Away_Team": "Sweden", "Home_Win_Odds": 2.6, "Draw_Odds": 3.2, "Away_Win_Odds": 2.8},
        {"Match_Num": 60, "Date_Str": "Jun 25", "Home_Team": "Tunisia", "Away_Team": "Netherlands", "Home_Win_Odds": 5.5, "Draw_Odds": 3.8, "Away_Win_Odds": 1.65},
        {"Match_Num": 61, "Date_Str": "Jun 26", "Home_Team": "Egypt", "Away_Team": "IR Iran", "Home_Win_Odds": 2.5, "Draw_Odds": 3.2, "Away_Win_Odds": 2.9},
        {"Match_Num": 62, "Date_Str": "Jun 26", "Home_Team": "New Zealand", "Away_Team": "Belgium", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.55},
        {"Match_Num": 63, "Date_Str": "Jun 26", "Home_Team": "Cabo Verde", "Away_Team": "Saudi Arabia", "Home_Win_Odds": 3.2, "Draw_Odds": 3.2, "Away_Win_Odds": 2.3},
        {"Match_Num": 64, "Date_Str": "Jun 26", "Home_Team": "Uruguay", "Away_Team": "Spain", "Home_Win_Odds": 5.0, "Draw_Odds": 3.8, "Away_Win_Odds": 1.7},
        {"Match_Num": 65, "Date_Str": "Jun 26", "Home_Team": "Norway", "Away_Team": "France", "Home_Win_Odds": 5.5, "Draw_Odds": 4.0, "Away_Win_Odds": 1.6},
        {"Match_Num": 66, "Date_Str": "Jun 26", "Home_Team": "Senegal", "Away_Team": "Iraq", "Home_Win_Odds": 1.7, "Draw_Odds": 3.5, "Away_Win_Odds": 5.0},
        {"Match_Num": 67, "Date_Str": "Jun 27", "Home_Team": "Algeria", "Away_Team": "Austria", "Home_Win_Odds": 2.9, "Draw_Odds": 3.2, "Away_Win_Odds": 2.5},
        {"Match_Num": 68, "Date_Str": "Jun 27", "Home_Team": "Jordan", "Away_Team": "Argentina", "Home_Win_Odds": 12.0, "Draw_Odds": 6.5, "Away_Win_Odds": 1.25},
        {"Match_Num": 69, "Date_Str": "Jun 27", "Home_Team": "Colombia", "Away_Team": "Portugal", "Home_Win_Odds": 3.6, "Draw_Odds": 3.2, "Away_Win_Odds": 2.1},
        {"Match_Num": 70, "Date_Str": "Jun 27", "Home_Team": "Congo DR", "Away_Team": "Uzbekistan", "Home_Win_Odds": 2.0, "Draw_Odds": 3.3, "Away_Win_Odds": 3.8},
        {"Match_Num": 71, "Date_Str": "Jun 27", "Home_Team": "Panama", "Away_Team": "England", "Home_Win_Odds": 8.0, "Draw_Odds": 5.5, "Away_Win_Odds": 1.38},
        {"Match_Num": 72, "Date_Str": "Jun 27", "Home_Team": "Croatia", "Away_Team": "Ghana", "Home_Win_Odds": 2.1, "Draw_Odds": 3.3, "Away_Win_Odds": 3.5}
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

# 🛑 PERSISTENT STREAMLIT RUNTIME MEMORY REPOSITORIES (Resets ONLY on a fresh code commit)
if "internal_bets_db" not in st.session_state:
    st.session_state.internal_bets_db = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "login"
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

# Auto Navigation configurations
if "user" in st.query_params and st.session_state.player_name == "":
    st.session_state.player_name = st.query_params["user"].strip()
    st.session_state.current_page = "dashboard"

# Auto Expiry Calculator Hook
for bet in st.session_state.internal_bets_db:
    try:
        m_lookup = match_data[match_data['Match_Num'] == int(bet['Match_Num'])]
        if not m_lookup.empty:
            bet["Is_Expired"] = current_date.date() > m_lookup.iloc[0]['Match_Date_Obj']
    except:
        bet["Is_Expired"] = False

is_admin = (st.session_state.player_name == "Fifa@2026")

# UI SCREEN 1: LOGIN LOUNGE
if st.session_state.current_page == "login":
    st.title("⚽ Fit N 40 Match Prediction")
    st.subheader("Welcome to the Arena")
    player_input = st.text_input("Profile Handle Name:")
    if st.button("Enter Dashboard", use_container_width=True, type="primary"):
        if player_input.strip():
            st.session_state.player_name = player_input.strip()
            st.query_params["user"] = player_input.strip()
            st.session_state.current_page = "dashboard"
            st.rerun()

# UI SCREEN 2: MAIN USER APP INTERFACE
elif st.session_state.current_page == "dashboard":
    st.title("🏆 Fit N 40 Dashboard")
    st.write(f"Logged in as: **{st.session_state.player_name}**")
    
       # Navigation Layer Blocks (With Added Logout Button)
    if is_admin:
        col_n1, col_n2, col_n3, col_n4 = st.columns(4)
    else:
        col_n1, col_n2, col_n4 = st.columns([1, 1, 1]) # Standard 3-column layout for players

    with col_n1:
        if st.button("➕ Open New Bet", use_container_width=True, type="primary"):
            st.session_state.current_page = "new_bet"
            st.rerun()
    with col_n2:
        if st.button("📊 Tournament Info", use_container_width=True):
            st.session_state.current_page = "view_excel"
            st.rerun()
    if is_admin:
        with col_n3:
            if st.button("⚙️ Dev Storage", use_container_width=True):
                st.session_state.current_page = "view_db"
                st.rerun()
    with col_n4:
        if st.button("🚪 Logout", use_container_width=True):
            # Clear out the session state completely to return to login screen safely
            st.session_state.player_name = ""
            st.query_params.clear()
            st.session_state.current_page = "login"
            st.rerun()

            
    st.markdown("---")
    
    open_bets = [b for b in st.session_state.internal_bets_db if b.get("Status", "Open") == "Open" and not b.get("Is_Expired", False)]
    live_bets = [b for b in st.session_state.internal_bets_db if b.get("Status") == "Matched" and not b.get("Is_Expired", False)]
    expired_bets = [b for b in st.session_state.internal_bets_db if b.get("Is_Expired", False)]

    # 1. Unmatched Open Block
    st.subheader("📋 1. Active Open Offers")
    if not open_bets:
        st.info("No open offers available.")
    else:
        for bet in open_bets:
            with st.container(border=True):
                st.markdown(f"🗓️ **Match Date:** {bet.get('Match_Date')} | **{bet.get('Creator')}** backs **{bet.get('Prediction')}**")
                st.caption(f"Fixture: {bet.get('Match_Name')} | Stakes: {bet.get('Points')} pts vs {bet.get('Opponent_Payout')} pts")
                if bet.get('Creator').lower() != st.session_state.player_name.lower():
                    if st.button(f"🤝 Match Offer #{bet.get('Bet_ID')}", key=f"m_{bet.get('Bet_ID')}", use_container_width=True):
                        st.session_state.selected_bet_to_match = bet
                        st.session_state.current_page = "confirm_match"
                        st.rerun()

    # 2. Live Matched Locked Block
    st.subheader("🔥 2. Live Matched Bets (Locked)")
    if not live_bets:
        st.caption("No matched transactions are locked right now.")
    else:
        for bet in live_bets:
            with st.container(border=True):
                st.markdown(f"🔒 **{bet.get('Creator')}** 🆚 **{bet.get('Opponent')}**")
                st.write(f"📅 **Kickoff Date:** {bet.get('Match_Date')} | **Match:** {bet.get('Match_Name')}")
                                # Pull the actual points allocated for the creator and opponent
                risk_pts = bet.get('Points', 100)
                win_pts = bet.get('Opponent_Payout', 55)

                st.write(f"📢 **{bet.get('Creator')}** bet on **{bet.get('Prediction')}** (Risking: {risk_pts} pts / Winning: {win_pts} pts) with **{bet.get('Opponent')}**.")

    # 3. Memory Closed Entries
    st.subheader("🏁 3. Past Bets")
    if not expired_bets:
        st.caption("No historical logs recorded inside this memory instance.")
    else:
        for bet in expired_bets:
            with st.container(border=True):
                st.write(f"🏆 **{bet.get('Match_Name')}** (Played: {bet.get('Match_Date')})")
                if bet.get("Status") == "Open":
                    st.error("❌ Expired Unmatched")
                else:
                    st.warning(f"⏳ Match time crossed. Please check the 'Live Excel Board' to see who won this fixture!")

# 🆕 THE UNTOUCHABLE GOOGLE SHEET EMBED SCREEN PAGE (REMOVED LINK)
elif st.session_state.current_page == "view_excel":
    st.title("📊 Tournament Board")
    st.info("The results board is currently offline. Please check your WhatsApp group for updates!")
            
    if st.button("⬅ Back to Dashboard", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()



# UI SCREEN: CONFIRM TO MATCH OFFER
elif st.session_state.current_page == "confirm_match":
    bet = st.session_state.selected_bet_to_match
    st.title("🤝 Lock Match Confirmation")
    st.write(f"Accepting **{bet.get('Creator')}**'s bet on **{bet.get('Match_Name')}** ({bet.get('Match_Date')})")
    if st.button("✅ Confirm & Lock Bet", use_container_width=True, type="primary"):
        for b in st.session_state.internal_bets_db:
            if b["Bet_ID"] == bet["Bet_ID"]:
                b["Status"] = "Matched"
                b["Opponent"] = st.session_state.player_name
        st.session_state.current_page = "dashboard"
        st.rerun()
    if st.button("⬅ Cancel", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()

# UI SCREEN: PLACE OFFERS
elif st.session_state.current_page == "new_bet":
    st.title("🎲 Create New Prediction Offer")
    active_fixtures = match_data[match_data['Match_Date_Obj'] >= current_date.date()]
    selected_match_str = st.selectbox("👉 Target Match Fixture:", options=["-- Select --"] + active_fixtures['Match_Display'].tolist())
    
    if selected_match_str != "-- Select --":
        match_row = match_data[match_data['Match_Display'] == selected_match_str].iloc[0]
        selected_prediction = st.selectbox("🔮 Outcome Selection:", options=["-- Select --", match_row['Home_Team'], match_row['Away_Team'], "Draw"])
        
        if selected_prediction != "-- Select --":
            points = st.number_input("💰 Points Risk Stake Allocation:", min_value=1, value=100)
            odds = float(match_row['Home_Win_Odds'] if selected_prediction == match_row['Home_Team'] else (match_row['Away_Win_Odds'] if selected_prediction == match_row['Away_Team'] else match_row['Draw_Odds']))
            payout = round(points * (odds - 1), 2)
            st.metric("Opponent Must Risk Allocation:", f"{payout} pts")
            
            if st.button("🚀 Publish Offer to Board", use_container_width=True, type="primary"):
                next_id = 1 if not st.session_state.internal_bets_db else max([b["Bet_ID"] for b in st.session_state.internal_bets_db]) + 1
                st.session_state.internal_bets_db.append({
                    "Bet_ID": next_id, "Creator": st.session_state.player_name, "Match_Num": int(match_row['Match_Num']),
                    "Match_Name": f"{match_row['Home_Team']} vs {match_row['Away_Team']}", "Match_Date": str(match_row['Date_Str']),
                    "Prediction": selected_prediction, "Points": points, "Opponent_Payout": payout, "Opponent": "", "Status": "Open", "Is_Expired": False
                })
                st.session_state.current_page = "dashboard"
                st.rerun()
                
    if st.button("⬅ Cancel", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()

# DEV INTERNAL LOOKOVER STORAGE MATRIX 
elif st.session_state.current_page == "view_db":
    st.title("📊 Running Memory Dump Instance")
    st.dataframe(pd.DataFrame(st.session_state.internal_bets_db), use_container_width=True, hide_index=True)
    if st.button("⬅ Back", use_container_width=True):
        st.session_state.current_page = "dashboard"
        st.rerun()
