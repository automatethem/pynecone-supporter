import pynecone as pc
import pynecone_helper

class State(pc.State):
    #color = "#aabbcc"
    pass

def index():
    return pc.box(
        pc.vstack(
            pc.heading(State.color),
            pynecone_helper.jumo_button(background_color='red'),
        ),
        #background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Jumo button")
app.compile()
