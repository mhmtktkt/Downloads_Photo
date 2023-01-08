import cv2
import os
import subprocess
import youtube_dl

# Video linklerini dosyadan oku
with open("video_urls.txt", "r") as f:
    for url in f:
        # URL'nin son kısmındaki videonun adını al
        video_name = url.strip().split("/")[-1]
        # YouTube videolarını indirme işlemini gerçekleştir
        subprocess.run(["youtube-dl", "--output", f"{video_name}.mp4","--format","mp4", url])

# İndirilecek saniye aralıklarını tutan bir liste oluştur
ranges = []

# İndirilecek saniye aralıklarını dosyadan oku
with open("ranges.txt", "r", encoding="utf-8-sig") as f:
    for line in f:
        video_name, aralik = line.strip().split(":")
        baslangic, bitis = map(int, aralik.split("-"))
        ranges.append((video_name, baslangic, bitis))

# Klasör oluştur (eğer zaten oluşturulmuşsa hata verme)
for video_name, baslangic, bitis in ranges:
    try:
        os.mkdir(video_name)
    except FileExistsError:
        pass

    # Video'yu aç
    video = cv2.VideoCapture(f"{video_name}.mp4")

    # Belirtilen saniye aralıklarında fotoğraf çek
    for i in range(baslangic, bitis + 1):
        video.set(cv2.CAP_PROP_POS_MSEC, i * 1000)
        success, image = video.read()
        if success:
            cv2.imwrite(os.path.join(video_name, f"{video_name}%d.jpg" % i), image)
                    
    # Video'yu kapat
    video.release()
    # İndirilen video dosyasını sil
    os.remove(f"{video_name}.mp4")
