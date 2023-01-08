# Videodan Kare Alma

Bu projemiz, bir video'yu belirtilen zaman aralıklarına göre bölmek ve sonuç olarak oluşan kareleri resimler olarak kaydetmek için bir komut satırı aracıdır. Örneğin, video dosyasındaki 1 dakikalık bir bölümün fotoğraflarını almak istediğimizde bu projeyi kullanabiliriz.

# Kurulum

Bu projemizi kullanabilmek için öncelikle gereken bağımlılıkları kurmamız gerekir. Bu bağımlılıkları kurmak için aşağıdaki komutu terminale yazıp çalıştırabilirsiniz:

pip install -r requirements.txt

# Kullanım

Projemizi çalıştırmak için aşağıdaki komutu terminale yazıp çalıştırmanız yeterlidir:

python photo_downloads.py

Program, video_urls.txt dosyasından video URL'lerini okuyacak ve bu videoları indirip, ranges.txt dosyasından okuduğu zaman aralıklarına göre belirtilen kareleri resimler olarak kaydedecektir. Örneğin, ranges.txt dosyasında 1 60 yazarsak program ilk dakikadaki tüm kareleri resimler olarak kaydedecektir. Resimler, videonun aynı isimli bir dizine kaydedilecektir.

# Bilinen Sorunlar

Program şu anda sadece MP4 formatında videoları destekler.Program bazı video URL'leriyle çalışmayabilir. Örneğin, YouTube gibi platformlardaki bazı videoları indirirken problem yaşanabilir.