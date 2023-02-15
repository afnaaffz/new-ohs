from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from online_home_service_app.forms import Login_Form, Login_Form, Register_Form, Register_Form1, FeedbackForm, \
    ScheduleForm, work_form, AddBill, CreditCardForm
from online_home_service_app.models import Register, Login, Register1, Complaints, Schedule, work, Take_Appointment, \
    Bill, CreditCard




# Create your views here.

def index(request):
    return render(request,"index.html")

def indexx(request):
    return render(request,"indexx.html")

def contact(request):
    return render(request,"contact.html")

def profile(request):
    return render(request,"profile.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("base")
            if user.is_customer:
                return redirect("customerbase")
            if user.is_worker:
                return redirect("workerbase")

        else:
            messages.info(request,"Invalid credentials")
    return render(request,"login.html")


#########################ADMIN######################
def adminbase(request):
    return render(request,"admin/admin base.html")

def feedbacks(request):
    n = Complaints.objects.all
    return render(request, "admin/feedbacks.html",{"feedbacks":n})

# this is for admin to view feedback data

def reply_feedback(request,id):
    feedback = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request,' Reply send for complaint')
        return redirect('feedbacks')
    return render(request, 'admin/reply_feedback.html',{'feedback':feedback})

# this is for admin to reply back to the feedback of customer
# date and complaint will be readonly value and admin can give reply in reply field

def view_schedule(request):
    n = Schedule.objects.all()
    return render(request, "admin/view_schedule.html",{"view_schedule":n})

# this is for admin to view schedules of workers data.
# workers details will be shown there and delete option is also available.

def work_add(request):
    form = work_form()
    if request.method =='POST':
        form = work_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work_view")
    return render(request,'admin/work_add.html',{'form':form})

#admin must add works and their charge so that the worker can select which work type during registration

def work_view(request):
    data = work.objects.all()
    return render(request,'admin/work_view.html',{'data':data})

# here details of work provided by admin will be shown
# details can be deleted or updated

def update_work_view(request,id):

    a = work.objects.get(id=id)
    form = work_form(instance=a)
    if request.method == 'POST':
        form = work_form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect("work_view")

    return render(request, "admin/update_work_view.html", {'form': form})

# here admin can update details of work ie, name and charge

def admin_view_appointment(request):
    a = Take_Appointment.objects.all()
    return render(request,"admin/admin_view_appointment.html",{"a":a})

# here admin can view appointment and can either accept or reject
# customer takes workers in
# worker logins and add schedule then customer can view appointment

def approve_appointment(request,id):
    n =Take_Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request,"Appointment is Confirmed")
    return redirect("admin_view_appointment")

# here admin can approve appointment using id

def reject_appointment(request,id):
    n =Take_Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request,"Appointment is Rejected")
    return redirect("admin_view_appointment")

# here admin can reject appointment using id

def bill(request):
    form = AddBill()
    if request.method == 'POST':
        form = AddBill(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_bill')
    return render(request, 'admin/generate_bill.html', {'form':form})

# here admin can generate bill for customers

def view_bill(request):
    bill = Bill.objects.all()
    print(bill)
    return render(request, 'admin/view_payment_details.html', {'bill': bill})

# admin can view payment details of customer and can see the status pending there...


def customers_data(request):
    data = Register.objects.all()
    print(data)
    return render(request,"admin/customers_data.html",{'data':data})

# this is for admin to view all the customers data

def delete_it(request,id):
    wm = Register.objects.get(id=id)
    wm.delete()
    return redirect("customers_data")

# this is to delete the data in the customers_data


def workers_data(request):
    data = Register1.objects.all()
    print(data)
    return render(request,"admin/workers_data.html",{'data':data})

# this is for admin to view all the workers data

def delete(request,id):
    wm = Register1.objects.get(id=id)
    wm.delete()
    return redirect("workers_data")

# this is to delete the data in the workers_data


def update(request,id):

    a = Register1.objects.get(id=id)
    form = Register_Form(instance=a)
    if request.method == 'POST':
        form = Register_Form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect("workers_data")

    return render(request, "admin/update.html", {'form': form})

# this is to update the data in the workers_data

####################CUSTOMER####################333
def customers(request):
    return render(request,"customer/customers.html")

def customerbase(request):
    return render(request,"customer/customer base.html")

# it is the dashboard of customer

def customer_registration(request):
    form1 = Login_Form()
    form2 = Register_Form()
    if request.method == "POST":
        form1 = Login_Form(request.POST)
        form2 = Register_Form(request.POST)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_customer = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request,"customer/customers.html", {'form1':form1, 'form2':form2})

# customer can register here


def feedback(request):
    form = FeedbackForm()
    u = request.user
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect("view")
    return render(request,"customer/feedback.html",{"form":form})

# this is for customer to write their feedback

def view(request):
    data = Complaints.objects.filter(user = request.user)
    print(data)
    return render(request, "customer/view.html", {"data": data})

# customer can see the reply given by admin for their feedback
# admin will reply to the feedback of the customer

def del_feedback(request,id):
    wm = Complaints.objects.get(id=id)
    wm.delete()
    return redirect("view")

# here customer can delete feedback

def customer_view_schedule(request):
    n = Schedule.objects.all
    return render(request, "customer/customer_view_schedule.html",{"view_schedule":n})

# here customer can view schedules of the worker

def delete_schedule(request,id):
    wm = Schedule.objects.get(id=id)
    wm.delete()
    return redirect("view_schedule")

# here customer can delete schedule of the worker

def view_worker(request):
    data = Register1.objects.all()
    return render(request,"customer/view_worker.html",{"data":data})

# here customer can view workers details

def take_appointment(request,id):
    s = Schedule.objects.get(id=id)
    c = Register.objects.get(user = request.user)
    app = Take_Appointment.objects.filter(user = c,schedule = s)
    if app.exists():
        messages.info(request,"Already booked")
        return redirect("customer_view_schedule")
    else:
        if request.method == "POST":
            obj = Take_Appointment()
            obj.user = c
            obj.schedule = s
            obj.save()
            messages.info(request,"Appointment is successfully booked")
            return redirect("view_appointment")
    return render(request,"customer/take_appointment.html",{"s":s})

# customer can book appointment of worker

def view_appointment(request):
    c = Register.objects.get(user = request.user)
    a = Take_Appointment.objects.filter(user=c)
    return render(request,"customer/view_appointment.html",{"a":a})

# here customer can see the details of appointment

def customer_view_payment_details(request):
    u = Register.objects.get(user=request.user)
    a = Bill.objects.filter(name=u)
    return render(request, 'customer/customer_view_payment_details.html', {'a': a})

# here customer can see the payment details and can either pay online or pay direct if admin has generated bill

def creditcard_add(request):
    form = CreditCardForm()
    u = request.user
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user=u
            obj.save()
            return redirect("view_creditcard")
    return render(request,"customer/creditcard_add.html",{"form":form})

def view_creditcard(request):
    data = CreditCard.objects.all()
    print(data)
    return render(request, "customer/view_creditcard.html", {"data": data})


def pay_bill(request,id):
    bi = Bill.objects.get(id=id)
    form = CreditCardForm()

    if request.method == 'POST':
        card = request.POST.get('card')
        c = request.POST.get('cvv')
        da = request.POST.get('exp.')
        CreditCard(card_no=card, card_cvv=c, expiry_date=da).save
        bi.status = 1
        bi.save()
        messages.info(request, "Bill paid successfully")
        return redirect("view_bill")
    return render(request, "customer/pay_bill.html",{'form': form})

# here when customer chooses PAY ONLINE option then you will get to pay bill using card number , cvv and month and after submitting , it will be paid


def direct_payment(request,id):
    bi =Bill.objects.get(id=id)
    bi.status = 2
    bi.save()
    messages.info(request,"Choose to Pay fee directly")
    return redirect("customer_view_payment_details")

 # here when customer chooses PAY DIRECT option...directly the payment will be paid

def bill_history(request):
    u = Register.objects.get(user=request.user)
    bill = Bill.objects.filter(name=u, status__in=[1, 2])
    return render(request,"customer/customer_view_bill_history.html", {'bill':bill})

# here only paid customers data will be shown....


##################worker######################

def workers(request):
    return render(request,"worker/workers.html")

def workerbase(request):
    return render(request,"worker/worker base.html")

def worker_registration(request):
    form1 = Login_Form()
    form2 = Register_Form1()
    if request.method == "POST":
        form1 = Login_Form(request.POST)
        form2 = Register_Form1(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            a = form1.save(commit=False)
            a.is_worker = True
            a.save()
            user1 = form2.save(commit=False)
            user1.user = a
            user1.save()
            return redirect("login_page")
    return render(request,"worker/workers.html", {'form1':form1,'form2':form2})





def schedules(request):
    form = ScheduleForm()
    # u = request.user
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.worker=Register1.objects.get(user=request.user)
            obj.save()
            return redirect("view_schedule")
    return render(request,"worker/schedules.html",{"form":form})

#  this is used to add schedules of workers

def worker_view_schedule(request):
    n = Schedule.objects.all
    return render(request, "worker/worker_view_schedule.html",{"view_schedule":n})

# this is used to view schedules of the worker


def delete_work_view(request,id):
    wm = work.objects.get(id=id)
    wm.delete()
    return redirect("work_view")

# this is used to delete work provided by admin

def worker_view_appointment(request):

    # b= Register1.objects.get(user=request.user)
    # print(b)
    # print("hii")
    # d=Schedule.objects.filter(worker=b)
    # print(d)
    # a = Take_Appointment.objects.filter(status=1)
    # print(a)
    # b = a.objects.get(user=request.user)

    c = request.user
    print(c)
    s = Schedule.objects.filter(worker__name=c)
    print(s)

    for i in s:
        app = []
        print(i)

        app = Take_Appointment.objects.filter(schedule=i)
        return render(request,"worker/worker_view_appointment.html",{"b":app})

def worker_view_workers_data(request):
    data = Register1.objects.all()
    print(data)
    return render(request,"worker/worker_view_workers_data.html",{'data':data})

def update_worker_data(request,id):
    a = Register1.objects.get(id=id)
    form = Register_Form(instance=a)
    if request.method == 'POST':
        form = Register_Form(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect("worker_view_workers_data")

    return render(request, "worker/update_worker_data.html", {'form': form})


