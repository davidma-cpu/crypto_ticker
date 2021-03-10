import os

from rgbmatrix import graphics
from cryptofeed.rest.coinbase import Coinbase

from samplebase import SampleBase


FONTS_PATH = r'/home/pi/rpi-rgb-led-matrix/fonts'


class CryptoTickerDisplay(SampleBase):

    def __init__(self, *args, **kwargs):
        super(CryptoTickerDisplay, self).__init__(*args, **kwargs)

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont(os.path.join(FONTS_PATH, "5x8.bdf"))
        green_color = graphics.Color(0, 128, 0)
        red_color = graphics.Color(255, 0, 0)
        btc_price_old = 0
        eth_price_old = 0

        coinbase = Coinbase()

        while True:
            offscreen_canvas.Clear()
            btc_price = coinbase.ticker('BTC-USD')['bid']
            eth_price = coinbase.ticker('ETH-USD')['bid']
            if btc_price > btc_price_old:
                btc_color = green_color
            else:
                btc_color = red_color
            if eth_price > eth_price_old:
                eth_color = green_color
            else:
                eth_color = red_color
            btc_price_old = btc_price
            eth_price_old = eth_price
            graphics.DrawText(offscreen_canvas, font, 2, 12, btc_color, f"BTC:{btc_price}")
            graphics.DrawText(offscreen_canvas, font, 2, 24, eth_color, f"ETH:{eth_price}")
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


if __name__ == "__main__":
    crypto_ticker_display = CryptoTickerDisplay()
    crypto_ticker_display.process()