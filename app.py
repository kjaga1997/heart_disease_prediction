# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
pickle_in= open('heart_disease.pkl','rb')
model= pickle.load(pickle_in)

def heart_disease(male, age, currentSmoker, cigsPerDay, BPMeds,prevalentStroke, prevalentHyp, diabetes, totChol, sysBP,
diaBP, BMI, heartRate, glucose):
    prediction= model.predict([[male, age, currentSmoker, cigsPerDay, BPMeds,prevalentStroke, prevalentHyp, diabetes, totChol, sysBP,
diaBP, BMI, heartRate, glucose]])
    
    if prediction==0:
        pred='No heart disease'
    else:
        pred='yes having heart disease'
    return pred

def main():
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Heart disease prediction</h1> 
    </div> 
    """
     
    st.markdown(html_temp, unsafe_allow_html = True)
    
    male = st.number_input('Enter Gender')
    age = st.number_input('Enter age')
    currentSmoker = st.number_input('current smoker or not')
    cigsPerDay= st.number_input('no. of cigs per day')
    BPMeds= st.number_input('Enter bpmeds')
    prevalentStroke = st.number_input('Enter prevalent stroke')
    prevalentHyp = st.number_input('Enter prevalent hyp')
    diabetes = st.number_input('diabetics')
    totChol= st.number_input('Alcohol content')
    sysBP= st.number_input('Enter sysbp')
    diaBP= st.number_input('Enter diabp')
    BMI = st.number_input('Enter BMI')
    heartRate= st.number_input('Enter Heart rate')
    glucose = st.number_input('Glucose value')
    if st.button('predict'):
        result = heart_disease(male, age, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, glucose)
        st.success(result)
if __name__=='__main__':
    main()
