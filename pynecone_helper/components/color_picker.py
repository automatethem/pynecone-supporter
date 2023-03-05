import pynecone as pc

#https://www.npmjs.com/package/react-colorful
class ColorPicker(pc.Component):
    library = "react-colorful" #from 뒤 npm 패키지 이름
    tag = "HexColorPicker" #import 뒤 리액트 컴포넌트의 태그 이름
    color: pc.Var[str]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_change": pc.EVENT_ARG} #onChange -> on_change

color_picker = ColorPicker.create
