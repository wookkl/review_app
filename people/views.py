from django.http import Http404
from django.views.generic import ListView
from people import models as person_models


class PersonListView(ListView):

    """ Person List View Definition """

    model = person_models.Person
    paginate_by = 10
    paginate_orphans = 5
    template_name = "people/people_list.html"
    ordering = ("pk",)

    def get_context_data(self, **kwargs):
        try:
            return super(PersonListView, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs["page"] = 1
            return super(PersonListView, self).get_context_data(**kwargs)
