# -*- coding: utf-8 -*-
import json
import junopy
import sys


def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    conta = junopy.DigitalAccount(
        type="PAYMENT",
        name="Usuario Teste",
        motherName="Nome Mãe Usuario",
        monthlyIncomeOrRevenue=5000,
        document="00000000000",
        email="email@usuario.com.br",
        birthDate="1986-07-16",
        phone="99999999999",
        businessArea=2015,
        linesOfBusiness="Pessoa Física - Digital Influencer",
        address=junopy.Address(
            street='Rua',
            number='Numero',
            complement='Complemento',
            neighborhood='Bairro',
            city='Cidade',
            state='UF',
            postCode='29000000'),
        bankAccount=junopy.BankAccount(
            bankNumber="000",
            agencyNumber="0000",
            accountNumber="000000000",
            accountComplementNumber="0",
            accountType="CHECKING",
            accountHolder=junopy.AccountHolder(name="Usuario Teste", document='00000000000')),
        emailOptOut=False,
        autoTransfer=False,
        socialName=False
    )

    conta.Create()


if __name__ == "__main__":
    main(sys.argv)
