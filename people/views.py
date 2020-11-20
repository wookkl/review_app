from django.views.generic import ListView
from people import models as person_models


class PersonListView(ListView):

    """ Person List View Definition """

    model = person_models.Person
    paginate_by = 10
    paginate_orphans = 5
    template_name = "people/people_list.html"
    ordering = ("pk",)
