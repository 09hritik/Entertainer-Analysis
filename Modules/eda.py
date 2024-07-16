import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set_style('whitegrid')

def display_basic_info(data):
    print("Basic Information:\n")
    print(data.info())

def display_descriptive_statistics(data):
    print("\nDescriptive Statistics:\n")
    print(data.describe(include='all'))

def plot_birth_year_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Birth Year'], bins=20, kde=True)
    plt.title('Distribution of Birth Year of Entertainers')
    plt.xlabel('Birth Year')
    plt.ylabel('Frequency')
    plt.show()

def plot_breakthrough_year_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Year of Breakthrough/#1 Hit/Award Nomination'], bins=20, kde=True)
    plt.title('Distribution of Breakthrough Year of Entertainers')
    plt.xlabel('Breakthrough Year')
    plt.ylabel('Frequency')
    plt.show()

def plot_last_major_work_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Year of Last Major Work (arguable)'], bins=20, kde=True)
    plt.title('Distribution of Year of Last Major Work')
    plt.xlabel('Year of Last Major Work')
    plt.ylabel('Frequency')
    plt.show()

def plot_gender_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Gender (traditional)', data=data)
    plt.title('Gender Distribution of Entertainers')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()



def plot_correlation_matrix(data):
    # Select only numeric columns for the correlation matrix
    numeric_data = data.select_dtypes(include=['number'])
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()


def plot_birth_vs_breakthrough(data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Birth Year', y='Year of Breakthrough/#1 Hit/Award Nomination', data=data)
    plt.title('Relationship between Birth Year and Breakthrough Year')
    plt.xlabel('Birth Year')
    plt.ylabel('Breakthrough Year')
    plt.show()

def calculate_age_at_breakthrough(data):
    data['Age at Breakthrough'] = data['Year of Breakthrough/#1 Hit/Award Nomination'] - data['Birth Year']

def calculate_age_at_last_major_work(data):
    data['Age at Last Major Work'] = data['Year of Last Major Work (arguable)'] - data['Birth Year']

def calculate_years_active(data):
    data['Years Active'] = data['Year of Last Major Work (arguable)'] - data['Year of Breakthrough/#1 Hit/Award Nomination']

def plot_age_at_breakthrough(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age at Breakthrough'], bins=20, kde=True)
    plt.title('Distribution of Age at Breakthrough')
    plt.xlabel('Age at Breakthrough')
    plt.ylabel('Frequency')
    plt.show()

def plot_age_at_last_major_work(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age at Last Major Work'], bins=20, kde=True)
    plt.title('Distribution of Age at Last Major Work')
    plt.xlabel('Age at Last Major Work')
    plt.ylabel('Frequency')
    plt.show()

def plot_years_active(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Years Active'], bins=20, kde=True)
    plt.title('Distribution of Years Active')
    plt.xlabel('Years Active')
    plt.ylabel('Frequency')
    plt.show()

def plot_genre_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Primary Genre', data=data)
    plt.title('Distribution of Entertainers by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def plot_top_entertainers_by_major_works(data):
    top_entertainers = data['Entertainer Name'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_entertainers.values, y=top_entertainers.index, palette='viridis')
    plt.title('Top 10 Entertainers by Major Work Count')
    plt.xlabel('Major Work Count')
    plt.ylabel('Entertainer Name')
    plt.show()

def plot_gender_distribution_over_time(data):
    data['Decade of Breakthrough'] = (data['Year of Breakthrough/#1 Hit/Award Nomination'] // 10) * 10
    plt.figure(figsize=(14, 6))
    sns.countplot(x='Decade of Breakthrough', hue='Gender (traditional)', data=data, palette='Set2')
    plt.title('Gender Distribution of Entertainers Over Time')
    plt.xlabel('Decade of Breakthrough')
    plt.ylabel('Count')
    plt.show()

def eda(data):
    display_basic_info(data)
    display_descriptive_statistics(data)
    plot_birth_year_distribution(data)
    plot_breakthrough_year_distribution(data)
    plot_last_major_work_distribution(data)
    plot_gender_distribution(data)
    plot_correlation_matrix(data)
    plot_birth_vs_breakthrough(data)
    
    calculate_age_at_breakthrough(data)
    calculate_age_at_last_major_work(data)
    calculate_years_active(data)
    
    plot_age_at_breakthrough(data)
    plot_age_at_last_major_work(data)
    plot_years_active(data)
    plot_genre_distribution(data)
    plot_top_entertainers_by_major_works(data)
    plot_gender_distribution_over_time(data)


