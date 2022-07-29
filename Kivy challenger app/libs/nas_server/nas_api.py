from synology_api import filestation, downloadstation
import requests
# Initiate the classes DownloadStation & FileStation with (ip_address, port, username, password)
# it will login automatically 
class Nas_geturl():

    fl = filestation.FileStation('輸入IP', '輸入port', '輸入帳號', '輸入密碼', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)

    def show_pic(self,path):
        
        try:
            # print(fl.get_info())
            # print('\n')
            # print(fl.get_list_share())
            # print("\n")
            # print(fl.get_file('/docker/PIC/KING1.jpg','download','./'))

            #check the url connect is OK else return ''
            pic = self.fl.get_file(path,'open','./')  
            r = requests.get(pic)
            if r.status_code == requests.codes.ok:
                pass
            else:
                pic = ''
            # print("\n")
            # print(fl.get_file_list('/docker/PIC'))
            
            self.fl.logout()
            return pic
        except:
            pass
    def upload_pic(self,pic_cwd):
        # fl = filestation.FileStation('khomestore.synology.me', '7000', 'Kevin', '33U07127138mj', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)
        try:
            self.fl.upload_file('/docker/PIC/Useruploadimage',pic_cwd)
        except:
            pass
        self.fl.logout()

