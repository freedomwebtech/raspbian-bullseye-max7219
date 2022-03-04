from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from datetime import datetime


serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4, block_orientation=-90, blocks_arranged_in_reverse_order=True)
device.contrast(10)


while True:  
     with canvas(device) as draw:
          now = datetime.now()  
#          text(draw, (0, -1), now.strftime("%H:%M:%S"),fill="red", font=(TINY_FONT))
          
          show_message(device, "Hello Youtube", fill="white",font=(CP437_FONT),scroll_delay=0.08)
          