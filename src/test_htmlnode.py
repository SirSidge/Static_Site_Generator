import unittest

from htmlnode import HTMLNode, LeafNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href='https://www.google.com'>Click me!</a>")

    def test_leaf_no_value(self):
        node = LeafNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
        node = LeafNode("div", "")
        with self.assertRaises(ValueError):
            node.to_html()
    
if __name__ == "__main__":
    unittest.main()
