from django.shortcuts import render, redirect, get_object_or_404
from .forms import ItemModel, ItemForm


# render home
def index(request):
    all_items = ItemModel.objects.all()
    form = ItemForm(request.POST or None)

    if request.method == 'POST':
        form.save()
        return redirect('index')

    context = {
        'all_items': all_items,
        'form': form
    }
    return render(request, 'BootCRUDApp/index.html', context)


# edit item
def editItem(request, ID):
    selected_item = get_object_or_404(ItemModel, pk=ID)
    edit_item = ItemForm(request.POST or None, instance=selected_item)
    if edit_item.is_valid():
        edit_item.save()
        return redirect('index')
    context = {
        'form': edit_item
    }
    return render(request, 'BootCRUDApp/edit.html', context)
