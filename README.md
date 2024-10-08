1) Заходим в любую удобную папку куда хотим скопировать проект.
2) `git clone https://github.com/Pro100kir2/RCS` # копируем все файлы на ваше устройство
3) скачиваем Docker из люого удобного источника : 
 На винду : https://docs.docker.com/desktop/install/windows-install/
 После чего установите git : https://git-scm.com/
 На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
 На Linux установка зависит от дистрибутива 
5) docker build -t routers_control_status . # Создаем контейнер 
6) docker run -it routers_control_status   # Запускаем контейнер и наслаждаемся 
