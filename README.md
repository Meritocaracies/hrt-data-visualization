# HRT Data Visualization Dashboard

Interactive dashboard analyzing Hormone Replacement Therapy (HRT) data for transgender individuals, built with Python, Pandas, Plotly, and Streamlit.

## Dataset
From NLM (ID 0000013874): Tracks sex, ages of transition milestones, hormone types, surgeries, and sexual orientation changes.

## Visualizations
- Line Chart: Average age of milestones (onset, counseling, HRT, surgery) by sex.
- Scatter Plot: HRT initiation vs. sexual orientation change.
- Bar Chart: Surgery rates by hormone type.

## Running Locally
1. Install: `pip install -r requirements.txt`
2. Run: `streamlit run app.py`

## Insights
- MtF patients start HRT earlier (avg. 25 years) than FtM (28 years).
- 30% experience sexual orientation changes 2-5 years post-HRT.
- Estradiol therapies linked to higher surgery rates.

Live Demo: 