from utils import ConvertImageToPixels, PixelsToText, CalculateClues

from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

from textual.app import App
from textual.widget import Widget

class Puzzle(Widget):
    imageMatrix = ConvertImageToPixels('./test_images/Boo.jpg',30,200)
    display = imageMatrix['binary']
    clues = CalculateClues(imageMatrix['binary'])

    cheat = PixelsToText(imageMatrix['binary'])

    console = Console()
    table = Table(show_header=False,box=box.MINIMAL,show_lines=True,padding=(0,1,0,1))


    # Add top corner blank col before adding column clues
    clues['cols'].insert(0,'')
    table.add_row(*clues['cols'])

    # Insert clues before each row
    for i,r in enumerate(display):
        display[i].insert(0, clues['rows'][i])

    # Add rows to table
    for col in display:
       table.add_row(*col)

    def render(self) -> Panel:
        return Panel(self.table,title="Puzzle")

    def getCheat(self) -> Text:
        return Text(this.cheat)

class Sidebar(Widget):
    def __init__(self, cheat: str) -> None:
        self.cheat = cheat

    def render(self) -> Text:
        return Text(self.cheat)

class NonoApp(App):

    async def on_mount(self) -> None:
        puz = Puzzle()
        sidebar = Sidebar(cheat=puz.cheat)
        await self.view.dock(puz, edge="top")
        #await self.view.dock(sidebar, edge="right")

NonoApp.run(log="textual.log")