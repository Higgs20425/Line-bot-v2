from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, ImagemapSendMessage, LocationSendMessage, BaseSize,
    Video, ImagemapArea, ExternalLink, URIImagemapAction, MessageImagemapAction, TemplateSendMessage, CarouselTemplate,
    CarouselColumn, PostbackAction, MessageAction, URIAction, ImageSendMessage
)
import webbrowser
from rsp import Rsp

app = Flask(__name__)

line_bot_api = LineBotApi(
    'kgbpKtdwPWMexRaCUBqIPFveRllZwfk7mROn1M1Z9mGDO37bbh/xtFq+UTCWMoeSN+OaLwYJl6N3ZYhv7Jimndn6n59XxRB1paI92wGcEjUfjPs2ZEy4z0VkPOYfr5aEWiecRrKfWv0kb7Jv9C6jbAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('ddbe30c10b53bebb600cbff244416c51')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    if msg == '梗圖':
        r = Rsp.memes_rsp()
        image_message = ImageSendMessage(
            original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
            preview_image_url='https://i.imgur.com/' + r + '.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    else:
        r = Rsp(msg).words_rsp()
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=r))
    # image_message = ImageSendMessage(
    #     original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
    #     preview_image_url='https://i.imgur.com/' + meme_id + '.jpg'
    # )
    #
    # line_bot_api.reply_message(event.reply_token, image_message)
    # if '梗圖' in msg:
    #     meme_id = pick_up_memes()
    #     image_message = ImageSendMessage(
    #         original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
    #         preview_image_url='https://i.imgur.com/' + meme_id + '.jpg'
    #     )
    #
    #     line_bot_api.reply_message(event.reply_token, image_message)
    #     return
    #
    # elif '在一句' in msg or '再一句' in msg:
    #     image_message = ImageSendMessage(
    #         original_content_url='https://i.imgur.com/tN7r7Xb.jpg',
    #         preview_image_url='https://i.imgur.com/SNw6cKV.jpg'
    #     )
    #
    #     line_bot_api.reply_message(event.reply_token, image_message)
    #     return
    #
    # elif '爬山' in msg:
    #     sticker_message = StickerSendMessage(
    #         package_id='789',
    #         sticker_id='10871'
    #     )
    #
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         sticker_message)
    #     return
    #
    # elif '凍未條' in msg or '憋不住啦' in msg or '憋不住' in msg:
    #     sticker_message = StickerSendMessage(
    #         package_id='446',
    #         sticker_id='2026'
    #     )
    #
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         sticker_message)
    #     return
    #
    # if msg == '酒吧 大安' in msg:
    #     carousel_template_message = TemplateSendMessage(
    #         alt_text='喝酒囉',
    #         template=CarouselTemplate(
    #             columns=[
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipOS1tOjI9741_1PjzmeuAsgE_LNggaGoTit0k81=w203-h270-k-no',
    #                     title='昨天 Bistro & Flavor',
    #                     text='每次都去這間?',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback1',
    #                         #     display_text='postback text1',
    #                         #     data='action=buy&itemid=1'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message1',
    #                         #     text='message text1'
    #                         # ),
    #                         URIAction(
    #                             label='Google Maps',
    #                             uri='https://reurl.cc/1gW80X'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://lh3.ggpht.com/p/AF1QipN3S5wnwsD71dVC_psP2GAlhJW42pFPlRvoUjQ5=s1536',
    #                     title='Intention',
    #                     text='尻Shot這邊請?',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='Google Maps',
    #                             uri='https://reurl.cc/v5xEke'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://lh3.ggpht.com/p/AF1QipNB1wIbgmTFzmQNujlcoJWW0Ys7OONlr-MV5ZbI=s1536',
    #                     title='Book ing bar',
    #                     text='Is it good to drink？ 謀哩崊跨賣馬',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='Google Maps',
    #                             uri='https://reurl.cc/raV05k'
    #                         )
    #                     ]
    #                 )
    #             ]
    #         )
    #     )
    #
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         carousel_template_message)
    #     return
    #
    # elif msg == '酒吧 信義':
    #     carousel_template_message = TemplateSendMessage(
    #         alt_text='喝酒囉',
    #         template=CarouselTemplate(
    #             columns=[
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://lh3.ggpht.com/p/AF1QipNoR50HukTk4v9v3vLlN8bdoDmzF8EZzC17qjJM=s1536',
    #                     title='Odin信義放感情',
    #                     text='餐酒館推薦 平價調酒酒吧 bar bistro 人氣特色餐酒美食推薦 網美酒吧',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback1',
    #                         #     display_text='postback text1',
    #                         #     data='action=buy&itemid=1'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message1',
    #                         #     text='message text1'
    #                         # ),
    #                         URIAction(
    #                             label='Google Maps',
    #                             uri='https://reurl.cc/Agl9AY'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://lh5.googleusercontent.com/p/AF1QipOY9Oan3beqkLkr2HVEGVqLqtM5ZwUYiphgAuEQ=s387-k-no',
    #                     title='榕 RON Xinyi',
    #                     text='吃寶飽煲去的那間的信義分店',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='Google Maps',
    #                             uri='https://reurl.cc/Xeb2E0'
    #                         )
    #                     ]
    #                 )
    #             ]
    #         )
    #     )
    #
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         carousel_template_message)
    #     return
    #
    # elif msg == '景點 嘉義':
    #     carousel_template_message = TemplateSendMessage(
    #         alt_text='@小哈',
    #         template=CarouselTemplate(
    #             columns=[
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://pic.pimg.tw/as660707/1507707816-3005797788_l.jpg',
    #                     title='愛木村休閒觀光工廠',
    #                     text='館內還有許多特色場景，讓旅人取景紀念親子來訪，也能體驗手作DIY唷',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback1',
    #                         #     display_text='postback text1',
    #                         #     data='action=buy&itemid=1'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message1',
    #                         #     text='message text1'
    #                         # ),
    #                         URIAction(
    #                             label='發車囉',
    #                             uri='https://reurl.cc/dVb56z'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://pic.pimg.tw/emily561025/1540898548-3106265433.jpg',
    #                     title='大埔情人公園',
    #                     text='位在嘉義的情人公園 佔地寬敞，景色幽美，旁邊就是曾文水庫 廣場以紅色花園為主題',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='立馬導航',
    #                             uri='https://reurl.cc/KxzxKn'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://decing.tw/wp-content/uploads/20200914152739_61.jpg',
    #                     title='嘉義市立美術館',
    #                     text='嘉義市立美術館成為歷史與當代場域的交匯點， 也是「嘉義文化新絲路」上的一道古典且新穎的風景。',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='飆風馬',
    #                             uri='https://reurl.cc/l0b0oY'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://img.fullfenblog.tw/20200310131442_80.jpg',
    #                     title='龍王金殿',
    #                     text='龍王金殿位在群山峻嶺的森林之中 金碧輝煌的唐宋建築，好似京都金閣寺 四周環山，還有一整片壯麗的茶田風光',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='忍不住前往',
    #                             uri='https://reurl.cc/GdqdXA'
    #                         )
    #                     ]
    #                 ),
    #                 CarouselColumn(
    #                     thumbnail_image_url='https://www.welcometw.com/wp-content/uploads/2020/09/S__26083409-850x638.jpg',
    #                     title='太平雲梯 遊客服務中心(附設餐廳、茶體驗、茶料理)',
    #                     text='太平雲梯長度281公尺、海拔約1000公尺，為全台最長、海拔最高之景觀吊橋。',
    #                     actions=[
    #                         # PostbackAction(
    #                         #     label='postback2',
    #                         #     display_text='postback text2',
    #                         #     data='action=buy&itemid=2'
    #                         # ),
    #                         # MessageAction(
    #                         #     label='message2',
    #                         #     text='message text2'
    #                         # ),
    #                         URIAction(
    #                             label='行程跑起來',
    #                             uri='https://reurl.cc/pmbmrd'
    #                         )
    #                     ]
    #                 )
    #             ]
    #         )
    #     )
    #
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         carousel_template_message)
    #     return


if __name__ == "__main__":
    app.run()
