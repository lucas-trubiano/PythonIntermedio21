from pytube import YouTube

link = "https://www.youtube.com/watch?v=lnX-bfsiNbs"
# curso completo sqlite

yt = YouTube(link)

# se muestra informacion del video
print("Su video es:")
print("\tTitulo:",yt.title)
print("\tAutor:",yt.author)
duracion = yt.length # seg
horas = int(duracion/60/60)
duracion -= horas*60*60
minutos = int((duracion)/60)
duracion -= minutos*60
segundos = int(duracion)

print("\tDuracion:",f"{horas}:{minutos}:{segundos}")

# comenzamos con la descarga
formato = "mp4" #audio/video mp4, avi, mkv, mp3 (solo audio)
calidad = "720p"

resoluciones = yt.streams.order_by('resolution')
resolucionesMayorMenor = yt.streams.filter(progressive=True,file_extension='mp4').order_by("resolution").desc()
resolucion = resolucionesMayorMenor.last()

print("Descargando")
video = resolucion.download(output_path="C:\\Users\\lucas\\Downloads")
print("Termino, adios!")