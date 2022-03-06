# -*- coding: utf-8 -*-
"""Games to streamlit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NGVPjUCPszdi_aHZAYcq0N-PYX58C_MI
"""
import streamlit as st
import datetime
import lunarcalendar
from lunarcalendar import Converter, Solar, Lunar
st.title('Check your Moon phase')
st.write('Please input your name')
name=st.text_input('Name')
st.write('Please input your date of birth (year, month, day), for ex: 1996 05 28')
dob=st.date_input('Date of birth')
#year,month,date=[int(i) for i in dob.split()]
import datetime
import lunarcalendar
from lunarcalendar import Converter, Solar, Lunar
def moon_phase():
  solar = Solar(dob)
  lunar = Converter.Solar2Lunar(solar)
  if lunar.day <=1:
    phase='New Moon'
    char='Creative, Adventurous, Impulsive'
  elif lunar.day <7:
    phase='Waxing Crescent'
    char= 'Ambitious, Diligent, Risk averse'
  elif lunar.day <9:
    phase='First Quarter'
    char='Talented, Brave, Patient'
  elif lunar.day <14:
    phase='Waxing Gibbous'
    char= 'Calm, Gracious, Perfectionist'
  elif lunar.day <17:
    phase='Full Moon'
    char= 'Sensitive, Empathetic, Emotional'
  elif lunar.day <22:
    phase='Waning Gibbous'
    char='Meditative, Analytical, Judgmental'
  elif lunar.day <24:
    phase='Third Quarter'
    char='Loyal, Emotional, Sociable'
  elif lunar.day >=24:
    phase='Waning Crescent'
    char= 'Imaginative, Divergent, Lonesome'
  st.write ('Hi {}, your Moon phase is \033[32m {}\033[30m, and your characteristics are \033[32m {}\033[30m.'.format(name,phase,char))
