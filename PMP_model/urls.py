"""PMP_model URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from mng import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.main),
    path('Search',views.Search,name='dataSearch'),
    path('Customers',views.customer,name="Customers"),
    path('ViewAllCustomer',views.customerview,name="customerview"),
    path("customerdelete/<int:id>",views.customerdelete),
    path("restorcus/<int:id>",views.restorcus),
    path("customerdlt/<int:id>",views.customerdlt),
    path('products',views.products,name="product"),
    path('ViewAllProduct',views.productview,name="productview"),
    path("Purchase",views.Purchase,name="Purchase"),
    path("Sales",views.salles,name="Sales"),
    path("DailystatusS",views.salesdata,name="salesdata"),
    path("Amount",views.amount, name="amount"),
    path("AllAmount",views.allamount, name="allamount"),
    path("testd",views.testdata, name="testd"),
    path("DailystatusP_E",views.dailystatusP_E, name="DailystatusP_E"),
    path("Dailystatus",views.dailystatus01, name="Dailystatus"),
    path("stock",views.stock01, name="stock"),
    path("stckDetails/<str:product_name>/<int:rate>",views.stckDetails, name="stckDetails"),
    path("amout0",views.amout0, name="amout0"),
    path("Expenses",views.expens, name="Expenses"),
    path('ViewAllExpenses',views.expensesview,name="expensesview"),
    path('expdelete/<int:id>',views.expdelete,name='dltexp'),
    path("Details/<int:id>",views.details, name="Details"),  
    path("Deleted",views.deleted, name="deleted"),  
    path("prodDetails/<int:id>",views.prodDetails, name="prodDetails"),
    path("amountdelete/<int:id>",views.amountdelete),
    path("deleteprod/<int:id>",views.deleteprod),
    path("restorpro/<int:id>",views.restorpro),
    path("restoramt/<int:id>",views.restoramt),
    path("restorexp/<int:id>",views.restorexp),
    path("pdelete/<int:id>",views.pdelete),
    path("expdlt/<int:id>",views.expdlt),
    path("amountdlt/<int:id>",views.amountdlt),
    path("resetd",views.resetdata, name="resetdata"),
    path("dltpro",views.dltpro, name="deleteproduct"),
    path("dltamt",views.dltamt, name="deleteamount"),
    path("dltcus",views.dltcus, name="deletecustomer"),
    path("dltexp",views.dltexp, name="deleteexpans"),
    # signup view 
    path('signup',views.signup,name='signup'),
    # login view
    path('login', LoginView.as_view(template_name='admin/signin.html'),name='login'),
    # logout view
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    # signin view
    path('signin',LoginView.as_view(template_name='log.html'),name='signin'),

]

handler404='mng.views.error_404_view'

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)