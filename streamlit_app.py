import streamlit as st
import random
import time

# Game data
WALLET_DATA = {
    "Bitkey": {
        "recovery_tools": ["Self-Custody Recovery", "Social Recovery", "Emergency Access"],
        "durability": 100,
        "security_rating": 95
    },
    "Trezor": {
        "recovery_tools": ["Seed Phrase Only"],
        "durability": 80,
        "security_rating": 85
    },
    "Ledger": {
        "recovery_tools": ["Seed Phrase Only"],
        "durability": 85,
        "security_rating": 85
    },
    "Foundation": {
        "recovery_tools": ["Seed Phrase Only"],
        "durability": 75,
        "security_rating": 80
    }
}

EVENTS = [
    {
        "title": "Water Damage!",
        "description": "Your device fell into water!",
        "bitkey_options": [
            "Use Self-Custody Recovery with your phone",
            "Contact trusted parties for Social Recovery",
            "Use Emergency Access"
        ],
        "other_options": [
            "Check your seed phrase backup",
            "Try to dry out the device",
            "Contact support"
        ]
    },
    {
        "title": "Device Lost!",
        "description": "You can't find your hardware wallet!",
        "bitkey_options": [
            "Use your phone for Self-Custody Recovery",
            "Activate Social Recovery protocol",
            "Contact Emergency Access trusted party"
        ],
        "other_options": [
            "Search for your seed phrase backup",
            "Hope you find the device",
            "Buy a new device and pray you find your seed phrase"
        ]
    }
]

# Initialize session state
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'started': False,
        'wallet': None,
        'btc': 1.0,
        'days': 1,
        'events_survived': 0
    }

# Title and styling
st.markdown("""
    <style>
    .main {
        background-color: black;
        color: #00FF00;
    }
    .stButton>button {
        background-color: black;
        color: #00FF00;
        border: 2px solid #00FF00;
    }
    .stButton>button:hover {
        background-color: #00FF00;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("The Bitcoin Trail")

# Main game logic
if not st.session_state.game_state['started']:
    st.write("Choose your hardware wallet:")
    cols = st.columns(4)
    for idx, wallet in enumerate(WALLET_DATA.keys()):
        if cols[idx].button(wallet):
            st.session_state.game_state['started'] = True
            st.session_state.game_state['wallet'] = wallet
            st.rerun()

else:
    # Game interface
    st.sidebar.markdown(f"""
    ### Stats
    - Wallet: {st.session_state.game_state['wallet']}
    - Bitcoin: {st.session_state.game_state['btc']} BTC
    - Days: {st.session_state.game_state['days']}
    - Events Survived: {st.session_state.game_state['events_survived']}
    """)

    # Generate random event
    event = random.choice(EVENTS)
    
    st.markdown(f"## {event['title']}")
    st.write(event['description'])

    # Show options based on wallet type
    if st.session_state.game_state['wallet'] == "Bitkey":
        options = event['bitkey_options']
        st.write("Thanks to Bitkey's recovery tools, you have multiple options:")
    else:
        options = event['other_options']
        st.write("With limited recovery options, you must choose carefully:")

    choice = st.radio("What would you like to do?", options)

    if st.button("Make Decision"):
        with st.spinner("Processing your decision..."):
            time.sleep(1)  # Add dramatic pause
            
            if st.session_state.game_state['wallet'] == "Bitkey":
                st.success("Successfully recovered your bitcoin! Bitkey's recovery tools save the day!")
                st.session_state.game_state['events_survived'] += 1
            else:
                if "seed phrase" in choice.lower():
                    if random.random() < 0.5:
                        st.error("Your seed phrase was damaged! Access to your bitcoin is lost forever.")
                        st.button("Start Over", on_click=lambda: st.session_state.clear())
                        st.stop()
                    else:
                        st.warning("You got lucky! The seed phrase was still readable.")
                        st.session_state.game_state['events_survived'] += 1

            st.session_state.game_state['days'] += 1
            
            if st.button("Continue Journey"):
                st.rerun()

    if st.button("Start Over"):
        st.session_state.clear()
        st.rerun()