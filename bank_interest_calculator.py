import math

def print_duration(ay):
    yil = ay // 12
    kalan_Ay = ay % 12
    print("-> yıl:", yil, ", ay:", kalan_Ay)


def print_money(para):
    para_yuvarla = math.floor(para * 10)/10.0
    print("%.1f" % para_yuvarla + "$")


def print_entry(kredi_miktari, faiz_orani, ay):
    print("---------------------------------")
    print_duration(ay)
    faizli_kredi_tutari = float(
        kredi_miktari + (kredi_miktari / 100 * faiz_orani/12 * ay))
    print("Toplam ödeme:")
    print_money(faizli_kredi_tutari)
    print("Aylık ödeme:")
    print_money(faizli_kredi_tutari / float(ay))
    print("---------------------------------")

def print_full_report(kredi_miktari, faiz_orani, maks_yil, maks_ay,  yineleme_araligi):
    toplam_ay = maks_yil * 12 + maks_ay
    i =  yineleme_araligi
    while i <= toplam_ay:
        print_entry(kredi_miktari, faiz_orani, i)
        i +=  yineleme_araligi


print("....................................................")
print("*.*.*.*.*. Faiz Hesaplayıcıya Hoş Geldiniz .*.*.*.*.*")
print("....................................................\n")

ad = input("lütfen adınızı giriniz: ")
# kredi tutarı ($ s cinsinden, ör. 1000.50)
kredi_miktari = float(input("kredi miktarı giriniz: "))
# yıllık faiz oranı (dalgalı yüzde olarak, ör. 1.5 veya 50 veya 150 veya ...)
yillik_faiz_orani = float(input("faiz oranı (yıllık): "))
print("-> ne kadar sürede istediğinizi giriniz.")
# maksimum yıl (tam sayı, ör. 0 veya 1 veya 2 veya ...)
maks_yil = int(input("\t maksimum yıl süresi: "))
# en fazla ay (tam sayı, ör. 0 veya 6 veya 18 veya ...)
maks_ay = int(input("\t maksimum ay süresi: "))
# yineleme aralığı (ay cinsinden tam sayı)
yineleme_araligi = int(input("\tyineleme aralığı: "))
print("....................................................\n")

print("şunun için rapor %s:" % ad)
print_full_report(kredi_miktari,  yillik_faiz_orani,
                  maks_yil, maks_ay,  yineleme_araligi)
