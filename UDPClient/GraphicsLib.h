#pragma once

#ifndef GraphicsLib_h
#define GraphicsLib_h

#include <stdint.h>

#ifndef bit16RGBConverter
//#define RGBConverter(r,g,b) (((r & 0xff) << 16) | ((g & 0xff) << 8) | ((b & 0xff))) //from rgb to 24-bit color code
//#define bit16RGBConverter(r,g,b) (((r << 11 & 0xf800)) | ((g << 5 & 0x7e0)) | ((b & 0x1f))) //from rgb to 16-bit color code
#define bit16RGBConverter(r,g,b) (((r & 0xF8) << 8)|((g & 0xFC) << 3)|((b & 0xF8) >> 3)) //RGB565: 5 red | 6 green | 5 blue
#endif

class GraphicsLib
{
public:
    GraphicsLib(uint_least16_t w, uint_least16_t h) : width(w), height(h) {};

    int_least16_t getWidth(void) { return width; };
    int_least16_t getHeight(void) { return height; };

    virtual void fillScreen(uint_least16_t color) = 0;
    virtual void drawPixel(int_least16_t x0, int_least16_t y0, uint_least16_t color) = 0;
    virtual void drawLine(int_least16_t x0, int_least16_t y0, int_least16_t x1, int_least16_t y1, uint_least16_t color) = 0;
    virtual void drawRect(int_least16_t x0, int_least16_t y0, int_least16_t w, int_least16_t h, uint_least16_t color) = 0;
    virtual void fillRect(int_least16_t x0, int_least16_t y0, int_least16_t w, int_least16_t h, uint_least16_t color) = 0;
    virtual void drawEllipse(int_least16_t x0, int_least16_t y0, int_least16_t r_x, int_least16_t r_y, uint_least16_t color) = 0;
    virtual void fillEllipse(int_least16_t x0, int_least16_t y0, int_least16_t r_x, int_least16_t r_y, uint_least16_t color) = 0;

private:
    int_least16_t width, height; //screen size
};

#endif GraphicsLib_h
