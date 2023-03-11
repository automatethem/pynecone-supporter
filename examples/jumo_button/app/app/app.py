import pynecone as pc
import pynecone_helper

class State(pc.State):
    background_color = "#aabbcc"
    font_color = "#aabbcc"
    
def index():
    #print(pynecone_helper.jumo_button(background_color='red', font_color= "#aabbcc")) #<JumoButton fontColor="#aabbcc" backgroundColor="red"/>
    #print(type(pynecone_helper.jumo_button(background_color='red', font_color= "#aabbcc"))) #<class 'test.test.JumoButton'>    
    return pc.box(
        pc.vstack(
            pc.text(State.background_color),
            pynecone_helper.jumo_button(background_color='red', font_color= "#aabbcc"),
        ),
        background_color=State.background_color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Jumo button")
app.compile()
