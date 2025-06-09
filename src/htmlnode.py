class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not Implemented at the moment")
    
    def props_to_html(self):
        print("props type:", type(self.props), "props value:", self.props)
        if self.props is None:
            return ""
        props = ""
        for key, value in self.props.items():
            props += f" {key}='{value}'"
        return props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return self.tag == other.tag and self.value == other.value
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("Leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return f"{self.value}"
        return f"<{self.tag}{HTMLNode.props_to_html(self)}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Must contain a tag")
        if self.children == None:
            raise ValueError("Must contain children to be parent")
        children_html = ""
        for child in self.children:
            if child.children == None:
                if child.tag is None or child.tag == "":
                    children_html += f"{child.value}"
                else:
                    children_html += f"<{child.tag}{HTMLNode.props_to_html(child)}>{child.value}</{child.tag}>"
            else:
                children_html += ParentNode.to_html(child)
        
        return f"<{self.tag}{HTMLNode.props_to_html(self)}>{children_html}</{self.tag}>"