from django.test import TestCase
from django.db import InternalError, IntegrityError

from .models import Offer

class OfferTest(TestCase):
    def test_term_min_lt_term_max(self):
        with self.assertRaisesMessage(IntegrityError, 'mortgage_offer_terms_min_lt_terms_max'):
            Offer.objects.create(bank_name='bank_1',
                                 term_min=21,
                                 term_max=20)

    def test_rate_min_lt_rate_max(self):
        with self.assertRaisesMessage(IntegrityError, 'mortgage_offer_rate_min_lt_rate_max'):
            Offer.objects.create(bank_name='bank_1',
                                 rate_min = 2.2,
                                 rate_max = 2.1)

    def test_payment_min_lt_payment_max(self):
        with self.assertRaisesMessage(IntegrityError, 'mortgage_offer_payment_min_lt_payment_max'):
            Offer.objects.create(bank_name='bank_1',
                             payment_min=5000000,
                             payment_max=4000000)
