import pynecone as pc

'''
#https://www.npmjs.com/package/react-colorful
#react-colorful reactjs 컴포넌트 사용 자바스크립트 코드
import { HexColorPicker } from "react-colorful";

const YourComponent = () => {
  const [color, setColor] = useState("#aabbcc");
  return <HexColorPicker color={color} onChange={setColor} />;
};
'''
class ColorPicker(pc.Component):
    library = "react-colorful" #from 뒤 npm 패키지 이름
    tag = "HexColorPicker" #import 뒤 리액트 컴포넌트의 태그 이름

    @classmethod  
    def get_controlled_triggers(cls):
        return {"on_change"} #onChange -> on_change

color_picker = ColorPicker.create
