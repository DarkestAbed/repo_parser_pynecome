import reflex as rx


def add_repo_bar() -> rx.Component:
    hstack = rx.vstack(
        rx.hstack(
            rx.text("Ingresa la URL de GitHub a guardar:"),
            rx.input(),
            rx.button("Add repo", size="lg")
        )
    )
    return hstack
