from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    MembershipSelectView,
    PaymentView,
    updateTransactionRecords,
    profile_view,
    cancelSubscription
)

app_name = 'membership'

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', PaymentView, name='payment'),
    path('update-transactions/<subscription_id>/',
         updateTransactionRecords, name='update-transactions'),
    path('profile/', profile_view, name='profile'),
    path('cancel/', cancelSubscription, name='cancel')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)