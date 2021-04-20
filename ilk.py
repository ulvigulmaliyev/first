tip1="lava ilə örtülü"
tip2="su ilə örtülü"
tip3="buz ilə örtülü"
import new 
print("dünya simulyasiyasına xoş gəlmisiz")
dünyaseçimi=input("dünyanızın tipini seçin(lava ilə örtülü,su ilə örtülü,buz ilə örtülü):")
if dünyaseçimi == tip1:
    print(tip1,"olan dünya yaradıldı")
    print(tip1,"""olan dünyanın əlamətləri:
1)orta temperatur 700 dərəcədən çox
2)quru səth yoxdur çünki temperaturun çox olması əlind?n bütün səth əridi
3)yaşam yoxdurr....""")
    term=int(input("orta temperaturnuzu seçin:"))
    oksigenfaizi=int(input("oksigen faizinizi seçin:"))
    karbonfaizi=int(input("karbon qazı faizinizi seçin:"))
elif dünyaseçimi == tip2:
    print(tip2,"olan dünya yaradıldı")
    print(tip2,"olan dünyanın əlamətləri")
    term=int(input("orta temperaturnuzu seçin:"))
    if term > 100:
        print("mal herif su buxarlaşdı")
        seçim=input("hələdə dəvam etmək istəyirsiniz?")
        if seçim == "yox":
            new.su()
        elif seçim == "hə":
            print("dəvam edilir...")
        else:
            print("get keçərli bir şey gir hə ya yoox")
            new.su_seçimi()   
    oksigenfaizi=int(input("oksigen faizinizi seçin:"))
    karbonfaizi=int(input("karbon qazı faizinizi seçin:"))
    
            
elif dünyaseçimi == tip3:
    print(tip3,"olan dünya yaradıldı")
    print(tip3,"olan dünyanın əlamətləri:orta temperatur 0 dan aşağı,canlı həyat yoxdur,")
    term=int(input("orta temperaturnuzu seçin:"))
    if term> 60:
        print("çoxhüceyrəli canlılar bu temperaturda çətinliklə sağ qalar")
    if term > 0:
       print("orta temperatur 0 dan böyük olduğu üçün buzlar əridi")
       seçim=input("hələdə dəvam etmək istəyirsiz(hə və ya yox):")
       if seçim == "hə":
          print("devam...")
       elif seçim == "yox":
          new.buz()
           
       
                     
else:
    print("belə dünya yoxdur")       
         
