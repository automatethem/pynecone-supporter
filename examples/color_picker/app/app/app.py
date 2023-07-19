import reflex as rx
import reflex_supporter

class State(rx.State):
    color = "#aabbcc"

def contents():
    return rx.box(
        rx.vstack(
            rx.text(State.color),
            pynecone_supporter.components.color_picker(on_change=lambda color: State.set_color(color)),
        ),
        background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = rx.App(state=State)
app.add_page(contents, route="/", title="Color picker")
app.compile()
