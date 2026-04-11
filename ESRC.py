import pandas as pandas
import streamlit as streamlit
import plotly.express as px
from PIL import Image
import requests
import base64
import io
import json
import streamlit.components.v1

## FRONT PAGE DESIGN
streamlit.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    .oxiline {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True)
streamlit.components.v1.iframe("https://oxiline.shop/product/pulse-9s-pro/", height=300)
streamlit.markdown('<h6 class="oxiline">Buy this</h6>', unsafe_allow_html=True)
streamlit.markdown('<h1 class="title">The Endocannabinoid System Research Company</h1>', unsafe_allow_html=True)
#streamlit.set_page_config(page_title='The Endocannabinoid System Research Company')

## ACTIVITY
columns = [
    "Name", "Date", "Heart Rate",
    "Perfusion Index", "Oxygen Saturation", "Product", "Price"
]
Activity = pandas.DataFrame(columns=columns)
streamlit.dataframe(Activity.tail(1), use_container_width=True)

with streamlit.form("ESRCActivity"):
   Name = streamlit.text_input("Name (cap-sensitive)")
   HeartRate = streamlit.text_input("Heart Rate")
   PerfusionIndex = streamlit.text_input("Perfusion Index")
   OxygenSaturation = streamlit.text_input("Oxygen Saturation")
   col1, col2, col3 = streamlit.columns(3)
   with col1:
       Product = streamlit.selectbox("Product",
    ["Flower", "Concentrate", "Tincture", "Beverage", "Edible", "Vapor", "Topical"]
)
   with col2:
       Amount = streamlit.text_input("grams")
   with col3:
       Price = streamlit.text_input("dollars, USD")
   submitted = streamlit.form_submit_button("Submit")
   if submitted:
       streamlit.dataframe(Activity)


## Activity INTERFACE
with streamlit.form("Name"):
   Name = streamlit.text_input("Name (cap-sensitive)")
   submitted = streamlit.form_submit_button("Submit")
   if "df_user" not in streamlit.session_state:
       streamlit.session_state.df_user = Activity['Name']str.contains(Name)
   if "df_financial" not in streamlit.session_state:
       streamlit.session_state.df_financial = Activity['Name', 'Date', 'Price']str.contains(Name)
   if "df_HR" not in streamlit.session_state:
       streamlit.session_state.df_HR = Activity['Name', 'Date', 'Heart Rate']str.contains(Name)
   if "df_Oxy" not in streamlit.session_state:
       streamlit.session_state.df_Oxy = Activity['Name', 'Date', 'Oxygen Saturation']str.contains(Name)
   if "df_PI" not in streamlit.session_state:
       streamlit.session_state.df_PI = Activity['Name', 'Date', 'Perfusion Index']str.contains(Name)

   # Get indices or rows from the filtered reference DataFrame
   df_productselect = streamlit.multiselect("Select the product:",options = df_user["Product"].unique(),default = df_user["Product"].unique())
   if "df_forproduct" not in streamlit.session_state:
       streamlit.session_state.df_forproduct = df_user[df_user["Product"].isin(df_productselect)]
   if "filtered_indices" not in streamlit.session_state:
       streamlit.session_state.filtered_indices = df_forproduct[df_forproduct.iloc[:, 0] == Name].index
    
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
if submitted:
   streamlit.display(streamlit_graphs)




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
