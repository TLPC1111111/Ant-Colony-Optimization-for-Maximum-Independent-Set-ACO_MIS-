import pandas as pd
from sklearn.preprocessing import LabelEncoder
class AFIT(object):
    '''
    read AFIT.data and construct edges
    '''
    def __init__(self , text_name):
        self.text_name = text_name
        self.support_id_list = []
        self.df = pd.read_csv(f'./{self.text_name}.dat', header=None, sep = '\s+', na_values='')
        self.visibility_arcs_length = 0
        self.RTS_antenna_ID_list = []
        self.begining_of_visibility_window = []
        self.end_of_visibility_window = []
        self.visibility_window = []
        self.support_duration = []
        self.antenna_turnaround_time = []

    def read_support_id(self):
        first_column = self.df.iloc[:, 0]
        first_column_list = first_column.tolist()
        for i in range(len(first_column_list)):
            self.support_id_list.append(first_column_list[i])
        return self.support_id_list

    def read_RTS_antenna_id(self):
        second_column = self.df.iloc[ :, 1]
        second_column_list = LabelEncoder().fit_transform(second_column)
        for i in range(len(second_column_list)):
            self.RTS_antenna_ID_list.append(second_column_list[i])
        return self.RTS_antenna_ID_list

    def read_time_of_visibility_window(self):
        third_column = self.df.iloc[ :, 2]
        third_column_list = third_column.tolist()
        for i in range(len(third_column_list)):
            self.begining_of_visibility_window.append(third_column_list[i])
        forth_colum = self.df.iloc[ :, 3]
        forth_colum_list = forth_colum.tolist()
        for i in range(len(forth_colum_list)):
            self.end_of_visibility_window.append(forth_colum_list[i])
        if len(self.begining_of_visibility_window) == len(self.end_of_visibility_window):
            for j in range(len(self.begining_of_visibility_window)):
                self.visibility_window.append([self.begining_of_visibility_window[j] , self.end_of_visibility_window[j]])
            return self.visibility_window
        else:
            print("The dimension of Visibility window not consistent")
            return False

    def read_support_duration(self):
        fifth_colum = self.df.iloc[ :, 4]
        fifth_colum_list = fifth_colum.tolist()
        for i in range(len(fifth_colum_list)):
            self.support_duration.append(fifth_colum_list[i])
        return self.support_duration

    def read_antenna_turnaround_time(self):
        sixth_colum = self.df.iloc[ :, 5]
        sixth_colum_list = sixth_colum.tolist()
        for i in range(len(sixth_colum_list)):
            self.antenna_turnaround_time.append(sixth_colum_list[i])
        return self.antenna_turnaround_time

    def calculate_visibility_arcs_length(self):
        self.visibility_arcs_length = len(self.df.iloc[:, 0].tolist())
        return self.visibility_arcs_length

