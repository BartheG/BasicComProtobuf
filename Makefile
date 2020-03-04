CC      = 	g++

NAME    =	cpp_file

SRC     =	main.cpp	\
			MapHandling.cpp	\
			NamedPipe.cpp	\
			protofiles/file.pb.cpp

OBJ     = 	$(SRC:.cpp=.o)

RM      = 	rm -rf

CPPFLAGS	+=	-Wall -Wextra -I./include/ -I./protofiles/ -std=c++17

all:    $(NAME)

$(NAME):        $(OBJ)
	$(CC) $(OBJ) -o $(NAME) $(CPPFLAGS) -lprotobuf

clean:
	$(RM) $(OBJ)

fclean:
	$(RM) $(NAME) $(OBJ)

re: fclean all