import pandas as pd

def load_data():
    basic_info = pd.read_excel('/Users/09hritik/ML/Entertainer-Analysis/data/Basic_Info.xlsx')
    breakthrough_info = pd.read_excel('/Users/09hritik/ML/Entertainer-Analysis/data/Breakthrough_ Info.xlsx')
    last_work_info = pd.read_excel('/Users/09hritik/ML/Entertainer-Analysis/data/Last_work_Info.xlsx')
    return basic_info, breakthrough_info, last_work_info

#if __name__ == '__main__':
    basic_info, breakthrough_info, last_work_info = load_data()
    print(basic_info.head())
    print(breakthrough_info.head())
    print(last_work_info.head())