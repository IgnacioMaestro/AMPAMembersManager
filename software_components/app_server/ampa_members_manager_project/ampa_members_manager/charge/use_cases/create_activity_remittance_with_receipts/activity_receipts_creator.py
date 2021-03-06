from typing import List

from ampa_members_manager.activity_registration.models.activity_registration import ActivityRegistration
from ampa_members_manager.charge.models.activity_receipt import ActivityReceipt, NotFound
from ampa_members_manager.charge.models.activity_remittance import ActivityRemittance


class ActivityReceiptsCreator:
    def __init__(self, activity_remittance: ActivityRemittance):
        self.__activity_remittance: ActivityRemittance = activity_remittance

    def create(self):
        activity_registrations: List[ActivityRegistration] = []
        for payable_part in self.__activity_remittance.payable_parts.all():
            activity_registrations.extend(ActivityRegistration.with_payable_part(payable_part=payable_part))
        for activity_registration in activity_registrations:
            self.create_receipt_for_activity_registration(activity_registration)

    def create_receipt_for_activity_registration(self, activity_registration: ActivityRegistration):
        activity_receipt: ActivityReceipt = self.find_or_create_receipt(activity_registration)
        price: float = activity_registration.payable_part.calculate_price(
            times=activity_registration.amount, membership=activity_registration.is_membership())
        activity_receipt.amount = activity_receipt.amount + price
        activity_receipt.activity_registrations.add(activity_registration)
        activity_receipt.save()

    def find_or_create_receipt(self, activity_registration: ActivityRegistration) -> ActivityReceipt:
        try:
            return ActivityReceipt.find_activity_receipt_with_bank_account(
                activity_remittance=self.__activity_remittance, bank_account=activity_registration.bank_account)
        except NotFound:
            return ActivityReceipt.objects.create(remittance=self.__activity_remittance, amount=0.0)
