# import required libraires
from groq import Groq
import streamlit as st
import time


# Set up GROQ client
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
groq_client = Groq(api_key=GROQ_API_KEY)


# Define system prompt
system_message = (
    "You are a highly relatable personal productivity coach for teenagers."
    "Your name is Pep (short for Pep Talker)."
    "Keep your response short and concise. Less than 100 words."
    "Your job is to help teens organize their lives, stay motivated, and achieve their goals."
    "Speak in a friendly, supportive tone, using a mix of teen-friendly language and practical advice."
    "Focus on school, hobbies, self-care, and finding balance between work and fun."
    "Be motivational, empathetic, and slightly witty but always positive."
    "Avoid being overly formal; keep your responses fun, actionable, and encouraging"

)

system_prompt = {
    "role": "system",
    "content": system_message
}


# Define llm response function
def get_response(chat_history):

    response = groq_client.chat.completions.create(
        model='llama3-70b-8192',
        messages=chat_history,
        max_tokens=100,
        temperature=1.2
    )

    chat_response = response.choices[0].message.content
    
    for word in chat_response:
        yield word + ""
        time.sleep(0.05)

# Define main function to run the streamlit app
def main():

    # title and about
    st.title("PepTalk")
    with st.expander("About Pep"):
        st.write("Pep is your go-to coach when you're feeling overwhelmed with school, procrastinating, or struggling to stay on top of things. Pep motivates with actionable tips and sprinkles in a bit of humor to keep things lighthearted.")


    # session state
    if "messages" not in st.session_state:
        st.session_state.messages = [system_prompt]
    
    for message in st.session_state.messages:
        if message != system_prompt:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # chat history
    if prompt := st.chat_input("Tell Pep what's up"):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.markdown(prompt)

            response = get_response(st.session_state.messages)

        with st.chat_message("assistant"):
            chat_response = st.write_stream(response)

        st.session_state.messages.append({"role": "assistant", "content": chat_response})

# Run the main function (entry point)
if __name__ == "__main__":
    main()
# Run the Streamlit app
# To run the app, use the command: streamlit run streamlit_app.py
# in the terminal
# and open the provided URL in your web browser.