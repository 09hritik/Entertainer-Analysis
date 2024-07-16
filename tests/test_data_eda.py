import pandas as pd
import pytest
from Modules.eda import eda

# Fixture to load sample data for testing EDA functions
@pytest.fixture
def sample_data_for_eda():
    sample_data = pd.DataFrame({
        'Entertainer': ['Entertainer1', 'Entertainer2'],
        'Birth Year': [1980, 1975],
        'Year of Breakthrough/#1 Hit/Award Nomination': [2000, 1990],
        'Year of Last Major Work (arguable)': [2020, 2015],
        'Gender (traditional)': ['Male', 'Female'],
        'Primary Genre': ['Pop', 'Rock']
    })
    return sample_data

# Test case for EDA functions
def test_eda_functions(sample_data_for_eda):
    sample_data = sample_data_for_eda
    
    # Test individual EDA functions
    try:
        eda.display_basic_info(sample_data)
        eda.display_descriptive_statistics(sample_data)
        eda.plot_birth_year_distribution(sample_data)
        eda.plot_breakthrough_year_distribution(sample_data)
        eda.plot_last_major_work_distribution(sample_data)
        eda.plot_gender_distribution(sample_data)
        eda.plot_correlation_matrix(sample_data)
        eda.plot_birth_vs_breakthrough(sample_data)
        
        eda.calculate_age_at_breakthrough(sample_data)
        eda.calculate_age_at_last_major_work(sample_data)
        eda.calculate_years_active(sample_data)
        
        eda.plot_age_at_breakthrough(sample_data)
        eda.plot_age_at_last_major_work(sample_data)
        eda.plot_years_active(sample_data)
        eda.plot_genre_distribution(sample_data)
        eda.plot_top_entertainers_by_major_works(sample_data)
        eda.plot_gender_distribution_over_time(sample_data)
        
        assert True
    except Exception as e:
        assert False, f"Error in EDA function: {e}"

# Run the tests
if __name__ == "__main__":
    pytest.main()

