class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_info = ""
        for prop in self.props:
            props_info += f' {prop}="{self.props[prop]}"'
        return props_info
    
    def __repr__(self):
        return (
            f"HTMLNode\n"
            f"tag: {self.tag}\n"
            f"value: {self.value}\n"
            f"children: {self.children}\n"
            f"props: {self.props}"
        )