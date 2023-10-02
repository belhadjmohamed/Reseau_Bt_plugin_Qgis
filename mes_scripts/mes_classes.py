# Renseignement des attributs qui disposent d'algorithmes simples ou un peu plus complexes mais qui sont assez nombreux.


"""
description : 

L'objectif était de remplir automatiquement plusieurs attributs en même temps en utilisant des attributs déjà renseignés. 
Pour ce faire, nous avons une classe globale qui contient des méthodes. 
Chaque méthode permet de remplir un champ spécifique en se basant sur un autre champ existant dans la table attributaire.
"""

class my_attributes:


    def __init__(self,layer):
        self.layer = layer 


    def type_conducteur(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                b = f['nat_cond']
                if ('NYY' in str(b) ):
                    f['metal_cond'] = 'NYY'
                elif ('TORSADE' in str(b) ):
                    f['metal_cond'] = 'TORSADE'
                self.layer.updateFeature(f)
            self.layer.commitChanges()
        else:
            print("Could not start editing")
    
    def metal_conducteur(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if ("ALU" in str(f['nat_cond'])):
                    f['type_cond'] = "ALU" 
                elif ("CU" in str(f['nat_cond'])): 
                    f['type_cond'] = "CU"
                self.layer.updateFeature(f)
            self.layer.commitChanges()
        else:
            print("could not start editing")


    def sect_phase_neutre(self):
        if self.layer.startEditing():
            for a in self.layer.getFeatures():
                b = a['nat_cond']
                if (b == ('2x6mm2_NYY_CU')):
                    a['sect_ph'] = '6'
                    a['sect_n'] = '6'
                elif (b == ('2x10mm2_NYY_CU')):
                    a['sect_ph'] = '10'
                    a['sect_n'] = '10'
                elif (b == ('2x16mm2_NYY_CU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('4x6mm2_NYY_CU')):
                    a['sect_ph'] = '6'
                    a['sect_n'] = '6'
                elif (b == ('4x10mm2_NYY_CU')):
                    a['sect_ph'] = '10'
                    a['sect_n'] = '10'
                elif (b == ('4x16mm2_NYY_CU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('4x25mm2_NYY_CU')):
                    a['sect_ph'] = '25'
                    a['sect_n'] = '25'
                elif (b == ('3x50+35mm2_NYY_CU')):
                    a['sect_ph'] = '50'
                    a['sect_n'] = '35'
                elif (b == ('3x70+50mm2_NYY_CU')):
                    a['sect_ph'] = '70'
                    a['sect_n'] = '50'
                elif (b == ('3x120+70mm2_NYY_CU')):
                    a['sect_ph'] = '120'
                    a['sect_n'] = '70'
                elif (b == ('2x16mm2_NAYY_ALU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('2x25mm2_NAYY_ALU')):
                    a['sect_ph'] = '25'
                    a['sect_n'] = '25'
                elif (b == ('4x16mm2_NAYY_ALU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('4x25mm2_NAYY_ALU')):
                    a['sect_ph'] = '25'
                    a['sect_n'] = '25'
                elif (b == ('4x70mm2_NAYY_ALU')):
                    a['sect_ph'] = '70'
                    a['sect_n'] = '70'
                elif (b == ('3x120+70mm2_NAYY_ALU')):
                    a['sect_ph'] = '120'
                    a['sect_n'] = '70'
                elif (b == ('3x240+120mm2_NAYY_ALU')):
                    a['sect_ph'] = '240'
                    a['sect_n'] = '120'
                elif (b == ('2x16mm2_TORSADE_ALU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('2x25mm2_TORSADE_ALU')):
                    a['sect_ph'] = '25'
                    a['sect_n'] = '25'
                elif (b == ('4x16mm2_TORSADE_ALU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('1x35+54.6mm2_TORSADE_ALU')):
                    a['sect_ph'] = '35'
                    a['sect_n'] = '54.6'
                elif (b == ('1x70+54.6mm2_TORSADE_ALU')):
                    a['sect_ph'] = '70'
                    a['sect_n'] = '54.6'
                elif (b == ('3x35+54.6mm2_TORSADE_ALU')):
                    a['sect_ph'] = '35'
                    a['sect_n'] = '54.6'
                elif (b == ('3x70+54.6mm2_TORSADE_ALU')):
                    a['sect_ph'] = '70'
                    a['sect_n'] = '54.6'
                elif (b == ('2x6mm2_TORSADE_CU')):
                    a['sect_ph'] = '6'
                    a['sect_n'] = '6'
                elif (b == ('2x10mm2_TORSADE_CU')):
                    a['sect_ph'] = '10'
                    a['sect_n'] = '10'
                elif (b == ('2x16mm2_TORSADE_CU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('4x6mm2_TORSADE_CU')):
                    a['sect_ph'] = '6'
                    a['sect_n'] = '6'
                elif (b == ('4x10mm2_TORSADE_CU')):
                    a['sect_ph'] = '10'
                    a['sect_n'] = '10'
                elif (b == ('4x16mm2_TORSADE_CU')):
                    a['sect_ph'] = '16'
                    a['sect_n'] = '16'
                elif (b == ('4x17.8mm2_NU_CU')):
                    a['sect_ph'] = '17.8'
                    a['sect_n'] = '17.8'
                elif (b == ('29_NU_CU')):
                    a['sect_ph'] = '29'
                    a['sect_n'] = '29'
                elif (b == ('38_NU_CU')):
                    a['sect_ph'] = '38'
                    a['sect_n'] = '38'
                elif (b == ('48_NU_CU')):
                    a['sect_ph'] = '48'
                    a['sect_n'] = '48'
                elif (b == ('AUTRE')):
                    a['sect_ph'] = 'AUTRE'
                    a['sect_n'] = 'AUTRE'
                elif (b == ('NC')):
                    a['sect_ph'] = 'NC'
                    a['sect_n'] = 'NC'
                self.layer.updateFeature(a)
            self.layer.commitChanges()
        else:
             print("could not start editing")

    def long_troncon(self):
        if self.layer.startEditing():        
            for q in self.layer.getFeatures():
                geom = q.geometry()
                lengthh = geom.length()
                q['long_m'] = lengthh
                self.layer.updateFeature(q)
            self.layer.commitChanges()
    

    def position_x_y(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                geom = f.geometry().asPoint()
                x, y = geom.x() , geom.y()
                f['x_32632'] = x 
                f['y_32632'] = y 
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def gouvernorat(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                f['gouv'] = 'SFAX'
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def delegation(self,deleg):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                f['deleg'] = deleg
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def localite(self,locali):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                f['localite'] = locali
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def sortie_poste_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_sortie_poste"):
                    f['sortie_pt'] = 'oui'
                else:
                    f['sortie_pt'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def derivation_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_der"):
                    f['derivation'] = 'oui'
                elif(f['obs'] == "nd_der_bran_col"):
                    f['derivation'] = 'oui'
                elif (f['obs'] == "nd_bout_der"):
                    f['derivation'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_col"):
                    f['derivation'] = 'oui'
                elif (f['obs'] == "nd_der_bran_ind"):
                    f['derivation'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_ind"):
                    f['derivation'] = 'oui'
                else:
                    f['derivation'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def branch_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_bran_col"):
                    f['branch'] = 'oui'
                elif(f['obs'] == "nd_der_bran_col"):
                    f['branch'] = 'oui'
                elif (f['obs'] == "nd_bout_der"):
                    f['branch'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_col"):
                    f['branch'] = 'oui'
                elif (f['obs'] == "nd_bran_ind"):
                    f['branch'] = 'oui'
                elif (f['obs'] == "nd_der_bran_ind"):
                    f['branch'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_ind"):
                    f['branch'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_ind"):
                    f['branch'] = 'oui'
                else:
                    f['branch'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges()


    def bout_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_bout"):
                    f['bout_res'] = 'oui'
                elif(f['obs'] == "nd_bout_der"):
                    f['bout_res'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_col"):
                    f['bout_res'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_col"):
                    f['bout_res'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_ind"):
                    f['bout_res'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_ind"):
                    f['bout_res'] = 'oui'
                else:
                    f['bout_res'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges()  

    def pl_ind_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif(f['obs'] == "nd_der_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif (f['obs'] == "nd_ind"):
                    f['pl_ind'] = 'oui'
                else:
                    f['pl_ind'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges()  

    def pl_ind_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif(f['obs'] == "nd_der_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_ind"):
                    f['pl_ind'] = 'oui'
                elif (f['obs'] == "nd_ind"):
                    f['pl_ind'] = 'oui'
                else:
                    f['pl_ind'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges()

    def pl_col_nd(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if (f['obs'] == "nd_bran_col"):
                    f['pl_col'] = 'oui'
                elif(f['obs'] == "nd_der_bran_col"):
                    f['pl_col'] = 'oui'
                elif (f['obs'] == "nd_bout_bran_col"):
                    f['pl_col'] = 'oui'
                elif (f['obs'] == "nd_bout_der_bran_col"):
                    f['pl_col'] = 'oui'
                else:
                    f['pl_col'] = 'non'
                self.layer.updateFeature(f)
            self.layer.commitChanges() 

    def chang_car(self):
        if self.layer.startEditing():
            for f in self.layer.getFeatures():
                if ("chang_carac" in str(f['obs']) ):
                    f['chgt_carac'] = 'OUI'
                else:
                    f['chgt_carac'] = 'NON'
                self.layer.updateFeature(f)
            self.layer.commitChanges() 

    def code_poste(self,indice,code,nom_p):
        if self.layer.startEditing():
            poste = self.layer.getFeature(indice)
            poste['code_pt'] = code +'_'+ nom_p
            a = poste['code_pt']
            my_attributes.chaine = a
            self.layer.updateFeature(poste)
            self.layer.commitChanges() 

    chaine = 'code'
    
    def code_ter(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_ter'] = i.id()
            i['code_ter'] = my_attributes.chaine + '_TER' + str(i['id_ter']+1)
            self.layer.updateFeature(i)
            self.layer.commitChanges()
    
    def centroid_ter(self):
        if self.layer.startEditing():
            for feature in self.layer.getFeatures():
                geom = feature.geometry()
                centroid = geom.centroid().asPoint()
                x, y = centroid.x() , centroid.y()
                feature['x_cent'] = x 
                feature['y_cent'] = y 
                self.layer.updateFeature(feature)
            self.layer.commitChanges()
    
    def surf_ter(self):
        if self.layer.startEditing():
            for feature in self.layer.getFeatures():
                geom = feature.geometry()
                surface = geom.area()
                feature['surf_m2']= surface
                self.layer.updateFeature(feature)
            self.layer.commitChanges()

    def code_nod(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_nod'] = i.id()
            i['code_nod'] = my_attributes.chaine + '_NOD' + str(i['id_nod']+1)
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def code_sup(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_sup'] = i.id()
            i['code_sup'] = my_attributes.chaine + '_SUP' + str(i['id_sup']+1)
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def code_anc(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_pta'] = i.id()
            i['code_pta'] = my_attributes.chaine + '_PTA' + str(i['id_pta']+1)
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def code_tc(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_tc'] = i.id()
            i['code_tc'] = my_attributes.chaine + '_TCP' + str(i['id_tc']+1)
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def code_ipv(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_ipv'] = i.id()
            i['code_ipv'] = my_attributes.chaine + '_IPV' + str(i['id_ipv']+1)
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def id_dep(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_dep'] = i.id()
            self.layer.updateFeature(i)
            self.layer.commitChanges()
    
    def id_der(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_der'] = i.id()
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def id_bran(self):
        for i in self.layer.getFeatures():
            self.layer.startEditing()
            i['id_bri'] = i.id()
            self.layer.updateFeature(i)
            self.layer.commitChanges()

    def code_depart_cle(self,mdict,code_poste):
        a=1
        for code2 in mdict :
            if self.layer.startEditing():
                ch = str(a)
                code2['code_dep'] = code_poste +'_'+'DEP' + ch +'_'
                a = a + 1
                self.layer.updateFeature(code2)
                self.layer.commitChanges()
    

    def code_depart_val(self,m,code):
        a = 1
        for i in range(len(m)-1):
            if self.layer.startEditing():
                if ((m[i]['type_tronc']=='Souterrain') or ((m[i]['nd_amont']==m[i+1]['nd_amont']) and (m[i]['nd_aval']==m[i+1]['nd_aval']))):
                    ch = str(a)
                    m[i]['code_dep'] =  code + ch
                    m[i+1]['code_dep'] =  code + ch
                else:
                    ch = str(a)
                    m[i]['code_dep'] =  code + ch
                    a = a + 1
                    ch = str(a)
                    m[i+1]['code_dep'] =  code + ch
                self.layer.updateFeature(m[i])
                self.layer.commitChanges()


    def code_der_dep_niv1(self,layer1,layer_iface,n):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                for i in layer1.getFeatures():
                    if i.geometry().intersects(a.geometry()):
                        print('intersect')
                        code_dep = i['code_dep']
                        break
                a['code_dep'] = code_dep
                a['code_der'] = a['code_dep'] + '_'+'DER' + n + '_' 
                self.layer.updateFeature(a)
            self.layer.commitChanges()
        else:
            print("Could not start editing")

    chaine3 = '_DER'


    def code_der_dep_niv2(self,layer_iface,code_poste,n,y,p,m,k):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                a['code_dep'] = code_poste+'_'+'DEP' + n + '_' + y
                a['code_der'] =  code_poste + '_'+'DEP' + n + '_' + y + my_attributes.chaine3 +  p +'_'+ m +'_DER'+ k +'_'
                self.layer.updateFeature(a)
            self.layer.commitChanges() 
        

    def codebri_dep_bran(self,layer1,layer_iface,n):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                for i in layer1.getFeatures():
                    if i.geometry().intersects(a.geometry()):
                        print('intersect')
                        code1 = i['code_dep']
                        break
                a['code_dep'] = code1
                a['code_der'] = None
                a['code_bri'] = a['code_dep'] + '_Bran' + n + '_'
                self.layer.updateFeature(a)
            self.layer.commitChanges()
        else:
            print("Could not start editing")


    def codebri_dep_bran_bran(self,layer_iface,n,p,b):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                a['code_dep'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n 
                a['code_der'] =  None 
                a['code_bri'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n + '_Bran_'+ p + '_Bran_'+ b
                self.layer.updateFeature(a)
            self.layer.commitChanges() 

    def codebri_dep_der_bran(self,layer1,layer_iface,n):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                for i in layer1.getFeatures():
                    if i.geometry().intersects(a.geometry()):
                        print('intersect')
                        code1 = i['code_der']
                        break
                a['code_dep'] = code1[:-7]
                a['code_der'] = code1
                a['code_bri'] = a['code_der'] + '_Bran' + n + '_'
                self.layer.updateFeature(a)
            self.layer.commitChanges() 
        
    def codebri_dep_der_bran_bran(self,layer_iface,n,p,b,c):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                a['code_dep'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n 
                a['code_der'] =  my_attributes.chaine + '_'+'DEP' + n + '_' + n + my_attributes.chaine3 + p  
                a['code_bri'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n + my_attributes.chaine3 + p + '_Bran_'+ b + '_Bran_' + c
                self.layer.updateFeature(a)
            self.layer.commitChanges() 
    
    
    def codebri_dep_der_der_bran(self,layer_iface,n,p,b,c):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                a['code_dep'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n 
                a['code_der'] =  my_attributes.chaine + '_'+'DEP' + n + '_' + n + my_attributes.chaine3 + p  
                a['code_bri'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n + my_attributes.chaine3 + p + '_DER_'+ b + '_Bran_' + c
                self.layer.updateFeature(a)
            self.layer.commitChanges() 

    
    def codebri_dep_der_der_bran_bran(self,layer_iface,n,p,b,c,r):
        selected = layer_iface.selectedFeatures()
        if self.layer.startEditing():
            for a in selected: 
                a['code_dep'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n 
                a['code_der'] =  my_attributes.chaine + '_'+'DEP' + n + '_' + n + my_attributes.chaine3 + p  
                a['code_bri'] = my_attributes.chaine + '_'+'DEP' + n + '_' + n + my_attributes.chaine3 + p + '_DER_'+ b + '_Bran_' + c + '_Bran_' + r
                self.layer.updateFeature(a)
            self.layer.commitChanges() 

