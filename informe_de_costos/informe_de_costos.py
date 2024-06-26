import reflex as rx
import informe_de_costos.styles.styles as styles
from informe_de_costos.views.nav_bar import navbar


def index()-> rx.Component:
    return rx.box(
        navbar(),
        
    )


app = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLE
)
app.add_page(
    index,
    title="Informe de Costos",
    description="Informe de costos discriminado por centro de costo y subcentro de costo"    
    )

app._compile()
