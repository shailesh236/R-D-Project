from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from pyrebase import pyrebase


config = {

    "apiKey": "AIzaSyB84D7Ri5_QRV5kYtrwNwanS_oAASoJXs8",
    "authDomain": "djangocrud-3561c.firebaseapp.com",
    "databaseURL": "https://djangocrud-3561c-default-rtdb.firebaseio.com",
    "projectId": "djangocrud-3561c",
    "storageBucket": "djangocrud-3561c.appspot.com",
    "messagingSenderId": "16200984584",
    "appId": "1:16200984584:web:2f9b492465c081668889bd",

  }


firebase = pyrebase.initialize_app(config)
database = firebase.database()
storage = firebase.storage()

def index(request):  
  return render(request,'index.html')

def test(request):
  return render(request,'test.html')

def test_result(request):
  q1=int(request.POST.get('q1'))
  q2=int(request.POST.get('q2'))
  q3=int(request.POST.get('q3'))
  q4=int(request.POST.get('q4'))
  q5=int(request.POST.get('q5'))
  q6=int(request.POST.get('q6'))
  q7=int(request.POST.get('q7'))
  q8=int(request.POST.get('q8'))
  q9=int(request.POST.get('q9'))
  q10=int(request.POST.get('q10'))
  q11=int(request.POST.get('q11'))
  q12=int(request.POST.get('q12'))
  q13=int(request.POST.get('q13'))
  q14=int(request.POST.get('q14'))
  q15=int(request.POST.get('q15'))

# Create your views here.
def demo(request):
    # if request.method == 'POST':
    #     file = request.FILES['file']
    #     file_save = default_storage.save(file.name, file)
    #     storage.child("files/" + file.name).put("media/" + file.name)
    #     delete = default_strage.delete(file.name)
    #     messages.success(request, "File upload in Firebase Storage successful")
    #     return redirect('main')
    # else:
    #     return render(request, 'index.html')
    msg=""
    if request.method=="POST":
      butt=request.POST["Send"]

      if butt=="Insert":
        table=database.child("Employee_Details").get().val()
        data=list(table.items())
        eid=[]
        for i in data:
          eid.append(i[0])
        name= request.POST.get('name')
        address= request.POST.get('adr')
        city= request.POST.get('city')
        gender= request.POST.get('gender')
        vehicle= request.POST.getlist('vehicle')
        id= request.POST.get('id')
        url= request.POST.get('url')

        
        if id in eid:
          msg="Employee ID already exists!"
          return render(request,'index.html',{'msg':msg})
  
        else:
          
    # storage.child(image.name).put(image)
    # print(storage.child(image).get_url(None))

          data = {
            "id":id,
            "name":name,
            "address":address,
            "city":city,
            "gender":gender,
            "vehicle":vehicle,
            "url":url,
          }

          database.child("Employee_Details").child(id).set(data)
          msg="Record Inserted"
          return render(request,'index.html',{'msg':msg})
      
      elif butt=="Select":
        try:
          id= request.POST.get('id')
          eid=database.child("Employee_Details").child(id).child("id").get().val()
          name=database.child("Employee_Details").child(id).child("name").get().val()
          adr=database.child("Employee_Details").child(id).child("address").get().val()
          city=database.child("Employee_Details").child(id).child("city").get().val()
          gender=database.child("Employee_Details").child(id).child("gender").get().val()
          veh=database.child("Employee_Details").child(id).child("vehicle").get().val()
          url=database.child("Employee_Details").child(id).child("url").get().val()
          veh1=''
          veh2=''
          veh3=''
          for i in veh:
            if i=="Car":
              veh2="Car"
            elif i=="Bike":
              veh1="Bike"
            elif i=="Scooter":
              veh3="Scooter"
          return render(request,'index.html',{'id':eid,'name':name,'adr':adr,'city':city,'veh1':veh1,'veh2':veh2,'veh3':veh3,'gender':gender,'url':url})
        except:
          msg="No Employee found!"
          return render(request,'index.html',{'msg':msg})

      elif butt=="Update":
        name= request.POST.get('name')
        address= request.POST.get('adr')
        city= request.POST.get('city')
        gender= request.POST.get('gender')
        vehicle= request.POST.getlist('vehicle')
        id= request.POST.get('id')
        url= request.POST.get('url')

        database.child("Employee_Details").child(id).update({"id":id})
        database.child("Employee_Details").child(id).update({"name":name})
        database.child("Employee_Details").child(id).update({"address":address})
        database.child("Employee_Details").child(id).update({"city":city})
        database.child("Employee_Details").child(id).update({"gender":gender})
        database.child("Employee_Details").child(id).update({"vehicle":vehicle})
        database.child("Employee_Details").child(id).update({"url":url})

        msg="Record Updated"
        return render(request,'index.html',{'msg':msg})

      elif butt=="Delete":
        id= request.POST.get('id')
        database.child("Employee_Details").child(id).remove()
        msg="Record Deleted"
        return render(request,'index.html',{'msg':msg})
        
      elif butt=="SelectAll":
        table=database.child("Employee_Details").get().val()
        data=list(table.items())
        eid=[]
        name=[]
        adr=[]
        city=[]
        gender=[]
        veh=[]
        url=[]
        for i in data:
          eid.append(i[0])
        # print(eid)
        for j in eid:
          nam=database.child("Employee_Details").child(j).child("name").get().val()
          ad=database.child("Employee_Details").child(j).child("address").get().val()
          cit=database.child("Employee_Details").child(j).child("city").get().val()
          gende=database.child("Employee_Details").child(j).child("gender").get().val()
          ve=database.child("Employee_Details").child(j).child("vehicle").get().val()
          ur=database.child("Employee_Details").child(j).child("url").get().val()
          name.append(nam)
          adr.append(ad)
          city.append(cit)
          gender.append(gende)
          veh.append(ve)
          url.append(ur)
        # print(name)
        # print(adr)
        # print(city)
        # print(gender)
        # print(veh)
        # print(url)
        com_list=zip(eid,name,adr,city,gender,veh,url)
        return render(request,'result.html',{'com_lis':com_list})
