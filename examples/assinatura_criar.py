# -*- coding: utf-8 -*-
import junopy
import json
import sys


def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # DESATIVAR
    assinatura = junopy.Subscription(
        dueDay=10,
        planId='pln_76A6AC4929EF068B',
        chargeDescription='Assinatura Recorrente Plano de Teste',
        creditCardDetails=junopy.CreditCard(
            creditCardId='9a453d71-3ec1-44a5-b2f3-0596ced42a35'
        ),
        billing=junopy.Billing(
            name='Usuario Teste',
            document='CPF/CNPJ',
            email='usuario@email.com.br',
            address=junopy.Address(
                street='Rua',
                number='Numero',
                complement='Complemento',
                neighborhood='Bairro',
                city='Cidade',
                state='UF',
                postCode='99999999')),
        notify=False
    ).Create()


if __name__ == "__main__":
    main(sys.argv)
