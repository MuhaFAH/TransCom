from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QFileDialog
import sqlite3
import sys
from datetime import datetime, timedelta
from start import Ui_Dialog
from MainWindow import Ui_MainWindow
from addTrans import Ui_addTrans
from controlTrans import Ui_ControlTrans
from redactTrans import Ui_RedactTrans
from remTrans import Ui_remTrans
from clients import Ui_Clients
from newOrder import Ui_NewOrder
from remClients import Ui_remClients
from addClients import Ui_addClient
# <-------- ФЛАГИ ДЛЯ ЗАПУСКА ОКОН -------->
START = True
START_main = False
START_controlTrans = False
START_controlClients = False
START_addTrans = False
START_remTrans = False
START_redactTrans = False
START_addClient = False
START_remClient = False
START_newOrder = False
# <-------- КОНСТАНТЫ -------->
AVAILABLE_FOR_USE = '''<<>>'"ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ
1234567890-.QWERTYUIOPASDFGHJKLZXCVBNM \t'''
AVAILABLE_NUMPLATES = '''АВЕКМНОРСТУХ1234567890'''


# <-------- СТАРТОВОЕ ОКНО -------->
def check_name_truck(name):
    # создаем временную переменную, чтобы проверить корректность имени тс
    temp = ''.join(filter(lambda x: x.lower() in AVAILABLE_FOR_USE.lower(), name))
    if not name or name != temp:
        return False
    return True


def check_numplate(name, numplate):
    connection = sqlite3.connect('information.db')
    cursor = connection.cursor()
    # получаем список всех номерных знаков
    models_and_numplates = cursor.execute('''
    SELECT Model, NumPlate
    FROM Trucks''').fetchall()
    connection.close()
    # очищаем от имен моделей и оставляем только номера
    numplates = [numplate[1] for numplate in models_and_numplates]
    # проверяем, нет ли уже такого номера в БД
    # проверяем корректность номера
    temp = ''.join(filter(lambda x: x in AVAILABLE_NUMPLATES, numplate))
    if ((numplate not in numplates or
            (numplates.count(numplate) == 1
             and models_and_numplates[numplates.index(numplate)][0] == name))
            and numplate == temp and numplate[:2].isalpha()
            and numplate[2:5].isdigit() and numplate[5:6].isalpha()
            and len(numplate) == 6):
        return True
    return False


def write_report(save):
    connection = sqlite3.connect('information.db')
    cursor = connection.cursor()
    # получаем всю полезную информацию для отчёта
    clients = cursor.execute("""
    SELECT Name 
    FROM Clients""").fetchall()
    trucks = cursor.execute("""
    SELECT Model, NumPlate, Tonnage
    FROM Trucks""").fetchall()
    log_orders = cursor.execute("""
    SELECT HowTone
    FROM LogOrders""").fetchall()
    # избавляемся от кортежей
    log_orders = [order[0] for order in log_orders]
    orders = cursor.execute("""
    SELECT Who
    FROM orders""").fetchall()
    connection.close()
    # создаем список, в котором содержится весь текст отсчёта
    file = [f'<--------> ОТСЧЁТ БЫЛ СОЗДАН '
            f'{datetime.now().strftime("%d-%m-%Y")} '
            f'В {datetime.now().strftime("%H:%M")} <-------->\n',
            f'--> За всё время было {len(log_orders)} заказов,'
            f' из которых {len(orders)} активные\n',
            f'--> Всего перевезено уже {sum(log_orders)} тонн груза\n',
            f'--> Клиентами и партнёрами компании являются:\n']
    for i in range(len(clients)):
        file.append(f'{i + 1}. {clients[i][0]}\n')
    file.append(f'Всего: {len(clients)}\n')
    file.append(f'--> В компании на данный момент {len(trucks)} грузовиков:\n')
    for i in range(len(trucks)):
        file.append(f'{i + 1}. {trucks[i][0]} | '
                    f'максимум {trucks[i][2]} тонн | '
                    f'номер: {trucks[i][1]}\n')
    # сохраняем файл в виде текстового документа
    with open(save[0], 'w', encoding='utf-8') as report:
        report.writelines(file)


def count_sorting(client):
    return client[1]


class StartWindow(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.continue_btn.clicked.connect(self.run)

    def run(self):
        global START_main
        if self.password.text() == 'admin' and self.login.text() == 'admin':
            START_main = True
            self.close()
        else:  # реагирование на неверный ввод данных
            self.login.setStyleSheet('''background-color: 'white';\n
            border-radius: 5px;\n
            border-style: solid;\n
            border-width: 2px;\n
            border-color: red;''')
            self.password.setStyleSheet('''background-color: 'white';\n
            border-radius: 5px;\n
            border-style: solid;\n
            border-width: 2px;\n
            border-color: red;''')
            self.error.show()


# <-------- ОКНО НОВОГО ЗАКАЗА -------->
class NewOrder(QDialog, Ui_NewOrder):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список клиентов
        clients = cursor.execute("""SELECT Name FROM Clients""").fetchall()
        clients = [client[0] for client in clients]
        clients.sort()  # сортировка для удобства
        # получаем список городов
        cities = cursor.execute("""SELECT Title FROM Cities""").fetchall()
        cities = [city[0] for city in cities]
        cities.sort()  # сортировка для удобства
        # проверка на наличие веса, чтобы можно было подобрать машину
        self.choosedTrans.addItem('-- сначала укажите вес груза --')
        # отлавливаем изменение значения поля веса
        self.orderTonnage.valueChanged.connect(self.open_trans)
        connection.close()
        # добавление в поле выбора клиентов и городов
        self.choosedClient.addItems(clients)
        self.choosedCity.addItems(cities)
        # кнопки закрытия окна
        self.acceptButton.clicked.connect(self.add_order)
        self.rejectButton.clicked.connect(self.quit)
        self.rejected.connect(self.quit)

    # <-------- ДОБАВЛЕНИЕ НОВОГО ЗАКАЗА -------->
    def add_order(self):
        global START_main
        try:
            # подключение к БД
            connection = sqlite3.connect('information.db')
            cursor = connection.cursor()
            # считывание данных с полей
            client_name = self.choosedClient.currentText()
            transport_name = self.choosedTrans.currentText()
            city = self.choosedCity.currentText()
            tones = self.orderTonnage.value()
            # проверка на верную грузоподъёмность
            if int(tones) <= 0:
                raise ValueError
            # проверка на доступность машин
            if transport_name == '-- нет машин --':
                raise NotADirectoryError
            # узнаем время пути до выбранного города
            time_need = cursor.execute(f"""
            SELECT Distance 
            FROM Cities 
            WHERE Title='{city}'""").fetchall()[0][0]
            # время в момент заказа
            time = datetime.now().strftime('%d-%m-%Y')
            # время когда вернётся ТС после заказа
            time_when_back = (datetime.now() +
                              timedelta(days=time_need * 2)).strftime('%d-%m-%Y')
            # <-------- ДОБАВЛЕНИЕ ЗАКАЗА В БД -------->
            cursor.execute(f"""
            INSERT INTO Orders(Who, BackInTime, WhereGo, 
            HowTone, Transport, NumPlate)
            VALUES('{client_name}', '{time_when_back}',
            '{city}', {tones}, 
            '{transport_name.split(" | ")[0]}',
            '{transport_name.split(": ")[1]}')""")
            # <-------- ДОБАВЛЕНИЕ ЗАКАЗА В ИСТОРИЮ -------->
            cursor.execute(f"""
            INSERT INTO LogOrders(Who, Time, WhereGo, 
            HowTone, Transport)
            VALUES('{client_name}', '{time}',
            '{city}', {tones}, 
            '{transport_name.split(" | ")[0]}')""")
            # <-------- ОТПРАВЛЕНИЕ ГРУЗОВИКА -------->
            cursor.execute(f"""
            UPDATE Trucks SET In_A_Way='ДА' 
            WHERE NumPlate='{transport_name.split(": ")[1]}'""")
            # <-------- ИЗМЕНЕНИЕ СЧЁТЧИКА ЗАКАЗОВ -------->
            cursor.execute(f"""
            UPDATE Clients SET CountOrder = CountOrder + 1 
            WHERE Name='{client_name}'""")
            connection.commit()  # сохранение изменений
            connection.close()
            # выход из окна и возвращение в главное
            START_main = True
            self.close()
        # <-------- ОТЛОВ ОШИБОК И РЕАКЦИЯ НА НИХ -------->
        except (ValueError, NotADirectoryError) as error:
            if error.__class__ == ValueError:
                self.orderTonnage.setStyleSheet(
                    '''background-color: 'white'; border-radius: 5px;
                       border-style: solid; border-width: 2px;
                       border-color: red; selection-background-color: white; 
                       selection-color:black''')
                self.choosedTrans.setStyleSheet(
                    '''background-color: 'white'; border-radius: 5px;
                       border-style: solid; border-width: 2px;
                       border-color: black;''')
                self.error.setText('Неверный вес груза')
            if error.__class__ == NotADirectoryError:
                self.choosedTrans.setStyleSheet(
                    '''background-color: 'white'; border-radius: 5px;
                       border-style: solid; border-width: 2px;
                       border-color: red;''')
                self.orderTonnage.setStyleSheet(
                    '''background-color: 'white'; border-radius: 5px;
                       border-style: solid; border-width: 2px;
                       border-color: black; selection-background-color: white; 
                       selection-color:black''')
                self.error.setText('Нет доступных машин')

    # <-------- ПОЛЕ ТРАНСПОРТА -------->
    def open_trans(self):
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем транспорт, не находящийся в пути
        # и подходящий по грузоподъёмности
        transport = cursor.execute(f"""
        SELECT Model, Tonnage, NumPlate 
        FROM Trucks
        WHERE In_A_Way='НЕТ'
        AND Tonnage >= {self.orderTonnage.value()}""").fetchall()
        # если такие машины есть
        if transport:
            self.choosedTrans.clear()
            # сортировать по грузоподъёмности
            transport.sort(key=self.sort_trans)
            # добавление транспорта в список выбора
            for trans in transport:
                self.choosedTrans.addItem(f'{trans[0]} | МАКСИМУМ '
                                          f'{trans[1]} ТОНН | НОМЕР: '
                                          f'{trans[2]}')
        # если машин нет
        else:
            self.choosedTrans.clear()
            self.choosedTrans.addItem('-- нет машин --')

    # <-------- СОРТИРОВКА ТС -------->
    def sort_trans(self, tonnage):
        # сортируем по минимальной разнице в весе
        # между грузоподъёмностью и весом заказа
        return tonnage[1] - self.orderTonnage.value()

    def quit(self):
        global START_main
        START_main = True
        self.close()


# <-------- ГЛАВНОЕ МЕНЮ -------->
class MainWindow(QDialog, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # <-------- ТРАНСПОРТ В ПУТИ -------->
        ordered_trans = cursor.execute("""
        SELECT Transport, Who, HowTone, WhereGo, BackInTime
        FROM Orders""").fetchall()
        # проверка, не наступил ли срок возвращения какого либо транспорта
        for ordered in ordered_trans:
            # дата заказа
            order_time = datetime.strptime(ordered[4], "%d-%m-%Y")
            if order_time.strptime(ordered[4], "%d-%m-%Y") < datetime.now():
                # получаем список номеров вернувшихся машин
                returning_trucks = cursor.execute(f"""
                SELECT NumPlate
                FROM Orders
                WHERE BackInTime='{ordered[4]}'""").fetchall()
                # очищаем от кортежей, оставляя только номера
                returning_trucks = [numplate[0] for numplate in returning_trucks]
                for numplate in returning_trucks:
                    # обновляем грузовики, обозначая их как вернувшихся
                    cursor.execute(f"""
                    UPDATE Trucks
                    SET In_A_Way='НЕТ'
                    WHERE NumPlate='{numplate}'""")
                # убираем уже старые заказы
                cursor.execute(f"""
                DELETE FROM Orders
                WHERE BackInTime='{ordered[4]}'""")
                connection.commit()
        # <-------- ОБНОВЛЕНИЕ ИНФО -------->
        free_trans = cursor.execute("""
                SELECT Model, Tonnage, NumPlate 
                FROM Trucks 
                WHERE In_A_Way='НЕТ'""").fetchall()
        ordered_trans = cursor.execute("""
                SELECT Transport, Who, HowTone, WhereGo, BackInTime
                FROM Orders""").fetchall()
        # <-------- ОБНОВЛЕНИЕ ИНФО -------->
        # получаем информацию для рейтинговой таблицы заказчиков
        count_rating = cursor.execute("""
        SELECT Name, CountOrder
        FROM Clients""").fetchall()
        # сортируем по количеству заказов
        count_rating.sort(key=count_sorting, reverse=True)
        # заполняем таблицы
        # <-------- ТАБЛИЦА СВОБОДНЫХ ТС -------->
        for i, row in enumerate(free_trans):
            self.free_tracks.setRowCount(
                self.free_tracks.rowCount() + 1)
            for j, elem in enumerate(row):
                self.free_tracks.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.free_tracks.resizeRowsToContents()
        self.free_tracks.verticalHeader().hide()
        # <-------- ТАБЛИЦА ТС В ПУТИ -------->
        for i, row in enumerate(ordered_trans):
            self.a_way_trucks.setRowCount(
                self.a_way_trucks.rowCount() + 1)
            for j, elem in enumerate(row):
                self.a_way_trucks.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.a_way_trucks.resizeRowsToContents()
        self.a_way_trucks.verticalHeader().hide()
        # <-------- ТАБЛИЦА РЕЙТИНГА -------->
        for i, row in enumerate(count_rating):
            self.rating_table.setRowCount(
                self.rating_table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.rating_table.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.rating_table.resizeRowsToContents()
        self.rating_table.verticalHeader().hide()
        # <---------------------------------->
        self.choose_client.currentTextChanged.connect(self.show_history)
        self.control_trans_btn.clicked.connect(self.run_control)
        self.control_btn.clicked.connect(self.run_control_clients)
        self.add_btn.clicked.connect(self.new_order)
        self.reportButton.clicked.connect(self.get_report)
        # заполняем список выбора истории клиентов
        self.choose_client.addItems(
            sorted([i[0] for i in cursor.execute("""SELECT Name FROM Clients""").fetchall()]))
        connection.close()

    def show_history(self):
        # устанавливаем количество колонок в ноль
        # чтобы при выборе другого клиента не было лишних
        self.story_orders.setRowCount(0)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список всех заказов, принадлежащих
        # выбранному клиенту из списка
        old_orders = cursor.execute(f"""
        SELECT Transport, Time, WhereGo, HowTone 
        FROM LogOrders
        WHERE Who='{self.choose_client.currentText()}'""").fetchall()
        connection.close()
        # <-------- ТАБЛИЦА ИСТОРИИ ЗАКАЗОВ -------->
        for i, row in enumerate(old_orders):
            self.story_orders.setRowCount(
                self.story_orders.rowCount() + 1)
            for j, elem in enumerate(row):
                self.story_orders.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.story_orders.resizeRowsToContents()
        self.story_orders.verticalHeader().hide()

    def new_order(self):
        global START_newOrder
        START_newOrder = True
        self.close()

    def run_control(self):
        global START_controlTrans
        START_controlTrans = True
        self.close()

    def run_control_clients(self):
        global START_controlClients
        START_controlClients = True
        self.close()

    def get_report(self):
        save = QFileDialog.getSaveFileName(self, 'Сохранить отчёт', '', '*.txt')
        if any(save):
            write_report(save)


# <-------- ДОБАВЛЕНИЕ КЛИЕНТОВ -------->
class AddClients(QDialog, Ui_addClient):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acceptButton.clicked.connect(self.add_client)
        self.rejectButton.clicked.connect(self.quit)
        self.rejected.connect(self.quit)

    def quit(self):
        global START_controlClients
        START_controlClients = True
        self.close()

    def add_client(self):
        global START_controlClients
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список всех клиентов
        clients = cursor.execute("""
        SELECT Name 
        FROM Clients""").fetchall()
        # убираем кортежи
        clients = [client[0] for client in clients]
        # проверяем, нет ли уже такого клиента
        if self.nameNewClient.text():
            if self.nameNewClient.text() not in clients:
                # добавляем клиента в базу
                cursor.execute(f"""
                INSERT INTO Clients(Name, CountOrder)
                VALUES('{self.nameNewClient.text()}', 0)""")
                connection.commit()
                connection.close()
                START_controlClients = True
                self.close()
            else:
                # ошибка, что такой уже есть в базе
                self.nameNewClient.setStyleSheet(
                    '''background-color: 'white';
                           border-radius: 5px;
                           border-style: solid;
                           border-width: 2px;
                           border-color: red;''')
                self.error.setText('Уже в базе')


# <-------- УДАЛЕНИЕ КЛИЕНТОВ -------->
class RemoveClients(QDialog, Ui_remClients):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acceptButton.clicked.connect(self.rem_client)
        self.rejectButton.clicked.connect(self.quit)
        self.rejected.connect(self.quit)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список всех клиентов
        clients = cursor.execute("""
        SELECT Name 
        FROM Clients""").fetchall()
        # очищаем от кортежей
        clients = [client[0] for client in clients]
        # получаем список тех клиентов, у которых активный заказ
        checking_order = cursor.execute("""
        SELECT Who 
        FROM Orders""").fetchall()
        # очищаем от кортежей
        checking_order = [order_client[0] for order_client in checking_order]
        # оставляем лишь тех, у кого нет активного заказа
        clients = list(filter(lambda x: x not in checking_order, clients))
        # проверяем, есть ли вообще такие клиенты
        if clients:
            for client in clients:
                self.selectRemClients.addItem(f'{client}')
        else:
            self.selectRemClients.addItem('-- нет доступных клиентов --')
        connection.commit()
        connection.close()

    def rem_client(self):
        global START_controlClients
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        cursor.execute(f"""
        DELETE 
        FROM Clients
        WHERE Name='{self.selectRemClients.currentText()}'""")
        connection.commit()
        connection.close()
        START_controlClients = True
        self.close()

    def quit(self):
        global START_controlClients
        START_controlClients = True
        self.close()


# <-------- УПРАВЛЕНИЕ БАЗОЙ КЛИЕНТОВ -------->
class ControlClients(QDialog, Ui_Clients):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_to_main2.clicked.connect(self.quit)
        self.remClients.clicked.connect(self.rem_client)
        self.addNewClient.clicked.connect(self.add_client)
        # получаем список всех клиентов
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        clients = cursor.execute("""
                SELECT Name
                FROM Clients """).fetchall()
        # убираем кортежи и сортируем для удобства
        clients = [client[0] for client in clients]
        clients.sort()
        # заполняем таблицу
        for client in clients:
            self.clientsList.addItem(client)

    def quit(self):
        global START_main
        START_main = True
        self.close()

    def rem_client(self):
        global START_remClient
        START_remClient = True
        self.close()

    def add_client(self):
        global START_addClient
        START_addClient = True
        self.close()


# <-------- ДОБАВЛЕНИЕ ТРАНСПОРТА -------->
class AddTrans(QDialog, Ui_addTrans):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.acceptButton.clicked.connect(self.add_trans)
        self.rejectButton.clicked.connect(self.quit)
        self.rejected.connect(self.quit)

    def add_trans(self):
        global START_controlTrans
        try:
            connection = sqlite3.connect('information.db')
            cursor = connection.cursor()
            # проверяем все данные на корректность
            name_truck = self.newModelName.text()
            if not check_name_truck(name_truck):
                raise NameError
            tonnage = self.newTonnage.value()
            if tonnage == 0:
                raise ZeroDivisionError
            new_number = self.newCarNumber.text().upper()
            if not check_numplate(name_truck, new_number):
                raise SyntaxError
            # добавляем транспорт в БД
            cursor.execute(f"""
            INSERT INTO Trucks(Model, Tonnage, NumPlate) 
            VALUES('{name_truck}','{tonnage}', '{new_number}')""")
            connection.commit()
            connection.close()
            START_controlTrans = True
            self.close()
        # выдаем ошибку при некорректных данных
        except (SyntaxError, ZeroDivisionError, NameError):
            self.newModelName.setStyleSheet('''
            background-color: 'white';\nborder-radius: 5px;\n
            border-style: solid;\nborder-width: 2px;\n
            border-color: red;''')
            self.newTonnage.setStyleSheet('''
            background-color: 'white'; border-radius: 5px;
            border-style: solid; border-width: 2px;
            border-color: red; selection-background-color: white; 
            selection-color: black''')
            self.newCarNumber.setStyleSheet('''
            background-color: 'white';\nborder-radius: 5px;\n
            border-style: solid;\nborder-width: 2px;\n
            border-color: red;''')
            self.error.setText('Допущена ошибка')

    def quit(self):
        global START_controlTrans
        START_controlTrans = True
        self.close()


# <-------- УДАЛЕНИЕ ТРАНСПОРТА -------->
class RemoveTrans(QDialog, Ui_remTrans):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список свободных тс
        free_trans = cursor.execute(f"""
        SELECT Model, Tonnage, NumPlate 
        FROM Trucks
        WHERE In_A_Way='НЕТ'""").fetchall()
        connection.close()
        # проверяем, остались ли вообще свободные тс
        if free_trans:
            # заполняем список выбора транспортом
            for trans in free_trans:
                self.selectRemTrans.addItem(f'{trans[0]} | МАКСИМУМ '
                                            f'{trans[1]} ТОНН | НОМЕР: '
                                            f'{trans[2]}')
        else:
            self.selectRemTrans.addItem('-- нет доступных машин --')
        self.acceptButton.clicked.connect(self.del_trans)
        self.rejectButton.clicked.connect(self.quit)
        self.rejected.connect(self.quit)

    def del_trans(self):
        global START_controlTrans
        numplate = self.selectRemTrans.currentText().split(": ")[1]
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        cursor.execute(f"""
                DELETE
                FROM Trucks
                WHERE NumPlate='{numplate}'""")
        connection.commit()
        connection.close()
        START_controlTrans = True
        self.close()

    def quit(self):
        global START_controlTrans
        START_controlTrans = True
        self.close()


# <-------- РЕДАКТИРОВАНИЕ ТРАНСПОРТА -------->
class RedactTrans(QDialog, Ui_RedactTrans):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список свободных тс
        free_trans = cursor.execute(f"""
        SELECT Model, Tonnage, NumPlate 
        FROM Trucks
        WHERE In_A_Way='НЕТ'""").fetchall()
        connection.close()
        # проверяем, есть ли вообще свободные тс
        if free_trans:
            # заполняем список выбора транспортом
            for trans in free_trans:
                self.selectRedactTrans.addItem(f'{trans[0]} | МАКСИМУМ '
                                               f'{trans[1]} ТОНН | НОМЕР: '
                                               f'{trans[2]}')
        else:
            self.selectRedactTrans.addItem('-- нет доступных машин --')
        # заполняем всю информацию с помощью выбранного из списка тс
        self.newModelName.setText(self.selectRedactTrans.currentText().split(" | ")[0])
        self.newTonnage.setValue(float(self.selectRedactTrans.
                                       currentText().split(" | ")[1].split(' ')[1]))
        self.newCarNumber.setText(self.selectRedactTrans.currentText().split(": ")[1])
        # проверяем, не выбрали ли другое тс из списка
        self.selectRedactTrans.currentTextChanged.connect(self.select_trans)
        self.acceptButton.clicked.connect(self.change_info)
        self.rejectButton.clicked.connect(self.quit)
        self.rejected.connect(self.quit)

    def quit(self):
        global START_controlTrans
        START_controlTrans = True
        self.close()

    def change_info(self):
        global START_controlTrans
        try:
            connection = sqlite3.connect('information.db')
            cursor = connection.cursor()
            # проверяем корректность введённых данных
            if not check_name_truck(self.newModelName.text()):
                raise NameError
            if self.newTonnage.value() == 0:
                raise ZeroDivisionError
            if not check_numplate(self.newModelName.text(), self.newCarNumber.text()):
                raise SyntaxError
            # обновляем информацию о ТС
            cursor.execute(f"""
            UPDATE Trucks SET 
            Model='{self.newModelName.text()}', 
            NumPlate='{self.newCarNumber.text()}', 
            Tonnage={self.newTonnage.value()} 
            WHERE NumPlate='{self.selectRedactTrans.currentText().split(": ")[1]}'""")
            connection.commit()
            connection.close()
            START_controlTrans = True
            self.close()
        # выдаем ошибку, если какие-либо данные некорректны
        except (SyntaxError, ZeroDivisionError, NameError):
            self.newModelName.setStyleSheet('''
            background-color: 'white';\nborder-radius: 5px;\n
            border-style: solid;\nborder-width: 2px;\n
            border-color: red;''')
            self.newTonnage.setStyleSheet('''
            background-color: 'white'; border-radius: 5px;
            border-style: solid; border-width: 2px;
            border-color: red; selection-background-color: white; 
            selection-color: black''')
            self.newCarNumber.setStyleSheet('''
            background-color: 'white';\nborder-radius: 5px;\n
            border-style: solid;\nborder-width: 2px;\n
            border-color: red;''')
            self.error.setText('Допущена ошибка')

    def select_trans(self):
        # устанавливаем актуальную информацию по ячейкам
        name = self.selectRedactTrans.currentText().split(" | ")[0]
        numplate = self.selectRedactTrans.currentText().split(": ")[1]
        tonnage = self.selectRedactTrans.currentText().split(" | ")[1].split(' ')[1]
        self.newModelName.setText(name)
        self.newTonnage.setValue(float(tonnage))
        self.newCarNumber.setText(numplate)


# <-------- УПРАВЛЕНИЕ БАЗОЙ ТС -------->
class ControlTrans(QDialog, Ui_ControlTrans):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_to_main1.clicked.connect(self.quit)
        self.addNewTrans.clicked.connect(self.run_addtrans)
        self.remOldTrans.clicked.connect(self.run_remtrans)
        self.redactOldTrans.clicked.connect(self.run_redacttrans)
        connection = sqlite3.connect('information.db')
        cursor = connection.cursor()
        # получаем список всего транспорта
        all_trans_list = cursor.execute("""
                SELECT Model, Tonnage, NumPlate, In_A_Way 
                FROM Trucks""").fetchall()
        # <-------- ТАБЛИЦА ТС -------->
        for i, row in enumerate(all_trans_list):
            self.allTransList.setRowCount(
                self.allTransList.rowCount() + 1)
            for j, elem in enumerate(row):
                self.allTransList.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.allTransList.resizeRowsToContents()
        self.allTransList.verticalHeader().hide()
        connection.close()

    def quit(self):
        global START_main
        START_main = True
        self.close()

    def run_addtrans(self):
        global START_addTrans
        START_addTrans = True
        self.close()

    def run_remtrans(self):
        global START_remTrans
        START_remTrans = True
        self.close()

    def run_redacttrans(self):
        global START_redactTrans
        START_redactTrans = True
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    while True:
        if (not START and not START_main
                and not START_newOrder and not START_addTrans
                and not START_addClient and not START_redactTrans
                and not START_remTrans and not START_remClient
                and not START_controlClients and not START_controlTrans):
            break
        if START:
            program = StartWindow()
            program.show()
            program.exec()
            START = False

        if START_main:
            program = MainWindow()
            program.show()
            program.exec()
            START_main = False

        if START_controlTrans:
            program = ControlTrans()
            program.show()
            program.exec()
            START_controlTrans = False

        if START_controlClients:
            program = ControlClients()
            program.show()
            program.exec()
            START_controlClients = False

        if START_addTrans:
            program = AddTrans()
            program.show()
            program.exec()
            START_addTrans = False

        if START_remTrans:
            program = RemoveTrans()
            program.show()
            program.exec()
            START_remTrans = False

        if START_redactTrans:
            program = RedactTrans()
            program.show()
            program.exec()
            START_redactTrans = False

        if START_addClient:
            program = AddClients()
            program.show()
            program.exec()
            START_addClient = False

        if START_remClient:
            program = RemoveClients()
            program.show()
            program.exec()
            START_remClient = False

        if START_newOrder:
            program = NewOrder()
            program.show()
            program.exec()
            START_newOrder = False
