from mutagen import File

file = File('Endless Game.mp3') # mutagen can automatically detect format and type of tags
artwork = file.tags['APIC:'].data # access APIC frame and grab the image
with open('image.jpg', 'wb') as img:
   img.write(artwork) # write artwork to new image