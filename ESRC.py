import pandas as pandas
import streamlit as streamlit
import plotly.express as px
from PIL import Image
import requests
import base64
import io
import json



## API CODE 
UsernameAndPassword = "Username and Password.csv"



## FRONT PAGE DESIGN
streamlit.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True)
streamlit.markdown('<h1 class="title">The Endocannabinoid System Research Company</h1>', unsafe_allow_html=True)
#streamlit.set_page_config(page_title='The Endocannabinoid System Research Company')
streamlit.header("User Portal - Access to Biometric Analysis, Industry Outreach, and Publications")




## LOGIN USER INTERFACE
##df = pandas.read_csv("Username and Password.csv", usecols=['A,B'],header =4)
Activity = "Activity.csv"
##df_activity = pandas.read_csv(Activity, usecols=['A:H'], header = 4)
##df_financial = pandas.read_csv(Activity, usecols=["A, B, C, E"], header = 4)
##df_HR = pandas.read_csv(Activity, usecols=['A, B, C, F'], header = 4)
##df_Oxy = pandas.read_csv(Activity, usecols=['A, B, C, G'], header = 4)
##df_PI = pandas.read_csv(Activity, usecols=['A, B, C, H'], header = 4)


def loginprocess (username, password):
    userexists = ((df["USER ID"] == username) & (df["PASSWORD"] == password)).any()
    if not userexists:
        return "Authentication failed"

    
    # Get indices or rows from the filtered reference DataFrame
    df_productselect = streamlit.multiselect("Select the product:",options = df_activity["Product"].unique(),default = df_activity["Product"].unique())
    df_forproduct = df_activity[df_activity["Product"].isin(df_productselect)]
    filtered_indices = df_forproduct[df_forproduct.iloc[:, 0] == username].index
    
    # Filter other data tables using the filtered indices or rows
    HRreport = px.line(df_HR.loc[filtered_indices],  x = "Date", y = "Heart Rate", title = "Heart Rate Metrics", markers=True)
    Oxyreport = px.line(df_Oxy.loc[filtered_indices],   x = "Date", y = "Oxygen Saturation", title = "Oxygen Saturation Metrics", markers=True)
    PIreport = px.line(df_PI.loc[filtered_indices],  x = "Date", y = "Perfusion Index", title = "Perfusion Index report", markers=True)
    Financialreport = px.line(df_financial.loc[filtered_indices], x="Date", y="Price", title = "Financial Report", markers=True)
        
    # Prepare data for line graphs in Streamlit (assuming simple structure for demonstration)
    streamlit_graphs = {
            streamlit.plotly_chart(HRreport),
            streamlit.plotly_chart(Oxyreport),
            streamlit.plotly_chart(PIreport),
            streamlit.plotly_chart(Financialreport)
        }
    return streamlit_graphs
def local_css(file_name):
        with open(file_name) as f:
           streamlit.markdown(f"<style>{f.read()}</styles>", unsafe_allow_html=True)




#Page Navigator
Journal = "Journal.csv"
##df_journal = pandas.read_csv(Journal, header= 7)

pages = ["Analysis", "Consumption Consultation", "Journal"]
page = streamlit.sidebar.selectbox("Choose a page", pages)
if page == "Analysis":
    with streamlit.form("Login"):
        username = streamlit.text_input(label ="Username")
        password = streamlit.text_input(label = "Password", type = "password")
        submit_button = streamlit.form_submit_button(label="Login")
        streamlit.caption("Usernames and Passwords are case-sensitive")
        streamlit.caption("text me at 7039014281 to have an update with your health metrics at each transaction with your own pulse oximeter to have freedom to be with any cannabis outlet you choose")
        if submit_button:
            loginprocess(username, password)
            #streamlit.multiselect("Select the product:",options = df_activity["Product"].unique(),default = df_activity["Product"].unique())
elif page == "Consumption Consultation":
    streamlit.subheader("Describe a cannabis consumption situation you would like to have consultation regarding")
    contact_form = """
    <form action="https://formsubmit.co/dpe.esrc@gmail.com" method="POST">
        <input type="hidden" name=" _captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Highlight aspects of your experience"></textarea>
        <button type="submit">Send</button>
        <clear_on_submit = True>
    </form>
    """
    streamlit.markdown(contact_form, unsafe_allow_html = True)
    local_css("style.css.txt")
elif page == "Journal":
    ##streamlit.dataframe(df_journal, width = 1000, hide_index= True)
    # Create a sample DataFrame
    data = pandas.DataFrame(
        columns=["Author", "Title", "Date"]
    )
    # Display the DataFrame as a static table
    streamlit.table(data)





DPEimage = Image.open("assets/DylanPeterEllislogo.jfif")
streamlit.image(DPEimage, caption = "Dylan Peter Ellis", use_container_width= 100)
