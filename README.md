# Web-app

Я попарсил 2 аниме-сайта. С первого брал названия аниме, жанры, годы выхода и ссылки на них. 
Со второго брал персонажей из каких-то аниме, те аниме, где они появлялись и их фотографию
Дальше получив 2 базы, создал веб-приложение, которое по году, слову из названия и жанрам (их можно поставить несколько только записывать все через пробел без лишних символов)
выдаёт случайное аниме, дальше с помощью youtube API выдаёт видео про это аниме, название аниме, ссылку на его просмотр, а также ищет случайного персонажа по второй базе данных,
который был в этом аниме. После чего выдаёт имя этого персонажа и его картинку, если она была на сайте. Если персонаж не найден, то выдаёт сообщение с изменениями.



Файл "Data-read" считывает данные (крайне долго), два csv-файла это итоговые данные. "Mini" файл с классом для поиска аниме и функцией поиска видео на youtube.

"Main", "Mini", файл с токеном и 2 csv файла у меня были в одной папке, в той же папке лежала папка templates, где были "data", "form" и "DataRead" 