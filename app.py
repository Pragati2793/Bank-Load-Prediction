from flask import Flask,render_template,request
import pickle
import numpy as np
import sklearn

model = pickle.load(open('svm_classifier.pkl','rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=["GET",'POST'])
def predict():
    if request.method == "POST":

        Dependents = eval(request.form.get('Dependents'))

        ApplicantIncome = eval(request.form.get('ApplicantIncome'))

        CoapplicantIncome = eval(request.form.get('CoapplicantIncome'))

        LoanAmount = eval(request.form.get('LoanAmount'))

        Loan_Amount_Term = eval(request.form.get('Loan_Amount_Term'))

        Credit_History = eval(request.form.get('Credit_History'))

        # Property_Area
        Property_Area = request.form["Property_Area"]

        if (Property_Area == 'Rural'):
            Property_Area = 0

        elif (Property_Area == 'Semiurban'):
            Property_Area = 1
           
        elif (Property_Area == 'Urban'):
            Property_Area = 2
            

        # Gender
        Gender = request.form["Gender"]
        if (Gender == 'Male'):
            Gender = 1

        else:
            Gender=0

        # Married
        Married = request.form["Married"]
        if (Married == 'Yes'):
            Married = 1

        else:
            Married=0

        # Education
        Education = request.form["Education"]
        if (Education == 'Graduate'):
            Education = 1

        else:
            Education=0

        # Self_Employed
        Self_Employed = request.form["Self_Employed"]
        if (Self_Employed == 'Yes'):
            Self_Employed = 1

        else:
            Self_Employed=0
    
        

    # prediction
    result = model.predict([[Gender,Married,Dependents,Education,Gender,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])

    if result == 1:
        result = 'Approved'
    else:
        result = 'Not Approved'

    return render_template('index.html',result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)