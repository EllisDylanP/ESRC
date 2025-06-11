import pandas as pandas
import streamlit as streamlit
import plotly.express as px
from PIL import Image

## PAGE OUTLINE
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

## DATA
UsernameAndPassword = "Username and Password.csv"
Activity = "Activity.csv"
Journal = "Journal.csv"
df_loginpage = pandas.read_excel(UsernameAndPassword, usecols= "A, B", header = 4)
df_journal = pandas.read_excel(Journal, header= 5)
df = pandas.read_excel(Activity, usecols='A:H', header = 4)
df_financial = pandas.read_excel(Activity, usecols="A, B, C, E", header = 4)
df_HR = pandas.read_excel(Activity, usecols='A, B, C, F', header = 4)
df_Oxy = pandas.read_excel(Activity, usecols='A, B, C, G', header = 4)
df_PI = pandas.read_excel(Activity, usecols='A, B, C, H', header = 4)

with streamlit.form(key = "Registration"):
    Username=streamlit.text_input("Username")
    Password=streamlit.text_input("Password")
    Email=streamlit.text_input("Email")
    PhoneNumber=streamlit.text_input("Phone Number")
    SubjectMatterExpert=streamlit.option("Subject Matter Expert")
    Retailer=streamlit.option("Retailer")
    RegistrationComplete = streamlit.form_submit_button("Register")
    #UserIDNumber=streamlit.number_input("Username and Password.csv".row() + 1)
    #Date=streamlit.write(date)

with streamlit.form(key = "New Entry"):
    UserID = df_loginpage["USER ID"]
    Date = streamlit.write(date)
    Product = streamlit.text_input("Product")
    Quantity = streamlit.text_input("Quantity")
    Price = streamlit.text_input("Price")
    HeartRate = streamlit.number_input("Heart Rate")
    OxygenSaturation = streamlit.number_input("Oxygen Saturation")
    PerfusionIndex = streamlit.number_input("Perfusion Index")

## REGISTRATION
def registration(registrationtable):
    Streamlit.table[Username] = registrationtable[1]
    Streamlit.table[Password] = registrationtable[2]
    Streamlit.table[Phone Number] = registrationtable[3]
    Streamlit.table[Email] = registrationtable[4]
    Streamlit.option["SME"].value() = registrationtable[5]
    Streamlit.option["Retailer"].value() = registrationtable[6]
    registrationtable[(Usernumber).value()][(Usernumber + 1).row()] = registrationtable[Usernumber] 
    registrationtable[date][getdate().value()] = registrationtable[date]
    streamlit.button("Register")
    return(registrationtable)


## LOGIN USER INTERFACE
def loginprocess (username, password):
    userexists = ((df_loginpage["USER ID"] == username) & (df_loginpage["PASSWORD"] == password)).any()
    if not userexists:
        return "Authentication failed"
    
    streamlit.button("Add a new entry")
    streamlit.table("Product, Quantity, Price, Heart Rate, Perfusion Index, Oxygen saturation")
    streamlit.table([Blank], [Blank], [Blank], [Blank], [Blank], [Blank])
    streamlit.button("New row")
    streamlit.button("New row") --> ([Blank], [Blank], [Blank], ["Heartrate"][Heart rate value][1], ["Perfusion Index"][Perfusion Index][1], ["Oxygen Saturation"][Oxygen Saturation value][1])
    Streamlit.button("Submit")
    df.write(streamlit.table("Product, Quantity, Price, Heart Rate, Perfusion Index, Oxygen saturation"))

    
    # Get indices or rows from the filtered reference DataFrame
    df_productselect = streamlit.multiselect("Select the product:",options = df["Product"].unique(),default = df["Product"].unique())
    df_forproduct = df[df["Product"].isin(df_productselect)]
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
pages = ["Analysis", "Consumption Consultation", "Journal"]
page = streamlit.sidebar.selectbox("Choose a page", pages)
if page == "Analysis":
    with streamlit.form("Login"):
        username = streamlit.text_input(label ="Username")
        password = streamlit.text_input(label = "Password", type = "password")
        submit_button = streamlit.form_submit_button(label="Login")
        streamlit.caption("Usernames and Passwords are case-sensitive")
        if submit_button:
            loginprocess(username, password)
            #streamlit.multiselect("Select the product:",options = df["Product"].unique(),default = df["Product"].unique())
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
    streamlit.dataframe(df_journal, width = 1000, hide_index= True)


DPEimage = Image.open("assets/DylanPeterEllislogo.jfif")
streamlit.image(DPEimage, caption = "Dylan Peter Ellis", use_container_width= 100)
