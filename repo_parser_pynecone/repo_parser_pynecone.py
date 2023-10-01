import reflex as rx

from repo_parser_pynecone.components.add_repo_bar import add_repo_bar
from repo_parser_pynecone.components.repo_list import full_repo_retrieval

from rxconfig import config


backend_url = "http://127.0.0.1:8080"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("RepoParser", font_size="2em"),
            add_repo_bar(),
            rx.divider(),
            rx.text(full_repo_retrieval(base_url=backend_url))
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
