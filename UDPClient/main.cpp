#include "iostream"
#include "Display.h"
#include <string>
#include <WinSock2.h>
#include <Ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")
using namespace std;


#define SOURCE_IP "127.0.0.1"
#define DESTINATION_IP "127.0.0.2"

#define DEFAULT_PORT 5005
#define BUFFER_SIZE 50

int main(int argc, char** argv)
{
    
    Display display = Display(320, 240);
    std::cout << "width: " << display.getWidth() << " height: " << display.getHeight() << std::endl;

    /*
    display.clearDisplay(RGBConverter(255, 0, 0));

    display.drawPixel(100, 200, RGBConverter(0, 255, 0));
    display.drawLine(100, 150, 200, 250, RGBConverter(0, 255, 0));

    display.drawRect(100, 200, 300, 400, RGBConverter(0, 0, 255));
    display.fillRect(150, 250, 350, 450, RGBConverter(0, 0, 100));

    display.drawEllipse(10, 20, 30, 40, RGBConverter(100, 0, 0));
    display.drawEllipse(110, 120, 130, 140, RGBConverter(20, 0, 0));

    return 0;
    */

    display.drawLine(100, 150, 200, 250, RGBConverter(0, 255, 0));

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

    // send the message
    sendto(s, display.getCommand(), strlen(display.getCommand()), 0, (sockaddr*)&dest, sizeof(dest));

    closesocket(s);
    WSACleanup();

    return 0;
}