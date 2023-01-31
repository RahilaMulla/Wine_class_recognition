from Project_app.utils import Wine_type
from flask import Flask , jsonify ,render_template , request


app = Flask(__name__)
##################################################################################
 ################################# Base API #####################################
##################################################################################

@app.route('/')



@app.route('/Homepage')
def Homepage():
    print('Welcome to Wine Class Model')
    return render_template('home.html')
    


##################################################################################
 ################################# Model API #####################################
##################################################################################

@app.route('/predict_class',methods=['POST'])
def get_wine_class():
       
    data = request.form
    alcohol             = eval(data['alcohol'])
    malic_acid          = eval(data['malic_acid'])
    ash                 = eval(data['ash'])
    alcalinity_of_ash   = eval(data['alcalinity_of_ash'])
    magnesium           = eval(data['magnesium'])
    total_phenols       = eval(data['total_phenols'])
    flavanoids          = eval(data['flavanoids'])
    nonflavanoid_phenol = eval(data['nonflavanoid_phenol'])
    proanthocyanins     = eval(data['proanthocyanins'])
    color_intensity     = eval(data['color_intensity'])
    hue                 = eval(data['hue'])
    diluted_wines       = eval(data['diluted_wines'])
    proline             = eval(data['proline'])
    wine1 = Wine_type(alcohol,malic_acid,ash,alcalinity_of_ash,magnesium,total_phenols,flavanoids,nonflavanoid_phenol,proanthocyanins,color_intensity,hue,diluted_wines,proline)
    classes = wine1.get_predicted_class()
    return render_template('after.html', data=classes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080, debug= False)
