import pickle
import numpy as np
class Wine_type():
    

    def __init__(self,alcohol,malic_acid,ash,alcalinity_of_ash,magnesium,total_phenols,flavanoids,nonflavanoid_phenols,proanthocyanins,color_intensity,hue,diluted_wines,proline):
        
        self.alcohol=alcohol
        self.malic_acid=malic_acid
        self.ash=ash
        self.alcalinity_of_ash=alcalinity_of_ash
        self.magnesium=magnesium
        self.total_phenols=total_phenols
        self.flavanoids=flavanoids
        self.nonflavanoid_phenol=nonflavanoid_phenols
        self.proanthocyanins=proanthocyanins
        self.color_intensity=color_intensity
        self.hue=hue
        self.diluted_wines= diluted_wines
        self.proline=proline
    def load_model(self):
        with open(r'C:\Users\Admin\Desktop\Wine_Data_Project\Project_app\Linear_model.pkl', 'rb') as f:
            self.model = pickle.load(f)
    def get_predicted_class(self):
        self.load_model()
        test_array=np.zeros(13) 
        test_array[0]=self.alcohol
        test_array[1]=self.malic_acid
        test_array[2]=self.ash
        test_array[3]=self.alcalinity_of_ash
        test_array[4]=self.magnesium
        test_array[5]=self.total_phenols
        test_array[6]=self.flavanoids
        test_array[7]=self.nonflavanoid_phenol
        test_array[8]=self.proanthocyanins
        test_array[9]=self.color_intensity
        test_array[10]=self.hue
        test_array[11]=self.diluted_wines
        test_array[12]=self.proline
        print('Test Array :', test_array)

        predicted_class =np.absolute (np.around(self.model.predict([test_array])[0]))
        #print('Types of wine :',predicted_class)
        return  predicted_class
if __name__ == '__main__':
    alcohol = 15
    malic_acid = 1.75
    ash = 2.5
    alcalinity_of_ash = 16.0
    magnesium = 128
    total_phenols = 2.8
    flavanoids = 3.5
    nonflavanoid_phenol = 0.30
    proanthocyanins = 2.80
    color_intensity = 5.70
    hue = 1.05
    diluted_wines = 3.92
    proline = 1065.0
    wine=Wine_type(alcohol,malic_acid,ash,alcalinity_of_ash,magnesium,total_phenols,flavanoids,nonflavanoid_phenol,proanthocyanins,color_intensity,hue,diluted_wines,proline)
    wine.get_predicted_class()