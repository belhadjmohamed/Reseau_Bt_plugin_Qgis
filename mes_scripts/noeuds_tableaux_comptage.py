# Création des nœuds à partir des tableaux de comptage (point de livraison individuelle)
"""
description : 

Pour développer l'algorithme de création des noeuds de points de livraison individuelle,
nous avons pris en entrée deux chemins de fichiers pointant vers les shapefiles des tableaux de comptage 
et des noeuds basse tension. La couche des noeuds basse tension initiale ne contenait que des noeuds collectifs 
collectant depuis les missions terrains. L'algorithme a cherché les compteurs qui étaient proches des noeuds collectifs,
créé de nouvelles entités dans la couche des noeuds basse tension pour les compteurs qui n'étaient pas proches de noeuds collectifs,
et a défini un attribut pour indiquer si l'entité représentait un point de livraison individuelle ou un point de livraison collectif.

"""


from qgis.core import *


def nd_comptage(fn1,fn2):
    layer_comptage = QgsVectorLayer(fn2,'tableau_comptage','ogr')

    layer_noeud_bt = QgsVectorLayer(fn1,'noeud_bt','ogr')

    n = layer_noeud_bt.getFeature(0)
    comptage_index = QgsSpatialIndex(layer_comptage)

    list_select_comptage=[]
    with edit(layer_noeud_bt):
        for comp_f in layer_noeud_bt.getFeatures():
            comp_f['obs']='nd_col'
        
            nearby_noeud = comptage_index.nearestNeighbor(comp_f.geometry(),10)
            for nddd_id in nearby_noeud:
                nd_feature = layer_comptage.getFeature(nddd_id)
                if (nd_feature.geometry().asPoint()==comp_f.geometry().asPoint()):
                    list_select_comptage.append(nd_feature.id())
            print(list_select_comptage)
            layer_noeud_bt.updateFeature(comp_f)
        

    
    l = []
    for s in layer_comptage.getFeatures():
        l.append(s.id())
    print(l)

    ll = []
    for i in l:
        if i not in list_select_comptage:
            ll.append(i)
    print(ll)

    layer_comptage.select(ll)
    a = layer_comptage.selectedFeatures()

    for k in a:
        print(k.id())


    for p in a:
        new_feature = QgsFeature()
        new_feature.setAttributes(n.attributes())
        new_feature.setGeometry(p.geometry())
        attribute_index = layer_noeud_bt.fields().indexFromName("obs")
        current_value = new_feature.attribute(attribute_index)
        new_value = "nd_ind"
        new_feature.setAttribute(attribute_index, new_value)
        layer_noeud_bt.startEditing()
        layer_noeud_bt.addFeature(new_feature)
        layer_noeud_bt.commitChanges()
    layer_comptage.deselect(ll)



     

