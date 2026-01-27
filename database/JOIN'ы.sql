SELECT 
	student.first_name as Фамилия, 
	student.second_name as Имя,
	student.last_name as Отчество,
	student.course as Курс,
	hostel_room.number as Номер_комнаты
FROM 
	student FULL OUTER JOIN hostel_room
ON
	student.id = hostel_room.student
WHERE 
	hostel_room.student IS null;

-- SELECT *
-- 
-- FROM
-- 		table_A [LEFT | FULL OUTER | INNER | RIGHT] JOIN table_B
-- ON
-- 		<условие сопоставления таблиц>
-- WHERE
-- 		<дополнительные условия выбора элементов>;

-- INNER JOIN - это обычный SELECT без JOIN


	