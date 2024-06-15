import streamlit as st
import requests
import time
import base64
import os




st.set_page_config(
    page_title="Dannon QR",
    page_icon="🧊",
)

params = st.query_params

if "key" in params:

    st.title("Dannon QR")

    # key = st.text_input("Enter your pass_key")

    r = requests.get(
        url=f"https://server.dannonapi.com/v1/auth/user/managers/{params.key}/"

    )

    time.sleep(3)
    con1 = st.container(border=True)


    if r.status_code == 200:
        # st.write(r.json())
        con1.write("User Details")
        con1.write(f"First Name: --------     {str(r.json()['first_name']).capitalize()}")
        con1.write(f"Last Name: --------     {str(r.json()['last_name']).capitalize()}")
        con1.write(f"Email: --------     {str(r.json()['email']).capitalize()}")
        con1.write(f"Role: --------     {str(r.json()['role']).capitalize()}")
        con1.write(f"UUID: --------     {str(r.json()['id']).upper()}")

    else:
        st.write(r.status_code)
        # st.write(r.json())
        st.write(r.text)


else:
    st.write("No key found in URL")

