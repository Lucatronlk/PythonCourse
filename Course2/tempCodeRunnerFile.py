def taxaMotor(capacitate):
     if capacitate < 1000:                                           
        return "Taxa este 100 ron"
     elif  capacitate > 1000 and capacitate < 2000:
        return "Taxa este 400 ron"
     elif capacitate > 2000 and capacitate < 4000:
        return "Taxa este 10000 ron"
     elif capacitate > 4000 and capacitate < 6000:
        return "Taxa este 15000 ron"
     else:
        return "Taxa este 25000 ron"
    
print(taxaMotor(2000))