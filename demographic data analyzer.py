import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education & salary >50K
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_edu = df[df['education'].isin(advanced)]
    lower_edu = df[~df['education'].isin(advanced)]

    higher_edu_rich = round((higher_edu['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((lower_edu['salary'] == '>50K').mean() * 100, 1)

    # 5. Minimum work hours
    min_work_hours = df['hours-per-week'].min()

    # 6. Rich percentage among min hour workers
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 7. Country with highest % of >50K earners
    country_salary_ratio = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_salary_ratio.idxmax()
    highest_earning_country_percentage = round(country_salary_ratio.max() * 100, 1)

    # 8. Top occupation in India for >50K earners
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_edu_rich}%")
        print(f"Min work hours per week: {min_work_hours}")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print(f"Top occupation in India for those who earn >50K: {top_IN_occupation}")

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
