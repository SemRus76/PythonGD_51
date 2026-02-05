import psycopg2
import uuid


class DBControl:

    __db_connection = 0

    def __init__(self):
        self.__db_connection = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432
        )

    def __del__(self):
        self.__db_connection.close()

    def print_student_list(self):
        cursor = self.__db_connection.cursor()

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
                 )

        cursor.execute(query)
        data = ([("Имя", "Фамилия", "Отчество", "Возраст", "Номер Комнаты")] +
                cursor.fetchall())
        cursor.close()

        print("-=====================-")
        for line in data:
            for element in line:
                print(str(element) + " ", end="")
            print()
        print("-=====================-")

    def add_student(self,
                    full_name: str,
                    age: int,
                    sex: bool,
                    course: float,
                    room_number: int):
        cursor = self.__db_connection.cursor()
        first_name, second_name, last_name = full_name.split()
        id = uuid.uuid4()

        query = f'''
                INSERT INTO student (
                        id, 
                        first_name, 
                        second_name, 
                        last_name,
                        age, 
                        sex, 
                        course)
                VALUES (
                        '{id}',
                        '{first_name}',
                        '{second_name}',
                        '{last_name}',
                        {age},
                        {sex},
                        {course}
                        )
                ON CONFLICT (id) DO UPDATE
                    SET first_name = EXCLUDED.first_name,
                        second_name = EXCLUDED.second_name,
                        last_name = EXCLUDED.last_name,
                        age = EXCLUDED.age,
                        sex = EXCLUDED.sex,
                        course = EXCLUDED.course;
                '''
        cursor.execute(query)
        cursor.close()

        cursor = self.__db_connection.cursor()
        query = f'''
                INSERT INTO 
                    hostel_room (
                        number, 
                        student, 
                        square
                        )
                VALUES (
                        {room_number},
                        '{id}',
                        8
                        )
                ON CONFLICT (id) DO UPDATE
                    SET number = EXCLUDED.number,
                        student = EXCLUDED.student,
                        square = EXCLUDED.square;
        '''
        cursor.execute(query)
        cursor.close()

        self.__db_connection.commit()
