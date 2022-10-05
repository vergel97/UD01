DIANACIMIENTO = 24
MESNACIMIENTO = 9
AÑO_NACIMIENTO = 2005
DIA_ACTUAL = 30
MES_ACTUAL = 9
AÑO_ACTUAL = 2022
print("w", True if AÑO_NACIMIENTO + 18 < AÑO_ACTUAL else False or True if AÑO_NACIMIENTO + 18 == AÑO_ACTUAL and MESNACIMIENTO ==MES_ACTUAL and DIANACIMIENTO <= DIA_ACTUAL else False or True if AÑO_NACIMIENTO + 18 == AÑO_ACTUAL and MESNACIMIENTO <MES_ACTUAL  else False )
#necesitamos hacer 3 operadores ternarios ya que hay 3 posibilidades:
# 1 que ya hayas cumplido años en un año anterior.

# True if AÑO_NACIMIENTO + 18 < AÑO_ACTUAL else False 
 
            #or

# 2 Que cumplas años este mismo año , en el mes en el que estamos y por tanto.
#  el dia tenga que coincidir o ser superior al actual.

#True if AÑO_NACIMIENTO + 18 == AÑO_ACTUAL and MESNACIMIENTO ==MES_ACTUAL and DIANACIMIENTO <= DIA_ACTUAL else False

                  #or


# 3 Que cumplas años este mismo año pero ya hayas cumplido en otro mes anterior al actual.
 
 #True if AÑO_NACIMIENTO + 18 == AÑO_ACTUAL and MESNACIMIENTO <MES_ACTUAL  else False