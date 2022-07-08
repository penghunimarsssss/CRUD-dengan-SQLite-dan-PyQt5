from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem
from matplotlib.pyplot import margins 
from DataMahasiswa import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection.py')
os.system('python CreateTable.py')

global nim, nama, kelas, prodi, jurusan, telefon, email

# Users (nim INT, nama TEXT, kelas TEXT, prodi TEXT, jurusan TEXT, telefon TEXT, email TEXT)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.pushButtonDaftarClick()
        self.ui.pushButtonDaftar.clicked.connect(self.pushButtonDaftarClick)
        self.ui.pushButtonSimpan.clicked.connect(self.pushButtonSimpanClick)
        self.ui.pushButtonHapus.clicked.connect(self.pushButtonHapusClick)
        self.ui.pushButtonPerbarui.clicked.connect(self.pushButtonPerbaruiClick)
        self.ui.tableWidgetDaftar.clicked.connect(self.ListOnClick) 
 
    def pushButtonClear(self):
        self.ui.lineEditNIM.clear()
        self.ui.lineEditNama.clear()
        self.ui.lineEditKelas.clear()
        self.ui.lineEditProdi.clear()
        self.ui.lineEditJurusan.clear()
        self.ui.lineEditTelefon.clear()
        self.ui.lineEditEmail.clear()

    def ListOnClick(self): 
        self.ui.lineEditNIM.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 0).text())
        self.ui.lineEditNama.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 1).text())
        self.ui.lineEditKelas.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 2).text())
        self.ui.lineEditProdi.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 3).text())
        self.ui.lineEditJurusan.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 4).text())
        self.ui.lineEditTelefon.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 5).text())
        self.ui.lineEditEmail.setText(self.ui.tableWidgetDaftar.item(self.ui.tableWidgetDaftar.currentRow(), 6).text())
 
    def pushButtonSimpanClick(self): 
        nim = self.ui.lineEditNIM.text()
        nama = self.ui.lineEditNama.text()
        kelas = self.ui.lineEditKelas.text()
        prodi = self.ui.lineEditProdi.text()
        jurusan = self.ui.lineEditJurusan.text()
        telefon = self.ui.lineEditTelefon.text()
        email = self.ui.lineEditEmail.text()

        try:
            self.conn = sql.connect("DataMahasiswa.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO Users VALUES (?,?,?,?,?,?,?)",(nim,nama,kelas,prodi,jurusan,telefon,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.pushButtonClear()
        self.pushButtonDaftarClick()

    def pushButtonDaftarClick(self):  
        self.ui.tableWidgetDaftar.clear()
        self.ui.tableWidgetDaftar.setColumnCount(7)
        self.ui.tableWidgetDaftar.setHorizontalHeaderLabels(('NIM','Nama','Kelas','Prodi','Jurusan','Telefon','Email'))
        self.ui.tableWidgetDaftar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('DataMahasiswa.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Users"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tableWidgetDaftar.setRowCount(len(rows))
        
        for rowIndeks, rowData in enumerate(rows):
            for columnIndeks, columnData in enumerate (rowData):
                self.ui.tableWidgetDaftar.setItem(rowIndeks,columnIndeks,QTableWidgetItem(str(columnData))) 
    
    def pushButtonPerbaruiClick(self):  
        nim = self.ui.lineEditNIM.text()
        nama = self.ui.lineEditNama.text()
        kelas = self.ui.lineEditKelas.text()
        prodi = self.ui.lineEditProdi.text()
        jurusan = self.ui.lineEditJurusan.text()
        telefon = self.ui.lineEditTelefon.text()
        email = self.ui.lineEditEmail.text()

        try:
            self.conn = sql.connect("DataMahasiswa.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Users SET nama = ?, kelas = ?, prodi = ?, jurusan = ?, \
                telefon = ?, email = ? WHERE nim = ?",(nama,kelas,prodi,jurusan,telefon,email,nim))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.pushButtonClear()
        self.pushButtonDaftarClick()

    def pushButtonHapusClick(self): 
        nim = self.ui.lineEditNIM.text() 

        try:
            self.conn = sql.connect("DataMahasiswa.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Users WHERE nim = ?  ', (nim,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.pushButtonClear()
        self.pushButtonDaftarClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()