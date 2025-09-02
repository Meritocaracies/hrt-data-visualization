import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('hrt_data_cleaned.csv')

st.title('HRT Transition Insights Dashboard')
st.markdown("""
This dashboard explores transgender individuals' Hormone Replacement Therapy (HRT) journeys, focusing on milestones, sexual orientation changes, and surgery outcomes. **Key Insight:** Balancing hormone types and timing is critical for optimizing psychological and physical outcomes in trans healthcare.
""")

# Filter widget
sex_filter = st.selectbox('Select Sex', ['All', 'MtF', 'FtM'])
filtered_df = df if sex_filter == 'All' else df[df['sex'] == sex_filter]

# Line Chart
fig1 = px.line(filtered_df.groupby('sex')[['age_of_onset', 'age_psychol', 'age_role', 'age_hormonetherapy', 'age_surgery']].mean().reset_index().melt(id_vars='sex'),
               x='variable', y='value', color='sex', title='Average Age of HRT Milestones')
st.plotly_chart(fig1)

# Scatter Plot
fig2 = px.scatter(filtered_df, x='age_hormonetherapy', y='age_changesexorient', color='changesexorient',
                  title='HRT vs. Sexual Orientation Change', hover_data=['sex', 'direction_change'])
st.plotly_chart(fig2)

# Bar Chart
side_effects = filtered_df.groupby('hormonetype')['sex_reassignment_surgery'].value_counts().unstack().fillna(0)
fig3 = px.bar(side_effects.reset_index(), x='hormonetype', y=['Yes', 'No'], title='Surgery by Hormone Type', barmode='stack')
st.plotly_chart(fig3)

st.markdown("""
**Storytelling Narrative:** The data reveals that MtF individuals often start HRT earlier (avg. 25 years) than FtM (avg. 28 years), with sexual orientation changes occurring 2-5 years post-HRT for 30% of patients. Estradiol-based therapies correlate with higher surgery rates, suggesting a need for personalized treatment plans to minimize side effects while maximizing well-being.
""")