import io ,requests ,os
# import ind2
from pydub import AudioSegment
import speech_recognition as sr
# import activation_link



def audio_lol(download_link):
	try:
		print("Audio Starting")
		#data = open('1.mp3', 'rb').read()
		os_get="wget -O  test1.wav "+download_link
		os.system(os_get)
		print("ok download_link")
		# request = requests.get(download_link)
		# audio_file = io.BytesIO(request.content)
		# sound = AudioSegment.from_mp3(audio_file)
		# print("ok request download_link")
		# dst = "test1.wav"
		# sound.export(dst, format="wav")
		r = sr.Recognizer()
		with sr.WavFile("test1.wav") as source:
		# with sr.WavFile("test1.wav") as source:
			audio = r.record(source)
		audio_output=r.recognize_google(audio)
		audio_output_2=audio_output.replace("please type the numbers you hear","")
		print("Transcription --> : " + audio_output_2)
		os.system("rm test1.wav")

	except Exception as error:
		print (str(error))
audio_lol("https://dd.prod.captcha-delivery.com/audio/2023-06-26/en/44378984af2b0cff217243362b246eb0.wav")