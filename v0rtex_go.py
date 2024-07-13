

import cnf_bvb
# import mod_vpn2
import mod_driver
import drive_md
import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
from selenium.webdriver import ActionChains
import json
import t00l
import io
import ind2
from pydub import AudioSegment
import speech_recognition as sr
import activation_link
import save_hamster
import undetected_chromedriver as uc



# urls_BVB="https://stripchat.com/vortexproject"
# urls_BVB="https://xhamsterlive.com/vortexproject"
# urls_BVB="https://xhamsterlive.com/chloe_vancab"
urls_BVB="https://xhamsterlive.com/BebKonie"
# urls_BVB="https://xhamsterlive.com/GiannaCarter"
urls_BVB_2="https://xhamsterlive.com/lia_rosens"

# urls_BVB="https://xhamsterlive.com/rozana_holmess"


# urls_BVB="https://indab0x.nl.eu.org/"


main_url="https://nordcheckout.com/"

user_agent = cnf_bvb.user_agent


try:
	sys_use_agent=re.findall('\(.*?\)',user_agent)[0]
	
except Exception as e:
	sys_use_agent="eereee"

file_list_1='succes_2'
########################################################################################################################################
def audio_fonction(download_link):
	#data = open('1.mp3', 'rb').read()
	# print("ok download_link")
	request = requests.get(download_link)
	# print("ok request download_link")
	audio_file = io.BytesIO(request.content)
	sound = AudioSegment.from_mp3(audio_file)
	dst = "test1.wav"
	sound.export(dst, format="wav")
	r = sr.Recognizer()
	with sr.WavFile("test1.wav") as source:
		audio = r.record(source)
	
	audio_output=r.recognize_google(audio)
	print("Transcription: " + audio_output)
	return audio_output

# print(file_list_1)
# input("")
def clean_up():
	try:
		os.system("rm -rf /tmp/*")
		os.system("rm -rf rm -rf __pycache__/")
		# os.system("rm geckodriver.log")

	except:
		pass






	#starting_tasks()

##############################################################
# def counetr_plus():
	# with open 

def read_current_l0g():
	final_msg=''
	with open(l05_00,'r') as file:
		lines = file.readlines()
		for i in lines:
			final_msg=final_msg + i
	return final_msg
############################################################################



def save_succed(logg):
	with open("Wsucced_nord_xxxx",'a') as fw:
		fw.write(logg[0]+":"+logg[1]+"\n")

def save_succed_final(logg):
	with open("ready_Wsucced_nord_xxxx",'a') as fw:
		fw.write(logg+"\n")

###############################################################################################

def ssave_succed_final(logg):
	with open("Amia_Wsucced_count_xxxx",'a') as fw:
		fw.write(logg+"\n")


###############################################################################################
def lets_play(l0g):
	try:
		width ,height=cnf_bvb.resolution_func()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))

	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='',flush=True)
	time.sleep(1)
	try:
		sz=height+","+width
		# print(sz)
		# driver = drive_md.build_driver(sz)
		# driver = uc.Chrome(headless=False,use_subprocess=False)
		driver = ind2.stealth_chr()
		print('driver ok')
		# driver.maximize_window()
		ads_class(driver,l0g)
		# lines=read_current_l0g()
		# cnf_bvb.send_msg(str(lines))
	except Exception as error:
		print(str(error))


	try:
		print("Close Firefox ...... ",end='')
		endiing(driver)
		

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass
	try:
		print("Clean LOGS ...... ",end='')
		os.system('rm /var/log/openvpn/openvpn.log')
		os.system('rm test1.wav ipifo.json')
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i chromedriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass
	# os.system('rm /var/log/openvpn/openvpn.log')


#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i chrome | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i chromedriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/.* > /dev/null 2>&1") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/.* > /dev/null 2>&1")
		os.system("rm l05_00 > /dev/null 2>&1") 
		# os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		# print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))

###############################################################################################
l05_00='l05_00'
def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")


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
		audio_output=audio_output.replace("zero","0")
		audio_output=audio_output.replace("one","1")
		audio_output=audio_output.replace("two","2")
		audio_output=audio_output.replace("three","3")
		audio_output=audio_output.replace("four","4")
		audio_output=audio_output.replace("five","5")
		audio_output=audio_output.replace("six","6")
		audio_output=audio_output.replace("seven","7")
		audio_output=audio_output.replace("eight","8")
		audio_output=audio_output.replace("nine","9")
		audio_output_2=audio_output.replace("please type the numbers you hear","")
		os.system('echo "locked" > last_working_config')

		print("Transcription --> : " + audio_output_2)

		os.system("rm test1.wav > /dev/null 2>&1")
	except Exception as error:
		print (str(error))

# def audio_lol(download_link):
# 	try:
# 		print("Audio Starting")
# 		#data = open('1.mp3', 'rb').read()
# 		# print("ok download_link")
# 		request = requests.get(download_link)
# 		audio_file = io.BytesIO(request.content)
# 		sound = AudioSegment.from_mp3(audio_file)
# 		print("ok request download_link")
# 		dst = "test1.wav"
# 		sound.export(dst, format="wav")
# 		r = sr.Recognizer()
# 		with sr.WavFile("test1.wav") as source:
# 			audio = r.record(source)
# 		audio_output=r.recognize_google(audio)
# 		print("Transcription --> : " + audio_output)
# 	except Exception as error:
# 		print (str(error))

def dev_captcha(driver):
	print("check captcha")
	try:
		number_fra=driver.find_element(By.TAG_NAME,("iframe"))
		# print(str(number_fra))
		# captcha__audio__button
		print(str(number_fra.get_attribute('title')))
		driver.switch_to.frame(0)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'captcha__audio__button')))
		SUCCESS_MSG_BUTTON.click()
		print("ok captcha")
		eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.audio-captcha-track')))
		download_link = eto_firstName.get_attribute('src')
		print(download_link)
		audio_lol(download_link)
		print("get the link")


	except Exception as e:
		print("looo2")
		driver.switch_to.default_content()
		time.sleep(3)
		pass


#################################"MAIN STARTING"##############################
def ads_class(driver,l0g):
	action = ActionChains(driver)
	user_arr_info=t00l.generate_name_add()
	# /html/body/div/div[2]/div
	try:
		driver.get(urls_BVB)
		# print("https://xhamsterlive.com/")
		driver.set_page_load_timeout(60)
		print("VISITING ! "+urls_BVB)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="agreement-root"]/div/div/div/div[2]/div[1]/button')))
		action.move_to_element(SUCCESS_MSG_BUTTON)
		action.perform()
		SUCCESS_MSG_BUTTON.click()
		print("I am 18")
		time.sleep(1)
		print('button click')
		try:
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[2]/div/div[4]/div[2]/div[2]/button[2]')))
			# SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[3]/div[2]/div[2]')))
			SUCCESS_MSG_BUTTON.click()
			print('Cookies clicked ok')
			
		except Exception as e:
			print("no Cookies")

		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[2]/div/header/div/div/nav[2]/div[2]/a[2]')))
		# SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[3]/div[1]/header/div/div/nav[2]/div[2]/a[1]/span[2]')))
		SUCCESS_MSG_BUTTON.click()
		print('@ button singup')
		time.sleep(2)
		# input("lolpt ")
		SINGUP_WITHOUT_EMAIL=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="portal-root"]/div[2]/div/dialog/div/div/div[2]/div[1]/div[2]/div[2]')))
		SINGUP_WITHOUT_EMAIL.click()
		print('@ Magic button ')
		time.sleep(2)
		# input('Stop')
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="username_input"]/input')))

		SUCCESS_MSG_BUTTON.send_keys(user_arr_info[5],Keys.TAB,user_arr_info[1],Keys.ENTER)
		# dev_captcha(driver)
		# input("llllll")
		time.sleep(4)
		print('Stop 2000')
		# input("lol")
		try:
			#pass
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[3]/button')))
			SUCCESS_MSG_BUTTON.click()
			print('hm... FAVORIT 222')
			time.sleep(3)	
		except Exception as e:
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[3]/button')))
			SUCCESS_MSG_BUTTON.click()
			# raise e
		logg=user_arr_info[5]+' '+user_arr_info[1]
		ssave_succed_final(logg)
		print('Stop 3000')
		driver.get(urls_BVB_2)
		try:
			#pass
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[3]/button')))
			SUCCESS_MSG_BUTTON.click()
			print('hm... FAVORIT 222')
			time.sleep(3)	
		except Exception as e:
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[3]/button')))
			SUCCESS_MSG_BUTTON.click()
			# raise e
		print('Stop 5000')
		endiing(driver)
	except Exception as error:
		print (str(error))
		# endiing(driver)
		endiing(driver)
def starting_tasks(l0g):
	width ,height=cnf_bvb.resolution_func()
	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)

######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# print(l0g)
		# os.system("curl -sx socks5://127.0.0.1:9050 ifconfig.co | grep -oP '(?<=Your IP</span>: ).*(?=</span>)'")
		# mod_vpn2.fnc_vpn ()
		# cnf_bvb.alias_send_msg("starting chom")
		# mod_vpn.renew_connection()
		# serv,ops=mod_driver.build_driver(width ,height)
		lets_play(l0g)
		clean_up()
		

	except Exception as error:
		print (str(error))


def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines







def save_successed_bin(card_numer):
	# l_bin=read_the_last_bin()
	print(card_numer)
	# new_bin=int(l_bin)+1
	# binani=str(new_bin)
	#################
	with open("succed_bin","a") as file_bin:
		file_bin.write(card_numer+"\n")


def endiing(driver):
	driver.close()
	try:
		driver.delete_all_cookies()
		# pass
	except Exception as e:
		pass
	# driver.quit()
	os.system("ps aux | grep -i chromedriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	os.system("ps aux | grep -i chrome | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
	os.system("rm -rf /tmp/.com.google*")
	os.system("service networking restart")
	print("REMOVE THE SHIIIT !!!!")


def main():
	os.system("rm -rf /tmp/.com.google* > /dev/null 2>&1")
	starting_tasks("l0g:l0g")
	os.system("rm -rf /tmp/.* > /dev/null 2>&1")



if __name__ == '__main__':

	main()
