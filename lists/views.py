from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

def home_page(request):

#    if request.method == 'POST':
 #       Item.objects.create(text = request.POST['item_text'])
  #      return redirect('/lists/the-only-list-in-the-world/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))

def add_item(request, list_id):
    list_= List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))