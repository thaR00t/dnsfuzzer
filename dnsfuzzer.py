import dns.resolver
from rich import print
import textwrap
import argparse


sub_domain_arr = ['www','mail','ftp','localhost','webmail','smtp','pop','ns1','webdisk','ns2','cpanel','whm','autodiscover','autoconfig','m','imap','test','ns','blog','pop3','dev','www2','admin','forum','news','vpn','ns3','mail2','new','mysql','old','lists','support','mobile','mx','static','docs','beta','shop','sql','secure','demo','cp','calendar','wiki','web','media','email','images','img','www1','intranet','portal','video','sip','dns2','api','cdn','stats','dns1','ns4','www3','dns','search','staging','server','mx1','chat','wap','my','svn','mail1','sites','proxy','ads','host','crm','cms','backup','mx2','lyncdiscover','info','apps','download','remote','db','forums','store','relay','files','newsletter','app','live','owa','en','start','sms','office','exchange','ipv4','mail3','help','blogs','helpdesk','web1','home','library','ftp2','ntp','monitor','login','service','correo','www4','moodle','it','gateway','gw','i','stat','stage','ldap','tv','ssl','web2','ns5','upload','nagios','smtp2','online','ad','survey','data','radio','extranet','test2','mssql','dns3','jobs','services','panel','irc','hosting','cloud','de','gmail','s','bbs','cs','ww','mrtg','git','image','members','poczta','s1','meet','preview','fr','cloudflare-resolve-to','dev2','photo','jabber','legacy','go','es','ssh','redmine','partner','vps','server1','sv','ns6','webmail2','av','community','cacti','time','sftp','lib','facebook','www5','smtp1','feeds','w','games','ts','alumni','dl','s2','phpmyadmin','archive','cn','tools','stream','projects','elearning','im','iphone','control','voip','test1','ws','rss','sp','wwww','vpn2','jira','list','connect','gallery','billing','mailer','update','pda','game','ns0','testing','sandbox','job','events','dialin','ml','fb','videos','music','a','partners','mailhost','downloads','reports','ca','router','speedtest','local','training','edu','bugs','manage','s3','status','host2','ww2','marketing','conference','content','network-ip','broadcast-ip','english','catalog','msoid','mailadmin','pay','access','streaming','project','t','sso','alpha','photos','staff','e','auth','v2','web5','web3','mail4','devel','post','us','images2','master','rt','ftp1','qa','wp','dns4','www6','ru','student','w3','citrix','trac','doc','img2','css','mx3','adm','web4','hr','mailserver','travel','sharepoint','sport','member','bb','agenda','link','server2','vod','uk','fw','promo','vip','noc','design','temp','gate','ns7','file','ms','map','cache','painel','js','event','mailing','db1','c','auto','img1','vpn1','business','mirror','share','cdn2','site','maps','tickets','tracker','domains','club','images1','zimbra','cvs','b2b','oa','intra','zabbix','ns8','assets','main','spam','lms','social','faq','feedback','loopback','groups','m2','cas','loghost','xml','nl','research','art','munin','dev1','gis','sales','images3','report','google','idp','cisco','careers','seo','dc','lab','d','firewall','fs','eng','ann','mail01','mantis','v','affiliates','webconf','track','ticket','pm','db2','b','clients','tech','erp','monitoring','cdn1','images4','payment','origin','client','foto','domain','pt','pma','directory','cc','public','finance','ns11','test3','wordpress','corp','sslvpn','cal','mailman','book','ip','zeus','ns10','hermes','storage','free','static1','pbx','banner','mobil','kb','mail5','direct','ipfixe','wifi','development','board','ns01','st','reviews','radius','pro','atlas','links','in','oldmail','register','s4','images6','static2','id','shopping','drupal','analytics','m1','images5','images7','img3','mx01','www7','redirect','sitebuilder','smtp3','adserver','net','user','forms','outlook','press','vc','health','work','mb','mm','f','pgsql','jp','sports','preprod','g','p','mdm','ar','lync','market','dbadmin','barracuda','affiliate','mars','users','images8','biblioteca','mc','ns12','math','ntp1','web01','software','pr','jupiter','labs','linux','sc','love','fax','php','lp','tracking','thumbs','up','tw','campus','reg','digital','demo2','da','tr','otrs','web6','ns02','mailgw','education','order','piwik','banners','rs','se','venus','internal','webservices','cm','whois','sync','lb','is','code','click','w2','bugzilla','virtual','origin-www','top','customer','pub','hotel','openx','log','uat','cdn3','images0','cgi','posta','reseller','soft','movie','mba','n','r','developer','nms','ns9','webcam','construtor','ebook','ftp3','join','dashboard','bi','wpad','admin2','agent','wm','books','joomla','hotels','ezproxy','ds','sa','katalog','team','emkt','antispam','adv','mercury','flash','myadmin','sklep','newsite','law','pl','ntp2','x','srv1','mp3','archives','proxy2','ps','pic','ir','orion','srv','mt','ocs','server3','meeting','v1','delta','titan','manager','subscribe','develop','wsus','oascentral','mobi','people','galleries','wwwtest','backoffice','sg','repo','soporte','www8','eu','ead','students','hq','awstats','ec','security','school','corporate','podcast','vote','conf','magento','mx4','webservice','tour','s5','power','correio','mon','mobilemail','weather','international','prod','account','xx','pages','pgadmin','bfn2','webserver','www-test','maintenance','me','magazine','syslog','int','view','enews','ci','au','mis','dev3','pdf','mailgate','v3','ss','internet','host1','smtp01','journal','wireless','opac','w1','signup','database','demo1','br','android','career','listserv','bt','spb','cam','contacts','webtest','resources','1','life','mail6','transfer','app1','confluence','controlpanel','secure2','puppet','classifieds','tunet','edge','biz','host3','red','newmail','mx02','sb','physics','ap','epaper','sts','proxy1','ww1','stg','sd','science','star','www9','phoenix','pluto','webdav','booking','eshop','edit','panelstats','xmpp','food','cert','adfs','mail02','cat','edm','vcenter','mysql2','sun','phone','surveys','smart','system','twitter','updates','webmail1','logs','sitedefender','as','cbf1','sugar','contact','vm','ipad','traffic','dm','saturn','bo','network','ac','ns13','webdev','libguides','asp','tm','core','mms','abc','scripts','fm','sm','test4','nas','newsletters','rsc','cluster','learn','panelstatsmail','lb1','usa','apollo','pre','terminal','l','tc','movies','sh','fms','dms','z','base','jwc','gs','kvm','bfn1','card','web02','lg','editor','metrics','feed','repository','asterisk','sns','global','counter','ch','sistemas','pc','china','u','payments','ma','pics','www10','e-learning','auction','hub','sf','cbf8','forum2','ns14','app2','passport','hd','talk','ex','debian','ct','rc','2012','imap4','blog2','ce','sk','relay2','green','print','geo','multimedia','iptv','backup2','webapps','audio','ro','smtp4','pg','ldap2','backend','profile','oldwww','drive','bill','listas','orders','win','mag','apply','bounce','mta','hp','suporte','dir','pa','sys','mx0','ems','antivirus','web8','inside','play','nic','welcome','premium','exam','sub','cz','omega','boutique','pp','management','planet','ww3','orange','c1','zzb','form','ecommerce','tmp','plus','openvpn','fw1','hk','owncloud','history','clientes','srv2','img4','open','registration','mp','blackboard','fc','static3','server4','s6','ecard','dspace','dns01','md','mcp','ares','spf','kms','intranet2','accounts','webapp','ask','rd','www-dev','gw2','mall','bg','teste','ldap1','real','m3','wave','movil','portal2','kids','gw1','ra','tienda','private','po','2013','cdn4','gps','km','ent','tt','ns21','at','athena','cbf2','webmail3','mob','matrix','ns15','send','lb2','pos','2','cl','renew','admissions','am','beta2','gamma','mx5','portfolio','contest','box','mg','wwwold','neptune','mac','pms','traveler','media2','studio','sw','imp','bs','alfa','cbf4','servicedesk','wmail','video2','switch','sam','sky','ee','widget','reklama','msn','paris','tms','th','vega','trade','intern','ext','oldsite','learning','group','f1','ns22','ns20','demo3','bm','dom','pe','annuaire','portail','graphics','iris','one','robot','ams','s7','foro','gaia','vpn3']
#creating a main function

def banner():
    a = """"[bold orange_red1]
     _            __
    | |          / _|
  __| |_ __  ___| |_ _   _ ___________ _ __
 / _` | '_ \/ __|  _| | | |_  /_  / _ \ '__|
| (_| | | | \__ \ | | |_| |/ / / /  __/ |
 \__,_|_| |_|___/_|  \__,_/___/___\___|_|[/bold orange_red1]    
    """
    return a

def display():
    print('[bold blue]-[/bold blue]'*50)
    print(f'[bold blue]Domain:  {domain}[/bold blue]')
    print('[bold blue]Ctrl^C to interrupt the script[/bold blue]')
    print('[bold blue]-[/bold blue]'*50)
    print('[bold blue]DOMAIN:\n[/bold blue]')
    

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Domain fuzzer resolver:",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    epilog=textwrap.dedent("""EXAMPLE:\n
    
    dnsfuzzer.py -d <domain> 
    dnsfuzzer.py -d <domain> -o <filename.txt>
    """))    
    parser.add_argument('-d','--domain',help='Insert a domain')
    parser.add_argument('-o','--output',help='Save the output into a .txt file')
    args=parser.parse_args()
    domain = args.domain
    out = args.output
    

def main():
    
    #create a list to append value
    subdomain_store = [] 
    #filtring the list
    if domain:
        print(banner())
        display()
        
        for subdom in sub_domain_arr:
            
            try:  
                #resolve the domain
                ip_value = dns.resolver.resolve(f'{subdom}.{domain}','A')
                #if there is a connection then...
                if ip_value:
                    
                    #append in subdomain_store the subdom and the domain
                    subdomain_store.append(f'{subdom}.{domain}')

                    #after append value, we valitading the value
                    if f"{subdom}.{domain}" in subdomain_store:

                        #with this var we can take the domain's ip
                        domain_scan = f'{subdom}.{domain}'

                                                
                        #creating an output
                                                                        
                        print(f"[bold purple]{domain_scan}[/bold purple]")
                        
                        #crating a output file if the user want
                        if out:
                            
                            output2 = domain_scan + '\n'
                            with open(out,'a') as f:
                                f.write(output2)
                                f.close()
                        
                    else:
                        pass                

            #Creating exception
            except dns.resolver.NXDOMAIN:            
                pass
            except dns.resolver.NoAnswer:
                pass
            except dns.resolver.LifetimeTimeout:
                pass
            except dns.resolver.NoNameservers:
                pass
            except KeyboardInterrupt:
                print("[bold red]\n[-]Script interrupt by user[-][/bold red]")
                
                quit()
       
        print(f"[bold blue]\nScan complete!")
    else:        
        print("[bold red]\n[!]Missing domain[/bold red]")
        print("[bold red]Use [-h] or [--help] to show the help\n[/bold red]")
main()
