from django.shortcuts import render
from projects.models import Components, Category
# Create your views here.
def category_list(request):
	category_list = Category.objects.all()
	return render(request, "index.html", {"Category":category_list})