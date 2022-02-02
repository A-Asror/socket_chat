from datetime import datetime
from os import system
import asyncio

from MySocked import Socket
from Encrypt import Encryptor


class Client(Socket):

    def __init__(self):
        super(Client, self).__init__()
        self.messages = ''
        self.encryptor = Encryptor()

    def set_up(self):
        try:
            self.socket.connect(("127.0.0.1", 8000))
            self.socket.setblocking(False)
        except ConnectionRefusedError:
            print('Sorry server is offline')
            exit(0)

    async def listen_socket(self, listened_socked=None):
        while True:
            data = await self.main_loop.sock_recv(self.socket, 2048)
            client_data = self.encryptor.decrypt(data.decode('utf-8'))
            self.messages += f'{datetime.now().date()}: {client_data}\n'

            system('cls')
            print(self.messages)

    async def send_data(self, data=None):
        while True:
            data = await self.main_loop.run_in_executor(None, input)
            encrypted_data = self.encryptor.encrypt(data)
            await self.main_loop.sock_sendall(self.socket, encrypted_data.encode('utf-8'))

    async def main(self):
        await asyncio.gather(
            self.main_loop.create_task(self.listen_socket()),
            self.main_loop.create_task(self.send_data()),
        )


if __name__ == '__main__':
    client = Client()
    client.set_up()

    client.start()