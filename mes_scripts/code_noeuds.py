fn1 = 'C:\\Users\\MSI\\Desktop\\sfff\\Jbeniena\\elfidh\\projet_poste_JBN\\noeud_bt.shp'

layer_noeud_bt = QgsVectorLayer(fn1,'noeud_bt','ogr')


for i in layer_noeud_bt.getFeatures():
    layer_noeud_bt.startEditing()
    i['id_nod'] = i.id()
    i['code_nod'] = 'NOD_' + str(i['id_nod'])
    layer_noeud_bt.updateFeature(i)
    layer_noeud_bt.commitChanges()
