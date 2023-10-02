# Création des nœuds de sortie du poste

"""
description : 

Nous avons développé un algorithme qui vise à identifier les points d'intersection entre les lignes de départ
et le poste haute tension basse tension. Ensuite, l'algorithme crée une nouvelle entité pour représenter chaque
point d'intersection trouvé, l'ajoute à la couche des noeuds basse tension et définit la valeur "Sortie_poste" 
dans le champ "obs" pour indiquer qu'il s'agit d'un noeud de sortie du poste.
"""


from qgis.core import *



def nd_s_poste(fn2,fn3,fn5,id_poste):
    layer_noeud_bt = QgsVectorLayer(fn5,'noeud_bt','ogr')
    poste_hta_bt = QgsVectorLayer(fn2,'poste_hta_bt','ogr')
    layer_depart = QgsVectorLayer(fn3,'depart_bt','ogr')

    depart_index = QgsSpatialIndex(layer_depart)

    n = layer_noeud_bt.getFeature(0)

    poste = poste_hta_bt.getFeature(id_poste)

    sortie_de_poste = []

    nearby_depart = depart_index.nearestNeighbor(poste.geometry(),0)

    for i in nearby_depart:
        dep =  layer_depart.getFeature(i)
        if (dep.geometry().intersects(poste.geometry())):
            print ('true')
            intersection = poste.geometry().intersection(dep.geometry())
            new_feature = QgsFeature()
            new_feature.setAttributes(n.attributes())
            new_feature.setGeometry(intersection)
            attribute_index = layer_noeud_bt.fields().indexFromName("obs")
            new_value = "nd_sortie_poste"
            new_feature.setAttribute(attribute_index, new_value)
            layer_noeud_bt.startEditing()
            layer_noeud_bt.addFeature(new_feature)
            layer_noeud_bt.commitChanges()
    

                        