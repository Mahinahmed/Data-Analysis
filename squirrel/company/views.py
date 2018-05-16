from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView


from company.models import Company, Review

@method_decorator(login_required, name='dispatch')
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'
    queryset = Company.objects.all()
    context_object_name = 'companies'
    it_companies = Company.objects.filter(type='IT')
    clothing_companies = Company.objects.filter(type='clothing')
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['it_companies'] = self.it_companies[:10]
        data['clothing_companies'] = self.clothing_companies[:10]
        return data

@method_decorator(login_required, name='dispatch')
class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'company_summery.html'
    queryset = Company.objects.all()
    context_object_name = 'company'
    it_companies = Company.objects.filter(type='IT')
    clothing_companies = Company.objects.filter(type='clothing')
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['it_companies'] = self.it_companies[:10]
        data['clothing_companies'] = self.clothing_companies[:10]
        data['reviews'] = Review.objects.filter(company=data['company']).order_by('-timestamp')
        return data

@method_decorator(login_required, name='dispatch')
class ReviewListView(ListView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'review_list.html'


@method_decorator(login_required, name='dispatch')

class ReviewCreateView(CreateView):
    template_name = 'review_create.html'
    model = Review
    def post(self, request, *args, **kwargs):

        val = dict(request.POST)
        val_dict = {key: value[0] for key, value in val.items()}
        print(val_dict)
        company = Company.objects.get(pk = val_dict['pk'])
        user = request.user
        del val_dict['csrfmiddlewaretoken']
        del val_dict['pk']
        val_dict.update({'user': user, 'company': company,
                         'rating': 2})

        self.model.objects.create(**val_dict)
        return self.get(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)


# @method_decorator(login_required, name='dispatch')
# class ReviewUpdateView(UpdateView):
#     form_class = ReviewUpdateForm
#     template_name = 'review_update.html'

@method_decorator(login_required, name='dispatch')
class ReviewDeleteView(DeleteView):
    model = Review
    queryset = Review.objects.all()
    template_name = 'review_delete.html'


