import streamlit as streamlit
import pandas as pandas
streamlit.header("The Endocannabinoid System Research Company")
streamlit.subheader("The Gazette of the United States")
streamlit.text("The Holy Grace adopts Biogeochemistry. The Holy Trinity struck Flesh and Blood. The Holy CEE claims the United States of America.")
Job = streamlit.slider("Post:", 0, 10,step=1, )
Vision = streamlit.scatter_chart(data=Job, x=10-Job, y=Job, x_label="Guns", y_label="Butter")
streamlit.text("Seek an endocannabinoid.")
