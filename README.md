1) Заходим в любую удобную папку куда хотим скопировать проект.
2) git clone https://github.com/Pro100kir2/RCS # копируем все файлы на ваше устройство
3) скачиваем Docker из люого удобного источника : 
3.1) На винду : https://docs.docker.com/desktop/install/windows-install/
3.2) На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
3.3) На Linux установка зависит от дистрибутива 
4) docker build -t routers_control_status . # Создаем контейнер 
5) docker run -it routers_control_status   # Запускаем контейнер и наслаждаемся 
