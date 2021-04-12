import asyncio
async def func1():
    while(True):
        print("func1")
        await asyncio.sleep(1)

async def func2():
    while(True):
        print("func2")
        await asyncio.sleep(3)

async def loop_stop():
    await asyncio.sleep(5)
    loop.stop()

loop = asyncio.get_event_loop()
for i in func1(),func2(),loop_stop():
    asyncio.ensure_future(i)
if(not loop.is_running()):
    loop.run_forever()
#loop.close()