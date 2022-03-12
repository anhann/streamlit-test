import streamlit as st
st.title('Bomb game')
st.write('To play, input the number of column & row you want (>=3 or else you could not win:))')
n=st.number_input('Pick a number',0)


print('This is a simple bomb game. The number of column and row is {} each. There will be {} bombs in the field.\nWhenever you input a row & column number (for ex 3 4 - remember to include space between 2 numbers!), I will inform you on the bomb risk.\nIn all cases, D letter means Danger zone, X letter mean Safer zone\nIf you can survive {} times of input, you win!'.format(n,n,n*2))
print('\nPlease choose the difficulty level. Input 1 for harder mode, which means there is only alert if you near 2 bombs and above.\n2 is for easier mode, means I will inform the number of bomb around your input area')
m=st.number_input('Pick a number',1,2)
import random
a=[['0']*n for i in range(n)]
#for col in a:
        #print (' '.join(col))
st.image(a)
bomb_list=[]
input_list=[]
while len(bomb_list)<=(n-1):
    l=[[random.randint(1,n),random.randint(1,n)]]
    if l[0] not in bomb_list:
        bomb_list+=l    
# playing part:
if m==2:
    while len(input_list)<n*2:
        st.write('Please input your row & column numbers')
        l=[int(i) for i in input().split()]
        if l[0]>n or l[1]>n or l[0]<=0 or l[1]<=0:
          st.write('Input out of table range')
          continue
        if l not in input_list:
            input_list+=[l]
        else:
            st.write('You enter the same cell. Please try again!')
            continue
        if l in bomb_list:
            st.write('Oops! You step on bomb. End game.')
            a[l[0]-1][l[1]-1]='\033[31mB\033[30m'
            break
        else:
            count=0
            for i in range(len(bomb_list)):
                if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                    count+=1
                    a[l[0]-1][l[1]-1]='\033[33mD\033[30m'
            if count==0:
                print('Safe zone!')
                a[l[0]-1][l[1]-1]='\033[32mX\033[30m'
            elif count>=1:
                st.write ('Watch out! You are close to {} bombs.'.format(count))
        #for col in a:
            #print (' '.join(col))
        st.image(a)
        st.write('Fighting! Only {} more times to win'.format(n*2-len(input_list)))
    st.image(a)
    #for col in a:
        #print (' '.join(col))
    if len(input_list)==n*2:
        print('\033[32mCongratulation! You win.\033[30m')
if m==1:
    while len(input_list)<n*2:
        st.write ('Please input your row & column numbers')
        l=[int(i) for i in input().split()]
        if l[0]>n or l[1]>n or l[0]<=0 or l[1]<=0:
          print('Input out of table range')
          continue
        if l not in input_list:
            input_list+=[l]
        else:
            st.write('You enter the same cell. Please try again!')
            continue
        if l in bomb_list:
            st.write('Oops! You step on bomb. End game.')
            a[l[0]-1][l[1]-1]='\033[31mB\033[30m'
            break
        else:
            count=0
            for i in range(len(bomb_list)):
                if abs(l[0]-bomb_list[i][0])<=1 and abs(l[1]-bomb_list[i][1])<=1:  
                    count+=1
            if count<=1:
                print('0 or 1 bombs LOL')
                a[l[0]-1][l[1]-1]='\033[32mX\033[30m'
            elif count>=2:
                st.write ('Watch out! You are close to +2 bombs.')
                a[l[0]-1][l[1]-1]='\033[33mD\033[30m'
        st.image(a)
        #for col in a:
            #print (' '.join(col))
        st.write('Fighting! Only {} more times to win'.format(n*2-len(input_list)))
    st.image(a)
    #for col in a:
        #print (' '.join(col))
    if len(input_list)==n*2:
        st.write('\033[32mCongratulation! You win.\033[30m')