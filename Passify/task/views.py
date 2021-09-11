from .models import *
from .forms import *
import smtplib
from cryptography.fernet import Fernet
from django.contrib import messages
from email.message import EmailMessage
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.

#Content page
@login_required(login_url='login')
def allobjects_view(request):
    myuser = request.user
    obj0 = LoginPass.objects.filter(user = myuser)

    obj1 = CreditPass.objects.filter(user = myuser)

    obj2 = NotesPass.objects.filter(user = myuser)
    # print(obj0)
    context={
        'loginpass': obj0,
        'creditpass': obj1,
        'notespass': obj2,
    }
    return render(request, 'index.html', context)

########## Login, Logout, Authentications and Verification ##############

#Sending mail using smtlib
def send_mail(usermail, usercode):
    
    #Provide the password and email(as string) through which verification code is being sent.
    mymail=""
    password="" 

    mymsg="Your verification code is: "+usercode

    #Setting subject, message, to and from
    msg=EmailMessage()
    msg.set_content(mymsg)
    msg['Subject']="Passify Verification"
    msg['From']=mymail
    msg['To']=usermail

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    #logging in to the smtlib server with my credentials
    server.login(mymail, password)

    server.send_message(msg)

    server.quit()


#for registration
def registration_view(request):
    form=CreateUserForm(request.POST or None)
    error=form.errors
    # print(form.errors.get("username"))
    usernameerror=error.get('username')
    passworderror2=error.get('password2')
    # if error.get('password'):
    # print(error)
    if form.is_valid():
        form.save()
        return redirect('login')
    
    context={
        'form':form,
        'usernameerror': usernameerror,
        'passworderror2': passworderror2,
    }

    return render(request, 'register.html', context)



#for logging in
@unauthenticated_user
def login_view(request):

    if request.method=='POST':
        #getting the entered the username and password
        username=request.POST.get("username")
        password=request.POST.get("password")

        #if this user exists
        user=authenticate(request, username=username, password=password)

        if user is not None:
            # login(request, user)
            # return redirect('/')
            #getting the primary key for that user and setting it equal to pk of session
            request.session['pk']=user.pk
            return redirect('verify')

        else:
            messages.info(request, "Username or Password is incorrect.")
            
    return render(request, 'login.html',{})


#for verification
@unauthenticated_user
def verification_view(request):
    pk=request.session.get('pk')

    if pk:
        #filtering the data based on the primary key
        obj=Authenticate.objects.filter(pk=pk)

        #getting user info
        myuser=obj[0].user
        useremail=obj[0].user.email
        code=obj[0].code

        if request.method != "POST":

            obj[0].save()   #generating a new code

            code=obj[0].code
            send_mail(useremail, code)  #sending the code

        else:

            msg=request.POST.get("enteredcode")

            if msg==code:

                obj[0].save() #making current code invalid
                
                # if code is correct login the user
                login(request, myuser)
                return redirect('/')

            else:
                messages.info(request, "Please enter the correct code!")

    return render(request, 'verify.html', {})


#for logout
@login_required(login_url='login')
def logout_view(request):

    logout(request)
    return redirect('login')



############# Hashing and Dehashing the password ##############

#Hashing the user password
def hashit(getpassword):
    #key to be used to hash the passwords and we throw it away i.e not store it anywhere
    key=b'qdPos09GPxOnR0Idcr9wauE5_8I3w3fWc_U2W7Wgl6c='

    ferkey=Fernet(key)

    encpassword=ferkey.encrypt(getpassword.encode())

    # decoded=fernet.decrypt(encmessage)
    return encpassword

#Dehashing the stored password
def dehashit(getpassword):
    if getpassword==None:
        return ""
    passwordkey = b'qdPos09GPxOnR0Idcr9wauE5_8I3w3fWc_U2W7Wgl6c='
    ferkey=Fernet(passwordkey)

    decoded_in_binary=ferkey.decrypt(getpassword)

    #decoding it in a string
    decmessage=decoded_in_binary.decode()
    return decmessage


############## Storing and Updating login ID and Password #############

############### Checking if the data requested belongs to the loggedin user ########
def checker(obj, my_id):
    check = False
    for i in obj:
        if str(i.id) == my_id:
            check=True
    
    return check

#For storing login id's and passwords
@login_required(login_url='login')
def storelogin_view(request):
    form=LoginStoreForm(request.POST or None)

    if form.is_valid():
        instance=form.save()
        #Get the instance of the user and save that form for this user
        instance.user=request.user
        instance.save()
        #Get the id of this created object
        my_id=instance.id
        obj=LoginPass.objects.get(id=my_id)
        obj.password=hashit(request.POST.get('getpassword')) #if we change it hashit it again
        obj.save()
        return redirect('/')

    context={
        'form': form,
    }

    return render(request, 'storelogin.html', context)


#Updating already stored Login id's and passwords
@login_required(login_url='login')
def updatelogin_view(request, my_id):
    obj=LoginPass.objects.get(id=my_id)

    form=LoginStoreForm(request.POST or None, instance=obj)

    #decrypting the password
    storedpassword=dehashit(obj.password)
    updated=obj.updated
    # print(storedpassword)
    # print(obj.password)
    thisuserobj = LoginPass.objects.filter(user=request.user)
    check = checker(thisuserobj, my_id)
    
    if not check:
        return redirect('login')

    if form.is_valid():
        form.save()
        if request.method=="POST":
            obj.password=hashit(request.POST.get('getpassword')) #getting password from the user and hashing it

            val = request.POST.get("pk")
            if val == 'delete':
                obj.delete()
            else:
                obj.save()
        return redirect('/')
    
    context={
        'form': form,
        'storedpassword': storedpassword,
        'updated': updated,
        'id': my_id,
    }

    return render(request, 'updatelogin.html', context)


############ Storing and updating credit card details ##############

#Storing credit card info
@login_required(login_url='login')
def storecredit_view(request):
    form = CreditStoreForm(request.POST or None)

    if form.is_valid():
        instance=form.save()
        instance.user=request.user
        instance.save()

        my_id = instance.id

        obj = CreditPass.objects.get(id = my_id)

        #get the cardnumber, pin and cvv from user and hashit
        obj.number = hashit(request.POST.get("getnumber"))
        obj.pin = hashit(request.POST.get("getpin"))
        obj.cvv = hashit(request.POST.get("getcvv"))
        obj.save()
        return redirect('/')
        # print(obj.number)
        # print(obj.pin)
        # print(obj.cvv)
    
    context={
        'form': form,
    }

    return render(request, 'storecredit.html', context)


#Updating the credit card details
@login_required(login_url='login')
def updatecredit_view(request, my_id):
    obj = CreditPass.objects.get(id = my_id)

    form = CreditStoreForm(request.POST or None, instance=obj)

    #decrypting the card number, pin and cvv
    storednumber = dehashit(obj.number)
    storedpin = dehashit(obj.pin)
    storedcvv = dehashit(obj.cvv)
    # print(obj.number)
    updated = obj.updated
    thisuserobj = CreditPass.objects.filter(user=request.user)
    check = checker(thisuserobj, my_id)

    if not check:
        return redirect('login')

    if form.is_valid():
        form.save()
        if request.method == "POST":
            # if we change it hashit again and store it
            obj.number = hashit(request.POST.get("getnumber"))
            obj.pin = hashit(request.POST.get("getpin"))
            obj.cvv = hashit(request.POST.get("getcvv"))
            if request.POST.get('pk') == 'delete':
                obj.delete()
            else:
                obj.save()
            return redirect('/')
    
    context={
        'form': form,
        'storednumber': storednumber,
        'storedpin': storedpin,
        'storedcvv': storedcvv,
        'updated': updated,
    }
    
    return render(request, 'updatecredit.html', context)



############# Storing and updating Secure notes #############

#storing secure note
@login_required(login_url='login')
def storenotes_view(request):
    form = NotesStoreForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        instance.user=request.user
        instance.save()

        my_id=instance.id
        obj=NotesPass.objects.get(id = my_id)

        obj.notes = hashit(request.POST.get("getnotes"))
        # print(obj.notes)
        obj.save()
        return redirect('/')
    
    context = {
        'form': form,
    }

    return render(request,'storenotes.html', context)



#updating the notes
@login_required(login_url='login')
def updatenotes_view(request, my_id):
    obj = NotesPass.objects.get(id = my_id)

    form = NotesStoreForm(request.POST or None, instance = obj)

    storednotes = dehashit(obj.notes)
    updated = obj.updated

    updated = obj.updated
    thisuserobj = NotesPass.objects.filter(user=request.user)
    check = checker(thisuserobj, my_id)

    if not check:
        return redirect('login')

    if form.is_valid():
        form.save()

        if request.method == "POST":
            obj.notes = hashit(request.POST.get("getnotes"))
            if request.POST.get('pk') == "delete":
                obj.delete()
            else:
                obj.save()
            return redirect('/')

    context = {
        'form': form,
        'storednotes': storednotes,
        'updated': updated,
    }
    
    return render(request, 'updatenotes.html', context)
