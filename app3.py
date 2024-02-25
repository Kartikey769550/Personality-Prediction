import streamlit as st
import pandas as pd
import time
import numpy as np
from PIL import Image
# importing cluster images
img0 = Image.open('cluster0.png')
img1 = Image.open('cluster1.png')
img2 = Image.open('cluster2.png')
img3 = Image.open('cluster3.png')
img4 = Image.open('cluster4.png')


import matplotlib.pyplot as plt
def app():
    st.markdown(
        '<h2 style="background-color:Grey; border-radius:5px; padding:5px 15px ; text-align:center ; font-family:arial;color:white"><i>Personality Prediction</i></h2>',
        unsafe_allow_html=True)
    st.subheader("- Wanna Predict your Personality ! TRY NOW BY ANSWERING FEW QUESTIONS...")
    col1, col2 , col3 = st.beta_columns((1, 2, 1))
    col4, col5, col6, col7 = st.beta_columns((1, 1, 1, 1))
    col8, col9, col10 , col11 = st.beta_columns((1, 1, 1, 1))
    col12, col13, col14, col15 = st.beta_columns((1, 1, 1, 1))
    mul_lr = pd.read_pickle('kmfinal32213.pickle')

    def format_func1(options):
        return choices1[options]
    def format_func2(options):
        return choices2[options]
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
        age = st.selectbox("Age:", range(17, 29), 1)

    with col8:
        st.markdown(
            '<h4 style="background-color:lightblue;border: inset 2px black; border-radius:2px; padding:2px 15px "; > <center><i>Questionnaire:</i></center></h4>',
            unsafe_allow_html=True)

    with col12:
        EXT1 = st.selectbox('Q1] I am the life of the party', options=list(choices1.keys()), format_func=format_func1)
        EXT5 = st.selectbox('Q5] I start conversations', options=list(choices1.keys()), format_func=format_func1)
        EXT9 = st.selectbox('Q9] I dont mind being the center of attention', options=list(choices1.keys()),format_func=format_func1)
        EST3 = st.selectbox('Q13] I worry about things', options=list(choices1.keys()), format_func=format_func1)
        EST7 = st.selectbox('Q17] I change my mood a lot', options=list(choices1.keys()), format_func=format_func1)
        AGR1 = st.selectbox('Q21] I feel little concern for others', options=list(choices1.keys()), format_func=format_func1)
        AGR5 = st.selectbox('Q25] I am not interested in other peoples problems', options=list(choices1.keys()), format_func=format_func1)
        AGR9 = st.selectbox('Q29] I feel others emotions', options=list(choices1.keys()), format_func=format_func1)
        CSN3 = st.selectbox('Q33] I pay attention to details', options=list(choices1.keys()), format_func=format_func1)
        CSN7 = st.selectbox('Q37] I like order', options=list(choices1.keys()), format_func=format_func1)
        OPN1 = st.selectbox('Q41] I have a rich vocabulary', options=list(choices1.keys()), format_func=format_func1)
        OPN5 = st.selectbox('Q45] I have excellent ideas', options=list(choices1.keys()), format_func=format_func1)
        OPN9 = st.selectbox('Q49] I spend time reflecting on things', options=list(choices1.keys()), format_func=format_func1)

    with col13:
        EXT2 = st.selectbox('Q2] I dont talk a lot', options=list(choices1.keys()), format_func=format_func1)
        EXT6 = st.selectbox('Q6] I have little to say', options=list(choices1.keys()), format_func=format_func1)
        EXT10 = st.selectbox('Q10] I am quiet around strangers', options=list(choices1.keys()), format_func=format_func1)
        EST4 = st.selectbox('Q14] I seldom feel blue', options=list(choices1.keys()), format_func=format_func1)
        EST8 = st.selectbox('Q18] I have frequent mood swings', options=list(choices1.keys()), format_func=format_func1)
        AGR2 = st.selectbox('Q22] I am interested in people', options=list(choices1.keys()), format_func=format_func1)
        AGR6 = st.selectbox('Q26] I have a soft heart', options=list(choices1.keys()), format_func=format_func1)
        AGR10 = st.selectbox('30] I make people feel at ease', options=list(choices1.keys()), format_func=format_func1)
        CSN4 = st.selectbox('Q34] I make a mess of things', options=list(choices1.keys()), format_func=format_func1)
        CSN8 = st.selectbox('Q38] I shirk my duties', options=list(choices1.keys()), format_func=format_func1)
        OPN2 = st.selectbox('Q42] I have difficulty understanding abstract ideas', options=list(choices2.keys()), format_func=format_func2)
        OPN6 = st.selectbox('Q46] I do not have a good imagination', options=list(choices2.keys()), format_func=format_func2)
        OPN10 = st.selectbox('Q50] I am full of ideas', options=list(choices1.keys()), format_func=format_func1)

    with col14:
        EXT3 = st.selectbox('Q3] I feel comfortable around people', options=list(choices1.keys()), format_func=format_func1)
        EXT7 = st.selectbox('Q7] I talk to a lot of different people at parties', options=list(choices1.keys()), format_func=format_func1)
        EST1 = st.selectbox('Q11] I get stressed out easily', options=list(choices1.keys()), format_func=format_func1)
        EST5 = st.selectbox('Q15] I am easily disturbed:', options=list(choices1.keys()), format_func=format_func1)
        EST9 = st.selectbox('Q19] I get irritated easily', options=list(choices1.keys()), format_func=format_func1)
        AGR3 = st.selectbox('Q23] I insult people', options=list(choices1.keys()), format_func=format_func1)
        AGR7 = st.selectbox('Q27] I am not really interested in others', options=list(choices1.keys()), format_func=format_func1)
        CSN1 = st.selectbox('Q31] I am always prepared', options=list(choices1.keys()), format_func=format_func1)
        CSN5 = st.selectbox('Q35] I get chores done right away', options=list(choices1.keys()), format_func=format_func1)
        CSN9 = st.selectbox('Q39] I follow a schedule', options=list(choices1.keys()), format_func=format_func1)
        OPN3 = st.selectbox('Q43] I have a vivid imagination', options=list(choices1.keys()), format_func=format_func1)
        OPN7 = st.selectbox('Q47] I am quick to understand things', options=list(choices1.keys()), format_func=format_func1)

    with col15:
        EXT4 = st.selectbox('Q4] I keep in the background', options=list(choices1.keys()), format_func=format_func1)
        EXT8 = st.selectbox('Q8] I dont like to draw attention to myself', options=list(choices1.keys()), format_func=format_func1)
        EST2 = st.selectbox('Q12] I am relaxed most of the time', options=list(choices1.keys()), format_func=format_func1)
        EST6 = st.selectbox('Q16] I get upset easily', options=list(choices1.keys()), format_func=format_func1)
        EST10 = st.selectbox('Q20] I often feel blue', options=list(choices1.keys()), format_func=format_func1)
        AGR4 = st.selectbox('Q24] I sympathize with others feelings', options=list(choices1.keys()), format_func=format_func1)
        AGR8 = st.selectbox('Q28] I take time out for others', options=list(choices1.keys()), format_func=format_func1)
        CSN2 = st.selectbox('Q31] I leave my belongings around', options=list(choices1.keys()), format_func=format_func1)
        CSN6 = st.selectbox('Q36] I often forget to put things back in their proper place',options=list(choices1.keys()), format_func=format_func1)
        CSN10 = st.selectbox('Q40] I am exacting in my work', options=list(choices1.keys()), format_func=format_func1)
        OPN4 = st.selectbox('Q44] I am not interested in abstract ideas', options=list(choices2.keys()), format_func=format_func2)
        OPN8 = st.selectbox('Q48] I use difficult words', options=list(choices2.keys()), format_func=format_func2)

    xyze = np.array([EXT1, EXT2, EXT3, EXT4, EXT5, EXT6, EXT7, EXT8, EXT9, EXT10,
                     EST1, EST2, EST3, EST4, EST5, EST6, EST7, EST8, EST9, EST10,
                     AGR1, AGR2, AGR3, AGR4, AGR5, AGR6, AGR7, AGR8, AGR9, AGR10,
                     CSN1, CSN2, CSN3, CSN4, CSN5, CSN6, CSN7, CSN8, CSN9, CSN10,
                     OPN1, OPN2, OPN3, OPN4, OPN5, OPN6, OPN7, OPN8, OPN9, OPN10])

    #if submit_button:
    if st.button('Submit'):
        result = mul_lr.predict([xyze])
        latest_iteration = st.empty()
        progress = st.progress(0)
        for i in range(100):
            latest_iteration.info(f' {i+1} %')
            progress.progress(i+1)
            time.sleep(0.1)
        time.sleep(0.2)
        latest_iteration.empty()
        progress.empty()
        time.sleep(0.1)
        xyy = st.balloons()

        time.sleep(1)
        xyy.empty()
        d1 = [{'EXT1': EXT1, 'EXT2': EXT2, 'EXT3': EXT3, 'EXT4': EXT4, 'EXT5': EXT5, 'EXT6': EXT6, 'EXT7': EXT7,
               'EXT8': EXT8, 'EXT9': EXT9, 'EXT10': EXT10,
               'EST1': EST1, 'EST2': EST2, 'EST3': EST3, 'EST4': EST4, 'EST5': EST5, 'EST6': EST6, 'EST7': EST7,
               'EST8': EST8, 'EST9': EST9, 'EST10': EST10,
               'AGR1': AGR1, 'AGR2': AGR2, 'AGR3': AGR3, 'AGR4': AGR4, 'AGR5': AGR5, 'AGR6': AGR6, 'AGR7': AGR7,
               'AGR8': AGR8, 'AGR9': AGR9, 'AGR10': AGR10,
               'CSN1': CSN1, 'CSN2': CSN2, 'CSN3': CSN3, 'CSN4': CSN4, 'CSN5': CSN5, 'CSN6': CSN6, 'CSN7': CSN7,
               'CSN8': CSN8, 'CSN9': CSN9, 'CSN10': CSN10,
               'OPN1': OPN1, 'OPN2': OPN2, 'OPN3': OPN3, 'OPN4': OPN4, 'OPN5': OPN5, 'OPN6': OPN6, 'OPN7': OPN7,
               'OPN8': OPN8, 'OPN9': OPN9, 'OPN10': OPN10}]
        my_data = pd.DataFrame(d1)

        col_list = list(my_data)
        ext = col_list[0:10]
        est = col_list[10:20]
        agr = col_list[20:30]
        csn = col_list[30:40]
        opn = col_list[40:50]

        my_sums = pd.DataFrame()
        my_sums['extroversion'] = my_data[ext].sum(axis=1) / 10
        my_sums['neurotic'] = my_data[est].sum(axis=1) / 10
        my_sums['agreeable'] = my_data[agr].sum(axis=1) / 10
        my_sums['conscientious'] = my_data[csn].sum(axis=1) / 10
        my_sums['openness'] = my_data[opn].sum(axis=1) / 10
        my_sums['cluster'] = result
        print('Sum of my question groups')
        print(my_sums)
        xl = my_sums['cluster'].iloc[-1]
        col16, col17  = st.beta_columns((1, 1))
        with col16:
            if xl==0:
                st.image(img0)
            elif xl==1:
                st.image(img1)
            elif xl==2:
                st.image(img2)
            elif xl==3:
                st.image(img3)
            elif xl==4:
                st.image(img4)
    

