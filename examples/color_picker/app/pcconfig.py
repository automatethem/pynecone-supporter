import pynecone as pc

config = pc.Config(
    app_name="my_app",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[ #
        "react-colorful", #
    ], #
)
