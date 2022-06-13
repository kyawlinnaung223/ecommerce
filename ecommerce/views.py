from django.shortcuts import render

# Create your views here.


#start storepageview
def storepage(request):
    return render(request,'store/store.html')

#end storepageview


#start cartpageview
def cartpageview(request):
    return render(request,'store/cart.html')
#end cartpageview



#start checkoutpageview
def checkoutpageview(request):
    return render(request,'store/checkout.html')
#end checkoutpageview


