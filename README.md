1) Открываем терминал
2) `git clone https://github.com/Pro100kir2/RCS` # используем данную команду для копирования всех файлов на ваше устройство
3) скачиваем Docker из любого удобного источника : 
 На винду : https://docs.docker.com/desktop/install/windows-install/
 После чего установите git : https://git-scm.com/
 На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
 На Linux установка зависит от дистрибутива 
4) `docker build -t routers_control_status .` # вводим команду для создания контейнера 
5) `docker run -it routers_control_status`   # Запускаем контейнер и наслаждаемся 
