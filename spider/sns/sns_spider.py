# coding: utf-8
import urllib2
import urllib
import cookielib
import re
from lxml import etree
from bs4 import BeautifulSoup
#from lxml.html import soupparser
#values = {"username":"1016903103@qq.com","password":"XXXX"}
#data = urllib.urlencode(values)
import xml.etree.ElementTree as ET


class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass


def req_302(opener, request):
    try:
        response = opener.open(request)
    except urllib2.HTTPError, e:
        print e.code
        if e.code == 301 or e.code == 302:
            response = req_302(opener, request)
    return response


def get_content(html, key_empha):
    content_list = []
    html = re.sub(key_empha, r'\1', html)
    dom = etree.HTML(html)
    for item in dom.iterfind("body/div"):
        if item.get("class") == 'c' and item.get("id"):
            if len(item) == 1:
                for subitem in item.iterfind("div/span"):
                    if subitem.get("class") == "ctt":
                        content = etree.tostring(subitem, method='text', encoding='utf-8').decode("utf-8")
                        content_list.append(content)
            else:
                for subitem in item.iterfind("div"):
                    is_target = True
                    for subsubitem in subitem.iterfind("span"):
                        if subsubitem.get("class") == "ctt":
                            is_target = False
                    if is_target:
                        raw = etree.tostring(subitem, method="text", encoding="UTF-8")
                        # raw = "赞[1]赞[1]"
                        pattern = re.compile(u'(赞\[\d*\])', re.U)
                        match = re.search(pattern, raw.decode("utf-8"))
                        content = raw.decode("utf-8")[:match.start()]
                        content_list.append(content)
    return content_list


headers = {"Cookie": "_T_WM=c5b9d937f930cc19d8ece8707cc62fc5; SUB=_2A256COhaDeRxGeRP41YW9y_Ozz2IHXVZ8ogSrDV6PUJbrdANLXCkkW1LHesEl_fj1Iyc9VMQ9_4OTANJhLuuGQ..; gsid_CTandWM=4uHucb1c1gOXARzCFZIuB9amf3T",
           "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2587.3 Safari/537.36"}
data = {"keyword": "荒野猎人"}
url = "http://weibo.cn/search/mblog?hideSearchFrame=&{}&page=".format(urllib.urlencode(data))
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(RedirectHandler)

key_empha = re.compile(u'<span\s*class="kt">(\w+)</span>', re.U|re.I)
fp = open("contents.txt", "w")
total = 0
for page in range(1, 101):
    print page
    request = urllib2.Request(url + str(page), headers=headers)
    #response = urllib2.urlopen(request)
    response = req_302(opener, request)
    html = response.read()
    content_list =  get_content(html, key_empha)
    for content in content_list:
        fp.write(content.encode("utf-8") + "\n")
        total += 1
fp.close()
print total


html = u"""
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta http-equiv="Cache-Control" content="no-cache"/><meta id="viewport" name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0, maximum-scale=2.0" /><link rel="icon" sizes="any" mask href="http://h5.sinaimg.cn/upload/2015/05/15/28/WeiboLogoCh.svg" color="black"><meta name="MobileOptimized" content="240"/><title>搜索结果</title><style type="text/css" id="internalStyle">html,body,p,form,div,table,textarea,input,span,select{font-size:12px;word-wrap:break-word;}body{background:#F8F9F9;color:#000;padding:1px;margin:1px;}table,tr,td{border-width:0px;margin:0px;padding:0px;}form{margin:0px;padding:0px;border:0px;}textarea{border:1px solid #96c1e6}textarea{width:95%;}a,.tl{color:#2a5492;text-decoration:underline;}/*a:link {color:#023298}*/.k{color:#2a5492;text-decoration:underline;}.kt{color:#F00;}.ib{border:1px solid #C1C1C1;}.pm,.pmy{clear:both;background:#ffffff;color:#676566;border:1px solid #b1cee7;padding:3px;margin:2px 1px;overflow:hidden;}.pms{clear:both;background:#c8d9f3;color:#666666;padding:3px;margin:0 1px;overflow:hidden;}.pmst{margin-top: 5px;}.pmsl{clear:both;padding:3px;margin:0 1px;overflow:hidden;}.pmy{background:#DADADA;border:1px solid #F8F8F8;}.t{padding:0px;margin:0px;height:35px;}.b{background:#e3efff;text-align:center;color:#2a5492;clear:both;padding:4px;}.bl{color:#2a5492;}.n{clear:both;background:#436193;color:#FFF;padding:4px; margin: 1px;}.nt{color:#b9e7ff;}.nl{color:#FFF;text-decoration:none;}.nfw{clear:both;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.s{border-bottom:1px dotted #666666;margin:3px;clear:both;}.tip{clear:both; background:#c8d9f3;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tip2{color:#000000;padding:2px 3px;clear:both;}.ps{clear:both;background:#FFF;color:#676566;border:1px solid #BACDEB;padding:3px;margin:2px 1px;}.tm{background:#feffe5;border:1px solid #e6de8d;padding:4px;}.tm a{color:#ba8300;}.tmn{color:#f00}.tk{color:#ffffff}.tc{color:#63676A;}.c{padding:2px 5px;}.c div a img{border:1px solid #C1C1C1;}.ct{color:#9d9d9d;font-style:italic;}.cmt{color:#9d9d9d;}.ctt{color:#000;}.cc{color:#2a5492;}.nk{color:#2a5492;}.por {border: 1px solid #CCCCCC;height:50px;width:50px;}.me{color:#000000;background:#FEDFDF;padding:2px 5px;}.pa{padding:2px 4px;}.nm{margin:10px 5px;padding:2px;}.hm{padding:5px;background:#FFF;color:#63676A;}.u{margin:2px 1px;background:#ffffff;border:1px solid #b1cee7;}.ut{padding:2px 3px;}.cd{text-align:center;}.r{color:#F00;}.g{color:#0F0;}.bn{background: transparent;border: 0 none;text-align: left;padding-left: 0;}</style><script>if(top != self){top.location = self.location;}</script></head><body><div class="tm"><a href="http://weibo.cn/msg/?unread=1"><span class="tmn">1</span>私信</a>&nbsp;&nbsp;<a href="http://weibo.cn/msg/clearAllUnread?type=dcm&amp;rl=1"><img src="http://u1.sinaimg.cn/upload/2011/08/01/5366.gif" alt="[X]" /></a><br/></div><div class="n" style="padding: 6px 4px;"><a href="http://weibo.cn/?tf=5_009" class="nl">首页</a>|<a href="http://weibo.cn/msg/?tf=5_010" class="nl">消息</a>|<a href="http://huati.weibo.cn" class="nl">话题</a>|<a href="http://weibo.cn/search/?tf=5_012" class="nl">搜索</a>|<a href="/search/mblog?keyword=%E6%B5%81%E6%84%9F&amp;page=95&amp;rand=1117&amp;p=r" class="nl">刷新</a></div><div class="c"><a href="/pub/?rand=433944">返回微博广场</a></div><div class="c"><form action="/search/" method="post"><div><input type="text" name="keyword" value="流感"  /><input type="submit" name="smblog" value="搜微博" /></div></form></div><div class="c"><span class="cmt">共8511493条</span></div><div class="tip">类型:全部-<a href="/search/mblog/?keyword=%E6%B5%81%E6%84%9F&amp;filter=hasori">原创</a>-<a href="/search/mblog/?keyword=%E6%B5%81%E6%84%9F&amp;filter=hasv">认证</a>-<a href="/search/mblog/?keyword=%E6%B5%81%E6%84%9F&amp;advanced=mblog&amp;rl=1">更多&gt;&gt;</a><br/>排序:实时-<a href="/search/mblog/?keyword=%E6%B5%81%E6%84%9F&amp;sort=hot">热门</a></div><div class="c" id="M_Dqi01ACA5"><div><a class="nk" href="http://weibo.cn/u/5217192387">不亦乐乎0505</a><span class="cmt">&nbsp;转发了&nbsp;<a href="http://weibo.cn/baby">新浪育儿</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5337.gif" alt="V"/><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M"/>&nbsp;的微博:</span><span class="ctt"><a href="http://weibo.cn/pages/100808topic?extparam=%E6%B5%81%E6%84%9F%E4%B8%8E%E6%84%9F%E5%86%923%E5%8C%BA%E5%88%AB&amp;from=feed">#流感与感冒3区别#</a>感和普通感冒最大的区别就在于，<span class="kt">流感</span>“急”，突然畏寒、急起高热、头痛、全身乏力、鼻塞、流涕等呼吸道症状，症状来得急却不容易好。而普通感冒在全身症状上较轻，不发热或者低热，会有流鼻涕 <br/>、打喷嚏的症状。一般的普通感冒3-5天就能痊愈…详细：<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRG8CVxU&amp;ep=Dqi01ACA5%2C5217192387%2CDpoHLpIzG%2C1655524143">http://t.cn/RG8CVxU</a></span> [<a href="http://weibo.cn/mblog/pic/DpoHLpIzG?rl=1">图片</a>]&nbsp;<span class="cmt">赞[12]</span>&nbsp;<span class="cmt">原文转发[29]</span>&nbsp;<a href="http://weibo.cn/comment/DpoHLpIzG?rl=1#cmtfrm" class="cc">原文评论[1]</a><!----></div><div><span class="cmt">转发理由:</span><a href="/n/%E4%B8%8D%E4%BA%A6%E4%B9%90%E4%B9%8E201405">@不亦乐乎201405</a> <span class="kt">流感</span>&nbsp;&nbsp;<a href="http://weibo.cn/attitude/Dqi01ACA5/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/Dqi01ACA5?uid=5217192387&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/Dqi01ACA5?uid=5217192387&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/Dqi01ACA5?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 10:16&nbsp;来自华为Ascend Mate7</span></div></div><div class="s"></div><div class="c" id="M_DqhZ3fOES"><div><a class="nk" href="http://weibo.cn/u/3206554861">忘多么难</a><span class="ctt">:【家有宠物的准妈妈应该注意什么？】宠物可能携带病菌或寄生虫，如果你发热或其他类似<span class="kt">流感</span>的症状，一定要去医院就诊。1.猫可能传播弓形虫，你需要做弓形虫抗体检查。2.乌龟、鸟类、蜥蜴等可能携带沙门氏菌。尽量请家里其他人照顾这些动物，处理粪便和清理笼舍等。</span> [<a href="http://weibo.cn/mblog/pic/DqhZ3fOES?rl=1">图片</a>]&nbsp;<a href="http://weibo.cn/attitude/DqhZ3fOES/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DqhZ3fOES?uid=3206554861&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhZ3fOES?uid=3206554861&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhZ3fOES?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 10:13&nbsp;来自三星Galaxy_S</span></div></div><div class="s"></div><div class="c" id="M_DqhYSE4eC"><div><a class="nk" href="http://weibo.cn/u/3968752700">用户rnoj5eyml5</a><span class="ctt">:【咖喱可抵御感冒】全球第一篇关于咖喱药用价值的研究文章发表于1970年，到现在为止，在医学文献检索系统上已有1700篇研究文章。可以说，咖喱的药用价值已经引起了全世界的关注。一位印度医生也说，<span class="kt">流感</span>很难在印度流行，就是因为人们天天吃咖喱，把<span class="kt">流感</span>消灭在了萌芽状态。</span> [<a href="http://weibo.cn/mblog/pic/DqhYSE4eC?rl=1">图片</a>]&nbsp;<a href="http://weibo.cn/attitude/DqhYSE4eC/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DqhYSE4eC?uid=3968752700&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhYSE4eC?uid=3968752700&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhYSE4eC?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 10:13&nbsp;来自微博 weibo.com</span></div></div><div class="s"></div><div class="c" id="M_DqhYvjJyF"><div><a class="nk" href="http://weibo.cn/u/1714080997">看绽放的灵犀</a><span class="ctt">:第190天。老公请吃肯德基啦，最近不是禽<span class="kt">流感</span>嘛，呵呵，没关系，我们不吃鸡肉！ [位置]<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRyhpIRU&amp;ep=DqhYvjJyF%2C1714080997%2CDqhYvjJyF%2C1714080997">宣城·汽车站</a></span>&nbsp;<a href="http://place.weibo.com/imgmap/poiid=8008634180200000015&amp;center=30.93345,118.75491&amp;backurl=http%253A%252F%252Fweibo.cn%252Fsearch%252Fmblog%253Fkeyword%253D%2525E6%2525B5%252581%2525E6%252584%25259F%2526amp%253Bpage%253D95%2526amp%253Brand%253D1117">显示地图</a> &nbsp;[<a href="http://weibo.cn/mblog/picAll/DqhYvjJyF?rl=2">组图共6张</a>][<a href="http://weibo.cn/mblog/pic/DqhYvjJyF?rl=1">图片</a>]&nbsp;<a href="http://weibo.cn/attitude/DqhYvjJyF/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DqhYvjJyF?uid=1714080997&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhYvjJyF?uid=1714080997&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhYvjJyF?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 10:12&nbsp;来自Flyme OS</span></div></div><div class="s"></div><div class="c" id="M_DqhYs4Gmq"><div><a class="nk" href="http://weibo.cn/u/5168302678">和乐堂小儿推拿</a><img src="http://u1.sinaimg.cn/upload/h5/img/hyzs/donate_btn_s.png" alt="M"/><span class="ctt">:清明不幸被<span class="kt">流感</span>击中，儿子也未能幸免，从开始流鼻涕到支气管炎再到后面的肺虚咳嗽，我的内心也经历了一番痛苦的挣扎！         支气管炎导致的剧咳让人窒息，但以往的经验告诉我，这是人体正气与邪气在搏斗，两天的剧咳，三次推拿，用穴八卦平肝肺四横纹天河水，到第三天剧咳停歇了！[耶]终于胜利了！</span> &nbsp;<a href="http://weibo.cn/attitude/DqhYs4Gmq/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DqhYs4Gmq?uid=5168302678&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhYs4Gmq?uid=5168302678&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhYs4Gmq?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 10:12&nbsp;来自三星GALAXY A</span></div></div><div class="s"></div><div class="c" id="M_DqhYgeWIc"><div><a class="nk" href="http://weibo.cn/u/3198262260">_番茄爱上炒蛋_</a><span class="ctt">:<a href="http://weibo.cn/pages/100808topic?extparam=%E4%BB%8A%E6%97%A5%E8%B4%B4%E7%BA%B8%E6%89%93%E5%8D%A1&amp;from=feed">#今日贴纸打卡#</a>“荣幸的”赶上<span class="kt">流感</span>的小尾巴[睡][白眼]</span> [<a href="http://weibo.cn/mblog/pic/DqhYgeWIc?rl=1">图片</a>]&nbsp;<a href="http://weibo.cn/attitude/DqhYgeWIc/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[3]</a>&nbsp;<a href="http://weibo.cn/repost/DqhYgeWIc?uid=3198262260&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhYgeWIc?uid=3198262260&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhYgeWIc?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 10:11&nbsp;来自iPhone 6s Plus</span></div></div><div class="s"></div><div class="c" id="M_DqhR17AsN"><div><a class="nk" href="http://weibo.cn/u/1891068794">蔡蔡妈-3-</a><span class="ctt">:女儿长大成人了，在这特别的日子里，<span class="kt">流感</span>君居然找上她[感冒][困]39度高温呀🌡，希望她快快好起来[强壮]🏻，同时也希望她努力冲刺，争取考上理想大学，爱你哦[爱你]<a href="/n/%E5%A4%A9%E7%B7%9A%E5%AF%B6%E5%AF%B6de%E5%B0%8F%E6%B3%A2">@天線寶寶de小波</a></span> &nbsp;<a href="http://weibo.cn/attitude/DqhR17AsN/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[2]</a>&nbsp;<a href="http://weibo.cn/repost/DqhR17AsN?uid=1891068794&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhR17AsN?uid=1891068794&amp;rl=1#cmtfrm" class="cc">评论[2]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhR17AsN?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 09:53&nbsp;来自iPhone 6 Plus</span></div></div><div class="s"></div><div class="c" id="M_DqhQQ7MGH"><div><a class="nk" href="http://weibo.cn/u/2535778800">Lawrance宝宝</a><span class="ctt">:人只有生病的时候才能体会到健康的重要性，被小朋友传染的<span class="kt">流感</span>让人浑身不舒服。</span> &nbsp;<a href="http://weibo.cn/attitude/DqhQQ7MGH/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DqhQQ7MGH?uid=2535778800&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhQQ7MGH?uid=2535778800&amp;rl=1#cmtfrm" class="cc">评论[2]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhQQ7MGH?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 09:53&nbsp;来自iPhone 6 Plus</span></div></div><div class="s"></div><div class="c" id="M_DqhPzziJI"><div><a class="nk" href="http://weibo.cn/u/2346268940">柏舟之鱼</a><span class="ctt">:春季的<span class="kt">流感</span>把我凶猛侵蚀。[哼]</span> &nbsp;<a href="http://weibo.cn/attitude/DqhPzziJI/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[2]</a>&nbsp;<a href="http://weibo.cn/repost/DqhPzziJI?uid=2346268940&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhPzziJI?uid=2346268940&amp;rl=1#cmtfrm" class="cc">评论[2]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhPzziJI?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 09:50&nbsp;来自<a href="http://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Fdown.sina.cn%2Fsinaclient%2Fweibo%2Findex%2Fgsid%2F0%2Fmid%2F0">iPhone客户端</a></span></div></div><div class="s"></div><div class="c" id="M_DqhK1kH9N"><div><a class="nk" href="http://weibo.cn/u/3738640233">四川搜号网</a><img src="http://u1.sinaimg.cn/upload/2011/07/28/5337.gif" alt="V"/><span class="ctt">:<a href="http://weibo.cn/pages/100808topic?extparam=%E5%9B%9B%E5%B7%9D%E5%9F%8E%E4%BA%8B&amp;from=feed">#四川城事#</a> 弓形虫的学名是“Toxoplasma gondii”，它是一种外形像新月牙的虫子，可以侵入人体中枢神经系统。人们通常吃未煮熟的肉食或接触被猫感染的垃圾物质会感染弓形虫。有些人体内存在抗体，即使暴露在弓形虫感染的环境下也不会出现任何症状。 人体表现症状：<span class="kt">流感</span>、发烧、发冷、疲劳、头痛。</span> [<a href="http://weibo.cn/mblog/pic/DqhK1kH9N?rl=1">图片</a>]&nbsp;<a href="http://weibo.cn/attitude/DqhK1kH9N/add?uid=2184771241&amp;rl=1&amp;st=ff2fed">赞[0]</a>&nbsp;<a href="http://weibo.cn/repost/DqhK1kH9N?uid=3738640233&amp;rl=1">转发[0]</a>&nbsp;<a href="http://weibo.cn/comment/DqhK1kH9N?uid=3738640233&amp;rl=1#cmtfrm" class="cc">评论[0]</a>&nbsp;<a href="http://weibo.cn/fav/addFav/DqhK1kH9N?rl=1&amp;st=ff2fed">收藏</a><!---->&nbsp;<span class="ct">04月10日 09:36&nbsp;来自贝贝微助手</span></div></div><div class="s"></div><div class="pa" id="pagelist"><form action="/search/mblog?hideSearchFrame=&amp;keyword=%E6%B5%81%E6%84%9F" method="post"><div><a href="/search/mblog?hideSearchFrame=&amp;keyword=%E6%B5%81%E6%84%9F&amp;page=96">下页</a>&nbsp;<a href="/search/mblog?hideSearchFrame=&amp;keyword=%E6%B5%81%E6%84%9F&amp;page=94">上页</a>&nbsp;<a href="/search/mblog?hideSearchFrame=&amp;keyword=%E6%B5%81%E6%84%9F">首页</a>&nbsp;<input name="mp" type="hidden" value="100" /><input type="text" name="page" size="2" style='-wap-input-format: "*N"' /><input type="submit" value="跳页" />&nbsp;95/100页</div></form></div><div class="pm" ><span class="pmf"><a href="#top" id="mblogform">返回页面顶部</a><br/></span>针对"#流感#"说点什么:<form action="/mblog/sendmblog?st=ff2fed" accept-charset="UTF-8" method="post"><div><input type="hidden" name="rl" value="1" /><textarea name="content" rows="2" cols="20">#流感#</textarea><br/><input type="submit" value="发布" /></div></form></div><div class="cd"><a href="#top"><img src="http://u1.sinaimg.cn/3g/image/upload/0/62/203/18979/5e990ec2.gif" alt="TOP"/></a></div><div class="pms"> <a href="http://weibo.cn">首页</a>.<a href="http://weibo.cn/topic/240489">反馈</a>.<a href="http://weibo.cn/page/91">帮助</a>.<a  href="http://down.sina.cn/weibo/default/index/soft_id/1/mid/0"  >客户端</a>.<a href="http://weibo.cn/spam/?rl=1&amp;type=3" class="kt">举报</a>.<a href="http://passport.sina.cn/sso/logout?r=http%3A%2F%2Fweibo.cn%2Fpub%2F%3Fvt%3D&amp;entry=mweibo">退出</a></div><div class="c">设置:<a href="http://weibo.cn/account/customize/skin?tf=7_005&amp;st=ff2fed">皮肤</a>.<a href="http://weibo.cn/account/customize/pic?tf=7_006&amp;st=ff2fed">图片</a>.<a href="http://weibo.cn/account/customize/pagesize?tf=7_007&amp;st=ff2fed">条数</a>.<a href="http://weibo.cn/account/privacy/?tf=7_008&amp;st=ff2fed">隐私</a></div><div class="c">彩版|<a href="http://m.weibo.cn/?tf=7_010">触屏</a>|<a href="http://weibo.cn/page/521?tf=7_011">语音</a></div><div class="b">weibo.cn[04-12 15:30]</div></body></html>
"""
# soup = BeautifulSoup(html)
# for item in soup.html.head.descendants:
#     print type(item)
#     print "<----->"
# html = '<html><body id="1">abc<div>123</div>def<div>456</div>ghi</body></html>'
# dom = etree.HTML(html)
# for item in dom[0].iterfind(""):
#     print item




