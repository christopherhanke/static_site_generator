class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        new_html = ""
        for prop in self.props:
            new_html = new_html + " " + prop + "=\"" + self.props[prop] + "\""
        return new_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        new_string = "<" + self.tag
        if self.props != None:
            new_string += self.props_to_html()
        new_string += ">" + self.value + "</" + self.tag + ">"
        return new_string


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: no tag")
        if self.children == None:
            raise ValueError("Invalid HTML: no children")
        new_string = "<" + self.tag
        if self.props != None:
            new_string += self.props_to_html()
        new_string += ">"
        for child in self.children:
            new_string += child.to_html()
        new_string += "</" + self.tag + ">"
        return new_string



        