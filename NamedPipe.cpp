#include "NamedPipe.hpp"

NamedPipe::NamedPipe(const std::string &pipName) : _pipName(pipName)
{
	if ((this->_fifo = mkfifo(
		this->_pipName.c_str(),
		S_IWUSR | S_IRUSR | S_IRGRP | S_IROTH
	)) == -1)
		this->_fifoErr = true;
	this->_fifoErr = false;
}

NamedPipe::~NamedPipe() {}

bool NamedPipe::rtError(const std::string &errMsg) {
	std::cout << errMsg << std::endl;
	return false;
}

bool NamedPipe::checkStreams() {
	if (this->_fifoErr)
		return this->rtError(ERR_O_MKFIFO_M);
	return true;
}

std::string NamedPipe::writeOnPipe(const std::string &toWrite) {
	this->_wPipe = std::make_shared<std::ofstream>("/tmp/fifo");
	if (!this->_wPipe->is_open())
		return ERR_W_STREAM_M;
	*this->_wPipe << toWrite;
	this->_wPipe->close();
	return toWrite;
}

std::string NamedPipe::readOnPipe() {
	this->_rPipe = std::make_shared<std::ifstream>("/tmp/fifo");
	if (!this->_rPipe->is_open())
		return ERR_R_STREAM_M;
	std::string line;
	std::getline(*this->_rPipe, line);
	this->_rPipe->close();
	return line;
}