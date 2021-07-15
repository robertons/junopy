
from junopy.utils import juno
from junopy import PaymentResource, CreditCard, Billing
from junopy.entities.lib.datatype import ListType


def Create(chargeId: str, creditcard: CreditCard, billing: Billing):
    data = juno.Post("/payments", {
        'chargeId': chargeId,
        'billing': {
            'email': billing.email,
            'address': billing.address.toJSON(),
            'delayed': billing.delayed
        },
        'creditCardDetails': {
            'creditCardId': creditcard.creditCardId,
            'creditCardHash': creditcard.creditCardHash
        }
    })
    return PaymentResource(**data)


def Refund(paymentId: str, amount: float = 0, split: list = []):
    data = {}

    if amount > 0:
        data['amount'] = amount

    split = [item if isinstance(item, dict) else item.toJSON() for item in split]
    if len(split) > 0:
        data['split'] = split

    data = juno.Post(f"/payments/{paymentId}/refunds", data)

    return PaymentResource(**data)


def Capture(paymentId: str, amount: float = 0):
    data = {}

    if amount > 0:
        data['amount'] = amount

    data = juno.Post(f"/payments/{paymentId}/capture", data)

    return PaymentResource(**data)
