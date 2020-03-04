#ifndef NAMEDPIPE_HPP_
    #define NAMEDPIPE_HPP_


//C++ Includes
#include <string>
#include <iostream>
#include <fstream>

//C Includes (mkfifo)
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define ERR_W_STREAM_M "Error while opening mkfifo write stream"
#define ERR_O_MKFIFO_M "Error while opening/create mkfifo"
#define ERR_R_STREAM_M "Error while opening mkfifo read stream"

class NamedPipe {
	public:
		NamedPipe(const std::string &pipName = "/tmp/fifo");
		~NamedPipe();
		bool checkStreams();
		std::string writeOnPipe(const std::string &toWrite);
		std::string readOnPipe();
		bool rtError(const std::string &errMsg);
	private:
		int _fifo;
		std::string _pipName;
		std::shared_ptr<std::ofstream> _wPipe;
		std::shared_ptr<std::ifstream> _rPipe;
		bool _fifoErr;
};

#endif /* !NAMEDPIPE_HPP_ */
