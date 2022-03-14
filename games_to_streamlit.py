
import streamlit as st
import datetime
from lunarcalendar import Converter, Solar, Lunar

st.title('Check your Moon phase')
st.markdown('_Anh''s game_')
st.write('Please input your name')
name=st.text_input('Name')
st.write('Please input your date of birth (yy/mm/dd). You can use the selection board or manually input')
dob=st.date_input('Date of birth',value=None, min_value=datetime.date(1800, 7, 6))
#year,month,date=[int(i) for i in st.text_input('Date of birth').split()]
import datetime
import lunarcalendar
from lunarcalendar import Converter, Solar, Lunar
solar = Solar(dob.year, dob.month, dob.day)
lunar = Converter.Solar2Lunar(solar)
if lunar.day <=1:
    phase='New Moon'
    char='Creative, Adventurous, Impulsive'
elif lunar.day <7:
    phase='Waxing Crescent'
    char= 'Ambitious, Diligent, Risk averse'
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
    phase='Waning Gibbous'
    char='Meditative, Analytical, Judgmental'
elif lunar.day <24:
    phase='Third Quarter'
    char='Loyal, Emotional, Sociable'
elif lunar.day >=24:
    phase='Waning Crescent'
    char= 'Imaginative, Divergent, Lonesome'
st.write ('Hi {}, your Moon phase is {}, and your characteristics are {}'.format(name,phase,char))

