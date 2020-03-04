#include "MapHandling.hpp"

MapHandling::MapHandling(int x, int y) : _x(x), _y(y) {
	GOOGLE_PROTOBUF_VERIFY_VERSION;
	_map = std::make_shared<pb::Map>();
}

MapHandling::~MapHandling() {}

void MapHandling::setMap() {
	this->_map->set__x(this->_x);
	this->_map->set__y(this->_y);
}