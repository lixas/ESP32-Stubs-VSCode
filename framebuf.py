"""
Module: 'framebuf' on esp32 1.11.0
"""
# MCU: (sysname='esp32', nodename='esp32', release='1.11.0', version='v1.11-580-g973f68780 on 2019-11-17', machine='ESP32 module with ESP32')
# Stubber: 1.3.2

GS2_HMSB = 5
"""Grayscale (2-bit) color format"""

GS4_HMSB = 2
"""Grayscale (4-bit) color format"""

GS8 = 6
"""Grayscale (8-bit) color format"""

MONO_HLSB = 3
"""Monochrome (1-bit) color format This defines a mapping where the bits in a byte are horizontally mapped. Each byte occupies 8 horizontal pixels with bit 0 being the leftmost. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered on the next row, one pixel lower."""

MONO_HMSB = 4
"""Monochrome (1-bit) color format This defines a mapping where the bits in a byte are horizontally mapped. Each byte occupies 8 horizontal pixels with bit 7 being the leftmost. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered on the next row, one pixel lower."""

MONO_VLSB = 0
"""Monochrome (1-bit) color format This defines a mapping where the bits in a byte are vertically mapped with bit 0 being nearest the top of the screen. Consequently each byte occupies 8 vertical pixels. Subsequent bytes appear at successive horizontal locations until the rightmost edge is reached. Further bytes are rendered at locations starting at the leftmost edge, 8 pixels lower."""

MVLSB = 0
RGB565 = 1
"""Red Green Blue (16-bit, 5+6+5) color format"""


class FrameBuffer:
    """
    The FrameBuffer class provides a pixel buffer which can be drawn upon with pixels, lines, rectangles, text and even other FrameBuffer’s. It is useful when generating output for displays.

    Parameters
    ----------
    - buffer : an object with a buffer protocol which must be large enough to contain every pixel defined by the width, height and format of the FrameBuffer;
    - width :  the width of the FrameBuffer in pixels;
    - height : the height of the FrameBuffer in pixels;
    - format : specifies the type of pixel used in the FrameBuffer; permissible values are listed under Constants below. These set the number of bits used to encode a color value and the layout of these bits in buffer. Where a color value c is passed to a method, c is a small integer with an encoding that is dependent on the format of the FrameBuffer;
    - stride=width : the number of pixels between each horizontal line of pixels in the FrameBuffer. This defaults to width but may need adjustments when implementing a FrameBuffer within another larger FrameBuffer or screen. The buffer size must accommodate an increased step size.

    http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer
    """

    def blit(self, fbuf, x, y, key):
        """

        Draw another FrameBuffer on top of the current one at the given coordinates. If key is specified then it should be a color integer and the corresponding color will be considered transparent: all pixels with that color value will not be drawn.

        This method works between FrameBuffer instances utilising different formats, but the resulting colors may be unexpected due to the mismatch in color formats.

        Parameters
        ----------
        - fbuf
        - x
        - y
        - [key]

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.blit
        """
        pass

    def fill(self, c):
        """
        Fill the entire FrameBuffer with the specified color.

        Parameters
        ----------
        - c : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.fill
        """
        pass

    def fill_rect(self, x, y, w, h, c):
        """
        Draw a rectangle at the given location, size and color. The rect method draws only a 1 pixel outline whereas the fill_rect method draws both the outline and interior.

        Parameters
        ----------
        - x
        - y
        - w
        - h
        - c : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.fill_rect
        """
        pass

    def hline(self, x, y, w, c):
        """
        Horizontal line

        Parameters
        ----------
        - x
        - y
        - w
        - c : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.hline
        """
        pass

    def line(self, x1, y1, x2, y2, c):
        """
        Draw a line from a set of coordinates using the given color and a thickness of 1 pixel. The line method draws the line up to a second set of coordinates whereas the hline and vline methods draw horizontal and vertical lines respectively up to a given length.

        Parameters
        ----------
        - x1
        - y1
        - x2
        - y2
        - c : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.line
        """
        pass

    def pixel(self, x, y, c):
        """
        If c is not given, get the color value of the specified pixel. If c is given, set the specified pixel to the given color.

        Parameters
        ----------
        - x
        - y
        - [c] : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.pixel
        """
        pass

    def rect(self, x, y, w, h, c):
        """
        Parameters
        ----------
        - x
        - y
        - w
        - h
        - c : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.rect
        """
        pass

    def scroll(self, xstep, ystep):
        """
        Shift the contents of the FrameBuffer by the given vector. This may leave a footprint of the previous colors in the FrameBuffer.

        Parameters
        ----------
        - xstep
        - ystep

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.scroll
        """
        pass

    def text(self, s, x, y, c):
        """
        Write text to the FrameBuffer using the the coordinates as the upper-left corner of the text. The color of the text can be defined by the optional argument but is otherwise a default value of 1. All characters have dimensions of 8x8 pixels and there is currently no way to change the font.

        Parameters
        ----------
        - string
        - x
        - y
        - [c] : color code

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.text
        """
        pass

    def vline(self, x, y, h, c):
        """
        Parameters
        - x
        - y
        - h
        - c

        http://docs.micropython.org/en/latest/library/framebuf.html#framebuf.FrameBuffer.vline
        """
        pass

def FrameBuffer1():
    pass

