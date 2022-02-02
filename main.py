from MySocked import Socket
import asyncio


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()

        self.users = []

    def set_up(self):
        self.socket.bind(('127.0.0.1', 8000))

        self.socket.listen(5)
        self.socket.setblocking(False)
        print('Server is listened')

    async def send_data(self, data=None):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data)

    async def listen_socket(self, listened_socket=None):
        if not listened_socket:
            return

        while True:
            try:
                data = await self.main_loop.sock_recv(listened_socket, 2048)
                print(data.decode('utf-8'))
                await self.send_data(data)
            except Exception:
                print('Client removed')
                self.users.remove(listened_socket)
                return

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
