import pandas as pandas
import streamlit as streamlit
import plotly.express as px
from PIL import Image
import requests
import base64
import io
import json

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
streamlit.header("User Portal - Access to Endocannabinoid Analysis, Industry Outreach, and Publications")

with streamlit.form("Activity"):
   streamlit.write("Use the same name as before if you are a return user *cap-sensitive*")
   name = streamlit.input("Name")
   heartrate = streamlit.input("Heart Rate")
   perfusionindex = streamlit.input("Perfusion Index")
   oxygensaturation = streamlit.input("Oxygen Saturation")
   flower = streamlit.input("Flower")
   concentrate = streamlit.input("Concentrate")
   tincture = streamlit.input("Ticture")
   beverage = streamlit.input("Beverage")
   edible = streamlit.input("Edible")
   vapor = streamlit.input("Vapor")
   topical = streamlit.input("Topical")
   submitted = streamlit.form_submit_button("Submit")
   if submitted:
      streamlit.append("Activity")


with streamlit.form("Name"):
   name = streamlit.input("Name")
   submitted - streamlit.form_submit_button("Submit")
   if submitted:
      streamlit.read("Activity", name)

## Activity INTERFACE

df_user = pandas.read_csv(Activity, usecols=['A:H'], header = 4)
df_financial = pandas.read_csv(Activity, usecols=["A, B, C, E"], header = 4)
df_HR = pandas.read_csv(Activity, usecols=['A, B, C, F'], header = 4)
df_Oxy = pandas.read_csv(Activity, usecols=['A, B, C, G'], header = 4)
df_PI = pandas.read_csv(Activity, usecols=['A, B, C, H'], header = 4)

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
##unknown
def local_css(file_name):
        with open(file_name) as f:
           streamlit.markdown(f"<style>{f.read()}</styles>", unsafe_allow_html=True)




#Page Navigator
Journal = "Journal.csv"
df_journal = pandas.read_csv(Journal, header= 7)

pages = ["Analysis", "Consumption Consultation", "Journal"]
page = streamlit.sidebar.selectbox("Choose a page", pages)
if page == "Analysis":
   thumbnail_url = "https://oxiline.shop/app/uploads/2024/09/pulse-9s-hero-web-1.png"
   iframe_url = "https://oxiline.shop/product/pulse-9s-pro/" 
   streamlit.markdown(
       f"""
       <a href="{iframe_url}" target="_blank">
           <img src="{thumbnail_url}" alt="Thumbnail" style="width:100%; max-width:300px; border-radius:10px;"/>
       </a>
       """,
       unsafe_allow_html=True,)
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
    # Upload the PDF file
    uploaded_file = streamlit.file_uploader("Cannabinoids tied to mineral necessities of daily suggested value", type="pdf")

    if uploaded_file is not None:
        with streamlit.open(uploaded_file) as pdf:
            # Extract text from all pages
            for page in pdf.pages:
                streamlit.popover(page.extract_text())
    data = pandas.DataFrame(
        columns=["Author", "Title", "Date"], 
         ##rows=[("Dylan", "Cannabinoids tied to mineral necessities of daily suggested value.pdf", "08/30/2025")]
    )
    # Display the DataFrame as a static table
    streamlit.table(data)





DPEimage = Image.open("assets/DylanPeterEllislogo.jfif")
streamlit.image(DPEimage, caption = "Dylan Peter Ellis", use_container_width= 100)
