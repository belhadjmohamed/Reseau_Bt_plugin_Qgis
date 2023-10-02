# Création des nœuds à partir des supports basse tension

"""
description : 

Pour développer notre algorithme de création des nœuds de dérivation,
de branchement et de bout, nous avons utilisé cinq chemins pointant vers les shapefiles de ligne de dérivation,
les noeuds basse tension, les supports basse tension, les lignes de départ et les lignes de branchement. 
Notre objectif était de déterminer les différents types de nœuds qui existent dans le réseau électrique, 
tels que les nœuds de bout, les nœuds de dérivation, les nœuds de branchements collectifs, les nœuds de branchements individuels,
les nœuds de dérivation et de branchements collectifs, et les nœuds de dérivation et de branchements individuels.
Notre algorithme a parcouru chaque point de la couche représentant les supports et a
recherché les lignes qui touchent ce point en utilisant des index spatiaux pour accélérer la recherche.
En fonction du nombre et du type de lignes connectées, le point a été classé comme l'un des types de nœuds mentionnés précédemment.
Nous avons ensuite créé sur chaque support un noeud basse tension correspondant et modifié l'attribut observation pour indiquer
le type de noeud pour chaque support.

"""

from qgis.core import *

def supp_nd(fn,fn2,fn3,fn4,fn5):
    
    layer_derivation_bt = QgsVectorLayer(fn2,'support_bt','ogr')
    layer_noeud_bt = QgsVectorLayer(fn4,'noeud_bt','ogr')
    layer_support_bt = QgsVectorLayer(fn5,'support_bt','ogr')
    layer_depart_bt = QgsVectorLayer(fn,'support_bt','ogr')
    layer_branchement_bt = QgsVectorLayer(fn3,'support_bt','ogr')

    depart_index = QgsSpatialIndex(layer_depart_bt)

    branch_index =  QgsSpatialIndex(layer_branchement_bt)

    der_index =  QgsSpatialIndex(layer_derivation_bt)


    nd_der = []
    nd_bran_col = []
    nd_der_bran_col = []
    nd_bout = []
    nd_bout_der = []
    nd_bout_bran_col = []
    nd_bout_der_bran_col = []
    nd_bran_ind = []
    nd_der_bran_ind = []
    nd_bout_bran_ind = []
    nd_bout_der_bran_ind = []

    for point_f in layer_support_bt.getFeatures():

        nearby_depart = depart_index.nearestNeighbor(point_f.geometry(),0)
        nearby_bran = branch_index.nearestNeighbor(point_f.geometry(),0)
        nearby_der = der_index.nearestNeighbor(point_f.geometry(),0)
    
        connected_der = []
        connected_bran = []
        connected_depart = []
    
        for dep_id in nearby_depart:
            line_feature = layer_depart_bt.getFeature(dep_id)
        
            if (point_f.geometry().touches(line_feature.geometry())):
            
                connected_depart.append(line_feature.id())
    
    
    
        for der_id in nearby_der:
            line_feature_der = layer_derivation_bt.getFeature(der_id)

            if (point_f.geometry().touches(line_feature_der.geometry())):
            
                connected_der.append(line_feature_der.id())
    
    
    
        for bran_id in nearby_bran:
            line_feature_bran = layer_branchement_bt.getFeature(bran_id)
        
            if (point_f.geometry().touches(line_feature_bran.geometry())):
            
                connected_bran.append(line_feature_bran.id())
    
    

        if ((len(connected_depart) == 2) and (len(connected_der)>=1) and (len(connected_bran)==0)) or ((len(connected_depart) == 0) and (len(connected_der)>2) and (len(connected_bran)==0)):
            nd_der.append(point_f.id())
        elif ((len(connected_depart) == 2) and (len(connected_der)==0) and (len(connected_bran)>1)) or ((len(connected_depart) == 0) and (len(connected_der)==0) and (len(connected_bran)>3)) or ((len(connected_depart) == 0) and (len(connected_der)==2) and (len(connected_bran)>1)):
            nd_bran_col.append(point_f.id())
    
        elif ((len(connected_depart) == 2) and (len(connected_der)==0) and (len(connected_bran)==1)) or ((len(connected_depart) == 0) and (len(connected_der)==0) and (len(connected_bran)==3)) or ((len(connected_depart) == 0) and (len(connected_der)==2) and (len(connected_bran)==1)):
            nd_bran_ind.append(point_f.id())

        elif ((len(connected_depart) == 2) and (len(connected_der)>=1) and (len(connected_bran)>1)) or ((len(connected_depart) == 0) and (len(connected_der) > 2) and (len(connected_bran)>1)):
            nd_der_bran_col.append(point_f.id())
    
        elif  ((len(connected_depart) == 2) and (len(connected_der)>=1) and (len(connected_bran)==1)) or ((len(connected_depart) == 0) and (len(connected_der) > 2) and (len(connected_bran)==1)):
            nd_der_bran_ind.append(point_f.id())

        elif ((len(connected_depart) == 1) and (len(connected_der)==0) and (len(connected_bran)==0)) or ((len(connected_depart) == 0) and (len(connected_der)==1) and (len(connected_bran)==0)) :
            nd_bout.append(point_f.id())
        elif ((len(connected_depart) == 1) and (len(connected_der)>=1) and (len(connected_bran)==0)):
            nd_bout_der.append(point_f.id())
        elif ((len(connected_depart) == 0) and (len(connected_der)==1) and (len(connected_bran)>1)) or ((len(connected_depart) == 1) and (len(connected_der)==0) and (len(connected_bran)>1)) :
            nd_bout_bran_col.append(point_f.id())
    
        elif ((len(connected_depart) == 0) and (len(connected_der)==1) and (len(connected_bran)==1)) or ((len(connected_depart) == 1) and (len(connected_der)==0) and (len(connected_bran)==1)) :
            nd_bout_bran_ind.append(point_f.id())

        elif ((len(connected_depart) == 1) and (len(connected_der)>=1) and (len(connected_bran)>1)):
            nd_bout_der_bran_col.append(point_f.id())

        elif ((len(connected_depart) == 1) and (len(connected_der)>=1) and (len(connected_bran)==1)):
            nd_bout_der_bran_ind.append(point_f.id())

    L = [nd_der,nd_bran_col,nd_der_bran_col,nd_bout,nd_bout_der,nd_bout_bran_col,nd_bout_der_bran_col,nd_bran_ind,nd_der_bran_ind,nd_bout_bran_ind,nd_bout_der_bran_ind] 
    print(L)
    for i in L:
    
        layer_support_bt.select(i)
        a = layer_support_bt.selectedFeatures()
    
        for w in a :
            print(w.id())
        for p in a:
        
            n = layer_noeud_bt.getFeature(0)
            new_feature = QgsFeature()
            new_feature.setAttributes(n.attributes())
            new_feature.setGeometry(p.geometry())
            attribute_index = layer_noeud_bt.fields().indexFromName("obs")
            current_value = new_feature.attribute(attribute_index)
            if (i==nd_der):
                new_value = "nd_der"
            elif (i==nd_bran_col):
                new_value = "nd_bran_col"
            elif (i==nd_der_bran_col):
                new_value = "nd_der_bran_col"
            elif (i==nd_bout):
                new_value = "nd_bout"
            elif (i==nd_bout_der):
                new_value = "nd_bout_der"
            elif (i==nd_bout_bran_col):
                new_value = "nd_bout_bran_col"
            elif (i==nd_bout_der_bran_col):
                new_value = "nd_bout_der_bran_col"
            elif (i==nd_bran_ind):
                new_value = "nd_bran_ind"
            elif(i==nd_der_bran_ind):
                new_value = "nd_der_bran_ind"
            elif(i==nd_bout_bran_ind):
                new_value = "nd_bout_bran_ind"
            elif(i==nd_bout_der_bran_ind):
                new_value = "nd_bout_der_bran_ind"
    
            new_feature.setAttribute(attribute_index, new_value)
            layer_noeud_bt.startEditing()  
            layer_noeud_bt.addFeature(new_feature)
            layer_noeud_bt.commitChanges() 
        
        layer_support_bt.deselect(i)

    


        



   
