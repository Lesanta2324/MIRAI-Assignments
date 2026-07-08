import streamlit as st

st.title("The Identity Echo Interface")
st.write("Welcome to the Identity Echo Interface. Enter the required information below, and then click the 'Send' button.")

user_name = st.text_input("Enter Your Name", placeholder="Your Name")
user_message = st.text_input("Enter your Message", placeholder="Message")


if st.button("Send"):

    if not user_name:
        st.error("Please provide your name.")
        
    elif not user_message:
        st.warning("Please type a message to transmit.")
        
    
    else:
        
        total_character = len(user_message)
        token_count = total_character / 4
        
        
        st.success(f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}")
        
       
        st.info(f"System Check: Your message will consume approximately {token_count} tokens from our context window.")