from rw_sheet import read_sheets, write_final_result

SPREADSHEET_ID = '1InajjWFP3YaZEdJmVbc8K2EBHnHtIeoneXCoZuj4omY'

cels_to_read = "Sheet1!A2:B2"
data_result = read_sheets(cels_to_read, SPREADSHEET_ID)
print(data_result)

where_to_write = "Sheet1!A3:B3"
data_to_write = [['Hello1'],['Hello2'],['Hello3'],['Hello4'],['Hello5'],]
data_write = write_final_result(data_to_write, where_to_write, SPREADSHEET_ID)
