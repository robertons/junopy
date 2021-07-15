# -*- coding: utf-8 -*-
import junopy
import uuid
import json
import sys


def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # PLANO
    pix = junopy.pix.StaticQRCode(
        idempotency='d63313cd-d01a-4091-b352-182a0a96baca',
        key='06c4e6fe-48cb-4263-89a3-c8bc342ce65e',
        includeImage=True,
        amount=100.00,
        reference='Teste de Pix',
        additionalData='Teste de Pix com Dados Adicionais')


if __name__ == "__main__":
    main(sys.argv)
