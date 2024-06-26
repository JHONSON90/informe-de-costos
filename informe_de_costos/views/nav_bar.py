import reflex as rx
from informe_de_costos.const.const import NOMBRE
from informe_de_costos.styles.fonts import FontWeight
from informe_de_costos.styles.styles import Size, Spacing
from informe_de_costos.styles.colors import Color


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, 
                weight= Size.LARGE.value,
                color= Color.SECUNDARY.value
                ), 
        href=url,
        
    )

def navbar() -> rx.Component:
    
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        NOMBRE,
                        size="8",
                        weight="bold",
                        padding = Spacing.BIG.value                         
                    ), 
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/home"),
                    navbar_link("About", "/about"),                
                    justify="end",
                    spacing= "5",
                ),
                justify="between",
                align_items="center",
            ),
            ),
        
        rx.mobile_and_tablet(
             rx.hstack(
                rx.hstack(
                    rx.heading(
                        NOMBRE,    
                        size="7",  
                        weight="bold",                                           
                    ), 
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size= 30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About")
                ), 
                    justify = "end",
                
                ),
                justify="between",
                align_items="center",
            ),
            ),
         bg= rx.color("black", 3),#'gray','mauve','slate','sage','olive','sand','tomato','red','ruby','crimson','pink','plum','purple','violet','iris','indigo','blue','cyan','teal','jade','green','grass','brown','orange','sky','mint','lime','yellow','amber','gold','bronze','accent','black','white'
         padding= Size.SMALL.value,
         width="100%",         
        )
    