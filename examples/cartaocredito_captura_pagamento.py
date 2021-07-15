# -*- coding: utf-8 -*-
import json
import sys

sys.path.append('/Users/robertoneves/Projetos/junopy')

import junopy

def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # CAPTURA TOTAL
    captura = junopy.payment.Capture(paymentId='pay_CA371C55F02F0F83D2D36AFA4142F7F2')

    print(captura.toJSON())

if __name__ == "__main__":
    main(sys.argv)
