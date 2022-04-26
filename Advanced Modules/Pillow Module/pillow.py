from PIL import Image,ImageFilter


image = Image.open("Exodus.jpg")
# image.save("Exodus2.jpg") # aynı resmi farklı isimle kaydetme 
# image.rotate(180).save("Exodus3.jpg") # resmi çevirme
# image.show()
# image.convert(mode="L").save("Exodus5.jpg") # L moduyle renkleri siyah beyaza çevirdik
# degistir = (960,600)
# image.thumbnail(degistir) # bu image i 960 600 e düşürücez
# image.save("exodus4.jpg")
# image.filter(ImageFilter.GaussianBlur(5)).save("ExodusBlur.jpg") # Filtre  ekledik blur filtresi

# kırpılacak_alan = (340,0,950,600)
# image.crop(kırpılacak_alan).save("Exodus9.jpg")