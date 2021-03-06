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
try:
        st.write('To play, input the number of column & row you want (>=3 or else you could not win:))')
        n=st.number_input('Pick a number',3,99)
        st.write('This is a simple bomb game. The number of column and row is {} each. There will be {} bombs in the field.\nWhenever you input a row & column number (for ex 3 4 - remember to include space between 2 numbers!), I will inform you on the bomb risk.\nIn all cases, D letter means Danger zone, X letter mean Safer zone\nIf you can survive {} times of input, you win!'.format(n,n,n*2))
        import random
        a=np.array([['0']*n for i in range(n)])
        #for col in a:
                #st.write (' '.join(col))
        st.dataframe(a)
        bomb_list=[]
        input_list=[]
        while len(bomb_list)<=(n-1):
                l=[[random.randint(0,n-1),random.randint(0,n-1)]]
                if l[0] not in bomb_list:
                        bomb_list+=l    
        # playing part:
        while len(input_list)<n*2:
                x=st.text_input('Please input your row & column numbers - please include space between 2 numbers')
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
                        break
                else:
                        count=0
                        for i in range(len(bomb_list)):
                                if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                                        count+=1
                                        a[l[0]][l[1]]='D'
                        if count==0:
                                print('Safe zone!')
                                a[l[0]][l[1]]='X'
                        elif count>=1:
                                st.write ('Watch out! You are close to {} bombs.'.format(count))
                #for col in a:
                #print (' '.join(col))
                #st.dataframe(a.style.applymap(color_code))
                st.dataframe(a)
                st.write('Fighting! Only {} more times to win'.format(n*2-len(input_list)))   
        #st.dataframe(a.style.applymap(color_code))
        st.dataframe(a)
        #for col in a:
                #print (' '.join(col))
        if len(input_list)==n*2:
                st.write('Congratulation! You win')
     
except:
        pass
