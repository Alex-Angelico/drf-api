from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Jets

# Create your tests here.

class JetTests(TestCase):

  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(username='testuser1', password='password',)
    testuser1.save()

    jet_fighter = Jets.objects.create(
      name = 'F-35',
      country_origin = 'USA',
      description = 'Multirole fighter/bomber',
      engine_count = 1,
      added_by = testuser1
    )


  def test_jet_fighter(self):
      jet = Jets.objects.get(id=1)
      actual_name = str(jet.name)
      actual_country_origin = str(jet.country_origin)
      actual_description = str(jet.description)
      actual_engine_count = str (jet.engine_count)
      actual_added_by = str(jet.added_by)
      self.assertEqual(actual_name, 'F-35')
      self.assertEqual(actual_country_origin, 'USA')
      self.assertEqual(actual_description, 'Multirole fighter/bomber')
      self.assertEqual(actual_engine_count, '1')
      self.assertEqual(actual_added_by, 'testuser1')