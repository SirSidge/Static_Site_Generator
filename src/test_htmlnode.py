import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_value(self):
        node = HTMLNode("div", "Testing the htmlnode")
        self.assertEqual(
            node.tag, 
            "div",
            )
        self.assertEqual(
            node.value,
            "Testing the htmlnode",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_props_to_html(self):
        node = HTMLNode.props_to_html(HTMLNode("a", "Prop to html test", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        }))
        self.assertEqual(node, " href='https://www.google.com' target='_blank'")

    def test_repr(self):
        node = HTMLNode("a", "Prop to html test", None, {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(repr(node), "HTMLNode(a, Prop to html test, None, {'href': 'https://www.google.com', 'target': '_blank'})")
    
if __name__ == "__main__":
    unittest.main()
