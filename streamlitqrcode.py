import streamlit as st
import qrcode
from datetime import datetime

st.title("QRCode Generator Program")

# Initialize a session state to store the input data and focus flag
if 'input_data' not in st.session_state:
    st.session_state.input_data = ""
    st.session_state.focus_input = True

# Text input for QR code data
data = st.text_input("Please enter your QR Code data:", value=st.session_state.input_data)

# Button to generate QR Code
if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(data)
        img_path = f"qrcodeimg/{datetime.today().strftime('%Y%m%d%H%M%S')}.png"
        img.save(img_path)
        # Preview image
        st.image(img_path, width=300)
        st.success("QRCode image saved")
        # Clear input data
        st.session_state.input_data = ""
        st.session_state.focus_input = True
    else:
        st.warning("Please enter your data before generating QR Code")

# Use JavaScript to set focus on the input field
if st.session_state.focus_input:
    st.write(
        f"""
        <script>
            document.querySelector('input').focus();
        </script>
        """,
        unsafe_allow_html=True
    )
    st.session_state.focus_input = False
