from django.urls import path

from online_home_service_app import views

urlpatterns =[
    path("",views.index,name="index"),
    path("login_page",views.login_page,name="login_page"),
    path("indexx",views.indexx,name="indexx"),


    ##############ADMIN#############

    path("base", views.adminbase, name="base"),
    path("feedbacks", views.feedbacks, name="feedbacks"),
    path("reply_feedback/<int:id>/", views.reply_feedback, name="reply_feedback"),
    path("view_schedule",views.view_schedule,name="view_schedule"),
    path("work_add", views.work_add, name="work_add"),
    path("work_view",views.work_view,name="work_view"),
    path("update_work_view/<int:id>/", views.update_work_view, name="update_work_view"),
    path("admin_view_appointment", views.admin_view_appointment, name="admin_view_appointment"),
    path("approve_appointment/<int:id>/", views.approve_appointment, name="approve_appointment"),
    path("reject_appointment/<int:id>/", views.reject_appointment, name="reject_appointment"),
    path("bill", views.bill, name="bill"),
    path("view_bill", views.view_bill, name="view_bill"),
    path("customer_view_payment_details", views.customer_view_payment_details, name="customer_view_payment_details"),
    path("customers_data", views.customers_data, name="customers_data"),
    path("delete_it/<int:id>/", views.delete_it, name="delete_it"),
    path("workers_data", views.workers_data, name="workers_data"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("update/<int:id>/", views.update, name="update"),

    ###############CUSTOMER##############
    path("customers", views.customers, name="customers"),
    path("customerbase", views.customerbase, name="customerbase"),
    path("customer_registration", views.customer_registration, name="customer_registration"),
    path("feedback", views.feedback, name="feedback"),
    path("view",views.view,name="view"),
    path("del_feedback/<int:id>/",views.del_feedback,name="del_feedback"),
    path("customer_view_schedule",views.customer_view_schedule,name="customer_view_schedule"),
    path("delete_schedule/<int:id>/", views.delete_schedule, name="delete_schedule"),
    path("view_worker", views.view_worker, name="view_worker"),
    path("take_appointment/<int:id>/", views.take_appointment, name="take_appointment"),
    path("view_appointment", views.view_appointment, name="view_appointment"),
    path("creditcard_add", views.creditcard_add, name="creditcard_add"),
    path("view_creditcard", views.view_creditcard, name="view_creditcard"),
    path("pay_bill/<int:id>", views.pay_bill, name="pay_bill"),
    path("direct_payment/<int:id>", views.direct_payment, name="direct_payment"),
    path("bill_history", views.bill_history, name="bill_history"),


    #############WORKER#######
  path("workers" ,views.workers ,name="workers"),
  path("workerbase", views.workerbase, name="workerbase"),
  path("worker_registration", views.worker_registration, name="worker_registration"),
  path("workers_data", views.workers_data, name="workers_data"),
  path("update_worker_data/<int:id>/", views.update_worker_data, name="update_worker_data"),
  path("worker_view_workers_data", views.worker_view_workers_data, name="worker_view_workers_data"),
  path("schedules" ,views.schedules ,name="schedules"),
  path("worker_view_schedule" ,views.worker_view_schedule ,name="worker_view_schedule"),
  path("delete_work_view/<int:id>/" ,views.delete_work_view ,name="delete_work_view"),
  path("worker_view_appointment", views.worker_view_appointment, name="worker_view_appointment"),
    path("edit_profile", views.edit_profile, name="edit_profile"),

]