import random

#gregergerge
class Rsp:
    def __init__(self):
        pass

    @staticmethod
    def words_rsp(msg):
        keys = {'胞弟': ['雙飛雙飛!', '要驗喔', '有房有老婆 有小孩?', '又在說胞弟壞話?', '壓進去喔', '我就是要雷你'], '老闆': ['石頭開大囉', '把你抱起來X', '就是這麼簡單'],
                '撈半': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'],
                '撈伴': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'],
                '指紋': ['石頭開大囉', '把你抱起來X', 'Hulk Smash!!!', '就是這麼簡單'],
                '有啥好吃': ['源坐?', '葛利麵吃爆?', '背包客?', '鴨肉李伺候?', '米干?', '下次吃茶六?', '碳佐再來?', '伊莉會館海鮮?'],
                '真的來了': ['當天再約?', '真的來了餒'],
                '意義': ['有意義沒逸逸'], '沒聲音': ['人走茶涼啦'], '會癢': ['要驗喔'], '不好說': ['不想說都不要說'], '笑死': ['死了沒?', '不要真的笑死餒'],
                '羊肉炒飯': ['真香', '身體很誠實'],
                '沒啥好吃': ['源坐?', '葛利麵吃爆?', '背包客?', '鴨肉李伺候?', '米干?', '下次吃茶六?', '碳佐再來?', '伊莉會館海鮮?'],
                '韓導': ['喔氣氣氣氣氣', '征服宇宙', '當個塞子', '可憐啊', '高雄發大財', '莫忘世上苦人多', '鳳凰都飛走了 進來一大堆雞'],
                '韓國': ['喔氣氣氣氣氣', '征服宇宙', '當個塞子', '可憐啊', '高雄發大財', '莫忘世上苦人多', '鳳凰都飛走了 進來一大堆雞'],
                '韓總': ['喔氣氣氣氣氣', '征服宇宙', '當個塞子', '可憐啊', '高雄發大財', '莫忘世上苦人多', '鳳凰都飛走了 進來一大堆雞'],
                '等等': ['麻吉得', '等殺小', '進棺材等?', '等投胎?'], '股票': ['林北台積電沒在賣', '這裡不談史塔克', 'all money back me home'],
                '買哪': ['跌了你也不敢買', '麗臺 @江忠諭', '長榮 @江忠諭'], '狗狗': ['to the moon', '@林老闆'], '推薦': ['@越南小哥?', '給你推薦好的'],
                'will': ['大家好 我是will', '歡迎來到X調查', '故事的主人公名叫: '], '大戶': ['誰找林老闆', '@胖安', '@林老闆'],
                '最敢': ['還是要帶套啦', '有我們ㄅ緯敢?', '有我們逸逸衝?'], '結婚': ['弄出人命?', '帶卡崔來吃?'], '要加': ['手打+500', '沒台錢了?'],
                '刷': ['刷卡加一成', '先刷賺回饋'],
                '硬': ['@ㄅ緯', '也不用動刀動槍啦', '廁所處理?', '-3000'], '虧': ['少去一次', '嗯?', 'all money back me home'],
                '窮': ['去跟你老闆談', '蔡英文不用負責?', 'all money back me home'], '蛇': ['消防隊姓楊的不抓蛇啦', '蔡英文~~', '馬英九哦'],
                '豆花': ['我的豆花30塊'],
                'ㄅ偉': ['辣個男人', '手機要接喔', 'coffee snake'], 'ㄅ緯': ['辣個男人', '手機要接喔', 'coffee snake'],
                'ㄅ委': ['辣個男人', '手機要接喔', 'coffee snake'], 'ㄅ尾': ['辣個男人', '手機要接喔', 'coffee snake'],
                '加非': ['one coffee snake', '下午來一杯?', '再補一點'], '加飛': ['one coffee snake', '下午來一杯?', '再補一點'],
                '咖啡': ['one coffee snake', '下午來一杯?', '再補一點'], '家非': ['one coffee snake', '下午來一杯?', '再補一點'],
                '家飛': ['one coffee snake', '下午來一杯?', '再補一點'], '投資': ['all money back me home', '這裡不談史塔克', '林北台積電沒在賣'],
                '檳榔': ['他說9粒50欸'],
                '羽球': ['羽球沒人在打一個小時的', 'ㄅ緯幫買個水'], '借錢': ['又要去喜來登?'], '基隆夜市': ['再提22號滷肉飯試試看'],# '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                # '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''], '': ['', '', ''],
                '諭哥': ['諭哥沒在上班啦!', '還在台東啦...', '省500', '什麼時候北上', '小孩長的像你', '在台東啦'],
                '小業': ['RAV4準備開出來了!', '準備做壞事? @13姨', '拒絕熊貓', '很奧豆?'], '逸逸': ['在釣魚啦!', '@小哈'],  ###開始
                '呆寶': ['電腦砸了 遊戲刪了', '轉速拉起來'], '偉航': ['辣個賺十萬的男人', '再牽一台啦', '三鐵報好玩的啦', '五天五次'],
                '胖安': ['這很林老闆', '退休了啦', '幫買幾隻狗狗?', '他不會來啦'],
                '開命': ['有400萬的藍人', '有在兼', '在接客', '蝦皮主管啦', '要多少'], '阿里': ['阿里巴巴', '阿里巴巴給我快一點起來'],
                '小馬雲': ['阿里 阿里巴巴', '歐歐歐', '那個長的很好看 我們去看看吧'], '蒼哥': ['蒼哥在默默操盤啦'],
                '買哪檔': ['跌了你也不敢買', '麗臺 @江忠諭', '長榮 @江忠諭'],
                '買哪支': ['跌了你也不敢買', '麗臺 @江忠諭', '長榮 @江忠諭'], '吉哥': ['吉丸吉丸', '大夜在補眠', '真香?'],
                '雞哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '機哥': ['吉丸吉丸', '大夜在補眠', '真香?'], '基哥': ['吉丸吉丸', '大夜在補眠', '真香?'],
                '媽媽桑': ['要來我家看貓嗎?', '哪個渣男?'], '靠北': ['嗯?', '嘿?', '出事了阿北?'], '告北': ['嗯?', '嘿?', '出事了阿北?'],
                '不是阿': ['嗯?', '嘿?'], '快': ['有小業快?', 'sensitive'], '快喔': ['諭哥準備交割'],
                '諭哥哩': ['在台東啦'], '乾': ['嘿?'], '不對喔': ['出事了阿北'], '幹': ['又有了?'], '...': ['...', '我不行了?'],
                '問題': ['你問題最多', '嗯?'],  ###結束
                }

        try:
            for key in keys.keys():
                if key in msg:
                    word = random.randint(0, len(keys[key])) - 1
                    rsp = keys[key][word]
                    return rsp
        except KeyError as e:
            rsp = ''
            return rsp


#if __name__ == "__main__":
