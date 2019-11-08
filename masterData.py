import pandas as pd
print('pandas imported as pd')
import datetime
print('datetime imported')

# Date and time of file execution
now = datetime.datetime.now()
FIRST_DAY = '03/01/2018'
print('Now is: ', str(now))

# Name of Excel file containing all sales data
EXCEL_MASTER_FILE = 'Sales Report 3-1-2018 - 12-31-2018.xlsx'
#OUTPUT_FILE = 'alldata' + str(now) + '.xlsx'
OUTPUT_FILE = 'allData.xlsx'

# Read excel file into DataFrame
print('Reading data from excel file: '+ EXCEL_MASTER_FILE)
master_df = pd.read_excel(EXCEL_MASTER_FILE, index_col='Sale Date',parse_date=True)
print(master_df.head())

# Clean column names
print('Renaming Columns')
master_df.columns = ['ticketsSold','cash','check','creditCard','misc','total']
print(master_df.head())

# Check datetime index work correctly
print(master_df.loc['Jul 2018'])

# Add day of week column
master_df['weekday'] = pd.to_datetime(master_df.index)
master_df.weekday = master_df.weekday.dt.day_name()
#master_df['weekday'] = pd.to_Date
print(master_df.head())

# Write data to excelfile
print('writing data to ' + OUTPUT_FILE)
master_df.to_csv(OUTPUT_FILE)

print('DONE')
