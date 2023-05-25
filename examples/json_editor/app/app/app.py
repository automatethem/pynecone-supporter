import pynecone as pc
import pynecone_supporter

class State(pc.State):
    #json_object = """{ "aaa": "bbb", "ddfd": "fgfg" }"""
    json_object = """[{ "aaa": "bbb", "ddfd": "fgfg" }]"""

def contents():
    return pc.box(
        pc.vstack(
            pc.text(State.json_object),
            pynecone_supporter.components.json_editor(json_object=State.json_object, on_change=lambda json_object: State.set_json_object(json_object)),
        ),
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(contents, route='/', title="Json editor")
app.compile()
