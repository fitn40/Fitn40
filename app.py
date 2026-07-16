import streamlit as st
import pandas as pd
import os
from datetime import datetime
from github import Github

# Page Branding Setup
st.set_page_config(page_title="FIFA WC Prediction", page_icon="⚽", layout="centered")

DATA_FILE = "data.csv"
current_date = datetime.now()
current_year = current_date.year

# 📋 Official Live Tournament Data Matrix (Finals Stage & Specialized Player/Match Props)
@st.cache_data
def get_match_data(year):
    raw_data = [
        # --- ⏳ PREVIOUSLY EXPIRED KNOCKOUT FIXTURES ---
        {"Match_Num": 101, "Date_Str": "Jul 15", "Home_Team": "France", "Away_Team": "Spain", "Home_Win_Odds": 1.85, "Draw_Odds": None, "Away_Win_Odds": 1.95, "Time_Str": "01:30"},
        {"Match_Num": 102, "Date_Str": "Jul 16", "Home_Team": "England", "Away_Team": "Argentina", "Home_Win_Odds": 2.10, "Draw_Odds": None, "Away_Win_Odds": 1.72, "Time_Str": "01:30"},

        # --- 🥉 THIRD PLACE PLAYOFF (2-WAY OUTRIGHT TO WIN BRONZE) ---
        {"Match_Num": 103, "Date_Str": "Jul 18", "Home_Team": "Spain", "Away_Team": "England", "Home_Win_Odds": 1.75, "Draw_Odds": None, "Away_Win_Odds": 2.10, "Time_Str": "21:30"},

        # --- 🏆 WORLD CUP FINAL (2-WAY MARKET TO LIFT THE TROPHY) ---
        {"Match_Num": 104, "Date_Str": "Jul 20", "Home_Team": "France", "Away_Team": "Argentina", "Home_Win_Odds": 1.80, "Draw_Odds": None, "Away_Win_Odds": 2.00, "Time_Str": "04:30"},

        # --- 🎯 SPECIALIZED PLAYER & MATCH PROPS (YES-ONLY CUSTOM OUTRIGHT STRUCTURES) ---
        {"Match_Num": 801, "Date_Str": "Jul 20", "Home_Team": "Lionel Messi NOT to score a goal (Final)", "Away_Team": "Field", "Home_Win_Odds": 1.65, "Draw_Odds": None, "Away_Win_Odds": 2.20, "Time_Str": "04:30"},
        {"Match_Num": 802, "Date_Str": "Jul 20", "Home_Team": "Goalless match (0-0) in Regulation Time (Final)", "Away_Team": "Field", "Home_Win_Odds": 8.50, "Draw_Odds": None, "Away_Win_Odds": 1.07, "Time_Str": "04:30"},
        {"Match_Num": 803, "Date_Str": "Jul 20", "Home_Team": "Kylian Mbappe to score a Hat-trick (Final)", "Away_Team": "Field", "Home_Win_Odds": 15.00, "Draw_Odds": None, "Away_Win_Odds": 1.02, "Time_Str": "04:30"},
        {"Match_Num": 804, "Date_Str": "Jul 20", "Home_Team": "Match to be decided on Penalty Shootout (Final)", "Away_Team": "Field", "Home_Win_Odds": 4.50, "Draw_Odds": None, "Away_Win_Odds": 1.22, "Time_Str": "04:30"},

        # --- 🏆 INDIVIDUAL TOURNAMENT WINNER SELECTION MARKETS (MATCHES 901-904) ---
        {"Match_Num": 901, "Date_Str": "Jul 20", "Home_Team": "France to win WC", "Away_Team": "Field", "Home_Win_Odds": 2.20, "Draw_Odds": None, "Away_Win_Odds": 1.65, "Time_Str": "04:30"},
        {"Match_Num": 902, "Date_Str": "Jul 20", "Home_Team": "Spain to win WC", "Away_Team": "Field", "Home_Win_Odds": 3.50, "Draw_Odds": None, "Away_Win_Odds": 1.30, "Time_Str": "04:30"},
        {"Match_Num": 903, "Date_Str": "Jul 20", "Home_Team": "Argentina to win WC", "Away_Team": "Field", "Home_Win_Odds": 3.80, "Draw_Odds": None, "Away_Win_Odds": 1.25, "Time_Str": "04:30"},
        {"Match_Num": 904, "Date_Str": "Jul 20", "Home_Team": "England to win WC", "Away_Team": "Field", "Home_Win_Odds": 6.00, "Draw_Odds": None, "Away_Win_Odds": 1.12, "Time_Str": "04:30"},

        # --- 🥇 INDIVIDUAL GOLDEN BOOT SELECTION MARKETS (MATCHES 1001-1005) ---
        {"Match_Num": 1001, "Date_Str": "Jul 20", "Home_Team": "Kylian Mbappe for Golden Boot", "Away_Team": "Field", "Home_Win_Odds": 1.85, "Draw_Odds": None, "Away_Win_Odds": 1.95, "Time_Str": "04:30"},
        {"Match_Num": 1002, "Date_Str": "Jul 20", "Home_Team": "Lionel Messi for Golden Boot", "Away_Team": "Field", "Home_Win_Odds": 2.10, "Draw_Odds": None, "Away_Win_Odds": 1.72, "Time_Str": "04:30"},
        {"Match_Num": 1004, "Date_Str": "Jul 20", "Home_Team": "Harry Kane for Golden Boot", "Away_Team": "Field", "Home_Win_Odds": 9.50, "Draw_Odds": None, "Away_Win_Odds": 1.05, "Time_Str": "04:30"},
        {"Match_Num": 1005, "Date_Str": "Jul 20", "Home_Team": "Jude Bellingham for Golden Boot", "Away_Team": "Field", "Home_Win_Odds": 12.00, "Draw_Odds": None, "Away_Win_Odds": 1.03, "Time_Str": "04:30"}
    ]
    df = pd.DataFrame(raw_data)
    df = df.sort_values(by="Match_Num").reset_index(drop=True)
    
    display_titles = []
    for idx, row in df.iterrows():
        n = row['Match_Num']
        if 801 <= n <= 899:
            display_titles.append(f"🎯 Prop: {row['Home_Team'].split(' (')[0]}")
        elif 901 <= n <= 904:
            display_titles.append(f"🏆 WC Winner: {row['Home_Team'].split(' to ')[0]}")
        elif 1001 <= n <= 1005:
            display_titles.append(f"🥇 Golden Boot: {row['Home_Team'].split(' for ')[0]}")
        elif n == 103:
            display_titles.append(f"🥉 3rd Place Playoff ({row['Date_Str']}): {row['Home_Team']} vs {row['Away_Team']}")
        elif n == 104:
            display_titles.append(f"🏆 World Cup Final ({row['Date_Str']}): {row['Home_Team']} vs {row['Away_Team']}")
        else:
            display_titles.append(f"Match {n} ({row['Date_Str']}): {row['Home_Team']} vs {row['Away_Team']}")
            
    df['Match_Display'] = display_titles
    
    dates_list = []
    for idx, row in df.iterrows():
        try:
            clean_date_str = " ".join(row['Date_Str'].split())
            time_part = row.get('Time_Str', '00:00')
            dates_list.append(datetime.strptime(f"{clean_date_str} {year} {time_part}", "%b %d %Y %H:%M"))
        except:
            dates_list.append(datetime(2000, 1, 1, 0, 0))
    df['Match_Date_Obj'] = dates_list
    return df
match_data = get_match_data(current_year)


# 🔄 AUTOMATIC PERMANENT STORAGE HOOKS
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

import datetime as dt
true_india_now = datetime.utcnow() + dt.timedelta(hours=5, minutes=30)

# 🛠️ SYSTEM-WIDE EXPIRY RULES ENGINE
for bet in combined_bets:
    try:
        raw_num = str(bet.get('Match_Num', '0')).strip()
        m_num = int(float(raw_num)) if '.' in raw_num else int(raw_num)
        
        if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005) or m_num in [999, 1000]:
            bet["Is_Expired"] = False
        elif m_num < 103:
            bet["Is_Expired"] = True
        else:
            m_lookup = match_data[match_data['Match_Num'] == m_num]
            if not m_lookup.empty:
                kickoff_time = m_lookup.iloc[0]['Match_Date_Obj']
                bet["Is_Expired"] = true_india_now >= (kickoff_time + dt.timedelta(hours=3))
            else:
                bet["Is_Expired"] = True
    except:
        bet["Is_Expired"] = True

is_admin = (st.session_state.player_name == "Fifa@2026")

# ==========================================
# ⚽ UI SCREEN 1: LOGIN LOUNGE
# ==========================================
if st.session_state.current_page == "login":
    st.title("⚽ FIFA 2026 WC Prediction")
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
    st.title("🏆 Prediction Dashboard")
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
    
    open_bets = []
    for b in combined_bets:
        if b.get("Status", "Open") == "Open" and not b.get("Is_Expired", False):
            m_num = int(b.get("Match_Num", 0))
            if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005) or m_num in [999, 1000]:
                open_bets.append(b)
            else:
                m_lookup = match_data[match_data['Match_Num'] == m_num]
                if not m_lookup.empty and true_india_now >= m_lookup.iloc[0]['Match_Date_Obj']:
                    continue
                open_bets.append(b)

    live_bets = [b for b in combined_bets if b.get("Status") == "Matched" and not b.get("Is_Expired", False)]

    def get_bet_sort_key(b):
        try:
            m_num = int(b.get("Match_Num", 0))
            if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005) or m_num in [999, 1000]:
                return datetime(2026, 7, 30, 0, 0)
            match_row = match_data[match_data['Match_Num'] == m_num]
            if not match_row.empty:
                return match_row.iloc[0]['Match_Date_Obj']
            else:
                return datetime(2026, 6, 1, 0, 0)
        except:
            return datetime(2026, 6, 1, 0, 0)

    open_bets = sorted(open_bets, key=get_bet_sort_key)
    live_bets = sorted(live_bets, key=get_bet_sort_key)

    st.subheader("📋 1. Active Open Offers")
    if not open_bets:
        st.info("No open offers available.")
    else:
        for bet in open_bets:
            with st.container(border=True):
                m_num = int(bet.get('Match_Num', '0'))
                try:
                    m_lookup = match_data[match_data['Match_Num'] == m_num].iloc[0]
                    prediction_type = bet.get('Prediction')
                    
                    if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005):
                        m_odds = m_lookup['Home_Win_Odds'] if prediction_type == "Yes" else m_lookup['Away_Win_Odds']
                    elif prediction_type in [m_lookup['Home_Team'], "France", "Kylian Mbappe"]:
                        m_odds = m_lookup['Home_Win_Odds']
                    elif prediction_type in [m_lookup['Away_Team'], "Spain", "Lionel Messi"]:
                        m_odds = m_lookup['Away_Win_Odds']
                    else:
                        m_odds = m_lookup['Draw_Odds']
                    
                    b_pts = float(bet.get('Points', 100))
                    market_payout = float(round(b_pts * (m_odds - 1), 1))
                    market_str = f"Market Odds - {market_payout} pts"
                except Exception as e:
                    market_str = "Market Odds - N/A"

                b_creator = bet.get('Creator')
                b_pred = bet.get('Prediction')
                b_match = bet.get('Match_Name')
                
                b_risk = float(bet.get('Points', 0))
                b_payout = float(bet.get('Opponent_Payout', 0))

                if 801 <= m_num <= 899:
                    clean_item_name = b_match.split(" (")[0]
                    st.markdown(f"🗓️ **{b_creator}** backs **{clean_item_name}**")
                    st.write(f"📅 **Date:** Jul 20 | Prop Market Parameter")
                elif 901 <= m_num <= 904 or m_num == 999:
                    clean_item_name = b_match.replace(" to win WC", "").replace(" Winner Team Market", "")
                    if "vs" in clean_item_name or clean_item_name == "Field" or "Market" in clean_item_name:
                        clean_item_name = b_pred if b_pred not in ["Yes", "No"] else "Tournament Winner Selection"
                    st.markdown(f"🗓️ **{b_creator}** backs **{clean_item_name}** to win WC")
                    st.write(f"📅 **Date:** Jul 20 | Fixture: World Cup 2026 Winner Team Market")
                elif 1001 <= m_num <= 1005 or m_num == 1000:
                    clean_item_name = b_match.replace(" for Golden Boot", "").replace(" (Top Goalscorer) Market", "")
                    if "vs" in clean_item_name or clean_item_name == "Field" or "Market" in clean_item_name:
                        clean_item_name = b_pred if b_pred not in ["Yes", "No"] else "Kylian Mbappe"
                    st.markdown(f"🗓️ **{b_creator}** backs **{clean_item_name}**")
                    st.write(f"📅 **Date:** Jul 20 | Fixture: Golden Boot (Top Goalscorer) Market")
                else:
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

    st.subheader("🔥 2. Live Matched Bets (Locked)")
    if not live_bets:
        st.caption("No matched transactions are locked right now.")
    else:
        for bet in live_bets:
            try:
                risk_pts = float(bet.get('Points', 100))
                win_pts = float(bet.get('Opponent_Payout', 55))
            except:
                risk_pts = 100.0
                win_pts = 55.0

            b_match = bet.get('Match_Name')
            m_num = int(bet.get('Match_Num', 0))
            b_pred = bet.get('Prediction')
            
            if 801 <= m_num <= 899:
                clean_item_name = b_match.split(" (")[0]
                action_text = f"backed prop option: <b>{clean_item_name}</b>"
                display_match_name = "Specialized Final Prop Board"
                display_date = "Jul 20"
            elif 901 <= m_num <= 904 or m_num == 999:
                clean_item_name = b_match.replace(" to win WC", "").replace(" Winner Team Market", "")
                if "vs" in clean_item_name or clean_item_name == "Field" or "Market" in clean_item_name:
                    clean_item_name = b_pred if b_pred not in ["Yes", "No"] else "Tournament Winner"
                action_text = f"backed <b>{clean_item_name} to win WC</b>"
                display_match_name = "World Cup 2026 Winner Team Market"
                display_date = "Jul 20"
            elif 1001 <= m_num <= 1005 or m_num == 1000:
                clean_item_name = b_match.replace(" for Golden Boot", "").replace(" (Top Goalscorer) Market", "")
                if "vs" in clean_item_name or clean_item_name == "Field" or "Market" in clean_item_name:
                    clean_item_name = b_pred if b_pred not in ["Yes", "No"] else "Kylian Mbappe"
                action_text = f"backed <b>{clean_item_name} for Golden Boot</b>"
                display_match_name = "Golden Boot (Top Goalscorer) Market"
                display_date = "Jul 20"
            else:
                action_text = f"bet on <b>{bet.get('Prediction')}</b>"
                display_match_name = b_match
                display_date = bet.get('Match_Date')

            st.markdown(
                f"""
                <div style="background-color: rgba(39, 174, 96, 0.08); 
                            border: 2px solid #27ae60; 
                            padding: 15px; 
                            border-radius: 6px; 
                            margin-bottom: 12px;
                            font-family: sans-serif;">
                    <div style="font-weight: bold; font-size: 1.05rem; margin-bottom: 6px;">
                        🔒 {bet.get('Creator')} <span style="opacity: 0.7; font-weight: normal; font-size: 0.85rem;">VS</span> {bet.get('Opponent')}
                    </div>
                    <div style="font-size: 0.85rem; opacity: 0.7; margin-bottom: 8px;">
                        📅 <b>Target Date:</b> {display_date} | <b>Market:</b> {display_match_name}
                    </div>
                    <div style="font-size: 0.9rem; line-height: 1.4;">
                        📢 <b>{bet.get('Creator')}</b> {action_text} 
                        (Risking: {risk_pts} pts / Winning: {win_pts} pts) with <b>{bet.get('Opponent')}</b>.
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            if is_admin:
                if st.button(f"🚨 Admin Override: Force Delete #{bet.get('Bet_ID')}", key=f"del_live_{bet.get('Bet_ID')}", use_container_width=True, type="secondary"):
                    execute_backend_deletion(bet.get('Bet_ID'))

    st.markdown("---")

    expired_matched_bets = [b for b in combined_bets if b.get("Status") == "Matched" and b.get("Is_Expired", False)]

    def get_expired_sort_key(b):
        try:
            m_num = int(b.get("Match_Num", 0))
            if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005) or m_num in [999, 1000]:
                return datetime(2026, 7, 30, 0, 0)
            match_row = match_data[match_data['Match_Num'] == m_num]
            if not match_row.empty:
                return match_row.iloc[0]['Match_Date_Obj']
            else:
                return datetime(2026, 6, 1, 0, 0)
        except:
            return datetime(2026, 6, 1, 0, 0)

    expired_matched_bets = sorted(expired_matched_bets, key=get_expired_sort_key, reverse=True)

    with st.expander("📁 View Expired Matched Bets History", expanded=False):
        if not expired_matched_bets:
            st.caption("No expired matched bets found in history.")
        else:
            for bet in expired_matched_bets:
                try:
                    risk_pts = float(bet.get('Points', 100))
                    win_pts = float(bet.get('Opponent_Payout', 55))
                except:
                    risk_pts = 100.0
                    win_pts = 55.0

                b_match = bet.get('Match_Name')
                st.markdown(
                    f"""
                    <div style="background-color: rgba(192, 57, 43, 0.06); 
                                border: 2px solid #c0392b; 
                                padding: 15px; 
                                border-radius: 6px; 
                                margin-bottom: 12px;
                                font-family: sans-serif;">
                        <div style="font-weight: bold; font-size: 1.05rem; margin-bottom: 6px; color: #c0392b;">
                            ⌛ [EXPIRED] {bet.get('Creator')} VS {bet.get('Opponent')}
                        </div>
                        <div style="font-size: 0.85rem; opacity: 0.7; margin-bottom: 8px;">
                            📅 <b>Kickoff Date:</b> {bet.get('Match_Date')} | <b>Match:</b> {b_match}
                        </div>
                        <div style="font-size: 0.9rem; line-height: 1.4;">
                            📢 <b>{bet.get('Creator')}</b> picked <b>{bet.get('Prediction')}</b> 
                            (Risking: {risk_pts} pts / Winning: {win_pts} pts) with <b>{bet.get('Opponent')}</b>.
                        </div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
                
                if is_admin:
                    if st.button(f"🚨 Admin Override: Clear Expired #{bet.get('Bet_ID')}", key=f"del_exp_{bet.get('Bet_ID')}", use_container_width=True, type="secondary"):
                        execute_backend_deletion(bet.get('Bet_ID'))

# ==========================================
# 📊 UI SCREEN: TOURNAMENT BOARD (LIVE EXCEL)
# ==========================================
elif st.session_state.current_page == "view_excel":
    st.title("📊 Live Tournament Board")
    st.write("This table updates dynamically whenever results are committed to the backend repository.")
    
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
        m_num = int(bet.get('Match_Num', 0))
        is_outright = (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005) or m_num in [999, 1000]
        
        b_match = bet.get('Match_Name', '')
        b_pred = bet.get('Prediction', '')
        
        if 801 <= m_num <= 899:
            clean_market_title = "Specialized Player/Match Prop Board"
            display_date = "Jul 20"
            target_selection = b_match.split(" (")[0]
        elif m_num == 999 or (901 <= m_num <= 904):
            clean_market_title = "World Cup 2026 Winner Team Market"
            display_date = "Jul 20"
            target_selection = b_match.replace(" to win WC", "").replace(" Winner Team Market", "")
            if "vs" in target_selection or target_selection == "Field" or "Market" in target_selection:
                target_selection = b_pred if b_pred not in ["Yes", "No"] else "Tournament Winner Selection"
        elif m_num == 1000 or (1001 <= m_num <= 1005):
            clean_market_title = "Golden Boot (Top Goalscorer) Market"
            display_date = "Jul 20"
            target_selection = b_match.replace(" for Golden Boot", "").replace(" (Top Goalscorer) Market", "")
            if "vs" in target_selection or target_selection == "Field" or "Market" in target_selection:
                target_selection = b_pred if b_pred not in ["Yes", "No"] else "Kylian Mbappe"
        else:
            clean_market_title = b_match
            display_date = bet.get('Match_Date')
            target_selection = b_pred
        
        try:
            m_lookup = match_data[match_data['Match_Num'] == m_num].iloc[0]
            prediction_type = b_pred
            
            if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005):
                m_odds = m_lookup['Home_Win_Odds']
            elif prediction_type in [m_lookup['Home_Team'], "France", "Kylian Mbappe"]:
                m_odds = m_lookup['Home_Win_Odds']
            elif prediction_type in [m_lookup['Away_Team'], "Spain", "Lionel Messi"]:
                m_odds = m_lookup['Away_Win_Odds']
            else:
                m_odds = m_lookup['Draw_Odds']
            
            b_pts = float(bet.get('Points', 100))
            market_payout = float(round(b_pts * (m_odds - 1), 1))
        except:
            market_payout = None

        creator_name = bet.get('Creator')
        creator_risk = float(bet.get('Points', 0))
        your_risk = float(bet.get('Opponent_Payout', 0))

        with st.container(border=True):
            st.subheader("📊 Bet Transaction Summary")
            st.write(f"📅 **Target Date:** {display_date}")
            st.write(f"🏆 **Market Target:** {clean_market_title}")
            
            if is_outright:
                st.write(f"🔮 **{creator_name}’s Choice:** Backing **{target_selection}**")
            else:
                st.write(f"🔮 **{creator_name}’s Prediction:** Backing **{target_selection}**")
                
            st.markdown("---")
            st.write(f"💵 **Your Risk Amount:** {your_risk} pts *(Amount you lose if {target_selection} wins)*")
            st.write(f"💰 **Your Potential Payout:** {creator_risk} pts *(Amount you win if {target_selection} fails)*")
            
            if is_outright:
                st.caption("ℹ️ *Result reflects official final tournament awards data.*")
            elif m_num >= 89:
                st.caption("ℹ️ *Result includes Regulation Time, Extra Time, and Penalty Shootouts.*")
            else:
                st.caption("ℹ️ *Result reflects 90 minutes of standard regulation play plus injury time.*")

            if market_payout is not None:
                st.write(f"📊 **Market Adjustment:** Creator baseline dictates a {market_payout} pts market offset adjustment.")
            else:
                st.write(f"📊 **Market odds for the bet is:** N/A")

        st.warning("⚠️ Once confirmed, this transaction is locked and cannot be deleted by either player.")

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
    active_fixtures = match_data[match_data['Match_Date_Obj'] > true_india_now]
    selected_match_str = st.selectbox("👉 Target Match Fixture:", options=["-- Select --"] + active_fixtures['Match_Display'].tolist())
    
    if selected_match_str != "-- Select --":
        match_row = match_data[match_data['Match_Display'] == selected_match_str].iloc[0]
        m_num = int(match_row['Match_Num'])
        
        if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005):
            prediction_options = ["-- Select --", "Yes"]
        elif pd.isna(match_row.get('Draw_Odds')) or match_row.get('Draw_Odds') is None:
            prediction_options = ["-- Select --", match_row['Home_Team'], match_row['Away_Team']]
        else:
            prediction_options = ["-- Select --", match_row['Home_Team'], match_row['Away_Team'], "Draw"]

        selected_prediction = st.selectbox("🔮 Outcome Selection:", options=prediction_options)        
        if selected_prediction != "-- Select --":
            points = st.number_input("Points You Want to Risk:", min_value=1, value=100, step=5)
            
            if (801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005):
                odds = float(match_row['Home_Win_Odds'])
            elif selected_prediction == match_row['Home_Team']:
                odds = float(match_row['Home_Win_Odds'])
            elif selected_prediction == match_row['Away_Team']:
                odds = float(match_row['Away_Win_Odds'])
            else:
                odds = float(match_row['Draw_Odds'])
                
            default_payout = int(round(points * (odds - 1), 0))
            payout = st.number_input("Points You Want to Win (Adjustable):", min_value=1, value=default_payout, step=5)
            
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
                
                saved_match_name = match_row['Home_Team'] if ((801 <= m_num <= 899) or (901 <= m_num <= 904) or (1001 <= m_num <= 1005)) else f"{match_row['Home_Team']} vs {match_row['Away_Team']}"
                        
                combined_bets.append({
                    "Bet_ID": int(next_id), "Creator": str(st.session_state.player_name), "Match_Num": int(m_num),
                    "Match_Name": saved_match_name, "Match_Date": str(match_row['Date_Str']),
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
