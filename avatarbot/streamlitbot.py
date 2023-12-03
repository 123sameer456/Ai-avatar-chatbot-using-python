import streamlit as st
import openai
import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()



import streamlit as st

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>' , unsafe_allow_html=True)
import streamlit as st
# openai.api_key = 'your api key is here'
messages = []

# bot = {'role': 'system', 'content': """
# your syste message is here
# """}
# messages.append(bot)
# Create two columns
col1, col2 = st.columns(2)
# Add content to the second column
with col2:
   
    st.header("CGD BOT")
    st.write("Content for column 2")
    # Create an input box
    input_start = st.text_input("Enter text here:")
    
    if input_start:
        input_obj = {"role": "user", "content": input_start}
        messages.append(input_obj)
    readonly_text = "This is some readonly text."

    response_text = st.text(readonly_text)
    send_btn = st.button("Clear Input")
    # while True:
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=messages
        # )

        # response_content = response['choices'][0]['message']['content'].strip()
        # Create an input box
   
# Add content to the first column
with col1:
    st.header("Column 1")
    
    st.write("Content for column 1")
        # Create a text area
    # output_text = st.text_area("Response:", value =  response_content)
    
    # response_obj = {"role": "assistant", "content": response_content}
    # messages.append(response_obj)
    
    # input_obj = {"role": "user", "content": input_text}
    # messages.append(input_obj)
    output_text= 0
    
    
    
        # Display an animated GIF in the sidebar
    vid = st.image("avatar.gif", use_column_width=True)
         # Define the text you want to convert to speech
        # text = response_content
        # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        # Convert text to speech
    text = "hello sameer! this is our sample text"
    engine.say(text)
    
        # Save the generated speech as an audio file (optional)
    engine.save_to_file(text, 'output.mp3')

        # Wait for the speech to finish
    engine.runAndWait()
        

    # else:
    #     st.image("avatar.jpeg", use_column_width=True)






