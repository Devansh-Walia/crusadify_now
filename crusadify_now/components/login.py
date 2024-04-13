import reflex as rx

@rx.page(route="/login")
def login():
    return  rx.center(
   rx.vstack(
    rx.form(
        rx.vstack(
           rx.flex(
                rx.input.root(
                rx.input(
                    name="email_id",
                    placeholder="Enter your email id...",
                    bg="white",
                    style={"padding":"24px"}
                ),
                width="100%",
                style={"margin-bottom":"24px"}
            ),
               rx.input.root(
                rx.input(
                    name="password",
                    placeholder="Enter your password...",
                    bg="white",
                   style={"padding":"24px"}
                ),
                width="100%",
                style={"margin-bottom":"24px"}
            ),
            

            rx.button("Login", style={"padding":"24px"},
                      cursor="pointer"
                      ),
            rx.link("Signup here", href="/signup",style={"padding-top":"24px"},
                        cursor="pointer"
                    ),
            style={"flex-direction":"column","width":"100%"}
           )
        ),
        # on_submit=LoginState.on_submit,
        reset_on_submit=True,
        width="100%",
    ),
      style={"margin": "80px", "width": "50%","padding":"36px", "border-radius":"12px","background-color":"rgba(237, 231, 225)"}
)
    )
