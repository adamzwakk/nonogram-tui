from utils import ConvertImageToPixels, PixelsToText, CalculateClues

from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich import box

imageMatrix = ConvertImageToPixels('./test_images/bowser.png',25,200)
print(PixelsToText(imageMatrix))
print(CalculateClues(imageMatrix['binary']))
quit()
console = Console()
table = Table(show_header=False,box=box.MINIMAL,show_lines=True,padding=0)

for col in imageMatrix['binary']:
   table.add_row(*col)

console.print(table)