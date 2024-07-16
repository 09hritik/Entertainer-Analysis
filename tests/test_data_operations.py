import pandas as pd
import pytest
from Modules.data_loader import load_data
from Modules.data_merger import merge_datasets
from Modules.data_preprocessor import preprocess_data

# Fixture to load sample data for testing
@pytest.fixture
def sample_data():
    basic_info = pd.DataFrame({
        'Entertainer': ['Entertainer1', 'Entertainer2'],
        'Basic_Info_Column': [1, 2]
    })
    
    breakthrough_info = pd.DataFrame({
        'Entertainer': ['Entertainer1', 'Entertainer2'],
        'Breakthrough_Column': [3, 4]
    })
    
    last_work_info = pd.DataFrame({
        'Entertainer': ['Entertainer1', 'Entertainer2'],
        'Last_Work_Column': [5, 6]
    })
    
    return basic_info, breakthrough_info, last_work_info

# Test case for load_data function
def test_load_data(sample_data):
    basic_info, breakthrough_info, last_work_info = sample_data
    assert isinstance(basic_info, pd.DataFrame), "Basic Info data is not a DataFrame"
    assert isinstance(breakthrough_info, pd.DataFrame), "Breakthrough Info data is not a DataFrame"
    assert isinstance(last_work_info, pd.DataFrame), "Last Work Info data is not a DataFrame"

# Test case for merge_datasets function
def test_merge_datasets(sample_data):
    basic_info, breakthrough_info, last_work_info = sample_data
    merged_data = merge_datasets(basic_info, breakthrough_info, last_work_info)
    assert isinstance(merged_data, pd.DataFrame), "Merged data is not a DataFrame"
    assert 'Entertainer' in merged_data.columns, "Entertainer column missing in merged data"

# Test case for preprocess_data function
def test_preprocess_data(sample_data):
    basic_info, breakthrough_info, last_work_info = sample_data
    preprocessed_data = preprocess_data(basic_info, breakthrough_info, last_work_info)
    assert isinstance(preprocessed_data, pd.DataFrame), "Preprocessed data is not a DataFrame"
    assert 'Entertainer' in preprocessed_data.columns, "Entertainer column missing in preprocessed data"

# Run the tests
if __name__ == "__main__":
    pytest.main()

