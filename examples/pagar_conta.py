# -*- coding: utf-8 -*-


import json
import sys
sys.path.append('/Users/robertoneves/Projetos/junopy')

import junopy

def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    # PLANO
    pagamento_conta = junopy.Bill(
        numericalBarCode="00190500954014481606906809350314337370000001000",
        paymentDescription="Boleto Bancário",
        beneficiaryDocument="CPF",
        dueDate="2021-07-14",
        paymentDate="2021-07-13",
        billAmount=10.00,
        paidAmount=10.00,
    ).Create()

    print(pagamento_conta.toJSON())


if __name__ == "__main__":
    main(sys.argv)
