Запуск:
```
sudo docker build -t todo_list .
sudo docker run -p 8000:8000 todo_list
```
История разработки:
1) Сделал todo-лист на джанго, запускающийся в venv.\\
2) Оказывается, нужен ещё докер...\\
3) В итоге, запускается докер, в котором запускается venv, в котором запускается сервер\\
4) ...
5) Теперь без venv.

Баги в процессе:
1) Почему 0.0.0.0:8000 а не 8000
https://stackoverflow.com/questions/27806631/docker-rails-app-fails-to-be-served-curl-56-recv-failure-connection-reset
2) Нельзя прервать Ctrl+C /+D
https://github.com/moby/moby/issues/2838  
 "1 year later we still can't Ctrl+C a docker container"