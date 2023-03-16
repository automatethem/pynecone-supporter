import pynecone as pc

#https://www.npmjs.com/package/rc-json-editor
class JsonEditor(pc.Component):
    library = "react-json-editor-ui" #from 뒤 npm 패키지 이름
    tag = "JsonEditor" #import 뒤 리액트 컴포넌트의 태그 이름
    #리액트 속성에 대응
    data: pc.Var[str] #data
    options_map: pc.Var[str]

    #리액트 이벤트에 대응
    @classmethod
    def get_controlled_triggers(cls):
        return {"on_change": pc.EVENT_ARG} #onChange

json_editor = JsonEditor.create
