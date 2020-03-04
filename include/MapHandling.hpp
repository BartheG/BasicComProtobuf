#ifndef MAPHANDLING_HPP_
    #define MAPHANDLING_HPP_

#include "file.pb.h"

#include <memory>

class MapHandling {
	public:
		MapHandling(int x = 20, int y = 1);
		~MapHandling();
		std::string getSMap() { this->_map->SerializeToString(&this->_s_map); return this->_s_map; }
		void setMap();
	private:
		int _x;
		int _y;
		std::shared_ptr<pb::Map> _map;
		std::string _s_map;
};

#endif /* !MAPHANDLING_HPP_ */
