import asyncio
from functools import partial
from aio_pika import connect, IncomingMessage, Exchange, Message


def echo_string(n):
    """ Возвращает переданное клиентом int число * 10
        Типы значений не проверяются.
    """
    return n * 10


async def on_message(exchange: Exchange, message: IncomingMessage):
    with message.process():
        n = int(message.body.decode())
        response = str(echo_string(n)).encode()

        await exchange.publish(
            Message(
                body=response,
                correlation_id=message.correlation_id
            ),
            routing_key=message.reply_to,
        )
        print("Request complete")


async def main(loop):
    connection = await connect(
        "amqp://guest:guest@localhost/", loop=loop
    )
    channel = await connection.channel()
    queue = await channel.declare_queue("rpc_queue")
    await queue.consume(partial(
        on_message, channel.default_exchange)
    )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    print("Ожидание RPC запроса...")
    loop.run_forever()
