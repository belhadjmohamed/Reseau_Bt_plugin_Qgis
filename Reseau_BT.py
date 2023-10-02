# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Reseau_BT
                                 A QGIS plugin
 Reseau_BT
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-04-12
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Reseau_BT
        email                : bemoh70@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction , QFileDialog

from .mes_scripts.noeuds_tableaux_comptage import nd_comptage
from .mes_scripts.noeud_sortie_poste import nd_s_poste
from .mes_scripts.noeuds_supports import supp_nd
from .mes_scripts.rempl_attributs import remplissage_attributes
from .mes_scripts.noeud_changement_caractere import nd_chang
from .mes_scripts.noeud_amont_aval import nd_amont_aval
from .mes_scripts.mes_classes import my_attributes
from .mes_scripts.code_derivation_de_derivation import code_der2
from .mes_scripts.code_lignes_derivation import code_der
from .mes_scripts.code_dep_finale import code_dep2
from .mes_scripts.code_lignes_branch_derivation import code_bran_dep_der
from .mes_scripts.code_lignes_branchement_dep import code_dep_bran


# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .Reseau_BT_dialog import Reseau_BTDialog,noeuds,noeuds_comptage,noeuds_POSTE,noeuds_supp,code_lignee,code_depart,code_derivation,code_branch,nd_amont_avall,rempl_att,Chang_car

import os.path

class Reseau_BT:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Reseau_BT_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Reseau_BT')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Reseau_BT', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/Reseau_BT/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Réseau_BT'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Reseau_BT'),
                action)
            self.iface.removeToolBarIcon(action)

    #nd_comtage_fonctions
    def select_shp_file2(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg2, '*.shp')
        self.dlg2.lineEdit_2.setText(filename)

    def select_shp_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg2, "Select output file ","", '*.shp')
        self.dlg2.lineEdit.setText(filename)

    def on_ok_button_clicked(self):
        a = self.dlg2.lineEdit.text()
        b = self.dlg2.lineEdit_2.text()
        nd_comptage(a,b)
        self.dlg2.close()
        self.dlg1.close()
        self.dlg.close()

    #nd_comptage_fonctions

    #nd_sortie_poste_fonctions
    def select_shp_file3(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg3, "Select output file ","", '*.shp')
        self.dlg3.lineEdit.setText(filename)
    
    def select_shp_file4(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg3, "Select output file ","", '*.shp')
        self.dlg3.lineEdit_2.setText(filename)
    
    def select_shp_file5(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg3, "Select output file ","", '*.shp')
        self.dlg3.lineEdit_3.setText(filename)

    def on_ok_button_clicked_s_poste(self):
        a = self.dlg3.lineEdit.text()
        b = self.dlg3.lineEdit_2.text()
        c = self.dlg3.lineEdit_3.text()
        d = self.dlg3.spinBox.value()
        nd_s_poste(a,b,c,d)
        self.dlg3.close()
        self.dlg1.close()
        self.dlg.close()
    
    #nd_sortie_poste_fonctions

    #ND_supp_fonctions
    def select_shp_file6(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg4, "Select output file ","", '*.shp')
        self.dlg4.lineEdit.setText(filename)
    
    def select_shp_file7(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg4, "Select output file ","", '*.shp')
        self.dlg4.lineEdit_2.setText(filename)

    def select_shp_file8(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg4, "Select output file ","", '*.shp')
        self.dlg4.lineEdit_3.setText(filename)

    def select_shp_file9(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg4, "Select output file ","", '*.shp')
        self.dlg4.lineEdit_4.setText(filename)

    def select_shp_file10(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg4, "Select output file ","", '*.shp')
        self.dlg4.lineEdit_5.setText(filename)

    def on_ok_button_clicked_supp(self):
        a = self.dlg4.lineEdit.text()
        b = self.dlg4.lineEdit_2.text()
        c = self.dlg4.lineEdit_3.text()
        d = self.dlg4.lineEdit_4.text()
        e = self.dlg4.lineEdit_5.text()
        supp_nd(a,b,c,d,e)
        self.dlg4.close()
        self.dlg1.close()
        self.dlg.close()

    #ND_supp_fonctions
    
    #nd_chang_fonctions

    def select_shp_file11(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg5, "Select output file ","", '*.shp')
        self.dlg5.lineEdit.setText(filename)
    
    def select_shp_file12(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg5, "Select output file ","", '*.shp')
        self.dlg5.lineEdit_2.setText(filename)

    def select_shp_file13(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg5, "Select output file ","", '*.shp')
        self.dlg5.lineEdit_3.setText(filename)

    def select_shp_file14(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg5, "Select output file ","", '*.shp')
        self.dlg5.lineEdit_4.setText(filename)

    def select_shp_file15(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg5, "Select output file ","", '*.shp')
        self.dlg5.lineEdit_5.setText(filename)

    def on_ok_button_clicked_CHANG_carac(self):
        a = self.dlg5.lineEdit.text()
        b = self.dlg5.lineEdit_2.text()
        c = self.dlg5.lineEdit_3.text()
        d = self.dlg5.lineEdit_4.text()
        e = self.dlg5.lineEdit_5.text()
        nd_chang(a,b,c,d,e)
        self.dlg5.close()
        self.dlg1.close()
        self.dlg.close()
  
    #nd_chang_fonctions

    #nd_supp
    def select_nd_supp(self):
        self.dlg4 =  noeuds_supp()
        self.dlg4.show()
        self.dlg4.toolButton_2.clicked.connect(self.select_shp_file6)
        self.dlg4.toolButton_4.clicked.connect(self.select_shp_file7)
        self.dlg4.toolButton_3.clicked.connect(self.select_shp_file8)
        self.dlg4.toolButton.clicked.connect(self.select_shp_file9)
        self.dlg4.toolButton_5.clicked.connect(self.select_shp_file10)
        self.dlg4.buttonBox.accepted.connect(self.on_ok_button_clicked_supp)

    #nd_sortie_du_poste
    def select_nd_poste(self):
        self.dlg3 =  noeuds_POSTE()
        self.dlg3.show()
        self.dlg3.toolButton.clicked.connect(self.select_shp_file3)
        self.dlg3.toolButton_2.clicked.connect(self.select_shp_file4)
        self.dlg3.toolButton_3.clicked.connect(self.select_shp_file5)
        self.dlg3.buttonBox.accepted.connect(self.on_ok_button_clicked_s_poste)

    #nd_comtage
    def select_nd_comptage(self):
        self.dlg2 =  noeuds_comptage()
        self.dlg2.show()
        self.dlg2.toolButton.clicked.connect(self.select_shp_file)
        self.dlg2.toolButton_2.clicked.connect(self.select_shp_file2)
        self.dlg2.buttonBox.accepted.connect(self.on_ok_button_clicked)


    #nd_chang_carac
    def select_nd_chang_carac(self):
        self.dlg5 =  Chang_car()
        self.dlg5.show()
        self.dlg5.toolButton_2.clicked.connect(self.select_shp_file11)
        self.dlg5.toolButton_4.clicked.connect(self.select_shp_file12)
        self.dlg5.toolButton_3.clicked.connect(self.select_shp_file13)
        self.dlg5.toolButton.clicked.connect(self.select_shp_file14)
        self.dlg5.toolButton_5.clicked.connect(self.select_shp_file15)
        self.dlg5.buttonBox.accepted.connect(self.on_ok_button_clicked_CHANG_carac)



    

    #LIGNE_dep_fonctions
    def select_shp_file16(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg7, "Select output file ","", '*.shp')
        self.dlg7.lineEdit.setText(filename)
    
    def select_shp_file17(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg7, "Select output file ","", '*.shp')
        self.dlg7.lineEdit_2.setText(filename)

    def select_shp_file18(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg7, "Select output file ","", '*.shp')
        self.dlg7.lineEdit_3.setText(filename)    

    def on_ok_button_clicked_LIGNE_DEP(self):
        a = self.dlg7.lineEdit.text()
        b = self.dlg7.lineEdit_2.text()
        c = self.dlg7.lineEdit_3.text()
        d = self.dlg7.spinBox_2.value()
        e = self.dlg7.spinBox.value()
        code_dep2(a,b,c,d,e)
        self.dlg7.close()
        self.dlg6.close()
        self.dlg.close()

    #LIGNE_dep_fonctions



    #LIGNE_der_fonctions
    def select_shp_file19(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg8, "Select output file ","", '*.shp')
        self.dlg8.lineEdit.setText(filename)
    
    def select_shp_file20(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg8, "Select output file ","", '*.shp')
        self.dlg8.lineEdit_2.setText(filename)
  
    def select_shp_file21(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg8, "Select output file ","", '*.shp')
        self.dlg8.lineEdit_3.setText(filename)

    def on_ok_button_clicked_LIGNE_DER(self):
        a = self.dlg8.lineEdit.text()
        b = self.dlg8.lineEdit_2.text()
        e = self.dlg8.spinBox.value()
        code_der(a,b,str(e))
        self.dlg8.close()
        self.dlg6.close()
        self.dlg.close()  
  
    def on_ok_button_clicked_LIGNE_DER_2(self):
        a = self.dlg8.lineEdit.text()
        c = self.dlg8.lineEdit_3.text()
        e = self.dlg8.spinBox_7.value()
        f = self.dlg8.spinBox_2.value()
        g = self.dlg8.spinBox_3.value()
        h = self.dlg8.spinBox_4.value()
        i = self.dlg8.spinBox_5.value()
        j = self.dlg8.spinBox_6.value()
        code_der2(a,c,e,str(f),str(g),str(h),str(i),str(j))
        self.dlg8.close()
        self.dlg6.close()
        self.dlg.close() 
    #LIGNE_der_fonctions 

    #LIGNE_bran_fonctions

    def select_shp_file22(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg9, "Select output file ","", '*.shp')
        self.dlg9.lineEdit.setText(filename)
    
    def select_shp_file23(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg9, "Select output file ","", '*.shp')
        self.dlg9.lineEdit_2.setText(filename)
  
    def select_shp_file24(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg9, "Select output file ","", '*.shp')
        self.dlg9.lineEdit_3.setText(filename)

    def on_ok_button_clicked_LIGNE_BRAN_dep(self):
        a = self.dlg9.lineEdit.text()
        b = self.dlg9.lineEdit_2.text()
        e = self.dlg9.spinBox.value()
        code_dep_bran(a,b,str(e))
        self.dlg9.close()
        self.dlg6.close()
        self.dlg.close()  
    
    def on_ok_button_clicked_LIGNE_BRAN_der(self):
        a = self.dlg9.lineEdit.text()
        b = self.dlg9.lineEdit_3.text()
        e = self.dlg9.spinBox_2.value()
        code_bran_dep_der(a,b,str(e))
        self.dlg9.close()
        self.dlg6.close()
        self.dlg.close()  

    #LIGNE_bran_fonctions

    #ligne_bran
    def select_ligne_bran(self):
        self.dlg9 =  code_branch()
        self.dlg9.show()
        self.dlg9.toolButton.clicked.connect(self.select_shp_file22)
        self.dlg9.toolButton_2.clicked.connect(self.select_shp_file23)
        self.dlg9.toolButton_3.clicked.connect(self.select_shp_file24)
        self.dlg9.pushButton.clicked.connect(self.on_ok_button_clicked_LIGNE_BRAN_dep)    
        self.dlg9.pushButton_2.clicked.connect(self.on_ok_button_clicked_LIGNE_BRAN_der) 

    #ligne_der
    def select_ligne_der(self):
        self.dlg8 =  code_derivation()
        self.dlg8.show()
        self.dlg8.toolButton.clicked.connect(self.select_shp_file19)
        self.dlg8.toolButton_2.clicked.connect(self.select_shp_file20)
        self.dlg8.toolButton_3.clicked.connect(self.select_shp_file21)
        self.dlg8.pushButton.clicked.connect(self.on_ok_button_clicked_LIGNE_DER)    
        self.dlg8.pushButton_2.clicked.connect(self.on_ok_button_clicked_LIGNE_DER_2)  
    
    #ligne_dep
    def select_ligne_dep(self):
        self.dlg7 =  code_depart()
        self.dlg7.show()
        self.dlg7.toolButton.clicked.connect(self.select_shp_file16)
        self.dlg7.toolButton_2.clicked.connect(self.select_shp_file17)
        self.dlg7.toolButton_3.clicked.connect(self.select_shp_file18)
        self.dlg7.buttonBox.accepted.connect(self.on_ok_button_clicked_LIGNE_DEP)

    #interface_noeuds
    def select_nd(self):
        self.dlg1 = noeuds()   
        self.dlg1.show()
        self.dlg1.pushButton_2.clicked.connect(self.select_nd_comptage)     
        self.dlg1.pushButton.clicked.connect(self.select_nd_poste) 
        self.dlg1.pushButton_3.clicked.connect(self.select_nd_supp)
        self.dlg1.pushButton_4.clicked.connect(self.select_nd_chang_carac)

    #interface_line
    def select_line(self):
        self.dlg6 = code_lignee()   
        self.dlg6.show()
        self.dlg6.pushButton.clicked.connect(self.select_ligne_dep)     
        self.dlg6.pushButton_2.clicked.connect(self.select_ligne_der) 
        self.dlg6.pushButton_3.clicked.connect(self.select_ligne_bran)

    #attributes_fonctions
    def select_shp_file25(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit.setText(filename)
    
    def select_shp_file26(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_2.setText(filename)
  
    def select_shp_file27(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_3.setText(filename)    
    
    def select_shp_file28(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_4.setText(filename)
    
    def select_shp_file29(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_5.setText(filename)
  
    def select_shp_file30(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_6.setText(filename)

    def select_shp_file31(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_7.setText(filename)
    
    def select_shp_file32(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_8.setText(filename)
  
    def select_shp_file33(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_9.setText(filename)

    def select_shp_file34(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg10, "Select output file ","", '*.shp')
        self.dlg10.lineEdit_10.setText(filename)
       

    def on_ok_button_clicked_REMPL_ATT(self):
        a = self.dlg10.lineEdit.text()
        b = self.dlg10.lineEdit_2.text()
        c = self.dlg10.lineEdit_3.text()
        d = self.dlg10.lineEdit_4.text()
        e = self.dlg10.lineEdit_5.text()
        f = self.dlg10.lineEdit_6.text()
        g = self.dlg10.lineEdit_7.text()
        h = self.dlg10.lineEdit_8.text()
        i = self.dlg10.lineEdit_9.text()
        j = self.dlg10.lineEdit_10.text()
        k = self.dlg10.lineEdit_11.text()
        l = self.dlg10.lineEdit_12.text()
        m = self.dlg10.spinBox.value()
        n = self.dlg10.lineEdit_13.text()
        o = self.dlg10.lineEdit_14.text()
        remplissage_attributes(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
        self.dlg10.close()
        self.dlg.close()    

    #attributes_fonctions

    #interface_ATTRIBUTS
    def select_attributes(self):
        self.dlg10 = rempl_att()   
        self.dlg10.show()
        self.dlg10.toolButton.clicked.connect(self.select_shp_file25)     
        self.dlg10.toolButton_2.clicked.connect(self.select_shp_file26) 
        self.dlg10.toolButton_3.clicked.connect(self.select_shp_file27)
        self.dlg10.toolButton_4.clicked.connect(self.select_shp_file28) 
        self.dlg10.toolButton_5.clicked.connect(self.select_shp_file29) 
        self.dlg10.toolButton_6.clicked.connect(self.select_shp_file30) 
        self.dlg10.toolButton_7.clicked.connect(self.select_shp_file31) 
        self.dlg10.toolButton_8.clicked.connect(self.select_shp_file32) 
        self.dlg10.toolButton_9.clicked.connect(self.select_shp_file33) 
        self.dlg10.toolButton_10.clicked.connect(self.select_shp_file34) 
        self.dlg10.buttonBox.accepted.connect(self.on_ok_button_clicked_REMPL_ATT)     

    #amont_aval_fonctions
    def select_shp_file35(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit.setText(filename)
    
    def select_shp_file36(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit_2.setText(filename)
  
    def select_shp_file37(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit_3.setText(filename)    
    
    def select_shp_file38(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit_4.setText(filename)
    
    def select_shp_file39(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit_5.setText(filename)
  
    def select_shp_file40(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit_6.setText(filename)

    def select_shp_file41(self):
        filename, _ = QFileDialog.getOpenFileName(
            self.dlg11, "Select output file ","", '*.shp')
        self.dlg11.lineEdit_7.setText(filename)  

    def on_ok_button_clicked_amont_aval(self):
        a = self.dlg11.lineEdit.text()
        b = self.dlg11.lineEdit_2.text()
        c = self.dlg11.lineEdit_3.text()
        d = self.dlg11.lineEdit_4.text()
        e = self.dlg11.lineEdit_5.text()
        f = self.dlg11.lineEdit_6.text()
        g = self.dlg11.lineEdit_7.text()
        m = self.dlg11.spinBox.value()
        nd_amont_aval(a,b,c,d,e,f,g,m)
        self.dlg11.close()
        self.dlg.close() 

    #amont_aval_fonctions
    
    #interface_amont_aval
    def select_amont_aval(self):
        self.dlg11 = nd_amont_avall()   
        self.dlg11.show()
        self.dlg11.toolButton.clicked.connect(self.select_shp_file35)     
        self.dlg11.toolButton_2.clicked.connect(self.select_shp_file36) 
        self.dlg11.toolButton_3.clicked.connect(self.select_shp_file37)
        self.dlg11.toolButton_4.clicked.connect(self.select_shp_file38) 
        self.dlg11.toolButton_5.clicked.connect(self.select_shp_file39) 
        self.dlg11.toolButton_6.clicked.connect(self.select_shp_file40) 
        self.dlg11.toolButton_7.clicked.connect(self.select_shp_file41) 
        self.dlg11.buttonBox.accepted.connect(self.on_ok_button_clicked_amont_aval)         
    

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = Reseau_BTDialog()

            self.dlg.pushButton_7.clicked.connect(self.select_nd)
            self.dlg.pushButton_4.clicked.connect(self.select_line)
            self.dlg.pushButton_5.clicked.connect(self.select_attributes)
            self.dlg.pushButton_6.clicked.connect(self.select_amont_aval)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop

