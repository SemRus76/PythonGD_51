SELECT * FROM student;

-- FOREIGN KEY - Внешний ключ - это ограничение создаваемой таблицы
--	которое позволяет принимать полю значения ТОЛЬКО из списка
-- 	УЖЕ существующих значений ДРУГОЙ таблицы
-- FOREIGN KEY (поля для связи) 
-- 		REFERENCES <название главной таблицы> (поля для ссылания)
-- 			ON UPDATE <действие при UPDATE>
-- 			ON DELETE <действие при DELETE>
--	ВАЖНО - (поля для связи) ОБЯЗАНЫ ПОЛНОСТЬЮ СОВПАДТЬ ПО ТИПУ
-- 				С (поля для ссылания)
-- ON UPDATE и ON DELETE могут принимать следующие значения:
-- 		CASCADE - продолжит изменения из главной таблицы
-- 		NO ACTION - вообще нифига не сделает
-- 		SET NULL - установит NULL значение (ЕСЛИ РАЗРЕШЕНО)
-- 		SET DEFAULT - установит DEFAULT значение (ЕСЛИ ЕСТЬ)

CREATE TABLE hostel_room
(
	id uuid DEFAULT gen_random_uuid(),
	number int NOT NULL,
	student uuid NOT NULL,
	square float,

	PRIMARY KEY(id),
	FOREIGN KEY (student) REFERENCES student(id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

INSERT INTO hostel_room (number, square, student)
VALUES 
	(1, 8.19, '7a543d9f-7006-4811-8831-66e08863d2c8'),
	(2, 8.19, '932ff60b-fbee-41a8-898c-2afa5bad3962'),
	(3, 8.19, '45c18971-53d6-4b2f-9afe-0119431186f9'),
	(4, 16  , '469f2aa3-1ca0-4f1a-b279-01634d246c9e'),
	(5, 16  , '763db483-a1ea-4562-bfa3-d6c2d1042dc9'),
	(6, 16  , '028534a6-6d9a-48b9-bb9e-49136bce06fa'),
	(7, 16  , '5a259bca-bff3-4f15-9284-fc0aca625b1e');