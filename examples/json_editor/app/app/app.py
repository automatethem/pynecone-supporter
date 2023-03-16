import pynecone as pc
#import pynecone_supporter

class State(pc.State):
    json_object = """
  {
    name: 'may',
    age: null,
    address: [
      'Panyu Shiqiao on Canton',
      'Tianhe',
      {
        city: 'forida meta 11',
      },
    ],
    ohters: {
      id: 1246,
      joinTime: '2017-08-20. 10:20',
      description: 'another',
    },
  }
    """

def index():
    #print(pynecone_supporter.json_editor(on_change=State.set_data)) #
    #print(type(pynecone_supporter.json_editor(on_change=State.set_data))) #
    return pc.box(
        pc.vstack(
            pc.text(State.json_object),
            #pynecone_supporter.json_editor(on_change=State.set_data),
            json_editor(on_change=State.set_json_object),
        ),
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Json editor")
app.compile()
