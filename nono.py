from utils import ConvertImageToPixels, PixelsToText, CalculateClues

from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich import box

imageMatrix = ConvertImageToPixels('./test_images/bowser.png',25,200)
print(PixelsToText(imageMatrix))
clues = CalculateClues(imageMatrix['binary'])

console = Console()
table = Table(show_header=False,box=box.MINIMAL,show_lines=True,padding=(0,1,0,1))

table.add_row(*clues['cols'])

display = imageMatrix['binary']

for i,r in enumerate(display):
    display[i].insert(0, clues['rows'][i])

for col in display:
   table.add_row(*col)

console.print(table)