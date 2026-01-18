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


            
with streamlit.form("ESRCActivity"):
   streamlit.write("Use the same name as before if you are a return user *cap-sensitive*")
    streamlit.write("Name:") 
    name = streamlit.text_input("Name")
    streamlit.write("Heart Rate")
    heartrate = streamlit.text_input("Heart Rate")
    streamlit.write("Perfusion Index:")
    perfusionindex = streamlit.text_input("Perfusion Index")
    streamlit.write("Oxygen Saturation:")
    oxygensaturation = streamlit.text_input("Oxygen Saturation")
    col1, col2, col3 = streamlit.columns(3)
    with col1:
        streamlit.write("Product")
        streamlit.write("Flower")
        streamlit.write("Concentrate")
        streamlit.write("Tincture")
        streamlit.write("Beverage")
        streamlit.write("Edible")
        streamlit.write("Vapor")
        streamlit.write("Topical")
    with col2:
        floweramount = streamlit.text_input("Amount")
        concentrateamount = streamlit.text_input("Amount")
        tinctureamount = streamlit.text_input("Amount")
        beverageamount = streamlit.text_input("Amount")
        edibleamount = streamlit.text_input("Amount")
        vaporamount = streamlit.text_input("Amount")
        topicalamount = streamlit.text_input("Amount")
     with col3:
        flowerprice = streamlit.text_input("Price")
        concentrateprice = streamlit.text_input("Price")
        tinctureprice = streamlit.text_input("Price")
        beverageprice = streamlit.text_input("Price")
        edibleprice = streamlit.text_input("Price")
        vaporprice = streamlit.text_input("Price")
        topicalprice = streamlit.text_input("Price")
    submitted = streamlit.form_submit_button("Submit")
 if submitted:
      streamlit.append("Activity")



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


## ACTIVITY

if "Activity" not in streamlit.session_state:
    streamlit.session_state.Activity - pandas.DataFrame(
        {
            "Date": [date.today()],
            "Name":[0],
            "Heart Rate":[0],
            "Perfusion Index":[0],
            "Oxygen Saturation":[0],
            "floweramount":[0],
            "flowerprice":[0],
            "concentrateamount":[0],
            "concentrateprice":[0],
            "tinctureamount":[0],
            "tinctureprice":[0],
            "beverageamount":[0],
            "beverageprice":[0],
            "edibleamount":[0],
            "edibleprice:[0],
            "vaporamount":[0],
            "vaporprice":[0],
            "Topical":[0],
            "topicalprice":[0],
        }
    )
column_config = {
    "Date": st.column_config.DateColumn(
        "Date",
        format="YYYY-MM-DD"
    )
}
for i in range(1, 13):
    column_config[f"Col_{i}"] = st.column_config.NumberColumn(
        f"Col {i}",
        min_value=0,
        step=1
    )
edited_df = st.data_editor(
    st.session_state.df,
    num_rows="dynamic",
    use_container_width=True,
    column_config=column_config
)
st.session_state.df = edited_df

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
