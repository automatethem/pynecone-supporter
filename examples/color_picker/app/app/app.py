import pynecone as pc
import pynecone_supporter

class State(pc.State):
    color = "#aabbcc"

def contents():
    return pc.box(
        pc.vstack(
            pc.text(State.color),
            pynecone_supporter.components.color_picker(on_change=lambda color: State.set_color(color)),
        ),
        background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(contents, route="/", title="Color picker")
app.compile()
