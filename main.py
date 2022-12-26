from asyncio.log import logger
import json
import sys
from maotai.config import Config

from maotai.jd_spider_requests import JdSeckill

if __name__ == '__main__':
    a = """

       oooo oooooooooo.            .oooooo..o                     oooo         o8o  oooo  oooo  
       `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888  
        888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888  
        888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888  
        888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888  
        888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888  
    .o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o 
    `Y888P                                                                                                                                                  
                                               
功能列表：                                                                                
 1.预约商品
 2.秒杀抢购商品
    """
    print(a)
    # global_config = Config()
    # seckill_init_info = dict()
    # sku_id = 2943430
    # s = """{"address":{"addressDetail":"金水湾9号楼403","addressName":"公司","areaCode":"86","cityId":1370,"cityName":"宁德市","countyId":46145,"countyName":"蕉城区","defaultAddress":false,"email":"","id":138327870,"mobile":"156****9180","mobileKey":"fa4d6bc9d5711c86764def8f71e4ee54","name":"陈言汉","overseas":0,"phone":"","postCode":"","provinceId":16,"provinceName":"福建","selected":true,"townId":46160,"townName":"金涵畲族乡","yuyueAddress":false},"buyNum":2,"code":"200","invoiceInfo":{"invoiceCode":"","invoiceContentType":1,"invoicePhone":"156****9180","invoicePhoneKey":"fa4d6bc9d5711c86764def8f71e4ee54","invoiceTitle":4,"invoiceType":3},"jingdouBO":{"canUseCount":0,"forbidUseJingdou":false,"jingdouDiscount":0,"jingdouSteps":[],"pointsDeductionRate":50,"rate":100,"totalCount":101,"usedCount":0},"orderPriceBO":{"couponAbleNum":5,"couponDiscount":0.00,"couponDiscountTotal":6.00,"couponSelectNum":1,"couponTypeList":[2],"freight":6.00,"giftCardAbleNum":0,"giftCardDiscount":0.00,"giftCardSelectNum":0,"jingdouDiscount":0,"manjianDiscount":0.00,"orderTax":0.00,"productTotalPrice":29.60,"redPacketDeductionAmount":0,"redPacketIsSelected":false,"redPacketTotalAmount":0,"showXuZhongInfo":false,"totalPrice":29.60,"weight":"0.06","yunfeiDiscount":6.00},"payment":{"paymentId":4,"paymentName":"在线支付"},"preSaleBO":{"hidePrice":false,"refundDeposit":false},"seckillOrderExt":{},"seckillSkuVO":{"color":"连花清瘟胶囊24粒","extMap":{"is7ToReturn":"0","new7ToReturn":"8","thwa":"0","SoldOversea":"0"},"height":0.0,"jdPrice":29.60,"length":0.0,"num":2,"rePrice":0.00,"size":"","skuId":2943430,"skuImgUrl":"jfs/t1/104567/3/34518/95921/63974a0dEa4249a6f/ebb959dcda5838cc.jpg","skuName":"以岭 连花清瘟胶囊 0.35g*24粒 连花清瘟 清瘟解毒 宣肺泄热 流行性感冒 发烧或发热头痛咳嗽","skuPrice":14.80,"thirdCategoryId":0.0,"venderName":"京东自营","venderType":0,"weight":0.027,"width":0.0},"shipment":{"bundleUuid":"BundleRelation_1160533463460827136","obtainAllCombinationBundle":"CombinationBundleRelation_1160533463339192320","obtainOrder":"-219789762","shipmentTimeType":3,"shipmentTimeTypeName":"工作日、双休日与节假日均可送货","shipmentType":65,"shipmentTypeName":"京东配送","uuid":"101612_1160533463473410048"},"token":"2bdca26a3a3b12109cc3021f6e7f5d9b","userInfoBO":{"userScore":5766}}"""
    # begin = s.find('{')
    # end = s.rfind('}') + 1
    # ss = json.loads(s[begin:end])
    # seckill_init_info[sku_id] = json.loads(s[begin:end])
    # init_info = seckill_init_info.get(sku_id)
    # default_address = init_info['address'] 
    # addressId = default_address['id']
    # invoice_info = init_info.get('invoiceInfo', {})  # 默认发票信息dict, 有可能不返回
    # token = init_info['token']
    # data = {
    #     'skuId': sku_id,
    #     'num': 1,
    #     'addressId': default_address['id'],
    #     'name': default_address['name'],
    #     'provinceId': default_address['provinceId'],
    #     'cityId': default_address['cityId'],
    #     'countyId': default_address['countyId'],
    #     'townId': default_address['townId'],
    #     'addressDetail': default_address['addressDetail'],
    #     'mobile': default_address['mobile'],
    #     'mobileKey': default_address['mobileKey'],
    #     'email': default_address.get('email', ''),
    #     'postCode': '',
    #     'invoiceTitle': invoice_info.get('invoiceTitle', -1),
    #     'invoiceCompanyName': '',
    #     'invoiceContent': invoice_info.get('invoiceContentType', 1),
    #     'invoiceTaxpayerNO': '',
    #     'invoiceEmail': '',
    #     'invoicePhone': invoice_info.get('invoicePhone', ''),
    #     'invoicePhoneKey': invoice_info.get('invoicePhoneKey', ''),
    #     'invoice': 'true' if invoice_info else 'false',
    #     'password': global_config.get('account', 'payment_pwd'),
    #     'codTimeType': 3,
    #     'paymentType': 4,
    #     'areaCode': '',
    #     'overseas': 0,
    #     'phone': '',
    #     'eid': global_config.getRaw('config', 'eid'),
    #     'fp': global_config.getRaw('config', 'fp'),
    #     'token': token,
    #     'pru': ''
    # }

    # logger.info("初始化信息接口,返回信息:{} ".format(s))

    # print(ss)


    jd_seckill = JdSeckill()
    choice_function = input('请选择:')
    if choice_function == '1':
        jd_seckill.reserve()
    elif choice_function == '2':
        jd_seckill.seckill_by_proc_pool()
    else:
        print('没有此功能')
        sys.exit(1)

