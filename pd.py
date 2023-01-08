import cv2
import os
import subprocess
import youtube_dl

# Video linkini dosyadan oku
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
                start, end = line.strip().split()
                ranges.append((int(start), int(end)))
        
        # Klasör oluştur (eğer zaten oluşturulmuşsa hata verme)
        try:
            os.mkdir(video_name)
        except FileExistsError:
            pass

        # Video'yu aç
        video = cv2.VideoCapture(f"{video_name}.mp4")

        # Belirtilen saniye aralıklarında fotoğraf çek
        for start, end in ranges:
            for i in range(start, end + 1):
                video.set(cv2.CAP_PROP_POS_MSEC, i * 1000)
                success, image = video.read()
                if success:
                    cv2.imwrite(os.path.join(video_name, f"{video_name}%d.jpg" % i), image)
                    

        # Video'yu kapat
        video.release()
        # İndirilen video dosyasını sil
        os.remove(f"{video_name}.mp4")

