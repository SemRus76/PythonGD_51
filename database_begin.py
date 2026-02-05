import psycopg2


connection_item = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )
username = "Иванов"
query = ("SELECT                             "
         "  first_name as Имя                "
         " ,second_name as Фамилия           "
         " ,last_name as Отчество            "
         " ,age as Возраст                   "
         " ,number as Номер_Комнаты          "
         "FROM                               "
         " student                           "
         "FULL OUTER JOIN                    "
         " hostel_room                       "
         "ON                                 "
         " student.id = hostel_room.student  "
         # "WHERE                              "
         # f" student.first_name = '{username}'"
         )

cursor = connection_item.cursor()
cursor.execute(query)
data = ([("Имя", "Фамилия", "Отчество", "Возраст", "Номер Комнаты")] +
            cursor.fetchall())
cursor.close()
for line in data:
    line_str = str()
    for element in line:
        line_str += f"{element} "
    print(line_str)

student = ("( 'Лобанов', 'Семен', 'Евгеньевич', 21, true, 3 ),"
           "( 'Семенов', 'Семен', 'Семенович', 22, true, 6 );")
query_insert = ("INSERT INTO        "
                " student           "
                " (   first_name    "
                "     ,second_name  "
                "     ,last_name    "
                "     ,age          "
                "     ,sex          "
                "     ,course       "
                " )                 "
	            f"VALUES {student}  "
                )
cursor = connection_item.cursor()
cursor.execute(query_insert)
connection_item.commit()
cursor.close()

print("-=============================-")

cursor = connection_item.cursor()
cursor.execute(query)
data = ([("Имя", "Фамилия", "Отчество", "Возраст", "Номер Комнаты")] +
            cursor.fetchall())
cursor.close()
for line in data:
    line_str = str()
    for element in line:
        line_str += f"{element} "
    print(line_str)
connection_item.close()


