import pynecone as pc
import pynecone_supporter

class State(pc.State):
    background_color = "#aabbcc"
    font_color = "#aabbcc"
    
def contents():
    return pc.box(
        pc.vstack(
            pc.text(State.background_color),
            pynecone_supporter.components.jumo_button(background_color='red', font_color= "#aabbcc"),
        ),
        background_color=State.background_color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(contents, route="/", title="Jumo button")
app.compile()
