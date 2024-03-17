import streamlit as st
import pickle

#lets load the saved vectorizer and naive model

tfidf = pickle.load(open('vectorizer.pk1', 'rb'))
model = pickle.load(open('model.pkl','rb'))

#saving streamlit code.

st.title("Email Spam Classifier")
input_sms = st.text_area("Enter message")

if st.button('Predict'):
#preprocess
transformed_sms = transform text(input_sms)
#vectorize
vector_input = tfidf.transform([transformed_sms])
#predict
result = model.predict(vector_input) [0] 
#display
if result ==1:
    st.header("Spam")
else:
    st.header("Not Spam")