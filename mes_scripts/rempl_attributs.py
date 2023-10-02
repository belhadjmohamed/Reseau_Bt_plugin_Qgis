# Utilisation de la classe "my_attributs" pour faciliter le renseignement des attributs dans un script

"""
description : 

Cet algorithme permet de remplir automatiquement les champs de différentes couches de données géographiques à partir des 
informations fournies par l'utilisateur. Les couches de données comprennent des couches de poste, de terrain, de tableau de comptage,
de points d'ancrage, de noeuds, de supports, d'installations photovoltaïques, de dérivations et de branchement. 
Pour chaque couche, l'algorithme crée une instance de la classe "my_attributs" pour remplir les champs spécifiques de cette couche. 
La fonction prend en entrée plusieurs paramètres, notamment les noms de fichiers pour chaque couche de données, 
la délégation, la localité, l'identifiant du poste hta_bt, et les deux chaines de caractères indiquant le code du poste.
""" 

from qgis.core import *


from .mes_classes import my_attributes

def remplissage_attributes(fn,fn1,fn3,fn2,fn4,fn5,fn6,fn7,fn8,fn9,deleg,local,id_poste,code1,code2):
    
    noeud_layer = QgsVectorLayer(fn4,'noeud_bt','ogr')
    depart_layer= QgsVectorLayer(fn7,'depart_bt','ogr')
    poste_hta_bt = QgsVectorLayer(fn,'poste_hta_bt','ogr')
    terrain_poste_bt = QgsVectorLayer(fn1,'terrain_poste','ogr')
    layer_comptage = QgsVectorLayer(fn3,'tableau_comptage','ogr')
    point_ancrage_bt = QgsVectorLayer(fn2,'point_ancrage_bt','ogr')
    support_bt = QgsVectorLayer(fn5,'support_bt','ogr')
    installation_pv = QgsVectorLayer(fn6,'installation_pv','ogr')
    derivation_bt = QgsVectorLayer(fn8,'derivation_bt','ogr')
    branchement_bt = QgsVectorLayer(fn9,'branchement_bt','ogr')
    

    # remplissage des champs du poste
    champs_poste = my_attributes(poste_hta_bt)
    champs_poste.code_poste(id_poste,code1,code2)
    champs_poste.delegation(deleg)
    champs_poste.gouvernorat()
    champs_poste.localite(local)


    # remplissage des champs du terrain 
    champs_ter = my_attributes(terrain_poste_bt)
    champs_ter.code_ter()
    champs_ter.centroid_ter()
    champs_ter.surf_ter()

    # remplissage des champs des tableaux de comptage 
    champs_comptage = my_attributes(layer_comptage)
    champs_comptage.code_tc()
    champs_comptage.delegation(deleg)
    champs_comptage.gouvernorat()
    champs_comptage.localite(local)
    champs_comptage.position_x_y()

    #remplissage des champs des points d'ancrage 
    champ_ptc = my_attributes(point_ancrage_bt)
    champ_ptc.code_anc()
    champ_ptc.delegation(deleg)
    champ_ptc.gouvernorat()
    champ_ptc.localite(local)
    champ_ptc.position_x_y()

    #remplissage des champs des noeuds
    champs_nd = my_attributes(noeud_layer)
    champs_nd.code_nod()
    champs_nd.delegation(deleg)
    champs_nd.gouvernorat()
    champs_nd.localite(local)
    champs_nd.position_x_y()
    champs_nd.sortie_poste_nd()
    champs_nd.derivation_nd()
    champs_nd.branch_nd()
    champs_nd.bout_nd()
    champs_nd.pl_ind_nd()
    champs_nd.pl_col_nd()
    champs_nd.chang_car()

    #remplissage des champs des supports
    champs_supp = my_attributes(support_bt)
    champs_supp.code_sup()
    champs_supp.delegation(deleg)
    champs_supp.gouvernorat()
    champs_supp.localite(local)
    champs_supp.position_x_y()

    #remplissage des champs des installation pv 
    champs_pv = my_attributes(installation_pv)
    champs_pv.code_ipv()
    champs_pv.delegation(deleg)
    champs_pv.gouvernorat()
    champs_pv.localite(local)

    # remplissage des champs depart_bt
    champs_depart = my_attributes(depart_layer)
    champs_depart.id_dep()
    champs_depart.delegation(deleg)
    champs_depart.gouvernorat()
    champs_depart.type_conducteur()
    champs_depart.metal_conducteur()
    champs_depart.sect_phase_neutre()
    champs_depart.long_troncon()

    # remplissage des champs derivation_bt
    champs_derivation = my_attributes(derivation_bt)
    champs_derivation.id_der()
    champs_derivation.delegation(deleg)
    champs_derivation.gouvernorat()
    champs_derivation.type_conducteur()
    champs_derivation.metal_conducteur()
    champs_derivation.sect_phase_neutre()
    champs_derivation.long_troncon()


    # remplissage des champs branchement_bt
    champs_branchement = my_attributes(branchement_bt)
    champs_branchement.id_bran()
    champs_branchement.type_conducteur()
    champs_branchement.metal_conducteur()
    champs_branchement.sect_phase_neutre()
    champs_branchement.long_troncon()

