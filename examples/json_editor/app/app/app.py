import pynecone as pc
import pynecone_supporter

class State(pc.State):
    #json_object = """{ "aaa": "bbb", "ddfd": "fgfg" }"""
    json_object = """[{ "aaa": "bbb", "ddfd": "fgfg" }]"""

def index():
    #print(pynecone_supporter.json_editor(on_change=State.set_data)) #
    #print(type(pynecone_supporter.json_editor(on_change=State.set_data))) #
    return pc.box(
        pc.vstack(
            pc.text(State.json_object),
            pynecone_supporter.json_editor(jsonObject=State.jsonObject, on_change=State.set_data),
        ),
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Json editor")
app.compile()
