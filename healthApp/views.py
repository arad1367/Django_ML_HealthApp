from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Symptom
import pandas as pd
import pickle
import joblib
import sklearn
from django.contrib.auth.decorators import login_required

# Load ML model
model_reload = joblib.load('./MLmodel/LR_Model.pkl')

# Create your views here.
def homepage(request):
    return render(request, 'healthApp/index.html')

@login_required
def testmodel(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        temp={}
        temp['age'] = request.POST.get('age')
        temp['sex'] = request.POST.get('sex')
        temp['cp'] = request.POST.get('cp')
        temp['trestbps'] = request.POST.get('trestbps')
        temp['chol'] = request.POST.get('chol')
        temp['fbs'] = request.POST.get('fbs')
        temp['restecg'] = request.POST.get('restecg')
        temp['thalach'] = request.POST.get('thalach')
        temp['exang'] = request.POST.get('exang')
        temp['oldpeak'] = request.POST.get('oldpeak')
        temp['slope'] = request.POST.get('slope')
        temp['ca'] = request.POST.get('ca')
        temp['thal'] = request.POST.get('thal')
        print(temp)

        symptom = Symptom(firstname=firstname, lastname=lastname, age=temp['age'], sex=temp['sex'], cp=temp['cp'],
                            trestbps=temp['trestbps'], chol=temp['chol'], fbs=temp['fbs'], restecg=temp['restecg'],
                             thalach=temp['thalach'], exang=temp['exang'], oldpeak=temp['oldpeak'], slope=temp['slope'],
                              ca=temp['ca'], thal=temp['thal'])
        symptom.save()

        testData = pd.DataFrame({'x':temp}).transpose(copy=True)
        testData = testData[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']]
        # print(testData)
        # print(type(testData))

        health_pred = model_reload.predict(testData)[0]

        context = {
            'health_pred': health_pred,
            'clientname': firstname
        }
        return render(request, 'healthApp/testHealth.html', context=context)
    return render(request, 'healthApp/testHealth.html')


def about(request):
    return render(request, 'healthApp/about.html')


def docs(request):
    return render(request, 'healthApp/docs.html')


def contacts(request):
    return render(request, 'healthApp/contacts.html')