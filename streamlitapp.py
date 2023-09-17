import streamlit as st
import pandas as pd
import numpy as np
import colorAndShape as cs
DATE_COLUMN = 'date/time'

st.title('Drug Wizard')
img = st.file_uploader("file plesas")
if img is not None:
    x = open("/tmp/incoming/onefile", "wb+")
    x.write(img.read())
    x.close()
    cs.identify("/tmp/incoming/onefile")
    st.image('drugWizard.webp', caption = None, width=250)
