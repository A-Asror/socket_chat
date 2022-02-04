import asyncio
import settings

from MySocked import Socket

from exceptions import SocketException


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()

        self.users = []

    def set_up(self):
        self.socket.bind(settings.SERVER_ADDRESS)

        self.socket.listen(5)
        self.socket.setblocking(False)
        print('Server is listened')

    async def send_data(self, **kwargs):
        for user in self.users:
            try:
                await super(Server, self).send_data(where=user, data=kwargs['data'])
            except SocketException as exc:
                print(exc)
                user.close()

    async def listen_socket(self, listened_socket=None):
        while True:
            try:
                data = await super(Server, self).listen_socket(listened_socket)
                await self.send_data(data=data['data'])
            except SocketException as exc:
                print(exc)
                listened_socket.close()

    async def accept_sockets(self):
        while True:
            user_socked, address = await self.main_loop.sock_accept(self.socket)
            print(f'User <{address[0]}> connected!')

            self.users.append(user_socked)
            self.main_loop.create_task(self.listen_socket(user_socked))

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())




if __name__ == '__main__':
    server = Server()
    server.set_up()

    server.start()
