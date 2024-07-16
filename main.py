from Modules.data_loader import load_data
from Modules.eda import eda
from Modules.data_merger import merge_datasets
def main():
    basic_info, breakthrough_info, last_work_info = load_data()
    merged_data = merge_datasets(basic_info, breakthrough_info, last_work_info)
    eda(merged_data)
    #print(merged_data.head())
    #print(basic_info.head())
    #print(breakthrough_info.head())
    #print(last_work_info.head())

    #print(basic_info.isna())

    #perform_eda(basic_info)
    #perform_eda(breakthrough_info)
    #perform_eda(last_work_info)



if __name__ == '__main__':
    main()