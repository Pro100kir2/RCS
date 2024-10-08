1) Открываем терминал
2) `ls` #  вводим чтобы посмотреть доступные папки
3) `cd $your_directory_name` # Заходим в папку куда хотим скачать проект 
4) `git clone https://github.com/Pro100kir2/RCS` # используем данную команду для копирования всех файлов на ваше устройство
5) скачиваем Docker из любого удобного источника : 
 На винду : https://docs.docker.com/desktop/install/windows-install/
 После чего установите git : https://git-scm.com/
 На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
 На Linux установка зависит от дистрибутива 
6) `docker build -t routers_control_status .` # вводим команду для создания контейнера 
7) `docker run -it routers_control_status`   # Запускаем контейнер и наслаждаемся 
