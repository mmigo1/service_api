# Web - service Django

 Это приложение представляет собой  WEB сервис реализованный на Фреймворке Django


## Функции веб сервиса

- Реализация  POST REST метода
- После получения запроса сервис запрашивает с публичного API (https://jservice.io/api/random?count=1) указанное количество вопросов
- Далее, сохраняет полученные ответы в БД
- Ответом на запрос является предыдущей сохранённый вопрос


## Установка
По умолчанию докер будет использовать порт 8000.
1)Используйте docker-compose что бы построить образ
```sh
docker-compose build
```
2)Выполните миграции
```sh
docker compose run --rm web-app sh -c "python manage.py migrate"
```
3)Создайте суперпользователя
```sh
docker compose run --rm web-app sh -c "python manage.py createsuperuser"
```
4)Запустите образ
```sh
docker-compose up
```
## Примеры запросов к POST API
Приложение работает по на хост-машине по адресу http://localhost:8000/ и обрабатывает апросы по двум url адресам:

1)admin/ - служит для входа в панель администратора и взаимодействия с БД

2)/question - служит для принятия POST методов и принимает следующие запросы -
```sh
{
    "questions_num" : "1"
}
```

В случае отправки GET запроса ответом будет последний сохранённый вопрос в БД.


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
