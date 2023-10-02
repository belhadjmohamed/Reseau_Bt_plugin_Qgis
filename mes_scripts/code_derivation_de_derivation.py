# Renseignement des codes des lignes de dérivations a partir des lignes de dérivations

"""
Description : 

L'algorithme en question permet de remplir automatiquement le champ code de dérivation pour les entités de la couche ligne
de dérivation sélectionnées, en fonction du numéro de départ, de la dérivation et de la dérivation de la dérivation donnés en entrée.
Ainsi, le champ code départ sera également rempli simultanément.
"""

from qgis.core import *
from qgis.utils import iface

from .mes_classes import my_attributes

def code_der2(fn4,fn3,id_poste,char1,char2,char3,char4,char5):

    layer_derivation_bt = QgsVectorLayer(fn4,'derivation_bt','ogr')
    poste_hta_bt = QgsVectorLayer(fn3,'poste_hta_bt','ogr')
    


    champs_der = my_attributes(layer_derivation_bt)

    layer_active = iface.activeLayer()

    poste = poste_hta_bt.getFeature(id_poste)
    code_poste = poste['code_pt']
    champs_der.code_der_dep_niv2(layer_active,code_poste,char1,char2,char3,char4,char5)


    selected = layer_active.selectedFeatures()
    m = 1
    code1 = selected[0]['code_der']
    for a in range(len(selected)-1):
        if layer_derivation_bt.startEditing():
            if ((selected[a]['nd_amont']==selected[a+1]['nd_amont']) and (selected[a]['nd_aval']==selected[a+1]['nd_aval'])):
                ch = str(m)
                selected[a]['code_der'] =  code1 + ch
                selected[a+1]['code_der'] =  code1 + ch
            else:
                ch = str(m)
                selected[a]['code_der'] =  code1 + ch
                m = m + 1
                ch1 = str(m)
                selected[a+1]['code_der'] =  code1 + ch1
            layer_derivation_bt.updateFeature(selected[a])
            layer_derivation_bt.updateFeature(selected[a+1])
            layer_derivation_bt.commitChanges()



