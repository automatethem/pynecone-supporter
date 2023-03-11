# pynecone-helper

Install Node.js (npm) (Windows)  
https://nodejs.org/ko/download/  
https://nodejs.org/download/release/v13.9.0/  

Supported APIs
<pre>
import pynecone_helper

pynecone_helper.color_picker
pynecone_helper.jumo_button
</pre>

https://github.com/automatethem/pynecone-helper/blob/main/examples/color_picker/app/pcconfig.py  
```
import pynecone as pc

config = pc.Config(
    app_name="my_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[ #
        "react-colorful", #
    ], #
)
```

https://github.com/automatethem/pynecone-helper/blob/main/examples/jumo_button/app/pcconfig.py  
```
import pynecone as pc

config = pc.Config(
    app_name="my_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[ #
        "react-supporter", #
    ], #
)
```

Examples:  

https://github.com/automatethem/pynecone-helper/blob/main/examples/color_picker/app/app/app.py  
https://github.com/automatethem/pynecone-helper/blob/main/examples/jumo_button/app/app/app.py
