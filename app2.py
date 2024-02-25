import streamlit as st
import pandas as pd
import time
import numpy as np
def app():
    st.markdown(
        '<h2 style="background-color:Grey; border-radius:5px; padding:5px 15px ; text-align:center ; font-family:arial;color:white"><i>Personality Prediction</i></h2>',
        unsafe_allow_html=True)
    st.subheader("- Wanna Predict your Personality ! TRY NOW BY ANSWERING FEW QUESTIONS...")
    col1, col2 , col3 = st.beta_columns((1, 2, 1))
    col4, col5, col6, col7 = st.beta_columns((1, 1, 1, 1))
    col8, col9, col10 , col11 = st.beta_columns((1, 1, 1, 1))
    col12, col13, col14, col15 = st.beta_columns((1, 1, 1, 1))
    mul_lr = pd.read_pickle('model1.pickle')

    def format_func1(options):
        return choices1[options]
    def format_func3(options):
        return choices3[options]
    choices1 = {1: "Strongly Dis-agree", 2: "Dis-agree", 3: "Neutral", 4: "Agree", 5: "Strongly Agree"}
    choices2 = {1: "Strongly Dis-agree", 2: "Dis-agree", 3: "Neutral", 4: "Agree", 5: "Strongly Agree"}
    choices3 = {1: "Male", 0: "Female"}

    with col1:
        st.markdown(
            '<h4 style="background-color:lightblue;border: inset 2px black; border-radius:2px; padding:2px 15px "; > <center><i>Demographic Data:</i></center></h4>',
            unsafe_allow_html=True)

    with col4:
        gender = st.selectbox('Select your gender:', options=list(choices3.keys()), format_func=format_func3)

    with col5:
        age = st.selectbox("Age:", range(17, 28), 1)

    with col8:
        st.markdown(
            '<h4 style="background-color:lightblue;border: inset 2px black; border-radius:2px; padding:2px 15px "; > <center><i>Questionnaire:</i></center></h4>',
            unsafe_allow_html=True)

    with col12:
        EXT1 = st.selectbox('Q1] I am the life of the party', options=list(choices1.keys()), format_func=format_func1)
        EST1 = st.selectbox('Q5] I get stressed out easily', options=list(choices1.keys()), format_func=format_func1)
        AGR1 = st.selectbox('Q9] I have a soft heart', options=list(choices1.keys()),format_func=format_func1)
        CSN1 = st.selectbox('Q13] I am always prepared', options=list(choices1.keys()), format_func=format_func1)
        OPN1 = st.selectbox('Q17] I have a rich vocabulary', options=list(choices1.keys()), format_func=format_func1)


    with col13:
        EXT2 = st.selectbox('Q2] I dont talk a lot', options=list(choices1.keys()), format_func=format_func1)
        EST2 = st.selectbox('Q6] I get irritated easily', options=list(choices1.keys()), format_func=format_func1)
        AGR2 = st.selectbox('Q10] I am interested in people', options=list(choices1.keys()), format_func=format_func1)
        CSN2 = st.selectbox('Q14] I leave my belongings around', options=list(choices1.keys()), format_func=format_func1)
        OPN2 = st.selectbox('Q18] I have difficulty understanding abstract ideas', options=list(choices1.keys()), format_func=format_func1)


    with col14:
        EXT3 = st.selectbox('Q3] I feel comfortable around people', options=list(choices1.keys()), format_func=format_func1)
        EST3 = st.selectbox('Q7] I worry about things', options=list(choices1.keys()), format_func=format_func1)
        AGR3 = st.selectbox('Q11] I insults people', options=list(choices1.keys()), format_func=format_func1)
        CSN3 = st.selectbox('Q15] I follow a schedule', options=list(choices1.keys()), format_func=format_func1)
        OPN3 = st.selectbox('Q19] I do not have a good imagination', options=list(choices1.keys()), format_func=format_func1)


    with col15:
        EXT4 = st.selectbox('Q4] I am quiet around strangers', options=list(choices1.keys()), format_func=format_func1)
        EST4 = st.selectbox('Q8] I change my mood a lot', options=list(choices1.keys()), format_func=format_func1)
        AGR4 = st.selectbox('Q12] I am not really interested in others', options=list(choices1.keys()), format_func=format_func1)
        CSN4 = st.selectbox('Q16] I make a mess of things', options=list(choices1.keys()), format_func=format_func1)
        OPN4 = st.selectbox('Q20] I use difficult words', options=list(choices1.keys()), format_func=format_func1)

    extroversion = (EXT1 + EXT2 + EXT3 + EXT4) / 2.50
    neuroticism = (EST1 + EST2 + EST3 + EST4) / 2.50
    agreeableness = (AGR1 + AGR2 + AGR3 + AGR4) / 2.50
    conscientiousness = (CSN1 + CSN2 + CSN3 + CSN4) / 2.50
    openness = (OPN1 + OPN2 + OPN3 + OPN4) / 2.50

    def roundfigure(a):
        x = int(a)
        y = x + 1
        z = float((x + y) / 2)
        print(x, y, z)
        import math
        if (a < z):
            n = math.floor(a)
        else:
            n = math.ceil(a)
        return n

    ext = roundfigure(extroversion)
    est = roundfigure(neuroticism)
    agr = roundfigure(agreeableness)
    csn = roundfigure(conscientiousness)
    opn = roundfigure(openness)

    xyze = np.array([gender, age, ext, est, agr, csn, opn])

    # if submit_button:
    if st.button('Submit'):
        result = mul_lr.predict([xyze])

        def listToString(result):
            str1 = ""
            for ele in result:
                str1 += ele
            return str1
        a = listToString(result)

        latest_iteration = st.empty()
        progress = st.progress(0)
        for i in range(100):
            latest_iteration.info(f' {i + 1} %')
            progress.progress(i + 1)
            time.sleep(0.1)
        time.sleep(0.2)
        latest_iteration.empty()
        progress.empty()
        time.sleep(0.1)
        xyy = st.balloons()
        st.markdown(
            f'<h2 style="background-color:Grey; border-radius:5px; padding:5px 15px ; text-align:center ; font-family:arial;color:white"><i>You are <b>{a}</b> type Personality Person</i></h2>',
            unsafe_allow_html=True)
        time.sleep(1)
        xyy.empty()
