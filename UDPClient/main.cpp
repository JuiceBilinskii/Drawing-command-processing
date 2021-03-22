#include "iostream"
#include "Display.h"
#include <string>
#include <WinSock2.h>
#include <Ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")
using namespace std;


#define SOURCE_IP "192.168.1.120"
#define DESTINATION_IP "192.168.1.121"

#define DEFAULT_PORT 5005
#define BUFFER_SIZE 50

int main(int argc, char** argv)
{
    sockaddr_in dest;
    sockaddr_in local;
    WSAData data;
    WSAStartup(MAKEWORD(2, 2), &data);

    local.sin_family = AF_INET;
    inet_pton(AF_INET, SOURCE_IP, &local.sin_addr.s_addr);
    local.sin_port = htons(0);

    dest.sin_family = AF_INET;
    inet_pton(AF_INET, DESTINATION_IP, &dest.sin_addr.s_addr);
    dest.sin_port = htons(5005);

    // create the socket
    SOCKET s = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    // bind to the local address
    bind(s, (sockaddr*)&local, sizeof(local));



    Display display = Display(300, 200, (SOCKET*)&s, (sockaddr*)&dest);
    std::cout << "width: " << display.getWidth() << " height: " << display.getHeight() << std::endl;

    for (int i = 0; i < 10; i++)
    {
        display.fillScreen(bit16RGBConverter(0, 0, 0));
        //display.drawLine(70, 110, 10, 15, bit16RGBConverter(255, 0, 150));
        //display.drawEllipse(110, 120, 130, 140, bit16RGBConverter(0, 220, 78));
        //display.fillEllipse(0, 0, 60, 60, bit16RGBConverter(255, 255, 0));
        display.fillEllipse(250, 50, 60, 60, bit16RGBConverter(255, 255, 0));
        display.fillEllipse(265, 50, 50, 50, bit16RGBConverter(0, 0, 0));

        //голова
        display.fillEllipse(150, 100, 30, 30, bit16RGBConverter(255, 255, 255));
        display.fillRect(140, 105, 20, 3, bit16RGBConverter(0, 0, 0));
        display.fillEllipse(140, 100, 4, 4, bit16RGBConverter(0, 0, 0));
        display.fillEllipse(160, 100, 4, 4, bit16RGBConverter(0, 0, 0));

        //туловище
        display.fillEllipse(150, 150, 50, 80, bit16RGBConverter(255, 255, 255));

        //ноги
        display.fillRect(85, 170, 65, 10, bit16RGBConverter(255, 255, 255));
        display.fillRect(85, 180, 10, 10, bit16RGBConverter(255, 255, 255));
        display.fillRect(150, 170, 65, 10, bit16RGBConverter(255, 255, 255));
        display.fillRect(205, 180, 10, 10, bit16RGBConverter(255, 255, 255));

        if (i % 2 == 0)
        {
            //руки вверх
            display.fillRect(85, 130, 65, 10, bit16RGBConverter(255, 255, 255));
            display.fillRect(85, 120, 10, 10, bit16RGBConverter(255, 255, 255));
            display.fillRect(150, 130, 65, 10, bit16RGBConverter(255, 255, 255));
            display.fillRect(205, 120, 10, 10, bit16RGBConverter(255, 255, 255));
        }
        else
        {
            //руки вниз
            display.fillRect(85, 130, 65, 10, bit16RGBConverter(255, 255, 255));
            display.fillRect(85, 140, 10, 10, bit16RGBConverter(255, 255, 255));
            display.fillRect(150, 130, 65, 10, bit16RGBConverter(255, 255, 255));
            display.fillRect(205, 140, 10, 10, bit16RGBConverter(255, 255, 255));
        }

        Sleep(500);
    }

    closesocket(s);
    WSACleanup();

    return 0;
}