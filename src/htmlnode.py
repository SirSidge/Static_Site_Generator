class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not Implemented at the moment")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props = ""
        for key, value in self.props.items():
            props += f" {key}='{value}'"
        return props
    
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
        
    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("Leaf nodes must have a value")
        return f"<{self.tag}{HTMLNode.props_to_html(self)}>{self.value}</{self.tag}>"