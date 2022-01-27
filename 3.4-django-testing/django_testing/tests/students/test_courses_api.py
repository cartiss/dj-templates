import pdb

import pytest
from model_bakery import baker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_301_MOVED_PERMANENTLY, HTTP_204_NO_CONTENT
from rest_framework.test import APIClient

from students.models import Course


@pytest.fixture
def api_client():
    """API клиента"""
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make("Student", **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make("Course", **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(api_client, student_factory, course_factory):
    course = course_factory(name='Test')
    url = 'http://127.0.0.1:8000/api/v1/courses/1/'
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert response.data['name'] == 'Test'


@pytest.mark.django_db
def test_get_list_of_courses(api_client, course_factory):
    course = course_factory(name='Test', _quantity=1)
    url = 'http://127.0.0.1:8000/api/v1/courses/'
    response = api_client.get(url)
    response_json = response.json()
    assert response.status_code == HTTP_200_OK
    assert response_json[0] == {'id': 2, 'name': 'Test', 'students': []}


@pytest.mark.django_db
def test_course_filter_by_id(api_client, course_factory):
    url = 'http://127.0.0.1:8000/api/v1/courses/?id=1'
    course = course_factory(id=1)
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert response.json()[0]['id'] == course.id


@pytest.mark.django_db
def test_course_filter_by_name(api_client, course_factory):
    url = 'http://127.0.0.1:8000/api/v1/courses/?name=Test1'
    course = course_factory(name='Test1')
    response = api_client.get(url)
    assert response.status_code == HTTP_200_OK
    assert response.json()[0]['name'] == course.name


@pytest.mark.django_db
def test_create_course(api_client):
    data = {
        'name': 'TestCreate',
        'students': []
    }
    url = 'http://127.0.0.1:8000/api/v1/courses/'
    response = api_client.post(url, data)
    assert response.status_code == HTTP_201_CREATED
    assert response.json()['name'] == data['name']


@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    course = course_factory(name='TestCreate1')
    data = {
        'name': 'TestUpdate',
        'students': []
    }
    url = f'http://127.0.0.1:8000/api/v1/courses/{course.id}/'
    response = api_client.put(url, data)
    assert response.status_code == HTTP_200_OK
    assert response.json()['name'] == data['name']


@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory(name='TestCreate1')
    url = f'http://127.0.0.1:8000/api/v1/courses/{course.id}/'
    response = api_client.delete(url)

    assert response.status_code == HTTP_204_NO_CONTENT


