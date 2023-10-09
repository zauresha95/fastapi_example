Минимальный перечень технологий/библиотек которые необходимо использовать при выполнении тестового задания:

	sqlalchemy ^2 (async_engine)
	asyncio
	pydantic
	fastapi	
	aiokafka
	pytest, pytest-asyncio
	alembic
	postgreSQL
	docker

Описание задания

Реализовать backend на FastAPI:
Реализовать модель User которая состоит из полей: id, name, surname, email, birthday. Все поля обязательные. Валидация email по маске.
Реализовать consumer, который обрабатывает входящий XML-запрос из Apache Kafka.
Парсит полученный запрос. Запрос состоит из полей модели User. И сохраняет в соответствующую таблицу.
При успешном сохранении в таблицу, отправляет через producer в Apache Kafka соответствующий XML-ответ.
При неуспешном сохранении в таблицу (например, пришел невалидный email или часть полей отсутствуют в XML-запросе) отправлять другой XML-ответ (см. пример).

Весь код, включая consumer и producer, необходимо покрыть тестами. При необходимости использовать mock-тесты.
Выбор библиотеки для парсинга на свой выбор.
	В коде использовать асинхронный подход к работе с данными. 
	Обернуть приложение в docker-образ. Через docker-compose настроить связанные сервисы.
	Результат выложить на Github, ссылку отправить HR.

Пример XML-запроса

	<ns2:Request xmlns:ns2="urn://www.example.com">
	<ns2:User>
	<ns2:Name>Иван</ns2:Name>
	<ns2:Surname>Иванов</ns2:Surname>
	<ns2:Email>ivan.ivanov.2023.2024@yandex.com</ns2:Email>
	<ns2:Birthday>2005-10-23T04:00:00+03:00</ns2:Birthday>
	</ns2:User>
	</ns2:Request>


Пример успешного XML-ответа

	<ns2:Response xmlns:ns2="urn://www.example.com">
	<ns2:User>
	<ns2:Id>50</ns2:Id>
	<ns2:Status>SUCCESS</ns2:Status>
	</ns2:User>
	</ns2:Response>

Пример неуспешного XML-ответа

	<ns2:Response xmlns:ns2="urn://www.example.com">
	<ns2:User>
	<ns2:Name>Иван</ns2:Name>
	<ns2:Surname>Иванов</ns2:Surname>
	<ns2:Email>ivan.ivanov.2023.2024@yandex.com</ns2:Email>
	<ns2:Birthday>2005-10-23T04:00:00+03:00</ns2:Birthday>
	<ns2:Status>FAILED</ns2:Status
	</ns2:User>
	</ns2:Response>

