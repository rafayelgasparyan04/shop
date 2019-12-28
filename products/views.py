from django.shortcuts import render
from .models import product, categories
from django.http import HttpResponseRedirect

# Create your views here.
def products_all(request):
	pr=product.objects.all()
	ct=categories.objects.all()
	return render(request, 'products/all.html', {'prod':pr,'categ':ct})

def cat_set(request, cat):
	pr=product.objects.filter(category=cat)
	ct=categories.objects.all()
	return render(request, 'products/all.html', {'prod':pr,'categ':ct})

def prd_det(request, prd):
	pr=product.objects.get(slug=prd)
	return render(request, 'products/about_prod.html',{'prod':pr})

def rate_prd(request, prd, rt):
	pr=product.objects.get(slug=prd)
	pr.rate_count+=1
	pr.rate_all+=int(rt)
	pr.rate=pr.rate_all/pr.rate_count
	pr.save()
	pr=product.objects.get(slug=prd)
	temp='/products/'+str(prd)
	return HttpResponseRedirect(temp)

def products_best(request):
	pr=product.objects.filter(best=True)
	ct=categories.objects.all()
	return render(request, 'products/all.html', {'prod':pr,'categ':ct})
