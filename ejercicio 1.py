donacion = input ("coloque su donacion")

tele = donacion*0.10;
sistemas = donacion*0.25;
administracion = donacion*0.35;
contabilidad = donacion-(tele + sistemas + administracion)

print 'Resultado final de las donaciones es: ' ,tele, sistemas, administracion, contabilidad