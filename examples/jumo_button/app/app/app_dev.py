import pynecone as pc

#https://www.npmjs.com/package/react-supporter
class JumoButton(pc.Component):
    library = "react-supporter" #from 뒤 npm 패키지 이름
    tag = "JumoButton" #import 뒤 리액트 컴포넌트의 태그 이름
    background_color: pc.Var[str]
    font_color: pc.Var[str]

    #@classmethod
    #def get_controlled_triggers(cls) -> dict[str, pc.Var]:
    #    return {"on_click": pc.EVENT_ARG} #onClick -> on_click

jumo_button = JumoButton.create

############

import pynecone as pc
#import pynecone_helper

class State(pc.State):
    background_color = "#aabbcc"
    font_color= "#aabbcc"
    #pass

def index():
    #print(jumo_button(background_color='red', font_color= "#aabbcc")) #<JumoButton fontColor="#aabbcc" backgroundColor="red"/>
    #print(type(jumo_button(background_color='red', font_color= "#aabbcc"))) #<class 'test.test.JumoButton'>
    return pc.box(
        pc.vstack(
            pc.text(State.background_color),
            #pynecone_helper.jumo_button('red'),
            jumo_button(background_color='red', font_color= "#aabbcc"),
            #jumo_button('red'),
        ),
        #background_color=State.color,
        padding="5em",
        border_radius="1em",
    )

app = pc.App(state=State)
app.add_page(index, title="Jumo button")
app.compile()
