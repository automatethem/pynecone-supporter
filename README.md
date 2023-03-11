# pynecone-helper

Install Node.js (npm) (Windows)  
https://nodejs.org/ko/download/  
https://nodejs.org/download/release/v13.9.0/  

Supported APIs
<pre>
import pynecone_helper

pynecone_helper.color_picker
</pre>

자바스크립트 패키지 설치 방법1
<pre>
npm install react-colorful
</pre>

자바스크립트 패키지 설치 방법2  
app\pcconfig.py  
react-colorful npm 패키지 자동 설치
```
import pynecone as pc

config = pc.Config(
    app_name="my_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[ #
        "react-colorful", #
        "react-supporter", #
    ], #
)
```

Examples:  

https://github.com/automatethem/pynecone-helper/blob/main/examples/color_picker/app/pcconfig.py  
https://github.com/automatethem/pynecone-helper/blob/main/examples/color_picker/app/app/app.py  

https://github.com/automatethem/pynecone-helper/blob/main/examples/jumo_button/app/pcconfig.py  
https://github.com/automatethem/pynecone-helper/blob/main/examples/jumo_button/app/app/app.py
