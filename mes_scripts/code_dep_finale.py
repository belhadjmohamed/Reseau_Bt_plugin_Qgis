# Renseignement des codes des lignes de départ 

"""
description : 
Cet algorithme permet de générer des identifiants uniques pour les lignes de départ en indiquant le numéro du départ,
le poste hta_bt associé à ce départ, ainsi que les tronçons de départ correspondants. 
Il est important de noter que l'un de ces tronçons de départ doit être situé entre deux nœuds basse tension. 
Le remplissage du code sera automatique en donnant simplement l'entité du poste.

"""

from qgis.core import *


from .mes_classes import my_attributes

def code_dep2(fn,fn2,fn3,id_poste,id_supp):

    layer_support_bt = QgsVectorLayer(fn,'support_bt','ogr')
    layer_depart = QgsVectorLayer(fn2,'depart_bt','ogr')
    poste_hta_bt = QgsVectorLayer(fn3,'poste_hta_bt','ogr')


    champs_dep = my_attributes(layer_depart)

    depart_inde = QgsSpatialIndex(layer_depart)
    poste = poste_hta_bt.getFeature(id_poste)
    code_poste = poste['code_pt']
    point = layer_support_bt.getFeature(id_supp)
    nearb_depart = depart_inde.nearestNeighbor(point.geometry(),0)

    nearby_support_depart = depart_inde.nearestNeighbor(poste.geometry(),0)

    depart_list = {}

    liste_dep_supp = []

    for dep_poste in nearby_support_depart:
        line_feature_poste = layer_depart.getFeature(dep_poste)
        if (poste.geometry().touches(line_feature_poste.geometry())):
            liste_dep_supp.append(line_feature_poste)
    



    for dep_i in nearb_depart:
        line_feature = layer_depart.getFeature(dep_i)
        if ((point.geometry().touches(line_feature.geometry())) and (line_feature not in liste_dep_supp)):
            depart_list[line_feature] = []


    print(depart_list)

    champs_dep.code_depart_cle(depart_list,code_poste)



    for cle_dep_poste in depart_list:
        for line_postee in liste_dep_supp:
            if (line_postee.geometry().touches(cle_dep_poste.geometry())):
                depart_list[cle_dep_poste].append(line_postee)
                liste_dep_supp.remove(line_postee)
                break
            
            
    print(depart_list)


    liste_dep_supp2 = []

    for dep_poste2 in nearby_support_depart:
        line_feature_poste2 = layer_depart.getFeature(dep_poste2)
        if (poste.geometry().touches(line_feature_poste2.geometry())):
            liste_dep_supp2.append(line_feature_poste2)
 
 
    len_features=[]
    for longueur in layer_depart.getFeatures():
        len_features.append(longueur)





    for liste_cle in depart_list:
        a = depart_list[liste_cle]
        a.append(liste_cle)
        kkk = 0
        while kkk <= 100:
            geome = a[-1].geometry()
            second_feature = None 
            for feat in len_features:
                if ((feat not in depart_list) and (feat not in liste_dep_supp2) and (feat.geometry().touches(geome))):
                    second_feature = feat
                    len_features.remove(feat)
                    break
            if second_feature is not None : 
                a.append(second_feature)
                kkk = kkk + 1
            else:
                print('none')
                break

        for ll in a:
            print(ll.id())


    for ccle in depart_list:
        b = depart_list[ccle]
        code =  ccle['code_dep']
        pp = 1
        if layer_depart.startEditing():
            if (len(b)==1):
                ch=str(pp)
                b[0]['code_dep'] =  code + ch
                layer_depart.updateFeature(b[0])
            layer_depart.commitChanges()
            
        for i in range(len(b)-1):
            if layer_depart.startEditing():
                if ((b[i]['type_tronc']=='Souterrain')):
                    ch = str(pp)
                    b[i]['code_dep'] =  code + ch
                    pp =pp +1
                    ch1 = str(pp)
                    b[i+1]['code_dep'] =  code + ch1
                elif ((b[i]['nd_amont']==b[i+1]['nd_amont']) and (b[i]['nd_aval']==b[i+1]['nd_aval'])):
                    ch = str(pp)
                    b[i]['code_dep'] =  code + ch
                    b[i+1]['code_dep'] =  code + ch
                else:
                    ch = str(pp)
                    b[i]['code_dep'] =  code + ch
                    pp =pp +1
                    ch1 = str(pp)
                    b[i+1]['code_dep'] =  code + ch1
               
                layer_depart.updateFeature(b[i])
                layer_depart.updateFeature(b[i+1])
                layer_depart.commitChanges()
                
                
