import reflex as pc
import reflex_supporter

class State(rx.State):
    #json_object = """{ "aaa": "bbb", "ddfd": "fgfg" }"""
    json_object = """[{ "aaa": "bbb", "ddfd": "fgfg" }]"""

def contents():
    return rx.box(
        rx.vstack(
            rx.text(State.json_object),
            pynecone_supporter.components.json_editor(json_object=State.json_object, on_change=lambda json_object: State.set_json_object(json_object)),
        ),
        padding="5em",
        border_radius="1em",
    )

app = rx.App(state=State)
app.add_page(contents, route='/', title="Json editor")
app.compile()
