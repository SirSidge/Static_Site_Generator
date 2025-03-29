import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_nested_children(self):
        child_node = LeafNode("div", "Click me!")
        child_node2 = LeafNode("c", "Final value")
        child_node3 = ParentNode("a", [child_node, child_node2])
        node = ParentNode("p", [child_node3,])
        self.assertEqual(node.to_html(), "<p><a><div>Click me!</div><c>Final value</c></a></p>")

        node2 = ParentNode("p", [child_node,])
        self.assertEqual(node2.to_html(), f"<p><div>Click me!</div></p>")
    
    def test_children_props(self):
        child_node = LeafNode("b", "I don't have children", {"href": "www.boot.dev"})
        child_node2 = ParentNode("div", [child_node,])
        node = ParentNode("d", [child_node2,])
        self.assertEqual(node.to_html(), f"<d><div><b href='www.boot.dev'>I don't have children</b></div></d>")
    
if __name__ == "__main__":
    unittest.main()
