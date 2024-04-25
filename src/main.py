from textnode import TextNode
from generate_page import generate_page


def main():
    generate_page("./content/index.md", "./template.html", "./public/index.html")


main()
