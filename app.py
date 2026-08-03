import streamlit as st
from chatbot import ask_bot

st.set_page_config(page_title="Vertexa Systems | Onboarding Navigator", page_icon="🤖", layout="centered")

# ---------- CUSTOM STYLING ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: radial-gradient(circle at 15% 0%, #1A2140 0%, #0E1226 55%, #0A0D1C 100%);
    color: #F0EEE6;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #10142A;
    border-right: 1px solid rgba(212, 162, 76, 0.15);
}
.sidebar-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    color: #D4A24C;
    letter-spacing: 0.3px;
    margin-bottom: 0.3rem;
}
.sidebar-divider {
    width: 36px;
    height: 3px;
    background: #D4A24C;
    border-radius: 2px;
    margin: 6px 0 20px 0;
}

/* Hero header */
.hero-logo-row {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 0.6rem;
}
.hero-monogram {
    width: 52px; height: 52px;
    border-radius: 14px;
    background: linear-gradient(135deg, #D4A24C, #A87A2E);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 1.5rem;
    color: #10142A;
    box-shadow: 0 4px 18px rgba(212, 162, 76, 0.35);
    flex-shrink: 0;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 2.4rem;
    letter-spacing: -0.5px;
    color: #F5F3EC;
    line-height: 1.1;
}
.hero-sub {
    color: #9099B8;
    font-size: 1.02rem;
    margin: 0.8rem 0 1.6rem 0;
    max-width: 640px;
}
.hero-badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 999px;
    background: rgba(212, 162, 76, 0.10);
    border: 1px solid rgba(212, 162, 76, 0.4);
    color: #D4A24C;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
}
.hero-divider {
    height: 1px;
    background: linear-gradient(90deg, rgba(212,162,76,0.5), rgba(212,162,76,0));
    margin: 1.5rem 0 2rem 0;
}

/* Waypoints trail in sidebar */
.waypoints { list-style: none; padding-left: 4px; margin: 0; }
.waypoints li {
    position: relative;
    padding-left: 26px;
    padding-bottom: 20px;
    font-size: 0.92rem;
    color: #DDD9CC;
}
.waypoints li::before {
    content: '';
    position: absolute;
    left: 5px; top: 6px;
    width: 2px; height: 100%;
    background: rgba(212, 162, 76, 0.3);
}
.waypoints li:last-child::before { height: 0; }
.waypoints li::after {
    content: '';
    position: absolute;
    left: -1px; top: 2px;
    width: 13px; height: 13px;
    border-radius: 50%;
    background: #D4A24C;
    box-shadow: 0 0 0 4px rgba(212, 162, 76, 0.15);
}

/* Chat bubbles */
.msg-row { display: flex; margin-bottom: 20px; }
.msg-bot { justify-content: flex-start; }
.msg-user { justify-content: flex-end; }

.msg-bubble {
    max-width: 76%;
    padding: 15px 19px;
    border-radius: 16px;
    font-size: 0.98rem;
    line-height: 1.6;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
}
.msg-bot .msg-bubble {
    background: #171C36;
    border: 1px solid rgba(212, 162, 76, 0.22);
    border-left: 3px solid #D4A24C;
    color: #F0EEE6;
    border-top-left-radius: 4px;
}
.msg-user .msg-bubble {
    background: linear-gradient(135deg, #2C7A6E, #1F5A52);
    color: #F0EEE6;
    border-top-right-radius: 4px;
}
.msg-avatar {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.05rem;
    margin: 0 10px;
    flex-shrink: 0;
}
.msg-bot .msg-avatar {
    background: rgba(212, 162, 76, 0.14);
    border: 1px solid rgba(212,162,76,0.4);
}
.msg-user .msg-avatar {
    background: rgba(63, 167, 150, 0.18);
    border: 1px solid rgba(63,167,150,0.45);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.5px;
    color: #7FD8C7;
}

/* Chat input */
[data-testid="stChatInput"] textarea {
    background: #171C36 !important;
    border: 1px solid rgba(212, 162, 76, 0.35) !important;
    border-radius: 14px !important;
    color: #F0EEE6 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO HEADER ----------
st.markdown('<div class="hero-badge">Vertexa Systems · New Joiner Assistant</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-logo-row">
    <div class="hero-monogram">V</div>
    <div class="hero-title">Onboarding Navigator</div>
</div>
""", unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Your guide through IT setup, leave policy, reimbursements, and everything else on the way to your first day.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-divider"></div>', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.markdown('<div class="sidebar-heading">Onboarding Trail</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="waypoints">
        <li>Company Overview</li>
        <li>First Day Checklist</li>
        <li>IT Setup Guide</li>
        <li>Leave & Attendance Policy</li>
        <li>Reimbursement Policy</li>
        <li>Communication & Escalation</li>
        <li>Technology Landscape</li>
        <li>Code of Conduct</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Answers are grounded in Vertexa Systems' internal onboarding documents — not guessed.")

# ---------- CHAT STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your onboarding navigator for Vertexa Systems. Ask me about IT setup, leave policy, reimbursements, or anything else about joining the team."}
    ]

# ---------- RENDER CHAT HISTORY ----------
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.markdown(f"""
        <div class="msg-row msg-bot">
            <div class="msg-avatar">🤖</div>
            <div class="msg-bubble">{message["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="msg-row msg-user">
            <div class="msg-bubble">{message["content"]}</div>
            <div class="msg-avatar">YOU</div>
        </div>
        """, unsafe_allow_html=True)

# ---------- CHAT INPUT ----------
if question := st.chat_input("Ask about onboarding, IT setup, leave, reimbursements..."):
    st.session_state.messages.append({"role": "user", "content": question})
    st.markdown(f"""
    <div class="msg-row msg-user">
        <div class="msg-bubble">{question}</div>
        <div class="msg-avatar">YOU</div>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("Charting your answer..."):
        answer = ask_bot(question)

    st.markdown(f"""
    <div class="msg-row msg-bot">
        <div class="msg-avatar">🤖</div>
        <div class="msg-bubble">{answer}</div>
    </div>
    """, unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": answer})