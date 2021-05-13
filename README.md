# FastAPI L9 Project

**Оглавление**  
[Технические характеристики](#Технические-характеристики)  
[Основные файлы](#основные-файлы)  
[Настройка и запуск](#настройка-и-запуск)  
[FastAPI](#fastapi)   
<!-- [Методы](#методы)   
[Workflow Runner](#workflow-runner)  
[Restart Queue](#restart-queue)  
 -->
# ✨Технические характеристики✨ 

- Python 3.8
- Framework:  - [FastAPI 0.63.0](https://fastapi.tiangolo.com/)


|Database| ORM|
| --- | --- |
|PostgreSQL 12.5-1 | [ORMAR 0.10.6](https://collerek.github.io/ormar/)|
|MongoDB 4.4.6 | [Motor 2.4.0](https://motor.readthedocs.io/en/stable/)|


# ✨Основные файлы✨ 

- main.py – запуск FastAPI

- processing.py – воркер

- env - изолированная среда проекта

# ✨Настройка и запуск✨ 

Подключаемся к удаленной машине и переходим в папку r2d2.
```
tmux attach -t fastapi 
```
> `Hotkeys и настройка tmux:`  
> [https://habr.com/ru/post/126996/](https://habr.com/ru/post/126996/)  
> [https://losst.ru/shpargalka-po-tmux](https://losst.ru/shpargalka-po-tmux)

# ✨FastAPI✨ 

Подключаемся к изолированной среде **env**

Запускаем FastAPI

```
uvicorn main:app --reload --host {IP} --port {port}
```

<!-- # ✨Методы✨ 

При работающем FastAPI можно найти документацию здесь:{ip}{port}/docs

| METHOD | URL | INFO |
| --- | --- | --- |
| GET | /api/v1/texts/information | статус очереди текстов |
| POST | /api/v1/texts/generate | генерация текста |
| GET | /api/v1/texts/{text\_id} | получить текст по ID |
| DELETE | /api/v1/texts/{text\_id} | удалить текст по ID |
| GET | /api/v1/clusters/information | список кластеров |
| GET | /api/v1/ai\_models/information | список ai моделей |
 -->

<!-- # ✨Workflow Runner✨ 

Запускаем процесс поочередной генерации текстов и последующей записи результатов в БД

Запуск через изолированную среду env
```
python workflow_runner.py
```
# ✨Restart Queue✨ 
Сбрасывает статус в БД из **in\_progress** в **not\_started**  
Запуск через изолированную среду env
```
python restart_queue.py 
```
 -->