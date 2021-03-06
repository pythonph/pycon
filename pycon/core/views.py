from django.db.models import Prefetch
from django.views.generic import TemplateView

from pycon.schedule.models import ProgramSchedule
from pycon.speakers.models import Speaker
from pycon.sponsors.models import Sponsor, SponsorType


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['keynote_speakers'] = Speaker.objects.filter(
            speaker_type=Speaker.KEYNOTE,
            is_active=True,
        ).distinct()

        context['regular_speakers'] = Speaker.objects.filter(
            speaker_type=Speaker.NORMAL,
            is_active=True,
        ).distinct()

        # There will always only be two instances of this model
        schedule = ProgramSchedule.objects.all()

        context['program_left_tab'] = (
            schedule.get(tab_position=ProgramSchedule.LEFT)
            if schedule.filter(tab_position=ProgramSchedule.LEFT).exists()
            else None
        )
        context['program_right_tab'] = (
            schedule.get(tab_position=ProgramSchedule.RIGHT)
            if schedule.filter(tab_position=ProgramSchedule.RIGHT).exists()
            else None
        )

        context['sponsor_types'] = (
            SponsorType.objects
            .filter(is_active=True)
            .prefetch_related(
                Prefetch(
                    'sponsor_set',
                    queryset=Sponsor.objects.filter(is_active=True),
                    to_attr='sponsors',
                )
            )
        )

        return context


home_page_view = HomePageView.as_view()
