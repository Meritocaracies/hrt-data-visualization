import pandas as pd

# Load dataset
df = pd.read_excel('hrt_data.xls') 

# Print raw column names
print("Raw Column Names:\n", df.columns.tolist())

# Rename columns
column_mapping = {
    'ID': 'id',
    'sex (1=MtF; 2 =FtM)': 'sex',
    'initial_sex_orientation (1= androphilic; 2 =gynephilic; 3 = bisexual, 4 = analloerotic)': 'initial_sex_orientation',
    'age_of_onset': 'age_of_onset',
    'onset_before_age_of_12 (1= before or at age of 12; after age of 12)': 'onset_before_12',
    'age_psychol (age of first psychological counselling)': 'age_psychol',
    'age_role (age of start everday-experience)': 'age_role',
    'hormontherapy (1 =yes; 2 =no)': 'hormonetherapy',
    'age_hormonetherapy (age of initiation of hormonetherapy)': 'age_hormonetherapy',
    'hormonetype (1= T transdermal; 2 = T intramuscular; 3 = E + Antiandrogen; 4 = Estradiol transdermal; 5 = Estradiol oral; 6 = estradiol +gestagen)': 'hormonetype',
    'sex reassignement surgery (1= yes; 2 = no)': 'sex_reassignment_surgery',
    'age_surgery (age of sex reassignement surgery)': 'age_surgery',
    'type_of_surgery (1 = hysterectomy + mastectomy; 2 = +penoid, 3 = neovagina, 4 = breast augmentation)': 'type_of_surgery',
    'changesexorient (there has been a change in self-reported sexual orientation: 1= yes; 2 = no)': 'changesexorient',
    'age_changesexorient (age when self-reported sexual orientation changed)': 'age_changesexorient',
    'direction_change (direction of change in sexual orientation; 1= androphilic to gynephilic;  2=androphilic to bisexual; 3=gynephilic to androphilic; 4=gynephilic to bisexual, 5 = analloerotic to gynephilic; 6 =analloerotic to androphilic; 7 = analloerotic to bisexual; 8 = gynephilic to analloerotic) ': 'direction_change',
    'interval_horm_surg (interval from initiation of hormone therapy to sex reassignement surgery)': 'interval_horm_surg'
}
df = df.rename(columns=column_mapping)

# Convert categorical columns to readable labels
df['sex'] = df['sex'].map({1: 'MtF', 2: 'FtM'})
df['initial_sex_orientation'] = df['initial_sex_orientation'].map({
    1: 'Androphilic', 2: 'Gynephilic', 3: 'Bisexual', 4: 'Analloerotic'
})
df['hormonetherapy'] = df['hormonetherapy'].map({1: 'Yes', 2: 'No'})
df['sex_reassignment_surgery'] = df['sex_reassignment_surgery'].map({1: 'Yes', 2: 'No'})
df['changesexorient'] = df['changesexorient'].map({1: 'Yes', 2: 'No'})
df['hormonetype'] = df['hormonetype'].map({
    1: 'T transdermal', 2: 'T intramuscular', 3: 'E + Antiandrogen',
    4: 'Estradiol transdermal', 5: 'Estradiol oral', 6: 'Estradiol + gestagen'
})
df['type_of_surgery'] = df['type_of_surgery'].map({
    1: 'Hysterectomy + Mastectomy', 2: '+Penoid', 3: 'Neovagina', 4: 'Breast Augmentation'
})
df['direction_change'] = df['direction_change'].map({
    1: 'Androphilic to Gynephilic', 2: 'Androphilic to Bisexual',
    3: 'Gynephilic to Androphilic', 4: 'Gynephilic to Bisexual',
    5: 'Analloerotic to Gynephilic', 6: 'Analloerotic to Androphilic',
    7: 'Analloerotic to Bisexual', 8: 'Gynephilic to Analloerotic'
})

# Handle missing values
df = df.fillna({
    'age_of_onset': df['age_of_onset'].mean(),
    'age_psychol': df['age_psychol'].mean(),
    'age_role': df['age_role'].mean(),
    'age_hormonetherapy': df['age_hormonetherapy'].mean(),
    'age_surgery': df['age_surgery'].mean(),
    'age_changesexorient': df['age_changesexorient'].mean(),
    'interval_horm_surg': df['interval_horm_surg'].mean(),
    'hormonetype': 'Unknown',
    'type_of_surgery': 'None',
    'direction_change': 'None'
})

# Explore
print("Shape:", df.shape)
print("\nColumns and Types:\n", df.dtypes)
print("\nFirst 5 Rows:\n", df.head())
print("\nMissing Values:\n", df.isnull().sum())

# Save cleaned data
df.to_csv('hrt_data_cleaned.csv', index=False)
print("Cleaned data saved as hrt_data_cleaned.csv")