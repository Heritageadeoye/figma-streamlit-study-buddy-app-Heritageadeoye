import streamlit as st
import pandas as pd
from io import StringIO
import google.generativeai as genai


color = '#1C2BAE'
# App title and caption

st.title("Study Buddy App")
st.caption("study Smarter, together") 

st.header("About the App" )
st.write(
"Welcome to StudyBuddy, your ultimate study companion! Whether you're preparing for exams, working on projects, or simply looking for a study buddy, we've got you covered."
)

st.header("How to use the App" )

st.write(
" 1. Sign Up/Login: Begin by signing up for an account or logging in if you're already a member. \n"
"2. Explore Features: Familiarize yourself with StudyPal's features, including chat, file sharing, scheduling, and more.\n"
"3. Find Study Buddies: Use the search or browse functionality to find study buddies with similar interests and goals.\n"
"4. Connect and Collaborate: Reach out to potential study partners and start collaborating on projects, assignments, or exam preparation.\n"
"5. Stay Organized: Utilize the calendar and task management tools to stay organized and on top of your study schedule.\n"
"6. Share Resources: Share study materials, notes, and resources with your study group for enhanced learning.\n"
"7. Give Feedback: Help us improve StudyPal by providing feedback and suggestions through the app.\n"
"8. Enjoy Learning: Most importantly, enjoy the journey of learning and growth with StudyPal by your side!\n"
)

# st.button("Click me", type="primary")

#file uploader section
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
 
st.image('birthdayShot6.jpg')

#text area section:





#Select buttons
option = st.selectbox(
    'What kind of help do you need?',
    ('Homework help', 'Project help'))

    
txt = st.text_area(
    "Enter your message here ",
    placeholder="Enter your message here",
    height=100,
    max_chars=200,
    key="message",
    help="This is a text area where you can type your message.",
        disabled=False,
    )




    
#genAI



genai.configure(api_key='AIzaSyD4MgQ0J1b_-sFP1XcRrDVXMa3d8U2dpoU')
model = genai.GenerativeModel('gemini-pro')




if st.button("Click to Send"):
    response = model.generate_content(txt)
    st.header("This is the response: " + str(response.text ))


