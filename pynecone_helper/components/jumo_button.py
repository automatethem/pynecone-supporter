import pynecone as pc

#https://www.npmjs.com/package/react-supporter
class JumoButton(pc.Component):
    library = "react-supporter" #from 뒤 npm 패키지 이름
    tag = "JumoButton" #import 뒤 리액트 컴포넌트의 태그 이름
    color: pc.Var[str]

    #@classmethod
    #def get_controlled_triggers(cls) -> dict[str, pc.Var]:
    #    return {"on_change": pc.EVENT_ARG} #onChange -> on_change

jumo_button = JumoButton.create
