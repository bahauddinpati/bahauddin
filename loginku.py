import os, sys

print ("\033[1;32mMONGGO MASUKKAN USERNAME DAN PASSWORDNYA DULLU LUR")

print ("\033[1;32mTOOLS INSTALLERKU Bahauddin ")

username = 'bahauddin'      

password = 'ganteng'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mALHAMDULILLAH WES ISO MASUK LUR", 

			sys.exit()



		else:

			print "\033[1;32mSEPURANE SENG AKEH LUR PASSWORD MU SALAH [?]\033[00m"

			print "JAJAL BALENI MANEH... ANDA KURANG BERUNTUNG VANGKE!!\n"

			restart()



	else:

		print "\033[1;32mSEPURANE SENG AKEH LUR PASSWORD MU SALAH [?]\033[00m"

		print "JAJAL BALENI MANEH... ANDA KURANG BERUNTUNG VANGKE!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
