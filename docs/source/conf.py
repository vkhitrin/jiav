from datetime import datetime

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.viewcode",
    "sphinxcontrib.video",
    "sphinxcontrib.mermaid",
]
templates_path = ["_templates"]
html_static_path = ["_static"]

source_suffix = ".rst"
master_doc = "index"

project = "jiav"
copyright = f"{datetime.now().year}, vkhitrin"
html_static_path = ["_static"]
author = "Vadim Khitrin"

language = "en"

html_theme = "alabaster"
html_sidebars = {
    "**": [
        "about.html",
        "searchfield.html",
        "navigation.html",
    ]
}
html_theme_options = {
    "description": "Jira Issue Auto Verification",
}
