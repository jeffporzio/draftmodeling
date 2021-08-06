from typing import Dict
from flask import render_template

# TODO: Set up oberver pattern and stores for data mangement?  
class WCProperties(object):
    def __init__(self, propsDict: Dict):
        # Set dynamic properties from income dict for nice syntax in .html templates
        for key in propsDict: 
            setattr(self, key, propsDict[key])

    def __repr__(self): 
        output: str = ""
        temp = vars(self)
        for item in temp:
            output += f"{item}  :  {temp[item]}\n\t"
        return output[:-2]

class WebComponent(object):

    def __init__(self, properties: WCProperties, template: str):
        self.properties: WCProperties = properties
        self.template: str = template

    def render(self):
        return render_template(self.template, properties=self.properties)

    def getProperties(self):
        return self.properties

    def setProperties(self, newProps):
        self.properties = newProps