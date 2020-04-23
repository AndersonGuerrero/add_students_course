import sys                
import pandas as pd

if len(sys.argv) == 3:
    file_name_xls = sys.argv[1]
    course_id = sys.argv[2]
    print(file_name_xls, course_id)
    file_excel = pd.read_excel(file_name_xls)

    columns = ['first_name', 'last_name', 'email', 'language']
    df_selected = file_excel[columns]

    for index_row, row in df_selected.iterrows():
        print(index_row)
        print('nombre:', row[0])
        print('apellido:', row[1])
        print('email:', row[2])
        print('lenguaje:', row[3])
        break

else:
    print("Debe ingresar ruta del archivo xls y el id del curso. ejemplo: python app.py file.xls 123")
