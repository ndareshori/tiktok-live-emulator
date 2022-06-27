from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
import pyautogui
import pydirectinput


def press_key(key):
    pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)

client: TikTokLiveClient = TikTokLiveClient(
    unique_id="therealv66", **(
        {
            "enable_extended_gift_info": True
        }
    )
)

@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to live ID:", client.room_id)

@client.on("comment")
async def on_connect(event: CommentEvent):
    print(f"{event.user.uniqueId} -> {event.comment}")

    comment = event.comment
    if comment.lower() == "left":
        press_key('left')
    elif comment.lower() == "right":
        press_key('right')
    elif comment.lower() == "down":
        press_key('down')
    elif comment.lower() == "up":
        press_key('up')
    elif comment.lower() == "start":
        press_key('enter')
        print("DDD")
    elif comment.lower() == "a":
        press_key('d')
    elif comment.lower() == "b":
        press_key('s')

dd
if __name__ == '__main__':
    client.run()
    pyautogui.keyDown('a')
