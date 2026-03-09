import pytest
from movies.models import Movie

@pytest.mark.django_db
def test_movie_is_completed():
    movie = Movie.objects.create(
        title="Test Movie",
        duration=120
    )

    assert movie.duration > 0