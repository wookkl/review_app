from django.http import Http404
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.views.generic import DetailView
from people import models as person_models
from users import mixins as user_mixins


class PersonList(ListView):

    """ Person List View Definition """

    model = person_models.Person
    paginate_by = 10
    paginate_orphans = 5
    template_name = "people/list.html"
    ordering = "-created"

    def get_context_data(self, **kwargs):
        try:
            return super(PersonList, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs["page"] = 1
            return super(PersonList, self).get_context_data(**kwargs)


class PersonDetail(DetailView):

    """ Detail Person View Definition """

    model = person_models.Person
    template_name = "people/detail.html"


class PersonEdit(user_mixins.LoggedInOnlyView, UpdateView):

    """ Person Edit View Definition """

    model = person_models.Person
    template_name = "people/edit.html"
    fields = (
        "name",
        "kind",
        "photo",
    )


class PersonCreate(user_mixins.LoggedInOnlyView, CreateView):

    """ Person Create View Definition """

    model = person_models.Person
    template_name = "people/create.html"
    fields = (
        "name",
        "kind",
        "photo",
    )
