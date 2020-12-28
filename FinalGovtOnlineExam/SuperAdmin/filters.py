from django.contrib.auth.models import User
import django_filters
from django import forms
from django.contrib.auth import get_user_model

from SuperAdmin.models import Ministry

User = get_user_model()


class GovtUserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    MinistryName = django_filters.ModelMultipleChoiceFilter(queryset=Ministry.objects.all(),
                                                            widget=forms.CheckboxSelectMultiple
                                                            )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','MinistryName']