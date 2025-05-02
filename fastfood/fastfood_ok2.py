# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QCoreApplication, QTime, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent 
from PyQt5.QtGui import * 
from PyQt5.uic import loadUiType
from PyQt5 import QtWidgets, QtCore
import sys
from os import path

#import UI file
FORM_CLASS,_ =loadUiType(path.join(path.dirname(__file__),'fastfood_ok4.ui'))	

class Resto(QMainWindow, FORM_CLASS):
    invoice_no = 1
    def __init__(self, parent=None):
        super(Resto, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.maFenetre()
        # facturetGrid = QGridLayout()
        # mealtGrid = QGridLayout()
        # drinktGrid = QGridLayout()
        # self.scrFacture.adjustSize()
        # date = QDate.currentDate()
        invNumber = QDateTime.currentDateTime()
        # time = QTime.currentTime()
        # self.lbl_recDate.setText("التاريخ: "+date.toString(Qt.ISODate))
        # self.lbl_recTime.setText("الوقت"+time.toString(Qt.DefaultLocaleLongDate))
        self.lbl_recNumberval.setText(str(Resto.invoice_no))
        self.lbl_recNumberValue.setText(invNumber.toString(Qt.ISODate))
        # self.lbl_recNumberText.setText("رقم الفاتورة")
        # self.closeButton.clicked.connect(self.CloseApp)
        self.closeButton.clicked.connect(lambda: self.close())        
        self.btn_calculerFact.clicked.connect(self.calculerFacture)
        self.btn_effacerTout.clicked.connect(self.remiseZero)

        # self.btn_Order.clicked.connect(self.LaCommande)
        # ###############################################
        self.chkShrimp.toggled.connect(lambda: self.selectedItem(self.chkShrimp,self.chkShrimpPrice,self.chkShrimpQuant))
        self.chkFish.toggled.connect(lambda: self.selectedItem(self.chkFish,self.chkFishPrice,self.chkFishQuant))
        self.chkBeef.toggled.connect(lambda: self.selectedItem(self.chkBeef,self.chkBeefPrice,self.chkBeefQuant))
        self.chkChicken.toggled.connect(lambda: self.selectedItem(self.chkChicken,self.chkChickenPrice,self.chkChickenQuant))
        self.chkBeefChawarma.toggled.connect(lambda: self.selectedItem(self.chkBeefChawarma,self.chkBeefChawarmaPrice,self.chkBeefChawarmaQuant))
        self.chkChickenChawarma.toggled.connect(lambda: self.selectedItem(self.chkChickenChawarma,self.chkChickenChawarmaPrice,self.chkChickenChawarmaQuant))
        self.chkMeatRiceNuts.toggled.connect(lambda: self.selectedItem(self.chkMeatRiceNuts,self.chkMeatRiceNutsPrice,self.chkMeatRiceNutsQuant))
        self.chkMeatKofta.toggled.connect(lambda: self.selectedItem(self.chkMeatKofta,self.chkMeatKoftaPrice,self.chkMeatKoftaQuant))
        self.chkVegetables.toggled.connect(lambda: self.selectedItem(self.chkVegetables,self.chkVegetablesPrice,self.chkVegetablesQuant))
        # ###############################################  
       
        
    def selectedItem(self, bt_check, lblPrice, lblQuantity):
        if bt_check.isChecked() == True:
            checkName = bt_check.text()
            price = float(lblPrice.text())
            quantity = float(lblQuantity.text())
            
            try:
                text = self.scrFacture.text()
                self.scrFacture.setText(text+"\n{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\n".format(checkName,price,quantity,str(price*quantity)))
                
                text2 = float(self.scrTotal.text()) 
                self.scrTotal.setText(str(text2 + (price * quantity)))
                self.scrFacture.adjustSize()
            except Exception as e:
                print(e)
                
                
    def calculerFacture(self):
        try:
            total = float(self.scrTotal.text())
            discount = total * 0.05
            valueBeforeTax = total - discount
            VATTax = valueBeforeTax * 0.14
            valueAfterTax = valueBeforeTax + VATTax
            self.totalValue.setText(str(total))
            self.disValue.setText(str(round(discount, 2)))
            self.VATvalue.setText(str(round(VATTax, 2)))
            self.netValue.setText(str(round(valueAfterTax, 2)))
        except Exception as e :
            print(e)
            
            
    def remiseZero(self):
        allCheck = [self.chkShrimp,self.chkFish,self.chkBeef,self.chkChicken,self.chkBeefChawarma,self.chkChickenChawarma,self.chkMeatRiceNuts,self.chkMeatKofta,self.chkVegetables]
        for check in allCheck:
            if check.isChecked()==True:
               check.setChecked(False)
        self.scrFacture.clear()
        allQuantite = [self.chkShrimpQuant,self.chkFishQuant,self.chkBeefQuant,self.chkChickenQuant,self.chkBeefChawarmaQuant,self.chkChickenChawarmaQuant,self.chkMeatRiceNutsQuant,self.chkMeatKoftaQuant,self.chkVegetablesQuant]
        for quat in allQuantite:
            quat.setText("0")
        
        try:
            self.scrTotal.setText("0")
            self.totalValue.setText("0")
            self.disValue.setText("0")
            self.VATvalue.setText("0")
            self.netValue.setText("0")
        except Exception as e :
            print(e)
            
        # date = QDate.currentDate()
        invNumber = QDateTime.currentDateTime()
        # time = QTime.currentTime()
        
        # self.lbl_recDate.clear()
        # self.lbl_recTime.clear()
        self.lbl_recNumberValue.clear()
        str(Resto.invoice_no)
        Resto.invoice_no +=1
        self.lbl_recNumberval.setText(str(Resto.invoice_no))
        # self.lbl_recDate.setText("التاريخ: "+date.toString(Qt.ISODate))
        # self.lbl_recTime.setText("الوقت"+time.toString(Qt.DefaultLocaleLongDate))
        self.lbl_recNumberValue.setText(invNumber.toString(Qt.ISODate))   
    
        
    # def CloseApp(self):
    #     sys.exit(app.exec_())   

    def maFenetre(self):            
        self.setFixedSize(1200,720)
        # self.setWindowIcon(QIcon('chat.png'))     

# Execute app
def main():            
    app = QApplication(sys.argv)
    window = Resto()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
        

