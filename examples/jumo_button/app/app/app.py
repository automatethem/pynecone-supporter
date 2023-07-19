import reflex as rx
import reflex_supporter

class State(rx.State):
    background_color = "#aabbcc"
    font_color = "#aabbcc"
    
def contents():
    return rx.box(
        rx.vstack(
            rx.text(State.background_color),
            pynecone_supporter.components.jumo_button(background_color='red', font_color= "#aabbcc"),
        ),
        background_color=State.background_color,
        padding="5em",
        border_radius="1em",
    )

app = rx.App(state=State)
app.add_page(contents, route="/", title="Jumo button")
app.compile()
