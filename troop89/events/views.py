from django.utils.timezone import now
from django.views import generic

from troop89.date_range.views import DayDateRangeView, MonthDateRangeView
from .models import Event
from .util import EventCalendar


class CalendarMonthView(MonthDateRangeView):
    model = Event
    allow_empty = True
    allow_future = True
    template_name = 'events/calendar_month.html'
    date_field_start = 'start'
    date_field_end = 'end'

    def get_context_data(self, *, object_list=None, **kwargs):
        year = self.get_year()
        month = self.get_month()
        if object_list is None:
            object_list = []

        calendar = EventCalendar(year, month, object_list)
        context = super().get_context_data(**kwargs)
        context['calendar'] = calendar

        return context


class EventMonthView(MonthDateRangeView):
    model = Event
    allow_empty = True
    allow_future = True
    date_field_start = 'start'
    date_field_end = 'end'
    context_object_name = 'events'


class EventDayView(DayDateRangeView):
    model = Event
    allow_empty = True
    allow_future = True
    date_field_start = 'start'
    date_field_end = 'end'
    context_object_name = 'events'


class EventDetailView(generic.DetailView, generic.dates.BaseDateDetailView):
    model = Event
    date_field = 'start'
    allow_future = True


class RedirectCurrentMonth(generic.RedirectView):
    permanent = False
    pattern_name = "events:calendar-month"

    def get_redirect_url(self, *args, **kwargs):
        today = now().date()
        return super().get_redirect_url(year=today.year, month=today.month)
