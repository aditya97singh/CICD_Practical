import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_dummy():
    assert 1 == 1