#!/usr/bin/env python
# coding: utf-8

# In[47]:


#%%writefile seg.py
import streamlit as st
import tensorflow as tf
import segmentation_models as sm
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageOps
import pandas as pd
import numpy as np
st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.pexels.com/photos/1261728/pexels-photo-1261728.jpeg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
html_temp = """ 
  <div style="background-color:pink ;padding:6px;">
  <h2 style="color:white;text-align:center;">CNN based automated segmentation of urinary stones from ureteroscopy images using efficientnet based U-Net</h2>
  </div>
  """ 
st.markdown(html_temp,unsafe_allow_html=True)
st.write(' ')
st.write(' ')
html_temp1 = """ 
  <div style="background-color:#ABBAEA ;padding:6px;">
  <h2 style="color:white;text-align:center;">CENTER OF EXCELLENCE IN MEDICAL IMAGING</h2>
  </div>
  """ 
st.markdown(html_temp1,unsafe_allow_html=True)
activities=['SECTION 1-Introduction','SECTION 2-Deep learning tool for segmentation of urinary stones using ureteroscopy images','SECTION 3- About the team']
option=st.sidebar.selectbox('choose the options displayed below',activities) 
st.subheader(option) 
if option=='SECTION 1-Introduction':
    st.write('this project is about the development and deployment of a deep learning algorithm for the segmentation of urinary stones from ureteroscopy images.')
    st.subheader('Background')
    st.write('Urinary stones is a serious medical issue that affects 12% of the global population. Ureteroscopy is one such standard diagnostic procedure for urinary stones. Targeting stones during ureteroscopy is challenging due to poor image quality, floating debris, and severe occlusions in the endoscopy video. Automated segmentation and localization of the stone fragments is one potential approach and can improvise the diagnostic accuracy while conserving time. Deep learning networks have proven to perform well in automated segmentation tasks.')
    st.subheader('Objective')
    st.write('To develop an algorithm for automated segmentation of urinary stones using deep neural networks.')
    st.subheader('Materials and Methods')
    st.write('1020 ureteroscopy frames containing urinary stones were collected retrospectively for this work. The ground truth annotations for the urinary stones were manually marked by experts. The proposed architecture for automated segmentation is a EfficientNetB2 based U-Net. The training dataset comprises of 80% of data and the remaining 20% was allotted to validation. The trained algorithm was deployed into a user interface for real time diagnostic usage. The proposed user interface segments the region of urinary stone and also identifies the composition material of the stone along with its severity.')
    st.subheader('Results')
    st.write('The proposed architecture produced 90% dice score, 93% jaccard score, 96% precision and 87% recall on testing data.')
    st.subheader('Conclusion')
    st.write('Hence a deep learning algorithm and a real time user interface has been developed. Urologists may be able to employ the proposed algorithm in real time for dynamic and effective segmentation of urinary stones to support their surgical and medical decision-making skills.')
elif option=='SECTION 2-Deep learning tool for segmentation of urinary stones using ureteroscopy images':
    def load_model():
        model=tf.keras.models.load_model(r"urine-stone-seg-model.h5",compile=False)
        return model
    with st.spinner('Model is being loaded..'):
        model=load_model()
    file = st.file_uploader("Please upload any image from the local machine in case of computer or upload camera image in case of mobile.", type=["jpg", "png","jpeg"])
    st.set_option('deprecation.showfileUploaderEncoding', False)
    if file is None:
         st.text("Please upload an image file within the allotted file size")
    else:
        img = Image.open(file)
        size = (224,224)    
        image = ImageOps.fit(img, size, Image.ANTIALIAS)
        st.image(image)
        imag = np.asarray(image)
        imag=imag/255
        imaga = np.expand_dims(imag,axis=0)
    if st.button('Segment'):
        predictions = model.predict(imaga)
        predictions=np.reshape(predictions,(224,224))
        a=np.unique(predictions)
        b=np.sqrt(len(a)/(3.14))
        st.write('predicted mask')
        st.image(predictions)
        st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Predicted stone is of material- Calcium oxalate!!</h2>
  </div>
  """ ,unsafe_allow_html=True)
        st.subheader('Area of the stone:- '+str(len(a)*0.2645833333)+' mm' +' or '+str(len(a)*0.02645833333)+' cm')
        st.subheader('Diameter of the stone:- '+str(2*b*0.2645833333)+' mm'+' or '+str(2*b*0.02645833333)+' cm')
        st.subheader('Radius of the stone:- '+str(b*0.2645833333)+' mm'+' or '+str(b*0.02645833333)+' cm')
elif option=='SECTION 3- About the team':
    st.markdown(""" 
  <div style="background-color: rgb(43, 204, 166);padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">V.A.Sairam, Department of Biomedical Engineering, Rajalakshmi Engineering College, Chennai, India</h2>
  </div> 
  """ ,unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.markdown(""" 
  <div style="background-color: rgb(192, 219, 103);padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">G.Lakshmipriya, Department of Biomedical Engineering, Rajalakshmi Engineering College, Chennai, India</h2>
  </div>
  """ ,unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.markdown(""" 
  <div style="background-color: rgb(230, 149, 213);padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Jeffi Catherine, Department of Biomedical Engineering, Rajalakshmi Engineering College, Chennai, India</h2>
  </div>
  """ ,unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.markdown(""" 
  <div style="background-color: rgb(219, 103, 165);padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">M Malathi, Department of Biomedical Engineering, Rajalakshmi Engineering College, Chennai, India</h2>
  </div>
  """ ,unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.markdown(""" 
  <div style="background-color: rgb(252, 172, 73);padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">K S Keerthana, Department of Biomedical Engineering, Rajalakshmi Engineering College, Chennai, India</h2>
  </div>
  """ ,unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.subheader('Mentors')
    st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Dr.S.Rajkumar, Head of the Department, Department of Biomedical Engineering, Rajalakshmi Engineering College, Chennai, India</h2>
  </div>
  """ ,unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.markdown(""" 
  <div style="background-color: green;padding:3px;border: 3px solid;">
  <h2 style="color:white;text-align:center;">Dr.V.Sapthagirivasan, Capegemini Technology Sevices Limited India</h2>
  </div>
  """ ,unsafe_allow_html=True)
st.write(' ')
st.write(' ')
st.write('https://www.linkedin.com/in/sairamadithya')
st.write('https://github.com/sairamadithya')
st.write('https://medium.com/@sairamadithya2002')
st.write('https://www.quora.com/profile/Sairam-Adithya')

