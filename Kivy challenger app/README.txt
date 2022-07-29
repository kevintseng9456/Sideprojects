!!需要有一台NAS 架設所需環境才能執行程式!!

請開啟libs內的nas_api檔案，找到下方程式碼做設定
fl = filestation.FileStation('輸入IP', '輸入port', '輸入帳號', '輸入密碼', secure=False, cert_verify=False, dsm_version=7, debug=True, otp_code=None)