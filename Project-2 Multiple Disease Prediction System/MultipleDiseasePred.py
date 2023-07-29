# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:09:26 2023

@author: taman
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading saved models
diabetes_model=pickle.load(open("C:/Users/taman/Desktop/Multiple Disease Prediction/diabetes_model.sav",'rb'))
heart_model=pickle.load(open("C:/Users/taman/Desktop/Multiple Disease Prediction/heart_model.sav",'rb'))
#parkinson_model=pickle.load(open("C:/Users/taman/Desktop/Multiple Disease Prediction/parkinson_model.sav",'rb'))

#side bar/navigation
with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',['Diabetes Prediction','Heart Disease Prediction'],icons=['activity','heart'],default_index=0)
    
    
#Diabetes Prediction System
if (selected=='Diabetes Prediction'):
    #page title
    st.title('Diabetes Prediction using ML')
    
    Pregnancies=st.text_input('Number of Pregnancies')
    Glucose=st.text_input('Glucose level')
    BloodPressure=st.text_input('Blood Pressure Value')
    SkinThickness=st.text_input('Skin Thickness Value')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    Age=st.text_input('Age of the person')
    
    #code for Prediction
    diab_diagnosis=''
    
    #creating a button
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if diab_prediction:
            diab_diagnosis='The person is Diabetic'
        else:
            diab_diagnosis='The person is not diabetic'
    st.success(diab_diagnosis)
   
#Heart Disease Prediction
#if (selected=='Heart Disease Prediction'):
    #page title
#    st.title('Heart Disease Prediction using ML')
    
 #   age=st.text_input('Age')
  #  sex=st.text_input('Sex (0 = Female; 1 = Male)')
   # chestpain=st.text_input('Chest Pain 0-3')
    #restingbp=st.text_input('Resting Blood Pressure')
    #cholestrol=st.text_input('Serum cholestrol in mg/dl')
    #bloodsugar=st.text_input('fasting blood sugar>120 mg/dl (1 = True; 0 = False)')
    #ecardio=st.text_input('Resting electrocardiagraphic results')
    #maxheartrate=st.text_input('Maximum heart rate achieved')
    #angina=st.text_input('Exercise induced angina (1 = yes; 0 = no)')
    #oldpeak=st.text_input('ST depression induced by exercise relative to rest')
    #slope=st.text_input('The slope of the peak exercise ST segment')
    #number=st.text_input('Number of major vessels(0-3) colored by flourosopy')
    #thal=st.text_input('thal(0 = normal; 1 = fixed defect; 2 = reversable effect)')
    
    #heart_diag=''
    
    #if st.button('Heart Disease Test Result'):
     #   heart_prediction=heart_model.predict([[age,sex,chestpain,restingbp,cholestrol,bloodsugar,ecardio,maxheartrate,angina,oldpeak,slope,number,thal]])
      #  if heart_prediction:
       #     heart_diag='The person has a Defective Heart'
        #else:
         #   heart_diag='The person has a Healthy Heart'
    #st.success(heart_diag)
    
    # Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex')
        
    with col3:
        cp = st.number_input('Chest Pain types')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    #Presentation Link https://www.canva.com/design/DAFn9vYon4Y/APVqPhZKu1vfsC7mqvApzw/edit
    
#if (selected=='Parkinsons Disease Prediction'):
    #page title
#    st.title('Parkinsons Disease Prediction using ML')
    
 #   col1, col2, col3, col4, col5 = st.columns(5)  
    
  #  with col1:
   #     fo = st.text_input('MDVP:Fo(Hz)')
        
    #with col2:
     #   fhi = st.text_input('MDVP:Fhi(Hz)')
        
   #  with col3:
   #      flo = st.text_input('MDVP:Flo(Hz)')
        
   #  with col4:
   #      Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
   #  with col5:
   #      Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
   #  with col1:
   #      RAP = st.text_input('MDVP:RAP')
        
   #  with col2:
   #      PPQ = st.text_input('MDVP:PPQ')
        
   #  with col3:
   #      DDP = st.text_input('Jitter:DDP')
        
   #  with col4:
   #      Shimmer = st.text_input('MDVP:Shimmer')
        
   #  with col5:
   #      Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
   #  with col1:
   #      APQ3 = st.text_input('Shimmer:APQ3')
        
   #  with col2:
   #      APQ5 = st.text_input('Shimmer:APQ5')
        
   #  with col3:
   #      APQ = st.text_input('MDVP:APQ')
        
   #  with col4:
   #      DDA = st.text_input('Shimmer:DDA')
        
   #  with col5:
   #      NHR = st.text_input('NHR')
        
   #  with col1:
   #      HNR = st.text_input('HNR')
        
   #  with col2:
   #      RPDE = st.text_input('RPDE')
        
   #  with col3:
   #      DFA = st.text_input('DFA')
        
   #  with col4:
   #      spread1 = st.text_input('spread1')
        
   #  with col5:
   #      spread2 = st.text_input('spread2')
        
   #  with col1:
   #      D2 = st.text_input('D2')
        
   #  with col2:
   #      PPE = st.text_input('PPE')
        
    
    
   #  # code for Prediction
   #  parkinsons_diagnosis = ''
    
   #  # creating a button for Prediction    
   #  if st.button("Parkinson's Test Result"):
   #      parkinsons_prediction = parkinson_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
   #      if (parkinsons_prediction[0] == 1):
   #        parkinsons_diagnosis = "The person has Parkinson's disease"
   #      else:
   #        parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
   # st.success(parkinsons_diagnosis)

    
    
    
#119.992 157.302 74.997 0.00784 0.00007 0.0037 0.00554 0.01109 0.04374 0.426 0.02182 0.0313 0.02971 0.06545 0.02211 21.033 0.414783 0.815285 -4.813031 0.266482 2.301442 0.284654