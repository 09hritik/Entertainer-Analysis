import pandas as pd

def merge_datasets(basic_info, breakthrough_info, last_work_info):
    merged_data = pd.merge(basic_info, breakthrough_info, on='Entertainer', how='left')
    merged_data = pd.merge(merged_data, last_work_info, on='Entertainer', how='left')
    return merged_data
