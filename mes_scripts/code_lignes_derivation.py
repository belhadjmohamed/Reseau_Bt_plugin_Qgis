# Renseignement des Codes des lignes de dérivation a partir d'une ligne de départ basse tension 

"""
Description : 

Cet algorithme permet de remplir le code de dérivation pour les entités de lignes de dérivation sélectionnées 
en indiquant le numéro de dérivation en entrée. Il utilise le code de départ intersectant la première entité de la liste de 
dérivation pour remplir automatiquement le champ du code de départ et de dérivation.
"""

from qgis.core import *
from qgis.utils import iface

from .mes_classes import my_attributes

def code_der(fn4,fn2,chhh):

    layer_derivation_bt = QgsVectorLayer(fn4,'derivation_bt','ogr')
    layer_depart = QgsVectorLayer(fn2,'depart_bt','ogr')

    champs_der = my_attributes(layer_derivation_bt)
    layer_active = iface.activeLayer()
    champs_der.code_der_dep_niv1(layer_depart,layer_active,chhh)


    selected = layer_active.selectedFeatures()
    m = 1
    code1 = selected[0]['code_der']
    for a in range(len(selected)-1) :
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
            






