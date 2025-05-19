import streamlit as st 
from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-id-en")
#UI Streamlit
st.title("Translator Bahasa Indonesia ke Inggris")
st.write("masukan teks yang ingin diterjemahkan")

text_input = st.text_area("tulis kalimat bahasa indonesia disini")

if st.button("Terjemahkan"):
    if text_input.strip():
        with st.spinner("Menerjemahkan..."):
            result = translator(text_input, max_length=100)[0]["translation_text"]
            st.success("berhasil diterjemahkan:")
            st.write(f"**{result}**")
    else:
        st.warning("tolong masukan teks terlebih dahulu")