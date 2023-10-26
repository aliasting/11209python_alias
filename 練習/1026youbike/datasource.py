import requests  # 讓人一進來就看到指令


def download_youbike_data():
    """
    下載台北市youbike資料2.0
    https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    """
    # import requests 這個function會只用到這裡,所以還是寫在最上面

    youbike_url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    response = requests.get(youbike_url)
    #因為用response.raise__for__status()所以以下指令可取消
    #主要是raise
    # def __加底線為呼叫內部function,例:def __create_table
    '''
    if requests.status_codes == 200:
        # print("下載成功")改寫
        raise Exception("下載失敗")
    else:
        # print("下載失敗")改寫
        raise Exception("下載失敗")
    '''