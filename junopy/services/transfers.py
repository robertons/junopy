
from junopy.utils.juno import *
from junopy import Transfer, BankAccount


def Default(amount: float):
    __transfer = Transfer(**{
        "type": "DEFAULT_BANK_ACCOUNT",
        "amount": amount
    })
    return __transfer.Create()


def P2P(name: str, document: str, amount: float, accountNumber: str):
    __transfer = Transfer(**{
        "type": "P2P",
        "name": name,
        "document": document,
        "amount": amount,
        "bankAccount": {"accountNumber":  accountNumber}
    })
    return __transfer.Create()


def Bank(name: str, document: str, amount: float, bank: BankAccount):
    __transfer = Transfer(**{
        "type": "BANK_ACCOUNT",
        "name": name,
        "document": document,
        "amount": amount,
        "bankAccount": bank
    })
    return __transfer.Create()


def Pix(name: str, document: str, amount: float, bank: BankAccount):
    __transfer = Transfer(**{
        "type": "PIX",
        "name": name,
        "document": document,
        "amount": amount,
        "bankAccount": bank
    })
    return __transfer.Create()
