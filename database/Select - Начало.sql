-- SELECT - позволяет получить данные из БД

-- SELECT <список полей> FROM <список таблиц> <=>
-- ВАЖНО - Alias - <название поля> as <алиас для отображения>
-- ВАЖНО - Выбор таблицы - <таблица>.<название поля>
-- ВАЖНО - Вместо конкретных таблиц, может выступать SELECT
-- <=> WHERE <условия выбора элементов>
-- {ORDER BY <поля для сортировки> [_ | DESC]}
--  Сортировка - по-умолчанию используется сортировка 
-- 		по-возрастанию, для обратной нужно указать DESC в ORDER BY



SELECT 
	student.first_name as Имя,
	student.second_name as Фамилия,
	student.last_name as Отчество,
	student.age as Возраст
FROM student
WHERE age < 23 AND age > 18
ORDER BY age DESC;


