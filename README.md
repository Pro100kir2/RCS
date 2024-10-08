1) Открываем терминал
2) `ls` #  вводим чтобы посмотреть доступные папки
3) `mkdir RCS` # создаем папку RCS
4) `cd RCS` # Заходим в папку
5) `git clone https://github.com/Pro100kir2/RCS` # используем данную команду для копирования всех файлов на ваше устройство
6) скачиваем Docker из любого удобного источника : 
 На винду : https://docs.docker.com/desktop/install/windows-install/
 После чего установите git : https://git-scm.com/
 На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
 На Linux установка зависит от дистрибутива 
7) `docker build -t routers_control_status .` # вводим команду для создания контейнера 
8) `docker run -it routers_control_status`   # Запускаем контейнер и наслаждаемся 
