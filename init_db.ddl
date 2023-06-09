CREATE TABLE if not exists questions (
    id int generated always as identity primary key,
	question TEXT,
	answer_1 TEXT,
	answer_2 TEXT,
	answer_3 TEXT,
	answer_4 TEXT,
	right_answer TEXT
);

insert INTO questions (question, answer_1, answer_2, answer_3, answer_4, right_answer)

values ('Какая страна производит больше всего кофе в мире?', '1) Колумбия', '2) Индонезия', '3) Бразилия', '4) Вьетнам', '4'),
	('Как называется колокол часов Вестминстерского дворца в Лондоне?', '1) Биг Бен', '2) Броненосец', '3) Калабаш', '4) Мумия', '1'),
	('Что означает термин “пиано”?', '1)  В бодром темпе', '2) В мягком темпе', '3) В умеренном темпе', '4) В быстром темпе', '2'),
	('Сколько длится мгновение?', '1) 60 секунд', '2) 90 секунд', '3) 120 секунд', '4) 180 секунд', '2'),
	('Сколько вкусовых рецепторов имеет средний человеческий язык?', '1) 100', '2) 1000', '3) 10000', '4) 10000', '3'),
	('Какая самая маленькая планета в нашей Солнечной системе?', '1) Земля', '2) Венера', '3) Марс', '4) Меркурий', '4'),
	('Какая служба электронной почты принадлежит компании Microsoft?', '1) Outlook', '2) Yahoo Mail', '3) Gmail', '4) iCloud Mail', '1'),
	('Как назывался батончик “Сникерс” до его смены названия в 1990 году?', '1) Race', '2) Marathon', '3) Smile', '4) Sprint', '1'),
	('Какого цвета была таблетка, которую принимает Нео в фильме “Матрица”?', '1) Красный', '2) Синий', '3) Зеленый', '4) Желтый', '1'),
	('Каково было первоначальное название Нью-Йорка?', '1) Новый Амстердам', '2) Большое яблоко', '3) Имперский штат', '4) Готэм', '1');