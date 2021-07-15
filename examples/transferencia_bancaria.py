# -*- coding: utf-8 -*-
import json
import junopy
import sys


def main(arg):
    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    transfer = junopy.transfers.Bank('Usuario Recebedor', 'CPF', 100.0,  junopy.BankAccount(
        bankNumber="000",
        agencyNumber="0000",
        accountNumber="000000000",
        accountComplementNumber="0",
        accountType="CHECKING"
    ))


if __name__ == "__main__":
    main(sys.argv)
