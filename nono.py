from utils import ConvertImageToPixels, PixelsToText, CalculateClues

from rich.text import Text
from rich.console import Console
from rich.table import Table
from rich import box

imageMatrix = ConvertImageToPixels('./test_images/Boo.jpg',30,200)
display = imageMatrix['binary']
clues = CalculateClues(imageMatrix['binary'])

#print(PixelsToText(imageMatrix['binary']))

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


console.print(table)