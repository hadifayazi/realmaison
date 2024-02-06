from django.db import models
from django.utils.translation import gettext_lazy as _
from realmaisonAPI.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile


class Rating(models.Model):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              related_name="ratings", verbose_name=_("Rater"), null=True,)
    agent = models.ForeignKey(Profile, on_delete=models.SET_NULL, verbose_name=_(
        'Agent being rated'), related_name="agent_review", null=True)
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices,
                                 help_text=_("1=Poor 2=Fair 3=Good 4=Very Good 5=Excellent"), default=0)
    comment = models.TextField(verbose_name=_("Comment"), default="", blank=True, null=True)

    class Meta:
        unique_together = (("rater", "agent"),)

    def __str__(self):
        return f"{self.agent} rated {self.rating}"
