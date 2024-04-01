import time
import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

st.title("Palmer's Penguins")
with st.spinner():
    time.sleep(2)
st.subheader('Use this Streamlit app to make your own scatterplot about penguins!')
penguins_df=st.file_uploader('Select your local Penguins CSV')
if penguins_df is not None:
    penguins_df=pd.read_csv(penguins_df)
else:
    penguins_df=pd.read_csv('penguins.csv')

sns.set_style('darkgrid')
markers={"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
gender=st.selectbox('Select a gender',['Male','Female','None'])
penguins_df=penguins_df[penguins_df['sex']==gender]
selected_species=st.selectbox('What species would you like to visualize?',['Adelie', 'Gentoo', 'Chinstrap'])

chosen_cloumns=pd.DataFrame(penguins_df.iloc[:,2:6]).columns.to_list()
#chosen_cloumns_df=chosen_cloumns.to_frame()
#print(chosen_cloumns)
x_var=st.selectbox('Choose the x value',chosen_cloumns)
y_var=st.selectbox('Choose the y value',chosen_cloumns)
#print(x_var)
#penguins_df=penguins_df[penguins_df['species']==selected_species]

st.write(penguins_df)

scatter = alt.Chart(penguins_df,title=f'Scatter plot for {selected_species} penguin').mark_circle().encode(
                x=x_var,
                y=y_var,
                tooltip=[x_var,y_var],
                color='species'
            ).interactive()
st.altair_chart(scatter,use_container_width=True)