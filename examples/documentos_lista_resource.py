#-*- coding: utf-8 -*-
import sys
import junopy

def main(arg):

    junopy.Juno('4E1574938F3DD69306BC336E348276ACC9CBE72B4E8396B2520436663C66C08E', '9OuOfYM2QZRhmUug', 'gw<Nl6bc2Ib,VX&)c2U{mX1?d_zEg0^d', sandbox=True)

    documentos_esperados = junopy.Document(resourceToken='8A596ED1DEB738091FDE8AF11CCD6E7730970A95503AB32CEA340FAB190139C9').Get()
    print(documentos_esperados.toJSON())


if __name__ == "__main__":
    main(sys.argv)
