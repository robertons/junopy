# -*- coding: utf-8 -*-
import junopy
import json
import sys


def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # ESTORNO TOTAL
    estorno = junopy.payment.Refund(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08')

    # ESTORNO PARCIAL
    estorno = junopy.payment.Refund(paymentId='pay_BDBBF5F40B8B94F23DB2117904EB4B08', amount=40.0)


if __name__ == "__main__":
    main(sys.argv)
