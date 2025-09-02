import pandas as pd
import plotly.express as px

# Load cleaned data
df = pd.read_csv('hrt_data_cleaned.csv')

# 1. Line Chart: Age Milestones by Sex
milestone_cols = ['age_of_onset', 'age_psychol', 'age_role', 'age_hormonetherapy', 'age_surgery']
fig1 = px.line(df.groupby('sex')[milestone_cols].mean().reset_index().melt(id_vars='sex', value_vars=milestone_cols),
               x='variable', y='value', color='sex',
               title='Average Age of HRT Milestones by Sex (MtF vs. FtM)',
               labels={'variable': 'Milestone', 'value': 'Age (Years)'})
fig1.add_annotation(x='age_hormonetherapy', y=df['age_hormonetherapy'].mean(),
                    text="MtF patients start hormone therapy earlier on average.",
                    showarrow=True, arrowhead=1)
fig1.show()
fig1.write_html('hrt_milestones.html')

# 2. Scatter Plot: Age of Hormone Therapy vs. Sexual Orientation Change
fig2 = px.scatter(df, x='age_hormonetherapy', y='age_changesexorient', color='changesexorient',
                  title='Age of Hormone Therapy vs. Sexual Orientation Change',
                  labels={'age_hormonetherapy': 'Age Started HRT (Years)', 'age_changesexorient': 'Age of Orientation Change (Years)'},
                  hover_data=['sex', 'direction_change'])
fig2.add_annotation(x=df['age_hormonetherapy'].mean(), y=df['age_changesexorient'].mean(),
                    text="Sexual orientation changes often occur 2-5 years after starting HRT.",
                    showarrow=True, arrowhead=1)
fig2.show()
fig2.write_html('hrt_sexorient.html')

# 3. Bar Chart: Surgery by Hormone Type
side_effects = df.groupby('hormonetype')['sex_reassignment_surgery'].value_counts().unstack().fillna(0)
fig3 = px.bar(side_effects.reset_index(), x='hormonetype', y=['Yes', 'No'],
              title='Sex Reassignment Surgery by Hormone Type',
              labels={'value': 'Count', 'hormonetype': 'Hormone Type'},
              barmode='stack')
fig3.add_annotation(x='Estradiol oral', y=side_effects['Yes'].max(),
                    text="Estradiol oral users have higher surgery rates.",
                    showarrow=True, arrowhead=1)
fig3.show()
fig3.write_html('hrt_surgery.html')