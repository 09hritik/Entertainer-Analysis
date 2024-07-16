import pandas as pd

def preprocess_data(basic_info, breakthrough_info, last_work_info):
    # Merge the datasets on 'Entertainer'
    combined_data = pd.merge(basic_info, breakthrough_info, on='Entertainer', how='left')
    combined_data = pd.merge(combined_data, last_work_info, on='Entertainer', how='left')
    # Additional cleaning steps if necessary
    return combined_data
