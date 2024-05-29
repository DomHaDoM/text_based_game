from flet import (
    app
    , Page
    , Row
    , Column
    , Text
    , ElevatedButton
    , IconButton
    , SegmentedButton, Segment
    , MainAxisAlignment
    , AppBar
    , icons
)

from assets.game import Game

def main(page: Page):

    page.title = "Text Based Game"
    page.theme_mode = "dark"
    page.vertical_alignment = MainAxisAlignment.CENTER

    game_difficulty: str = None


    def show_game_settings(e) -> None:
        game = Game(game_difficulty)
        page.add(Row([Text(game.current_settings)] , alignment=MainAxisAlignment.CENTER))
        page.update()

    def handle_change(e) -> None:
        nonlocal game_difficulty
        sel = int(list(difficulty_selector.selected)[0])
        if sel is not None:
            game_btn.disabled = False
            if sel == 1:
                game_difficulty = "easy"
            elif sel == 2:
                game_difficulty = "medium"
            elif sel == 3:
                game_difficulty = "hard"
            elif sel == 4:
                game_difficulty = "insane"
        else:
            game_btn.disabled = True
            game_difficulty = None
        page.update()
            

    difficulty_selector = SegmentedButton(
                        on_change=handle_change
                        , selected={}
                        , allow_empty_selection=True
                        , allow_multiple_selection=False
                        , segments=[
                            Segment(
                                value="1"
                                , label=Text("Easy")
                                )
                            , Segment(
                                value="2"
                                , label=Text("Medium")
                                )
                            , Segment(
                                value="3"
                                , label=Text("Hard")
                                )
                            , Segment(
                                value="4"
                                , label=Text("Insane")
                                )
                            ]
                        )
    
    game_btn = ElevatedButton("Start the game"
                              , disabled=True
                              , on_click=show_game_settings
                              )

    game_page = Row(
        [
            Column(
                [
                    Text("Game Page")
                    , difficulty_selector
                    , game_btn
                ]
            )
        ], alignment=MainAxisAlignment.CENTER
    )

    def open_game_page(e):
        page.clean()
        page.add(game_page)
        page.update()

    starting_page = Row(
        [
            Column(
                [
                    Text(f"Welcome to {page.title.title()}")
                    , ElevatedButton("Start", on_click=open_game_page)
                ]
            )
        ], alignment=MainAxisAlignment.SPACE_AROUND
    )

    def open_starting_page(e) -> None:
        page.clean()
        page.add(starting_page)
        page.update()

    page.appbar = AppBar(
        leading=IconButton(
            icon=icons.HOME_FILLED
            , on_click=open_starting_page
        )
    )
    
    page.add(
        starting_page
        )
app(main)