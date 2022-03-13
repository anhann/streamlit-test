import streamlit as st
import numpy as np
import pandas as pd
st.title('Bomb game')
def color_code(val):
        if val == 'X':
                color = 'green'
        elif val == 'B':
                color = 'red'
        elif val == 'D':
                color = 'yellow' 
        return f'background-color: {color}'

st.write('To play, input the number of column & row you want (>=3 or else you could not win:))')
n=st.number_input('Pick a number',3,99)
st.write('This is a simple bomb game. The number of column and row is {} each. There will be {} bombs in the field'.format(int(n),int(n)))
st.write('Whenever you input a row & column number (for ex 3 4 - remember to include space between 2 numbers!), I will inform you on the bomb risk.In all cases, D letter means Danger zone where you are close to bomb, X letter mean Safer zone.')
st.write('If you can survive {} times of input, you win!'.format(int(n*2)))
st.write('Please choose the difficulty level. Input 1 for harder mode, which means there is only alert if you near 2 bombs and above.\n2 is for easier mode, means I will inform the number of bomb around your input area')
m=st.number_input('Pick a number',1,2)
import random
a=np.array([['0']*n for i in range(n)])
#for col in a:
        #st.write (' '.join(col))
st.dataframe(a)
bomb_list=[]
input_list=[]
text_input_list=[str(i+1) for i in range(n*2)]
while len(bomb_list)<=(n-1):
        l=[[random.randint(0,n-1),random.randint(0,n-1)]]
        if l[0] not in bomb_list:
                bomb_list+=l    
# playing part:
if m==2:
        while len(input_list)<n*2:
                #st.text_input('Please input your row & column numbers the {} time - please include space between 2 numbers'.format(text_input_list[len(input_list)]))
                l=[int(i) for i in st.text_input('Please input your row & column numbers the {} time - please include space between 2 numbers'.format(text_input_list[len(input_list)])).split()]
                if l[0]>n-1 or l[1]>n-1 or l[0]<0 or l[1]<0:
                        st.write('Input out of table range')
                        continue
                if l not in input_list:
                        input_list+=[l]
                else:
                        st.write('You enter the same cell. Please try again!')
                        continue
                if l in bomb_list:
                        st.write('Oops! You step on bomb. End game.')
                        a[l[0]][l[1]]='B'
                        st.dataframe(a)
                        break
                else:
                        count=0
                        for i in range(len(bomb_list)):
                                if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                                        count+=1
                                        a[l[0]][l[1]]='D'
                        if count==0:
                                st.write('Safe zone - no bomb around!')
                                a[l[0]][l[1]]='X'
                        elif count>=1:
                                st.write ('Watch out! You are close to {} bombs.'.format(count))
                #for col in a:
                #print (' '.join(col))
                #st.dataframe(a.style.applymap(color_code))
                st.dataframe(a)
                st.write('Fighting! Only {} more times to win'.format(n*2-len(input_list)))

                if len(input_list)==n*2:
                        #st.dataframe(a.style.applymap(color_code))
                        #for col in a:
                                #print (' '.join(col))
                        st.write('Congratulation! You win')
                continue

if m==1:
        while len(input_list)<n*2:
                x= st.text_input('Please input your row & column numbers the {} time - please include space between 2 numbers'.format(text_input_list[len(input_list)]))
                l=[int(i) for i in x.split()]
                if l[0]>n-1 or l[1]>n-1 or l[0]<0 or l[1]<0:
                        st.write('Input out of table range')
                        continue
                if l not in input_list:
                        input_list+=[l]
                else:
                        st.write('You enter the same cell. Please try again!')
                        continue
                if l in bomb_list:
                        st.write('Oops! You step on bomb. End game.')
                        a[l[0]][l[1]]='B'
                        st.dataframe(a)
                        break
                else:
                        count=0
                        for i in range(len(bomb_list)):
                                if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                                        count+=1
                        if count<=1:
                                st.write('0 or 1 bombs around')
                                a[l[0]][l[1]]='X'
                        elif count>=2:
                                st.write ('Watch out! You are close to +2 bombs.')
                                a[l[0]][l[1]]='D'
                #for col in a:
                #print (' '.join(col))
                #st.dataframe(a.style.applymap(color_code))
                st.dataframe(a)
                st.write('Fighting! Only {} more times to win'.format(n*2-len(input_list)))

                if len(input_list)==n*2:
                        #st.dataframe(a.style.applymap(color_code))
                        #for col in a:
                                #print (' '.join(col))
                        st.write('Congratulation! You win')
                continue
