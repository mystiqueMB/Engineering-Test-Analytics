import pandas as pd
import os
import csv

#Taking path input from user
take_path = input('Enter the complete path of files to be proccessed')   
col_list =['Source IP']

def read_files(file):
# Reading files of folder and retriving unique data of specific column 'Source IP'
  temp_df=pd.read_csv(file, usecols=col_list)
  temp_df['Environment']=Env_create(file)
  return(temp_df)

def Env_create(file):
#Splitting file name
  o=file.split('/')
  env=(o[0])  
# remove last number and extension csv from csv file name string
  env=env.rstrip("1234567890.csv"
# add file_source column
  return(env)
  
def main():
master_df= pd.DataFrame({'Source IP':[],'Environment':[]})
c_file_new=pd.DataFrame()
c_file=pd.DataFrame()

for file in os.listdir(os.chdir(take_path)):
    if ((file != 'Combined.csv'  and file.endswith(".csv"))):
     master_df=pd.concat([read_files(file),master_df]).drop_duplicates().reset_index(drop=True)
     
 #Concated Source IP column and Env column
     c_file=pd.concat([master_df,c_file_new]).drop_duplicates().reset_index(drop=True)
     c_file_new=c_file.append(master_df)
     c_file_new=pd.concat([c_file_new]).drop_duplicates().reset_index(drop=True)

#Overwrting the existing file
c_file_new.to_csv("Combined.csv" , mode="w" ,header=True , index=False) 
