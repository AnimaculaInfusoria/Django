from django.shortcuts import render
from wagtail.search.models import Query
from wagtail.core.models import Page
from django.views.generic.edit import FormView



def search(request):
   
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    
    return render(request, 'search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
    })



class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)