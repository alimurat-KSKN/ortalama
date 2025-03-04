def ortalama_hesapla(snv1,snv2,per1,per2):
    sonuc= (snv1+snv2+per1+per2)/4.0
    return sonuc

if ortalama_hesapla(100,50,60,20) < 50 :
    print("kaldın")
else :
    print("geçtin tebrikler")
