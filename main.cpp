#include "MapHandling.hpp"
#include "NamedPipe.hpp"

#include <iostream>

int main() {
	MapHandling m;
	m.setMap();
	std::string send = m.getSMap();

	NamedPipe n;
	if (!n.checkStreams())
		return 1;
	std::cout << "Writing on pipe" << std::endl;
	n.writeOnPipe(send);
	std::cout << "Reading..." << std::endl;
	std::cout << "Data: " << n.readOnPipe() << std::endl;
	return 0;
}