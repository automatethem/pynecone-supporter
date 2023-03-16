import pynecone as pc
import pynecone_supporter

class State(pc.State):
    data = """
  {
    order: {
      id: 'order_124831sf23j123',
      isSuccess: true,
      price: 70000
    }
  }
    """

def index():
    #print(pynecone_supporter.json_editor(on_change=State.set_data)) #
    #print(type(pynecone_supporter.json_editor(on_change=State.set_data))) #
    return pc.box(
        pc.vstack(
            pc.text(State.data),
            pynecone_supporter.json_editor(on_change=State.set_data),
        ),
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Json editor")
app.compile()
