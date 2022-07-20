from datetime import datetime
from typing import List

from ampa_members_manager.charge.models.activity_remittance import ActivityRemittance
from ampa_members_manager.charge.receipt import Receipt
from ampa_members_manager.charge.remittance import Remittance


class RemittanceGenerator:
    def __init__(self, activity_remittance: ActivityRemittance):
        self.__activity_remittance: ActivityRemittance = activity_remittance
        self.__name: str = str(activity_remittance) + '_' + datetime.now().strftime("%Y%m%d_%H%M%S")

    def generate(self) -> Remittance:
        receipts: List[Receipt] = []
        for activity_receipt in self.__activity_remittance.activityreceipt_set.all():
            receipts.append(activity_receipt.generate_receipt())
        return Remittance(receipts, self.__name)
