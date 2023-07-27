import subprocess
import pandas as pd

def call_executable():
    # Call the compiled executable
    result = subprocess.check_output(['my_function.exe'])
    
    # Split the output into two tables
    table1_str, table2_str = result.split(b'\n\n')
    
    # Convert the tables from strings to pandas dataframes
    table1 = pd.read_csv(pd.compat.StringIO(table1_str.decode()), sep='\t')
    table2 = pd.read_csv(pd.compat.StringIO(table2_str.decode()), sep='\t')
    
    return table1, table2
