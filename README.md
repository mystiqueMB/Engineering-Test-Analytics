In this project I had to write Python code that traverses through the files in the zipped folder (Engineering Test Files.zip) and generates the combined.csv file also found in the folder. If a new file called NA Preview.csv gets dropped in the same folder, the script will be able to process it and rows in the combined.csv file will be added with the environment value being set to NA Preview. Same applies if a new file called Asia Prod 4.csv gets dropped. It should add new rows to the combined.csv file with the environment being set to Asia Prod. File path to be taken by the user.

Steps for building code:

1. File path is requested from the user.

2. Extracted files from a zip folder are read in a data frame using the function 'read_files'. The function reads specific required column from all files. A new column 'Environment' is created which stores and return values from the Env_create function.

3. The 'Env_create' function, which is called in the 'read_files' function, firstly splits file name and then strips off the right part of the file name (since the name may have some number reference in it). The stripeed file name is returned by this function.

4. A main function is created under which a for loop is initiated to iterate all the .csv files except combined.csv. The data frame is concatenated and appended with the data proccessed by the 'read_files' and 'Env_create' function.

5. The concatenated dataframe is then over-written in combined.csv file.

6. In a new file unit test are written using the assertEqual() method.
