1) Заходим в любую удобную папку куда хотим скопировать проект.
git clone https://github.com/Pro100kir2/RCS # копируем все файлы на ваше устройство
2) скачиваем Docker из люого удобного источника : 
На винду : https://docs.docker.com/desktop/install/windows-install/
На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
На Linux установка зависит от дистрибутива 
3) docker build -t routers_control_status . # Создаем контейнер 
4) docker run -it routers_control_status   # Запускаем контейнер и наслаждаемся 
