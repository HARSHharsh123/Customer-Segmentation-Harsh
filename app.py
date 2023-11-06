import warnings as w
w.filterwarnings('ignore')
import streamlit as st
import pickle

st.title("Customer Segmentation System")
st.subheader("BY HARSH SHUKLA")

input_ai = int(st.number_input("Enter Your Annual Income in (15k - 137k) "))
st.write("Annual Income Entered " + str(input_ai))

input_sc = int(st.number_input("Enter your Spending Score (1 - 100)"))
st.write("Spending Score Entered " + str(input_sc))

# Loading the pickle file
model = pickle.load(open("Customer_Segmentation_pred.pkl", 'rb'))
def customer(result):
    if result == 0:
        st.write("Moderate Annual Income as well as Moderate Spending Score")
    elif result == 1:
        st.write("High Annual Income but Less Spending Score")
    elif result == 2:
        st.write("Less Annual Income as well as Less Spending Score")
    elif result ==3:
        st.write("Less Annual Income but very high Spending Score")
    else:
        st.write("High Annual Income as well High Spending Score")

def prediction(ai , sc):
    result = model.predict([[ai , sc]])
    return result[0]

if st.button("Predict"):
    result = prediction(input_ai , input_sc)
    customer(result)
    st.write("Cluster -> " + str(result))

