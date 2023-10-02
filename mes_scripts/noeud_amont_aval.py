# Génération des nœuds amont et aval pour chaque tronçon des lignes basse tension (entre deux support basses tension)

"""
description : 

Cet algorithme parcourt une couche de lignes de départ pour chaque ligne dans la couche, 
identifie le nœud aval le plus proche qui est également un nœud de réseau et le relie à la ligne de départ 
en modifiant la colonne d'attributs 'nd_aval' par le code du nœud aval correspondante. 
De même, il parcourt la couche de lignes de départ pour chaque ligne, 
identifie le nœud amont le plus proche qui est également un nœud de réseau et le relie à la ligne de départ 
en modifiant la colonne d'attributs 'nd_amont' par le code du nœud amont correspondante.
"""

from qgis.core import *

def nd_amont_aval(fn,fn2,fn3,fn7,fn4,fn5,fn6,id_poste):

   
    layer_support_bt = QgsVectorLayer(fn,'support_bt','ogr')
    layer_depart_bt = QgsVectorLayer(fn2,'support_bt','ogr')
    poste_hta_bt = QgsVectorLayer(fn3,'poste_hta_bt','ogr')
    layer_branchement_bt = QgsVectorLayer(fn7,'support_bt','ogr')
    layer_derivation_bt = QgsVectorLayer(fn4,'support_bt','ogr')
    layer_noeud_bt = QgsVectorLayer(fn5,'noeud_bt','ogr')
    layer_comptage = QgsVectorLayer(fn6,'tableau_comptage','ogr')


    comptage_index = QgsSpatialIndex(layer_comptage)

    depart_index = QgsSpatialIndex(layer_depart_bt)

    branch_index =  QgsSpatialIndex(layer_branchement_bt)

    der_index =  QgsSpatialIndex(layer_derivation_bt)

    sortie_de_poste = []
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
    nd_chang_carac = []
    nd_chang_carac_der = []
    nd_chang_carac_bran = []
    nd_comptage = []

    n = layer_noeud_bt.getFeature(0)
    poste = poste_hta_bt.getFeature(id_poste)
    nearby_depart = depart_index.nearestNeighbor(poste.geometry(),0)
    for iii in nearby_depart:
        deppp =  layer_depart_bt.getFeature(iii)
        if (deppp.geometry().intersects(poste.geometry())):
            intersection = poste.geometry().intersection(deppp.geometry())
            new_feature0 = QgsFeature()
            new_feature0.setAttributes(n.attributes())
            new_feature0.setGeometry(intersection)
            sortie_de_poste.append(new_feature0)

    for point_f in layer_support_bt.getFeatures():

        nearby_depart = depart_index.nearestNeighbor(point_f.geometry(),0)
        nearby_bran = branch_index.nearestNeighbor(point_f.geometry(),0)
        nearby_der = der_index.nearestNeighbor(point_f.geometry(),0)
    
        connected_der = []
        connected_bran = []
        connected_depart = []
        # Parcourir les entités linéaires connectées
        for dep_id in nearby_depart:
            line_feature = layer_depart_bt.getFeature(dep_id)

            # Vérifier si l'entité ponctuelle est connectée à l'entité linéaire
            if (point_f.geometry().touches(line_feature.geometry())):
                # Ajouter l'entité linéaire à la liste des entités connectées
                connected_depart.append(line_feature.id())
        
        for depart_id in nearby_depart:
            line_feature1 = layer_depart_bt.getFeature(depart_id)
            line_feature2 = layer_depart_bt.getFeature(depart_id+1)
            if (point_f.geometry().touches(line_feature1.geometry())):
                if (point_f.geometry().touches(line_feature2.geometry())):
                    if (line_feature1['nat_cond'] != line_feature2['nat_cond']):
                        nd_chang_carac.append(point_f)
                        break
    
        for derivation_id in nearby_der:
            line_feature1_der = layer_derivation_bt.getFeature(derivation_id)
            line_feature2_der = layer_derivation_bt.getFeature(derivation_id+1)
            if (point_f.geometry().touches(line_feature1_der.geometry())):
                if (point_f.geometry().touches(line_feature2_der.geometry())):
                    if (line_feature1_der['nat_cond'] != line_feature2_der['nat_cond']):
                        nd_chang_carac_der.append(point_f)
                        break
    
        for branch_id in nearby_bran:
            line_feature1_bran = layer_branchement_bt.getFeature(branch_id)
            line_feature2_bran = layer_branchement_bt.getFeature(branch_id+1)
            if (point_f.geometry().touches(line_feature1_bran.geometry())):
                if (point_f.geometry().touches(line_feature2_bran.geometry())):
                    if (line_feature1_bran['nat_cond'] != line_feature2_bran['nat_cond']):
                        nd_chang_carac_bran.append(point_f)
                        break
    
    
        for comptage_id in layer_comptage.getFeatures():
            nd_comptage.append(comptage_id)
    
        for der_id in nearby_der:
            line_feature_der = layer_derivation_bt.getFeature(der_id)

            # Vérifier si l'entité ponctuelle est connectée à l'entité linéaire
            if (point_f.geometry().touches(line_feature_der.geometry())):
                # Ajouter l'entité linéaire à la liste des entités connectées
                connected_der.append(line_feature_der.id())
    
    
        
    
        for bran_id in nearby_bran:
            line_feature_bran = layer_branchement_bt.getFeature(bran_id)

            # Vérifier si l'entité ponctuelle est connectée à l'entité linéaire
            if (point_f.geometry().touches(line_feature_bran.geometry())):
                # Ajouter l'entité linéaire à la liste des entités connectées
                connected_bran.append(line_feature_bran.id())
    
    

        if ((len(connected_depart) == 2) and (len(connected_der)>=1) and (len(connected_bran)==0)) or ((len(connected_depart) == 0) and (len(connected_der)>2) and (len(connected_bran)==0)):
            nd_der.append(point_f)
        elif ((len(connected_depart) == 2) and (len(connected_der)==0) and (len(connected_bran)>1)) or ((len(connected_depart) == 0) and (len(connected_der)==0) and (len(connected_bran)>3)) or ((len(connected_depart) == 0) and (len(connected_der)==2) and (len(connected_bran)>1)):
            nd_bran_col.append(point_f)
    
        elif ((len(connected_depart) == 2) and (len(connected_der)==0) and (len(connected_bran)==1)) or ((len(connected_depart) == 0) and (len(connected_der)==0) and (len(connected_bran)==3)) or ((len(connected_depart) == 0) and (len(connected_der)==2) and (len(connected_bran)==1)):
            nd_bran_ind.append(point_f)

        elif ((len(connected_depart) == 2) and (len(connected_der)>=1) and (len(connected_bran)>1)) or ((len(connected_depart) == 0) and (len(connected_der) > 2) and (len(connected_bran)>1)):
            nd_der_bran_col.append(point_f)
    
        elif  ((len(connected_depart) == 2) and (len(connected_der)>=1) and (len(connected_bran)==1)) or ((len(connected_depart) == 0) and (len(connected_der) > 2) and (len(connected_bran)==1)):
            nd_der_bran_ind.append(point_f)

        elif ((len(connected_depart) == 1) and (len(connected_der)==0) and (len(connected_bran)==0)) or ((len(connected_depart) == 0) and (len(connected_der)==1) and (len(connected_bran)==0)) :
            nd_bout.append(point_f)
        elif ((len(connected_depart) == 1) and (len(connected_der)>=1) and (len(connected_bran)==0)):
            nd_bout_der.append(point_f)
        elif ((len(connected_depart) == 0) and (len(connected_der)==1) and (len(connected_bran)>1)) or ((len(connected_depart) == 1) and (len(connected_der)==0) and (len(connected_bran)>1)) :
            nd_bout_bran_col.append(point_f)
    
        elif ((len(connected_depart) == 0) and (len(connected_der)==1) and (len(connected_bran)==1)) or ((len(connected_depart) == 1) and (len(connected_der)==0) and (len(connected_bran)==1)) :
            nd_bout_bran_ind.append(point_f)

        elif ((len(connected_depart) == 1) and (len(connected_der)>=1) and (len(connected_bran)>1)):
            nd_bout_der_bran_col.append(point_f)

        elif ((len(connected_depart) == 1) and (len(connected_der)>=1) and (len(connected_bran)==1)):
            nd_bout_der_bran_ind.append(point_f)

    L = [sortie_de_poste,nd_der,nd_bran_col,nd_der_bran_col,nd_bout,nd_bout_der,nd_bout_bran_col,nd_bout_der_bran_col,nd_bran_ind,nd_der_bran_ind,nd_bout_bran_ind,nd_bout_der_bran_ind,nd_chang_carac,nd_chang_carac_der,nd_chang_carac_bran,nd_comptage] 
    print(L)

    def point_in_nd(L,point_arrivee):
        for i in L:
            for w in i:
                if point_arrivee == w.geometry().asPoint():
                    return True 
        return False

    for line_dep_aval in layer_depart_bt.getFeatures():
    
        geom_aval = line_dep_aval.geometry()
    
        point_arrivee = geom_aval.asMultiPolyline()[-1][-1]
    
        p = line_dep_aval
        arriver=0
        arriver_dep =''
        nearby_pt_arrivee = depart_index.nearestNeighbor(point_arrivee,0)
        while (point_in_nd(L,point_arrivee) == False)and(len(nearby_pt_arrivee) > 1):
            nearby_pt_arrivee = depart_index.nearestNeighbor(point_arrivee,0)
            for arriver in nearby_pt_arrivee:
                if arriver != p:
                    arriver_dep = layer_depart_bt.getFeature(arriver)
                    point_arrivee = arriver_dep.geometry().asMultiPolyline()[-1][-1]
                    print(arriver_dep.id())
                    break
            p = arriver
        if point_in_nd(L, point_arrivee)== True:
            print('nd_aval')
            for nd in layer_noeud_bt.getFeatures():
                if point_arrivee == nd.geometry().asPoint():
                    if layer_depart_bt.startEditing():
                        code_nd = nd['code_nod']
                        line_dep_aval['nd_aval'] = code_nd
                        layer_depart_bt.updateFeature(line_dep_aval)
                        layer_depart_bt.commitChanges() 
             
      

    def point_in_nd1(L,point_depart):
        for i in L:
            for w in i:
                if point_depart == w.geometry().asPoint():
                    return True 
        return False


    for line_dep_amont in layer_depart_bt.getFeatures():
    
        geom_amont = line_dep_amont.geometry()
    
        point_depart = geom_amont.asMultiPolyline()[0][0]
    
        p1 = line_dep_amont
        depaart=0
        depart_dep =''
        k1 = 0
        while (point_in_nd1(L,point_depart) == False) and (k1< 50):
            nearby_pt_depart = depart_index.nearestNeighbor(point_depart,0)
            if len(nearby_pt_depart) > 1:
                for depaart in nearby_pt_depart:
                    if depaart != p1:
                        depart_dep = layer_depart_bt.getFeature(depaart)
                        point_depart = depart_dep.geometry().asMultiPolyline()[0][0]
                        print(depart_dep.id())
                        break
            p1 = depaart
            k1=k1+1
        if point_in_nd1(L, point_depart)== True:
            print('nd_amont')
            for nd1 in layer_noeud_bt.getFeatures():
                if point_depart == nd1.geometry().asPoint():
                    if layer_depart_bt.startEditing():
                        code_nd1 = nd1['code_nod']
                        line_dep_amont['nd_amont'] = code_nd1
                        layer_depart_bt.updateFeature(line_dep_amont)
                        layer_depart_bt.commitChanges()    
                
                
    for line_der_aval in layer_derivation_bt.getFeatures():
    
        geom_aval_der = line_der_aval.geometry()
    
        point_arrivee_der = geom_aval_der.asMultiPolyline()[-1][-1]
    
        p_der = line_der_aval
        arriver_der=0
        arriver_derr =''
        nearby_pt_arrivee_der = der_index.nearestNeighbor(point_arrivee_der,0)
        while (point_in_nd(L,point_arrivee_der) == False)and(len(nearby_pt_arrivee_der) > 1):
            nearby_pt_arrivee_der = der_index.nearestNeighbor(point_arrivee_der,0)
            for arriver_der in nearby_pt_arrivee_der:
                if arriver_der != p_der:
                    arriver_derr = layer_derivation_bt.getFeature(arriver_der)
                    point_arrivee_der = arriver_derr.geometry().asMultiPolyline()[-1][-1]
                    print(arriver_derr.id())
                    break
            p_der = arriver_der
        if point_in_nd(L, point_arrivee_der)== True:
            print('nd_aval')
            for nd_der in layer_noeud_bt.getFeatures():
                if point_arrivee_der == nd_der.geometry().asPoint():
                    if layer_derivation_bt.startEditing():
                        code_nd_der = nd_der['code_nod']
                        line_der_aval['nd_aval'] = code_nd_der
                        layer_derivation_bt.updateFeature(line_der_aval)
                        layer_derivation_bt.commitChanges() 
             
      



    for line_der_amont in layer_derivation_bt.getFeatures():
    
        geom_amont_der = line_der_amont.geometry()
    
        point_depart_der = geom_amont_der.asMultiPolyline()[0][0]
    
        p1_der = line_der_amont
        deriv=0
        depart_der =''
        k1_der = 0
        while (point_in_nd1(L,point_depart_der) == False) and (k1_der< 50):
            nearby_pt_depart_der = der_index.nearestNeighbor(point_depart_der,0)
            if len(nearby_pt_depart_der) > 1:
                for deriv in nearby_pt_depart_der:
                    if deriv != p1_der:
                        depart_der = layer_derivation_bt.getFeature(deriv)
                        point_depart_der = depart_der.geometry().asMultiPolyline()[0][0]
                        print(depart_der.id())
                        break
            p1_der = deriv
            k1_der=k1_der+1
        if point_in_nd1(L, point_depart_der)== True:
            print('nd_amont')
            for nd1_der in layer_noeud_bt.getFeatures():
                if point_depart_der == nd1_der.geometry().asPoint():
                    if layer_derivation_bt.startEditing():
                        code_nd1_der = nd1_der['code_nod']
                        line_der_amont['nd_amont'] = code_nd1_der
                        layer_derivation_bt.updateFeature(line_der_amont)
                        layer_derivation_bt.commitChanges()
        

    for line_bran_aval in layer_branchement_bt.getFeatures():
    
        geom_aval_bran = line_bran_aval.geometry()
    
        point_arrivee_bran = geom_aval_bran.asMultiPolyline()[-1][-1]
    
        p_bran = line_bran_aval
        arriver_bran=0
        arriver_brann =''
        nearby_pt_arrivee_bran = branch_index.nearestNeighbor(point_arrivee_bran,0)
        while (point_in_nd(L,point_arrivee_bran) == False)and(len(nearby_pt_arrivee_bran) > 1):
            nearby_pt_arrivee_bran = branch_index.nearestNeighbor(point_arrivee_bran,0)
            for arriver_bran in nearby_pt_arrivee_bran:
                if arriver_bran != p_bran:
                    arriver_brann = layer_branchement_bt.getFeature(arriver_bran)
                    point_arrivee_bran = arriver_brann.geometry().asMultiPolyline()[-1][-1]
                    print(arriver_brann.id())
                    break
            p_bran = arriver_bran
        if point_in_nd(L, point_arrivee_bran)== True:
            print('nd_aval')
            for nd_bran in layer_noeud_bt.getFeatures():
                if point_arrivee_bran == nd_bran.geometry().asPoint():
                    if layer_branchement_bt.startEditing():
                        code_nd_bran = nd_bran['code_nod']
                        line_bran_aval['nd_aval'] = code_nd_bran
                        layer_branchement_bt.updateFeature(line_bran_aval)
                        layer_branchement_bt.commitChanges() 



    for line_bran_amont in layer_branchement_bt.getFeatures():
    
        geom_amont_bran = line_bran_amont.geometry()
    
        point_depart_bran = geom_amont_bran.asMultiPolyline()[0][0]
    
        p1_bran = line_bran_amont
        branch=0
        depart_bran =''
        k1_bran = 0
        while (point_in_nd1(L,point_depart_bran) == False) and (k1_bran< 50):
            nearby_pt_depart_bran = branch_index.nearestNeighbor(point_depart_bran,0)
            if len(nearby_pt_depart_bran) > 1:
                for branch in nearby_pt_depart_bran:
                    if branch != p1_bran:
                        depart_bran = layer_branchement_bt.getFeature(branch)
                        point_depart_bran = depart_bran.geometry().asMultiPolyline()[0][0]
                        print(depart_bran.id())
                        break
            p1_bran = branch
            k1_bran=k1_bran+1
        if point_in_nd1(L, point_depart_bran)== True:
            print('nd_amont')
            for nd1_bran in layer_noeud_bt.getFeatures():
                if point_depart_bran == nd1_bran.geometry().asPoint():
                    if layer_branchement_bt.startEditing():
                        code_nd1_bran = nd1_bran['code_nod']
                        line_bran_amont['nd_amont'] = code_nd1_bran
                        layer_branchement_bt.updateFeature(line_bran_amont)
                        layer_branchement_bt.commitChanges()
             
      




        
        
        
        
        
        
        
        