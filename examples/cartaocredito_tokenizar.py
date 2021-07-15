# -*- coding: utf-8 -*-
import json
import junopy
import sys


def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E',
                '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    cartao_credito = junopy.creditcard.Tokenize(hash="0210da66-6c54-4f3b-9e95-9e044be38d79")


if __name__ == "__main__":
    main(sys.argv)
