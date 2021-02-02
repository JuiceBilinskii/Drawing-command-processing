#pragma once

#ifndef Display_h
#define Display_h

#include <iostream>
#include "stdio.h"

#include "GraphicsLib.h"

class Display : public GraphicsLib
{
public:
    Display(uint_least16_t w, uint_least16_t h) : GraphicsLib(w, h) {};

    void clearDisplay(uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%cd_%06x@", color);
        sendCommand(buffer);
    };

    void drawPixel(int_least16_t x0, int_least16_t y0, uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%dp_%i_%i_%06x@", x0, y0, color);
        sendCommand(buffer);
    };

    void drawLine(int_least16_t x0, int_least16_t y0, int_least16_t x1, int_least16_t y1, uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%dl_%i_%i_%i_%i_%06x@", x0, y0, x1, y1, color);
        sendCommand(buffer);
    };

    void drawRect(int_least16_t x0, int_least16_t y0, int_least16_t w, int_least16_t h, uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%dr_%i_%i_%i_%i_%06x@", x0, y0, w, h, color);
        sendCommand(buffer);
    };

    void fillRect(int_least16_t x0, int_least16_t y0, int_least16_t w, int_least16_t h, uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%fr_%i_%i_%i_%i_%06x@", x0, y0, w, h, color);
        sendCommand(buffer);
    };

    void drawEllipse(int_least16_t x0, int_least16_t y0, int_least16_t r_x, int_least16_t r_y, uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%de_%i_%i_%i_%i_%06x@", x0, y0, r_x, r_y, color);
        sendCommand(buffer);
    };

    void fillEllipse(int_least16_t x0, int_least16_t y0, int_least16_t r_x, int_least16_t r_y, uint_least32_t color)
    {
        snprintf(buffer, buffer_length, "%%fe_%i_%i_%i_%i_%06x@", x0, y0, r_x, r_y, color);
        sendCommand(buffer);
    };

    char* getCommand(void) { return buffer; };

private:
    static const unsigned char buffer_length = 50;
    char buffer[buffer_length];

    void sendCommand(const char* command) {
        std::cout << "sendCommand: " << command << std::endl;
    }
};

#endif //Display_h
