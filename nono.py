from utils import ConvertImageToPixels, PixelsToText, CalculateClues

from rich.text import Text
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import box

from textual.app import App
from textual.widget import Widget
from textual.reactive import Reactive

class GridItem(Widget):
    mouse_over = Reactive(False)

    def __init__(self, val: bool) -> None:
        self.val = val
        self.t = Text()

    def render(self) -> Text:
        #default to blank
        return self.t

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

    def on_click(self) -> None:
        self.t.text('1')
        self.render()

class Puzzle(Widget):
    imageMatrix = ConvertImageToPixels('./test_images/Boo.jpg',29,200)
    display = imageMatrix['binary']
    clues = CalculateClues(imageMatrix['binary'])
    cheat = PixelsToText(imageMatrix['binary'])

    table = Table(show_header=False,box=box.MINIMAL,show_lines=True,padding=(0,1,0,1))

    # Add top corner blank col before adding column clues
    clues['cols'].insert(0,'')
    table.add_row(*clues['cols'])

    # Add rows to table
    for i,col in enumerate(display):
        items = []
        for j,r in enumerate(col):
            display[i][j] = GridItem(val=r)

    # Insert clues before each row
    for i,r in enumerate(display):
        display[i].insert(0, clues['rows'][i])

    for col in display:
        table.add_row(*col)

    def render(self) -> Panel:
        return Panel(Align.center(self.table,vertical="middle"),title="Puzzle")

    def getCheat(self):
        return self.cheat

class Sidebar(Widget):
    def setCheat(self,cheat):
        self.cheat = cheat

    def render(self) -> Panel:
        return Panel(self.cheat,title="Sidebar")

class NonoApp(App):

    async def on_mount(self) -> None:
        puz = Puzzle()
        sidebar = Sidebar()
        sidebar.setCheat(puz.getCheat())

        grid = await self.view.dock_grid(edge="left", name="left")
        grid.add_column(fraction=3, name="left", min_size=90)
        grid.add_column(min_size=10, name="right")

        grid.add_row(fraction=2, name="middle")

        grid.add_areas(
            puzzle="left,middle",
            sidebar="right,middle"
        )

        grid.place(
            puzzle=puz,
            sidebar=sidebar
        )

NonoApp.run(log="textual.log")