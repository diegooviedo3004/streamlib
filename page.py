import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Just Testing",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#hide_st_style = """
          #  <style>
            #MainMenu {visibility: hidden;}
         #   footer {visibility: hidden;}
         #   header {visibility: hidden;}
         #   </style>
         #   """
#st.markdown(hide_st_style, unsafe_allow_html=True)



st.title('Generate random name for your pet :dog:')
st.caption('Hope it works!')

st.sidebar.title('Check my other apps')
link = '[*GitHub*](http://github.com/diegooviedo3004)'
st.sidebar.markdown(link, unsafe_allow_html=True)


st.button('Generate')