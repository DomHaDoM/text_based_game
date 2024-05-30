from sys import version
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
    , CupertinoAppBar
    , icons
)

from assets.game import Game, version as game_version
from assets.chest import Chest

def main(page: Page):

    page.title = "Text Based Game"
    page.theme_mode = "dark"
    page.vertical_alignment = MainAxisAlignment.CENTER
    app_version: str = "0.1"

    game_difficulty: str = None

    game_settings = Text("")

    def show_game_settings(e) -> None:
        game = Game(game_difficulty)
        game_settings.value = game.current_settings
        page.update()

    def handle_change(e) -> None:
        nonlocal game_difficulty
        try:
            sel = int(list(difficulty_selector.selected)[0])
        except:
            sel = None
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
    opened_chests: int = 0
    total_chests: int = 10
    result = Text("")

    def open_chest(e):
        nonlocal opened_chests, total_chests
        if total_chests > 0:
            chest_btn.disabled = False
            opened_chests += 1
            total_chests -= 1
            a = Chest("sword")
            result.value = f"{a.item}\nTotal opened chests: {opened_chests}"
        else:
            chest_btn.disabled = True
            result.value = f"No chests avaliable"
        page.update()

    chest_btn = ElevatedButton("Open Chest", on_click=open_chest)

    game_page = Row(
        [
            Column(
                [
                    Text("Game Page")
                    , difficulty_selector
                    , game_btn
                    , chest_btn
                    , result
                    , game_settings
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

    # Function to create a starting page
    def open_starting_page(e) -> None:
        page.clean()
        page.add(starting_page)
        page.update()

    # function to change theme and icon depending on current theme
    def change_theme(e):
        if page.theme_mode == "dark":
            theme_button.icon = icons.SUNNY
            page.theme_mode = "light"
        else:
            theme_button.icon = icons.NIGHTLIGHT_ROUND
            page.theme_mode = "dark"
        page.update()

    # Button to change page theme mode
    theme_button = IconButton(
        icon=icons.NIGHTLIGHT_ROUND
        , on_click=change_theme
    )

    # Appbar for all pages
    page.appbar = CupertinoAppBar(
        leading=IconButton(
            icon=icons.HOME_FILLED
            , on_click=open_starting_page
        )
        , trailing=theme_button
    )
    

    version = Row([Text(f"App Version: v{app_version}\nGame Version: v{game_version}")], alignment=MainAxisAlignment.CENTER)

    page.add(
        starting_page
        , version
        )
app(main)