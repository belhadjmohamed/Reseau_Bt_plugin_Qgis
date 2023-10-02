# Renseignement des codes des lignes de brachement a partir des lignes de dérivation

"""
description : 

Cet algorithme permet de remplir le code de branchement pour les entités des lignes de branchements sélectionnées
en indiquant le numéro de branchement en entrée. Il utilise le code de dérivation intersectant la première entité
de la liste de branchement pour remplir automatiquement le champ du code de départ, de dérivation et de branchement.
"""

from qgis.core import *
from qgis.utils import iface


from .mes_classes import my_attributes


def code_bran_dep_der(fn4,fn5,char1):

    layer_derivation_bt = QgsVectorLayer(fn5,'derivation_bt','ogr')
    layer_branchement_bt = QgsVectorLayer(fn4,'support_bt','ogr')

    remp_bran = my_attributes(layer_branchement_bt)
    layer_active = iface.activeLayer()
    remp_bran.codebri_dep_der_bran(layer_derivation_bt,layer_active,char1)

    selected = layer_active.selectedFeatures()
    m = 1
    code1 = selected[0]['code_bri']
    for a in range(len(selected)-1) :
        if layer_branchement_bt.startEditing():
            if ((selected[a]['nd_amont']==selected[a+1]['nd_amont']) and (selected[a]['nd_aval']==selected[a+1]['nd_aval'])):
                ch = str(m)
                selected[a]['code_bri'] =  code1 + ch
                selected[a+1]['code_bri'] =  code1 + ch
            else:
                ch = str(m)
                selected[a]['code_bri'] =  code1 + ch
                m = m + 1
                ch1 = str(m)
                selected[a+1]['code_bri'] =  code1 + ch1
            layer_branchement_bt.updateFeature(selected[a])
            layer_branchement_bt.updateFeature(selected[a+1])
            layer_branchement_bt.commitChanges()



