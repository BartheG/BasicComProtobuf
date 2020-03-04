import sys, os

from protofiles import file_pb2

class NamedPipeWriteMode:
	def __init__(self, pipName = '/tmp/fifo'):
		self.pipName = pipName
		self.wPipe = open(self.pipName, 'w')

	def __del__(self):
		self.wPipe.close()

	def writeOnPipe(self, toWrite):
		self.wPipe.write(toWrite)

class NamedPipeReadMode:
	def __init__(self, pipName = '/tmp/fifo'):
		self.pipName = pipName
		t_rPipe = os.open(self.pipName, os.O_RDONLY)
		self.rPipe = os.fdopen(t_rPipe)

	def __del__(self):
		self.rPipe.close()

	def readOnPipe(self):
		return self.rPipe.readline()

class NamedPipe:
	def __init__(self, pipName = '/tmp/fifo'):
		self.pipName = pipName
		try:
			os.mkfifo(self.pipName)
			print('FIFO created')
		except OSError:
			print('FIFO already exists')
			pass

	def write(self, toWrite):
		w = NamedPipeWriteMode(self.pipName)
		w.writeOnPipe(toWrite)
		del w

	def read(self):
		r = NamedPipeReadMode(self.pipName)
		data = r.readOnPipe()
		del r
		return data

class ParseData:
	def __init__(self,data):
		self.data = file_pb2.Map()
		self.data.ParseFromString(bytes(data,'utf-8'))

	def run(self,):
		print('Map x:',self.data._x)
		print('Map y:',self.data._y)

def main():
	p = NamedPipe()
	print('Reading...')
	data = p.read()
	ParseData(data).run()
	print('Writing on pipe')
	p.write(data)
	return 0

if __name__ == '__main__':
	sys.exit(main())