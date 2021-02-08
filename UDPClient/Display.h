#pragma once

#ifndef Display_h
#define Display_h

#include <iostream>
#include "stdio.h"
#include <Ws2tcpip.h>


#include "GraphicsLib.h"

#ifndef bit24_16Converter
//#define bit24_16RGBConverter(colour) (((((colour & 0xf800) >> 11) * 527 + 23) >> 6 << 16) | ((((colour & 0x7e0) >> 5) * 259 + 33) >> 6 << 8) | (((colour & 0x1f) * 527 + 33) >> 6)) //from 16-bit to 24-bit color code
#define bit24_16RGBConverter(colour) ((((color & 0xf800) >> 11 << 3) | (color & 0xf800) >> 11 >> 2) << 16) | ((((color & 0x7e0) >> 5 << 2) | (color & 0x7e0) >> 5 >> 4) << 8) | (((color & 0x1f) >> 0 << 3 | (color & 0x1f) >> 2) << 0) //from 16-bit to 24-bit color code
#endif

class Display : public GraphicsLib
{
public:
    Display(uint_least16_t w, uint_least16_t h, SOCKET* s, sockaddr* dest) : GraphicsLib(w, h), socket(s), dest(dest) {};

    void fillScreen(uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%cd_%06x@", bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    void drawPixel(int_least16_t x0, int_least16_t y0, uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%dp_%i_%i_%06x@", x0, y0, bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    void drawLine(int_least16_t x0, int_least16_t y0, int_least16_t x1, int_least16_t y1, uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%dl_%i_%i_%i_%i_%06x@", x0, y0, x1, y1, bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    void drawRect(int_least16_t x0, int_least16_t y0, int_least16_t w, int_least16_t h, uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%dr_%i_%i_%i_%i_%06x@", x0, y0, w, h, bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    void fillRect(int_least16_t x0, int_least16_t y0, int_least16_t w, int_least16_t h, uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%fr_%i_%i_%i_%i_%06x@", x0, y0, w, h, bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    void drawEllipse(int_least16_t x0, int_least16_t y0, int_least16_t r_x, int_least16_t r_y, uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%de_%i_%i_%i_%i_%06x@", x0, y0, r_x, r_y, bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    void fillEllipse(int_least16_t x0, int_least16_t y0, int_least16_t r_x, int_least16_t r_y, uint_least16_t color)
    {
        snprintf(buffer, buffer_length, "%%fe_%i_%i_%i_%i_%06x@", x0, y0, r_x, r_y, bit24_16RGBConverter(color));
        sendCommand(buffer);
    };

    //char* getCommand(void) { return buffer; };

private:
    static const unsigned char buffer_length = 50;
    char buffer[buffer_length];

    SOCKET* socket;
    sockaddr* dest;

    void sendCommand(const char* command) {
        sendto(*socket, command, strlen(command), 0, dest, sizeof(*dest));
        std::cout << "sendCommand: " << command << std::endl;
    }
};

#endif //Display_h
