from typing import List

from django.test import TestCase
from model_bakery import baker

from ampa_members_manager.academic_course.models.academic_course import AcademicCourse
from ampa_members_manager.academic_course.models.established_course import EstablishedCourse
from ampa_members_manager.activity.models.single_activity import SingleActivity
from ampa_members_manager.activity_registration.generate_payment_orders import GeneratePaymentOrders
from ampa_members_manager.activity_registration.models.activity_registration import ActivityRegistration
from ampa_members_manager.family.models.child import Child


class TestGeneratePaymentOrders(TestCase):
    def setUp(self):
        self.academic_course: AcademicCourse = baker.make('AcademicCourse')
        EstablishedCourse.objects.create(course=self.academic_course)
        self.single_activity: SingleActivity = baker.make('SingleActivity')

    def test_generate_payment_orders_no_activity_registration(self):
        GeneratePaymentOrders.generate(self.single_activity)
        self.assertEqual(ActivityRegistration.objects.count(), 0)

    def test_generate_payment_orders_one_activity_registration(self):
        child: Child = baker.make('Child')
        activity_registration: ActivityRegistration = baker.make(
            'ActivityRegistration',
            registered_child=child, registered_family=None, single_activity=self.single_activity, amount=2.5)
        GeneratePaymentOrders.generate(self.single_activity)
        activity_registration.refresh_from_db()
        self.assertIsNotNone(activity_registration.payment_order)

    def test_generate_payment_orders_more_than_one_activity_registration(self):
        child: Child = baker.make('Child')
        activity_registrations: List[ActivityRegistration] = baker.make(
            'ActivityRegistration',
            registered_child=child, registered_family=None, single_activity=self.single_activity, amount=2.5,
            _quantity=3)
        GeneratePaymentOrders.generate(self.single_activity)
        for activity_registration in activity_registrations:
            activity_registration.refresh_from_db()
            self.assertIsNotNone(activity_registration.payment_order)