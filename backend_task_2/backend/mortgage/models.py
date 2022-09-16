from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q, F

class Offer(models.Model):

    bank_name = models.CharField(
        max_length=255,
        help_text='Название банка',
    )

    term_min = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10)],
        default=10,
        help_text='Срок ипотеки, от'
    )

    term_max = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(30)],
        default=30,
        help_text='Срок ипотеки, до'
    )

    rate_min = models.FloatField(
        validators=[MinValueValidator(1.8)],
        default=1.8,
        help_text='Ставка, от'
    )

    rate_max = models.FloatField(
        validators=[MaxValueValidator(9.8)],
        default=9.8,
        help_text='Cтавка, до'
    )

    payment_min = models.PositiveIntegerField(
        validators=[MinValueValidator(1000000)],
        default=1000000,
        help_text='Сумма кредита, от'
    )

    payment_max = models.PositiveIntegerField(
        validators=[MaxValueValidator(10000000)],
        default=10000000,
        help_text='Сумма кредита, до'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
        constraints = [
            models.CheckConstraint(
                name='mortgage_offer_terms_min_lt_terms_max',
                check=Q(term_min__lt=F('term_max'))
            ),

            models.CheckConstraint(
                name='mortgage_offer_rate_min_lt_rate_max',
                check=Q(rate_min__lt=F('rate_max'))
            ),

            models.CheckConstraint(
                name='mortgage_offer_payment_min_lt_payment_max',
                check=Q(payment_min__lt=F('payment_max'))
            )
        ]

    def __str__(self):
        return f"Offer №{self.id}"

