import pynecone as pc

#https://www.npmjs.com/package/react-supporter
class JumoButton(pc.Component):
    library = "react-supporter" #from 뒤 npm 패키지 이름
    tag = "JumoButton" #import 뒤 리액트 컴포넌트의 태그 이름
    background_color: pc.Var[str]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_click": pc.EVENT_ARG} #onClick -> on_click

jumo_button = JumoButton.create
