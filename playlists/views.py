from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Case, When

from playlists.models import Track
from playlists.algorithms import merge_sort

ORDERING_CRITERIA_DICT = {
    "nome": "name",
    "popularidade": "popularity",
    "duração": "duration",
    "artistas": "artists"
}

class HomePageView(TemplateView):
    template_name = "home.html"


class TrackListView(ListView):
    template_name = "track_list.html"
    category = None
    paginate_by = 6

    def get_queryset(self):
        if "ordering" in self.request.GET and self.request.GET["ordering"] in ["nome", "popularidade", "duração", "artistas"]:
            ordering_criteria = self.request.GET["ordering"]
            track_list = list(
                Track.objects.all().values_list(
                    ORDERING_CRITERIA_DICT[ordering_criteria], "id"
                )
            )
            merge_sort(track_list)

            preserved_ordering = Case(*[When(pk=pk, then=i) for i, (pos, pk) in enumerate(track_list)])
            pk_list = [pk for value, pk  in track_list]
            queryset = Track.objects.filter(pk__in=pk_list).order_by(preserved_ordering)

            return queryset
        else:
            popularity_list = list(
                Track.objects.all().values_list(
                    ORDERING_CRITERIA_DICT["popularidade"], "id"
                )
            )
            merge_sort(popularity_list)

            preserved_ordering = Case(*[When(pk=pk, then=i) for i, (pos, pk) in enumerate(popularity_list)])
            pk_list = [pk for value, pk  in popularity_list]
            queryset = Track.objects.filter(pk__in=pk_list).order_by(preserved_ordering)

            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ordering_criteria = ["nome", "popularidade", "duração", "artistas"]
        context["ordering_criteria"] = ordering_criteria
        if "ordering" in self.request.GET and self.request.GET["ordering"] in ["nome", "popularidade", "duração", "artistas"]:
            context["ordering"] = self.request.GET["ordering"]
        else:
            context["ordering"] = "popularidade"
        return context
