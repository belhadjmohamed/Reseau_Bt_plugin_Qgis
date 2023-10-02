# Création des nœuds de changement de caractère

"""
description : 

Notre objectif avec cet algorithme est d'identifier les points où deux segments de lignes électriques ayant des caractéristiques
différentes se touchent, appelés "noeuds de changement de caractère". 
Nous créons ensuite une nouvelle entité pour stocker ces noeuds en indiquant dans le champ 'obs' qu'il s'agit d'un noeud
de changement de caractère. Si une entité existe déjà dans une couche shapefile correspondant aux noeuds,
nous modifions l'attribut "obs" de cette entité pour indiquer qu'elle est également un noeud de changement de caractère.
"""

from qgis.core import *

def nd_chang(fn,fn2,fn5,fn3,fn4):

    layer_derivation_bt = QgsVectorLayer(fn2,'derivation_bt','ogr')
    layer_branchement_bt = QgsVectorLayer(fn5,'branchement_bt','ogr')
    layer_noeud_bt = QgsVectorLayer(fn3,'noeud_bt','ogr')
    layer_depart_bt = QgsVectorLayer(fn,'depart_bt','ogr')
    layer_support_bt = QgsVectorLayer(fn4,'support_bt','ogr')

    n = layer_noeud_bt.getFeature(0)

    depart_index_spatiale = QgsSpatialIndex(layer_depart_bt)

    branch_index_spatiale =  QgsSpatialIndex(layer_branchement_bt)

    der_index_spatiale = QgsSpatialIndex(layer_derivation_bt)

    l=[]

    for point_f in layer_support_bt.getFeatures():
        nearby_depart_supp = depart_index_spatiale.nearestNeighbor(point_f.geometry(),0)
        nearby_bran_supp = branch_index_spatiale.nearestNeighbor(point_f.geometry(),0)
        nearby_der_supp = der_index_spatiale.nearestNeighbor(point_f.geometry(),0)
        for depart_id in nearby_depart_supp:

            line_feature1 = layer_depart_bt.getFeature(depart_id)
            line_feature2 = layer_depart_bt.getFeature(depart_id+1)
            if (point_f.geometry().touches(line_feature1.geometry())):
                if (point_f.geometry().touches(line_feature2.geometry())):
                    if (line_feature1['nat_cond'] != line_feature2['nat_cond']):
                        if point_f not in l :
                            l.append(point_f)
                    
                            break

                  
        for der_id in nearby_der_supp:
            line_feature11 = layer_derivation_bt.getFeature(der_id)
            line_feature22 = layer_derivation_bt.getFeature(der_id+1)
            if (point_f.geometry().touches(line_feature11.geometry())):
                if (point_f.geometry().touches(line_feature22.geometry())):
                    if (line_feature11['nat_cond'] != line_feature22['nat_cond']):
                        if point_f not in l :
                            l.append(point_f)
                      
                            break


        for bran_id in nearby_bran_supp:

            line_feature111 = layer_branchement_bt.getFeature(bran_id)
            line_feature222 = layer_branchement_bt.getFeature(bran_id+1)
            if (point_f.geometry().touches(line_feature111.geometry())):
                if (point_f.geometry().touches(line_feature222.geometry())):
                    if (line_feature111['nat_cond'] != line_feature222['nat_cond']):
                        if point_f not in l :
                            l.append(point_f)
                            break

    geom_nd = []  
    for noeud1 in layer_noeud_bt.getFeatures():
        geom_nd.append(noeud1.geometry().asPoint())
  
    for i in l:
        print(i.id())
        if (i.geometry().asPoint() not in geom_nd):
            print('in')
            new_feature = QgsFeature()
            new_feature.setAttributes(n.attributes())
            new_feature.setGeometry(i.geometry())
            attribute_index1 = layer_noeud_bt.fields().indexFromName("obs")
            new = "chang_carac"
            new_feature.setAttribute(attribute_index1, new)
            layer_noeud_bt.startEditing()
            layer_noeud_bt.addFeature(new_feature)
            layer_noeud_bt.commitChanges()
        else:
            print('no')
            for noeud in layer_noeud_bt.getFeatures():
                if (i.geometry().asPoint()== noeud.geometry().asPoint()):
                    layer_noeud_bt.startEditing()
                    noeud['obs']= noeud['obs'] + '_chang_carac'
                    print(noeud['obs'])
                    layer_noeud_bt.updateFeature(noeud)
                    layer_noeud_bt.commitChanges()
                    break


            