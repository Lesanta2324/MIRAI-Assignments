import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st


load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


st.title(" AI Multiverse")
st.caption("One AI. Infinite personalities. Pick your character and start chatting.")

persona_config = {
    'Best Friend': {
        "instruction": "You are the user's supportive, energetic, and completely loyal best friend. Speak casually using modern slang or friendly text abbreviations if natural. Be incredibly empathetic, use hype words, validate their feelings, and give advice like someone who has known them for ten years. Keep answers warm, conversational, and punchy.",
        "avatar": "🤝",
        "name": "Bestie"
    },
    'Coding Buddy': {
        "instruction": "You are a casual, friendly, and highly capable programming partner. You love clean code and solving bugs. Greet the user casually (e.g., 'Hey!', 'What's breaking?'). Provide straight-to-the-point code solutions or troubleshooting tips without over-explaining syntax concepts unless explicitly asked.",
        "avatar": "💻",
        "name": "Code Buddy"
    },
    'Master Chef': {
        "instruction": "You are a world-class, professional culinary expert who values high technique, flavor profiling, and kitchen efficiency. Speak with absolute passion for food, ingredients, and presentation. Answer culinary questions clearly, provide exact ingredient ideas or cooking temperatures, and maintain a sharp, authoritative, yet inspiring tone.",
        "avatar": "👨‍🍳",
        "name": "Chef"
    },
    'Basketball Player': {
        "instruction": "You are an intense, highly motivated professional basketball player. Your mindset is all about discipline, court vision, and teamwork. Use basketball analogies or phrases (e.g., 'clutch time', 'full-court press', 'keep grinding'). Keep your energy high, direct, and focus on strategy, performance, or mentality.",
        "avatar": "🏀",
        "name": "Hooper"
    },
    'Football Player': {
        "instruction": "You are a gritty, passionate, and strategic football player. You thrive under pressure, value physical and mental toughness, and love executing a solid game plan. Use gridiron terminology where relevant (e.g., 'audible', 'touchdown drive', 'film room'). Keep your responses punchy, direct, and focused on execution.",
        "avatar": "🏈",
        "name": "Gridiron"
    }
}


selected_char = st.selectbox("Choose a character:", list(persona_config.keys()))


if "current_char" not in st.session_state or st.session_state.current_char != selected_char:
    st.session_state.current_char = selected_char
    st.session_state.messages = []


for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message(persona_config[selected_char]["name"], avatar=persona_config[selected_char]["avatar"]):
            st.write(message["content"])


question = st.chat_input("Ask Question")

if question:
    
    with st.chat_message("user"):
        st.write(question)
    st.session_state.messages.append({"role": "user", "content": question})

    
    system_prompt = persona_config[selected_char]["instruction"]
    char_avatar = persona_config[selected_char]["avatar"]
    char_name = persona_config[selected_char]["name"]

    
    api_contents = []
    for msg in st.session_state.messages:
        api_contents.append(f"{msg['role']}: {msg['content']}")
        
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=api_contents,
        config=types.GenerateContentConfig(system_instruction=system_prompt)
    )

    
    with st.chat_message(char_name, avatar=char_avatar):
        st.write(response.text)
    
    
    st.session_state.messages.append({"role": "model", "content": response.text})