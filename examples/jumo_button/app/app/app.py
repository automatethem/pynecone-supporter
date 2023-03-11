import pynecone as pc
import pynecone_helper

def index():
    #print(jumo_button(background_color='red', font_color= "#aabbcc")) #<JumoButton fontColor="#aabbcc" backgroundColor="red"/>
    #print(type(jumo_button(background_color='red', font_color= "#aabbcc"))) #<class 'test.test.JumoButton'>    
    return pc.box(
        pc.vstack(
            pc.text(State.color),
            pynecone_helper.jumo_button(background_color='red', font_color= "#aabbcc"),
        ),
        #background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Jumo button")
app.compile()
