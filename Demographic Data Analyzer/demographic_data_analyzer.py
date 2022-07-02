import pandas as pd



def calculate_demographic_data(print_data=True):
    # Read data from file
    df=pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.value_counts('race')

    # What is the average age of men?
    average_age_men =round(df.loc[df['sex']=='Male',"age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'].value_counts()['Bachelors']/df['education'].count())*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round((df[df["education"].isin (['Bachelors','Masters','Doctorate'])]['education'].count()/df['education'].count())*100,1)

    lower_education = round((df[~df["education"].isin (['Bachelors','Masters','Doctorate'])]['education'].count()/df['education'].count())*100,1)

    # percentage with salary >50K
    higher_education_rich =round((df[df["education"].isin (['Bachelors','Masters','Doctorate']) & (df['salary']=='>50K')]['education'].count()/df[df['education'].isin(['Bachelors','Masters','Doctorate'])]['education'].count())*100,1)

    lower_education_rich =round((df[(~df["education"].isin (['Bachelors','Masters','Doctorate'])) & (df['salary']=='>50K')]['education'].count()/df[~df['education'].isin(['Bachelors','Masters','Doctorate'])]['education'].count())*100,1)



    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours =df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers =df[df['hours-per-week']==min_work_hours]['hours-per-week'].count()

    rich_percentage =round((df[(df['salary']=='>50K')&(df['hours-per-week']==min_work_hours)]['salary'].count()/df[df['hours-per-week']==min_work_hours]['salary'].count())*100,1)

    # What country has the highest percentage of people that earn >50K?

    df1=df[['native-country','salary']].groupby('native-country').count().reset_index().sort_values(by='salary', ascending = False)

    df2=df[['native-country','salary']].loc[df['salary']=='>50K'].groupby('native-country').count().reset_index().sort_values(by='salary',ascending=False)
    final_df=pd.merge(df1,df2,on='native-country',how='left')
    final_df['portion']=final_df["salary_y"]/final_df['salary_x']

    highest_earning_country =final_df.sort_values(by='portion',ascending=False)['native-country'].iloc[0]
    highest_earning_country_percentage =round(final_df.sort_values(by='portion',ascending=False)['portion'].iloc[0]*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation =df[(df['salary']=='>50K')&(df['native-country']=='India')][['occupation','salary']].groupby('occupation').count().reset_index().sort_values(by='salary',ascending=False)['occupation'].iloc[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }





calculate_demographic_data()
  
