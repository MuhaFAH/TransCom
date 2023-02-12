RUSSIAN LANGUAGE:

TRANSCOM

Автор: Мухаммед Абдуллоев

Цель программы (идея): помощь в отправлениях и учёте транспортных перевозок, чтобы было легче определять время возвращения ТС, контролировать базу клиентов и иметь информацию об истории перевозок

Целевая аудитория: транспортные компании

Реализация: имеется 10 основных классов (StartWindow, MainWindow, NewOrder, AddClients, RemoveClients, ControlClients, AddClients, ControlClients, AddTrans, RemoveTrans, RedactTrans, ControlTrans), каждый из которых отвечает за какое-либо окно и его работоспособность, а также 4 функции (check_name_truck, check_numplate, write_report, count_sorting)

При запуске открывается окно входа, запрашивающее логин и пароль (класс StartWindow), нажатие на кнопку «OK» открывает главное окно (класс MainWindow). На главном окне две вкладки. На первой вкладке «Заказы», расположены две таблицы (QTableWidget) нужные чтобы отслеживать расположение транспорта и возможность их отправки, а также вторая вкладка «Клиенты», на которой ещё две таблицы: одна отвечает за рейтинг по количеству заказанных доставок (используется функция count_sorting), вторая за историю клиента, выбираемого из выпадающего списка (QComboBox). Все таблицы заполняются информацией из базы данных. Также на первой вкладке вы увидите 3 кнопки: «Отчёт» (нажатие на неё приводит к открытию окна (QFileDialog), в котором выбирается путь сохранения отчёта и ввод названия документа, в текстовом документе краткая нужная информация о работе компании (используется функция write_report)), «Управление транспортом» и «Новый заказ». 

Нажатие на кнопку «Управление транспортом» приводит к открытию нового окна (класс ControlTrans), в котором таблица всего транспорта и нужная информация о транспорте, а также есть кнопки:
- Кнопка «Добавить новый транспорт», открывающая окно (класс AddTrans), в котором вводится имя, вес, и номер нового транспорта.
- Кнопка «Удалить транспорт», отвечающая за открытие окна (класс RemoveTrans), в котором выбирается удаляемый транспорт из выпадающего списка. Транспорт в пути выбрать нельзя.
- Кнопка «Изменить информацию о транспорте», открывающая окно (класс RedactTrans), в котором выбирается доступный транспорт, после чего заполняются автоматически поля доступной информацией, и допускается их замена нужной.

Стоить учесть, что при добавлении нового транспорта или редактировании информации, есть проверка, на соответствие нормам, номерного знака и названия транспорта (функции check_name_truck, check_numplate)

Нажатие на кнопку «Новый заказ» приводит к открытию окна (класс NewOrder), в котором вводится соответствующая информация: нужный клиент, город, куда доставляется заказ, вес самого груза и транспорт. Всё выбирается из выпадающего списка, кроме веса груза, он записывается (QDoubleSpinBox). Пункт выбора транспорта будет недоступен до тех пор, пока не будет указан вес груза. При указании веса груза, программа автоматически будет подбирать, и сортировать список выбираемого транспорта по оптимальности, при этом выбрав сразу же наиболее оптимальный вариант.

На вкладке «Клиенты» также расположена кнопка «Управление базой клиентов», открывающая еще одно окно (класс ControlClients), на нем расположена таблица, в которой все клиенты компании, сортированные по алфавиту, и 2 кнопки:
- Кнопка «Добавить нового клиента», открывающая окно (класс AddClients), в котором вводится имя клиента. Одного и того же добавить еще раз нельзя.
- Кнопка «Удалить клиента», отвечающая за открытие окна (класс RemoveClients), в котором выбирается удаляемый клиент из выпадающего списка. Убрать клиента, имеющего активный заказ, нельзя.

Вся информация в программе обновляется в течение реального времени. Поэтому внесение новой информации будет сразу же добавлено в соответствующие таблицы.

Библиотеки, необходимые для запуска: PyQt5

ENGLISH LANGUAGE:

TRANSCOM

Author: Muhammed Abdulloev

The purpose of the program (idea): assistance in dispatches and accounting of transportation, so that it is easier to determine the time of return of the vehicle, monitor the customer base and have information about the history of transportation

Target audience: transport companies

Implementation: there are 10 main classes (StartWindow, MainWindow, NewOrder, AddClients, RemoveClients, ControlClients, AddClients, ControlClients, AddTrans, RemoveTrans, RedactTrans, ControlTrans), each of which is responsible for a window and its operability, as well as 4 functions (check_name_truck, check_numplate, write_report, count_sorting)

At startup, the login window opens, requesting login and password (StartWindow class), clicking on the "OK" button opens the main window (MainWindow class). There are two tabs on the main window. On the first tab "Orders", there are two tables (QTableWidget) necessary to track the location of transport and the possibility of sending them, as well as the second tab "Customers", on which there are two more tables: one is responsible for the rating by the number of deliveries ordered (the count_sorting function is used), the second for the history of the client selected from the drop-down list (QComboBox). All tables are filled with information from the database. Also on the first tab you will see 3 buttons: "Report" (clicking on it opens a window (QFileDialog), in which you select the way to save the report and enter the name of the document, in a text document a brief necessary information about the company's work (the write_report function is used)), "Transport Management" and "New order".

Clicking on the "Transport Management" button opens a new window (ControlTrans class), in which a table of all transport and the necessary information about transport, as well as there are buttons:
- The "Add new transport" button, which opens a window (AddTrans class) in which the name, weight, and number of the new transport are entered.
- The "Delete transport" button, which is responsible for opening a window (RemoveTrans class), in which the transport to be deleted is selected from the drop-down list. Transport on the way cannot be selected.
- The "Change transport information" button, which opens a window (RedactTrans class) in which the available transport is selected, after which the fields are filled in automatically with the available information, and their replacement with the necessary one is allowed.

It is worth considering that when adding a new transport or editing information, there is a check for compliance with the norms of the license plate and the name of the transport (check_name_truck, check_numplate functions)

Clicking on the "New Order" button opens a window (the NewOrder class), in which the relevant information is entered: the desired customer, the city where the order is delivered, the weight of the cargo itself and transport. Everything is selected from the drop-down list, except the weight of the cargo, it is recorded (QDoubleSpinBox). The transport selection point will be unavailable until the weight of the cargo is specified. When specifying the weight of the cargo, the program will automatically select and sort the list of selected transport by optimality, while immediately selecting the most optimal option.

On the "Clients" tab there is also a button "Managing the customer base", which opens another window (ControlClients class), it contains a table in which all the company's clients are sorted alphabetically, and 2 buttons:
- The "Add new client" button, which opens a window (AddClients class) in which the client's name is entered. You can't add the same thing again.
- The "Delete Client" button, which is responsible for opening a window (RemoveClients class), in which the client to be deleted is selected from the drop-down list. You cannot remove a client who has an active order.

All information in the program is updated in real time. Therefore, the introduction of new information will be immediately added to the corresponding tables.

Libraries required to run: PyQt5
