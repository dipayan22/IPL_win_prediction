import streamlit as st
import pickle
import pandas as pd

st.title('IPL WIN PREDICTION')

col1,col2=st.columns(2)

teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe=pickle.load(open('ipl.pkl','rb'))

with col1:
    batting_team=st.selectbox('Select the Bating team',sorted(teams))

with col2:
    bowling_team=st.selectbox('Select the Bowling team',sorted(teams))

selected_city=st.selectbox('Selct the Venue of the Match',sorted(cities))

target=st.number_input("Target")

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input('Score')

with col4:
    overs=st.number_input('Over Completed')

with col5:
    wicket=st.number_input('Wickets')

if st.button('Predict Probablity'):
    run_left=target-score

    ball_left=120-(overs*6)

    wickets=10-wicket

    crr=score/overs
    rrr=(run_left*6)/ball_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[run_left],'balls_left':[ball_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result=pipe.predict_proba(input_df)

    loss=result[0][0]
    win=result[0][1]

    st.header(batting_team+"- "+str(round(win*100))+"%")
    st.header(bowling_team+"- "+str(round(loss*100))+"%")
    

