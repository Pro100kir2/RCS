1) Если у вас Windows с начала скачайте git : https://git-scm.com/downloads/win
2) Открываем Git Bash на Windows или просто заходим в терминал если на MacOS или Linux.
3) `git clone https://github.com/Pro100kir2/RCS` # используем данную команду для копирования всех файлов на ваше устройство
4) скачиваем Docker из любого удобного источника : 
 На винду : https://docs.docker.com/desktop/install/windows-install/
 На Мак ОС : https://docs.docker.com/desktop/install/mac-install/
 На Linux установка зависит от дистрибутива 
5) cd RCS/
6) `docker build -t routers_control_status .` # вводим команду для создания контейнера 
7) `docker run -it routers_control_status`   # Запускаем контейнер и наслаждаемся 


Для дальнейшего использования нужно будет запускать докер и в терминале вводить `docker run -it routers_control_status`
