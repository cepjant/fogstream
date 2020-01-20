# fogstream


## Описание

Проект предоставляет возможность регистрации, авторизации, и отправки сообщения на указанный email в асинхронной задаче Celery.

Перед отправкой сообщения еобходимо запустить также и сервер Celery:
в консоле из директории, содержащей папку 'project', ввести:
celery -A project worker -l info

Сообщения имеют два статуса: SENT, NOT_SENT. 
Посмотреть количество отправленных и не отправленных сообщений можно на админ-странице проекта.

![Админ-панель](https://i.imgur.com/BzMChSP.png "Админ-панель")

В файле project/settings.py необходимо указать свои параметры SMTP сервера, иначе вернет SMTP authentication error.

Задание по парсингу данных с сайта http://jsonplaceholder.typicode.com/users реализовано, но не подключено: 
доступ к ресурсу заблокирован и возможен только через VPN. Протестировать не удалось.

____

## Сборка и запуск:


```bash
git clone https://github.com/cepjant/fogstream.git
cd fogstream
pip install virtualenv
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
celery -A project worker -l info
```
