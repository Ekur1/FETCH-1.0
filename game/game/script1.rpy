define zeke = Character("吉克", color="#ff0000")  
define levi = Character("利威尔", color="#ff0000")  
define 查卡员 = Character("查卡员", color="#ffffff")
define 保安A = Character("保安A", color="#ffffff")
define 保安B = Character("保安B", color="#ffffff")
define 保安 = Character("保安", color="#ffffff")
define 警官 = Character("警官", color="#ffffff")
define 司机 = Character("司机", color="#ffffff")
define ？？？ = Character("？？？", color="#ff0000")

image lh1 amazedin:
    "images/lh1 amazedin.png"
    zoom 0.2

image lh1 amazedout:
    "images/lh1 amazedout.png"
    zoom 0.2

image lh1 annoyedin:
    "images/lh1 annoyedin.png"
    zoom 0.2

image lh1 annoyedout:
    "images/lh1 annoyedout.png"
    zoom 0.2

image lh1 normalout:
    "images/lh1 normalout.png"
    zoom 0.2

image lh1 normalin:
    "images/lh1 normalin.png"
    zoom 0.2

image lh1 shyin:
    "images/lh1 shyin.png"
    zoom 0.2

image lh1 shyout:
    "images/lh1 shyout.png"
    zoom 0.2

image lh1 upsetin:
    "images/lh1 upsetin.png"
    zoom 0.2

image lh1 upsetout:
    "images/lh1 upsetout.png"
    zoom 0.2

image lh2 annoyedin:
    "images/lh2 annoyedin.png"
    zoom 0.2

image lh2 annoyedout:
    "images/lh2 annoyedout.png"
    zoom 0.2


image lh2 laughin:
    "images/lh2 laughin.png"
    zoom 0.2


image lh2 laughout:
    "images/lh2 laughout.png"
    zoom 0.2


image lh2 normalin:
    "images/lh2 normalin.png"
    zoom 0.2


image lh2 normalout:
    "images/lh2 normalout.png"
    zoom 0.2


image lh2 shyin:
    "images/lh2 shyin.png"
    zoom 0.2


image lh2 shyout:
    "images/lh2 shyout.png"
    zoom 0.2


image lh2 upsetin:
    "images/lh2 upsetin.png"
    zoom 0.2


image lh2 upsetout:
    "images/lh2 upsetout.png"
    zoom 0.2



image CG1-1 = "images/CG1-1.jpg"
image CG1-2 = "images/CG1-2.jpg"
image CG2-1 = "images/CG2-1.jpg"
image CG2-2 = "images/CG2-2.jpg"
image CG3-1 = "images/CG3-1.jpg"
image CG3-2 = "images/CG3-2.jpg"
image CG4 = "images/CG4.jpg"
image CG5 = "images/CG5.jpg"
image CG6 = "images/CG6.jpg"
image CG7-1 = "images/CG7-1.jpg"
image CG7-2 = "images/CG7-2.jpg"
image BE1 = "images/BE1.jpg"
image park = "images/park.jpg"
image bg = "images/bg.jpg"
image hall = "images/hall.jpg"
image kitchen = "images/kitchen.jpg"
image apartment = "images/apartment.jpg"
image apartment2 = "images/apartment2.jpg"
image supermarket = "images/supermarket.jpg"
image garage = "images/garage.jpg"
image garage2 = "images/garage2.jpg"
image garage3 = "images/garage3.jpg"
image pet_section = "images/pet_section.jpg"
image target = "images/target.jpg"
image car = "images/car.jpg"
image inside = "images/inside.jpg"
image fight = "images/fight.jpg"
image interrogation_room = "images/interrogation.jpg"
image pigeon1 = "images/pigeon1.jpg"
image pigeon2 = "images/pigeon2.jpg"
image dog = "images/dog.jpg"
# 定义雪花粒子图片
image white = "images/white.png"
image white2 = "images/white2.png"

# 添加雪花效果
image snow:
    # 第一层雪花 - 慢速
    SnowBlossom("white",  
        count=200,  
        border=50,  
        xspeed=(10, 30),  
        yspeed=(30, 60),  
        start=0,  
        fast=False,  
        horizontal=False)
    
    # 第二层雪花 - 快速
    SnowBlossom("white2",  
        count=210,  # 数量减少以免太密集
        border=50,  
        xspeed=(20, 40),  # 加快水平速度
        yspeed=(50, 80),  # 加快垂直速度
        start=0,  
        fast=True,  # 启用快速模式
        horizontal=False)

label start:
    scene start with dissolve 
    "{color=#ff0000}什么是爱？{/color}"
    "{color=#ff0000}因为切除舌头所以无法描述的——什么是爱？{/color}"
    "{color=#ff0000}因为无法描述出，所以品尝到了更深处无法被舌头捕捉的铁锈味。{/color}"
    "{color=#ff0000}爱着它的人，爱着他的人，爱着飞机的人，爱着粒子的人，爱着公式的人，爱着羊羔的人，爱着描述的人，爱着自杀的人，爱着警钟的人，爱着幻想的人爱着回忆的人爱着欺骗的人{/color}"
    "{color=#ff0000}那些人，全人类和那些不同的爱人{/color}"
    "{color=#ff0000}你们、在得知真相后，是会因为感到欺骗而痛哭流涕。{/color}"
    "{color=#ff0000}还是剖出双眼，继续贪恋片刻的欢愉呢。{/color}"
    "{color=#ff0000}……{/color}"
    "{color=#ff0000}……{/color}"
    "{color=#ff0000}……然后，因为没有反抗的勇气。{/color}"
    "{color=#ff0000}然后、因为直到现在还活着。{/color}"
    scene black2 with dissolve  
    "利威尔是在凌晨三点十七分被吵醒的。"
    "这不是一个估算，而是从床头电子钟上红色数字精准确认过的时间。"
    "至于唤醒他的声音——"
    play sound "audio/dog_whimper.mp3"
    "——那是一声细微、持续、且极具穿透力的呜咽。"
    "它化作一根生了锈的钢针，不偏不倚地搅动起他本就浅薄的睡眠。"
    "这声音来自楼上。"
    #前面这些地方都可以黑屏，从下一句开始切开场cg，黑屏渐入
    scene CG1-1 with dissolve  
    "利威尔在黑暗中睁开双眼。"
    "天花板是令人烦躁的灰色，他能清晰地分辨出这声音的来源。"
    "那是从楼上传来的…"
    "一种属于小型哺乳动物的声音。"
    "如同节拍器失灵，顽固地敲打在寂静的地面上。"
    scene CG1-2 with dissolve
    "他花了三分钟试图用理性压制住这股无名火。"
    "这只是一点噪音，他告诉自己。"
    "噪音是现代文明不可割舍的一部分。"
    "呜咽声还在继续。那根钢针已经开始在他的太阳穴里钻孔。"
    scene apartment with dissolve 
    show lh1 upsetin at center_left

    levi "…………"
    
    play sound "audio/bed_rustle.mp3"
    "他终于放弃了与天花板的对视，坐起身。"
    
    menu:
        "上楼质问":
            jump midnight_confrontation


label midnight_confrontation:
    scene apartment with dissolve  # 
    "利威尔打开灯，走向门口。"
    "他的公寓一尘不染，地板光洁如新，所有物品都以几乎偏执的秩序排列着。"
    "这栋楼不算太旧，隔音效果对他来说依然聊胜于无。"
    #可以加一个客厅的背景图片！后面还可以用到
    scene elevator with dissolve  
    "当他走出门站在走廊里时，能听到那个呜咽声正在变得清晰。"
    "利威尔冷笑了一声，电梯缓慢上升。"
    "这也许不是简单的扰民，因为他听见了属于男人自言自语和器械碰撞的模糊声音。"
    #电梯背景，无人物立绘
    
    "他记得楼上是一个新搬来的高个子男人，戴着眼镜。"
    "看起来像是会把薪水花一大半在买书上的知识分子。"
    "利威尔在电梯里见过他一次，对方捧着几个搬家公司的纸箱，身上有一股消毒水和动物绒毛混合的味道。"
    
    play sound "audio/elevator_arrival.mp3"
    #从这里开始切走廊背景+人物立绘
    scene hall2 with dissolve  
    show lh1 normalout at center_left 
    "电梯到达楼上，利威尔走出去，径直来到他家正上方那扇门的门口。"
    "他的指关节叩在门板上，里面的噪音戛然而止。"
    
    "——死寂持续了大约一分钟，久到利威尔开始怀疑对方是不是已经畏罪潜逃。"
    play sound "audio/door_push.mp3"
    "正当他打算进行第二次敲门时，门锁打开了一条缝。"

    scene CG2-1 with dissolve 
    "一颗金色的脑袋从门缝里探出来，正是前几天在电梯里遇见的那个男人。"
    "他戴着一双溅了些不明红色液体的医用手套，乱糟糟的金发有几缕粘在额头上。"
    "神情介于你是谁和我别烦我之间。"
    zeke "……不好意思，我刚刚从猫眼里没看到人，还以为大半夜有鬼找我。"
    zeke "有事吗？"
    
    levi "你在楼上肢解什么？动静太大了，吵得我睡不着觉。"
    
    zeke "抱歉。事情有点麻烦，我会小点声。"
    
    "利威尔的眉毛拧了起来，他的手指已经塞进了门缝里。"

    levi "你在屋里做什么？"

    scene CG2-2 with dissolve  # 
    "男人愣了一下，随即像是理解了什么，嘴角扯出一个没什么笑意的弧度。"
    "他干脆退后两步，利威尔越过对方的肩膀，审视起屋内的状况。"
    "原本应该是客厅的区域此时此刻显得拥挤而怪异，两张桌子被强行拼凑在一起，形成了一个高低不平的平面。"
    "现在那张简陋的台面上，躺着一条脏兮兮的中型犬。"
    "吉克顺着他的视线看了过去。"
    scene apartment2 with dissolve  # 
    show lh1 normalout at center_left 
    show lh2 normalin at center_right
    zeke "你说这个？"
    zeke "它是路边捡来的，后腿完全萎缩了…看样子是旧伤，大概是因为行动不便才没躲开车流。"
    zeke "身上有一条被车刮开的伤口，万幸骨头没断，也没有内伤。"
    zeke "我刚刚正在给它止血，所以"
    zeke "...不管你想的是什么变态杀人或和虐待动物的戏码。"
    zeke "很遗憾，都不是那样。"
    "桌子上一堆杂乱的器械确实像是医疗用品，桌角堆着纱布，碘伏被打翻在地板上。"
    "那条狗正在虚弱地喘息，伤口还在渗血。"
    
    levi "给我个理由不去怀疑你是罪魁祸首。"
    
    zeke "……"
    zeke "好吧，那边有我的行医资格证，要是还不信的话，你就进来搭把手。"
    zeke "这家伙虽然是个瘸子，但求生欲太强了，一直乱动。"
    zeke "我一个人快要按不住了。"
    show lh1 annoyedout at center_left 
    show lh2 normalin at center_right
    "利威尔在门口站了两秒，像是评估。"
    play sound "audio/door_push.mp3"
    "最终，他发出一声极轻的咋舌声，反手带上了门。"
    
    levi "洗手间在哪？"
    
    zeke "右转，厨房。"
    zeke "别用那块粉色的毛巾，那是擦狗的。"
    scene apartment2 with dissolve
    "一分钟后，利威尔带着一身淡淡的洗手液味回到了客厅。"
    
    zeke "按住它的头和前肢……很好，你叫什么名字？"
     
 
    levi "利威尔，我住你楼下。"
    
    zeke "是吗？吵醒你我感到很抱歉。"
    
    levi "…不用再说了。"
    scene black1 with dissolve
    "接下来的两个小时里，二人并没有过多的交流。"
    "利威尔像一台会自己行动的医疗机器，将他需要的东西递到手边，或者配合调整狗的姿势。"
    "……"
    "…………"
    "………………"
    #加一些省号代表时间流逝？这边感觉太快了
    "时针指向凌晨五点，窗边的天空泛起像是兑了太多水的牛奶般的颜色。"
    scene apartment2 with dissolve
    show lh1 normalout at center_left 
    show lh2 normalin at center_right
    zeke "好了，结束了……"
    
    "气势汹汹的狗最终被妥善安置在铺着电热毯的笼子里，脖子被套上了伊丽莎白圈，呼吸平稳。"
    "那个主刀的兽医瘫在客厅的沙发里，甚至还没脱掉那双沾满了血和消毒水的手套。"
    "只能像僵尸一样微微举着手，避免日后多出一桩清洗沙发套的家务。"
    "利威尔的状态比他好得多，正在忙着把医疗垃圾分类打包。"
    "做完一切，他看向那个在沙发上半死不活的男人。"
    
    zeke "水……"
    
    levi "瘸的又不是你。"
    
    zeke "求你了。"
    
    levi "…………"
    levi "………"
    levi "你烦不烦。"
    #想要一个说出这句话之后立绘淡淡的消失的样子，很好笑
    
    "几分钟之后，利威尔端着一杯水回来，递到他面前。"
    play sound "audio/water_cup.mp3"
    "他已经脱下了沾满血的手套，随手放在桌子上，利威尔只好过去捏起来，塞进桌子底下的垃圾袋里。"
    
    zeke "谢了，我是吉克.耶格尔，叫我吉克就好，还需要看我的行医资格证吗。"
    
    levi "哦，顺便把你的身份证件也交出来吧，信息多一点警察也会来快一点。"
    
    "吉克没笑，喝完最后一口水，瘫回靠背眼神涣散，像在是逃避问题。"
    show lh1 annoyedout at center_left 
    show lh2 shyin at center_right
    zeke "好困，利威尔……你在水里放了什么……为什么我这么困……"
    
    levi "你想喝到什么？艾司唑仑还是狗尿？"
    
    zeke "却之不恭………但我想喝巧克力牛奶……"
    zeke "圣诞节快乐，很有节日氛围吧……？"
    
    levi "……"
    levi "我是不是对你有点太好了。"
    
    "利威尔觉得自己今晚已经是圣母附体，不仅当了免费的助理，还兼职了护工"
    "甚至……明明一开始是被扰民，想来讨要个说法的。"
    
    levi "再有下次就杀了你。"
    
    play sound "audio/footsteps_leave.mp3"
    "他本就不多的耐心已经彻底清零，利威尔头也不回地走向入户门。"
    

    jump day2



label day2:
    scene apartment with dissolve  
    play sound "audio/doorbell.mp3"
    #第二天 黑幕空镜头 
    "第二天下午，利威尔的门铃响了"
    "他透过监控看到外面站着的人，眉心再次拧紧。"
    play sound "audio/door_open1.mp3"
    show lh2 normalout at center_right
    "打开门，吉克老老实实站在门外。"
    "他换了一身干净的衬衫和卡其色的长裤，头发梳理的整整齐齐。"
    "手里捧着一个黑色的包装礼盒，上面已经系好缎带。"
    "看起来已经完全没有了昨夜的狼狈。"
    show lh1 normalin at center_left 
    show lh2 shyout at center_right
    zeke "下午好。"
    "吉克笑着打招呼，将礼盒递过去"
    "利威尔没动，视线扫过他，还落回礼盒上"
    levi "这是什么？定时炸弹？"

    zeke "天地良心！"
    zeke "纯粹是为了感谢您昨晚的英雄壮举，我特意在楼下买的。"
    show lh1 annoyedin at center_left 
    show lh2 shyout at center_right
    levi "我记得楼下没有超市。"
    
    zeke "哦，不是隔壁小区新楼盘开盘了吗？"
    zeke "我去领了份伴手礼，顺便帮您领了一份。"
    
    "利威尔看着他，隔壁那个所谓的新楼盘还在打地基，除了泥坑和起重机外什么都没有。"
    show lh1 annoyedin at center_left 
    show lh2 shyout at center_right
    levi "你有病。"
    
    menu:
        "接过盒子":
            jump choice1_accept
        "关上门":
            jump choice1_reject

label choice1_accept:
    show lh1 annoyedin at center_left 
    "利威尔给出了精准的诊断，但他还是伸手接过了那个盒子，然后当着吉克的面，砰的一声关上门。"
    play sound "audio/door_close1.mp3"
    "门板震颤了一下，连带着走廊里的空气似乎都凝固了一瞬。"
    "然后，从外面传来吉克的一声轻笑。"
    "紧接着就是走远的声音。"
    
    "利威尔低头看着手里的黑色礼盒，犹豫了片刻，还是拆开了丝带。"
    "里面并没有什么定时炸弹，也没有恶作剧。"
    "那是一个过度包装的礼盒装隔音耳塞。"
    "黑色的天鹅绒衬垫上，一对小巧的椭圆形硅胶正躺在上面。"
    
    jump day3  # 跳转到片尾

label choice1_reject:   
    show lh1 annoyedin at center_left 
    "利威尔给出了精准的诊断。"
    "他没有伸手去接那个悬在半空中的礼盒，而是直接向后退了一步，握住门把手——"
    play sound "audio/door_close1.mp3"
    "「砰」"
    "他毫不留情地把门甩上了。"
    "门板震颤了一下，利威尔在门后站了两秒，确认门外那个金毛混蛋没有再按门铃或者发出什么奇怪的声音后，才转身回屋。"
    "他对于这种无聊的社交毫无兴趣，昨晚的帮忙纯粹是为了…止损。"
    "止住该死的噪音，好让他能睡觉。"
    "出门的时候，利威尔看见那个礼盒依然躺在门外。 "
    "他顺手抓起来，混进另一袋生活垃圾里"
    jump day3  # 跳转到片尾

label day3:   #转场加时间
# 这一行把 dissolve 改成 fade，黑屏淡入淡出
    scene hall2 with fade 
    show lh1 normalout at center_left
    show text "{size=40}DEC 24 | 02:00 PM{/size}" at truecenter with dissolve:
        xalign 0.05
        yalign 0.05

    $ renpy.pause(1.5) 
    
    hide text with dissolve

    "利威尔手里提着两袋垃圾。"
    "左手是昨天的打包好的生活废弃物，右手是那个仅仅拆封了五分钟的黑色礼盒。"
    play sound "audio/trash.mp3"
    "塑料制垃圾桶盖合上，发出沉闷的撞击声。"
    "他没有上楼把这东西塞进吉克的食道里，已经算他在和平年代修身养性的极限。"
    scene road with fade 
    
    show lh1 normalout at center_left
    "利威尔扔完垃圾，白皑皑的云已经飘到头顶。"
    "也许过一会就要下雪，他转身走向单元楼。"
    "家里的冰箱快要见底，该去趟超市了。"
    #黑屏转场
    
    "路过一楼大厅的公告栏时，利威尔看见一个熟悉的身影正弯着腰，手里拿着卷透明胶带，往布满灰尘的玻璃上贴一张A4纸。"
    "……又是那颗金色的脑袋。"
    "听到脚步声，吉克回过头。"
    show lh1 normalout at center_left 
    show lh2 normalout at center_right
    zeke "哟。这么巧。"
    
    levi "你在贴什么？寻人启事？"
    scene dog with fade
    "利威尔走近扫了一眼。那是张打印极其敷衍的寻狗启事，甚至连照片都没有，只有加粗的手写黑体字："
    "寻找一条中型犬，腿脚不便，性格暴躁。大概这么大。"
    levi "……那是昨天的狗？"
    
    zeke "显而易见。"
    
    levi "死了？你在招魂？"
    
    zeke "跑了。"
    play sound "audio/clothes.mp3"

    "吉克拍了拍手上的灰，语气里听不出多少焦急，倒是有几分无奈。"
    
    zeke "今天早上带它出门解决生理问题，刚打开门，它就像见了鬼一样冲了出去。"
    zeke "……很遗憾我没追上。"
    
    levi "。"
    levi "它断了一条腿，还缝了十几针。"
    
    zeke "是啊，医学奇迹，肾上腺素是个好东西。"
    
    levi "所以你在这贴这种东西有什么用？连张照片都没有。"
    
    zeke "总不能不管吧......"
    
    levi "早干嘛去了，当时怎么没叫住它。"
    
    zeke "叫了......但事情发生的太突然，我还来得及没给它起名......"
    zeke "......所以我刚在楼下喊了半天'喂'和'狗'，它完全没有回头的打算。"
    zeke "我也试过喊一些常见的，比如'Buddy'，或者'小黑'，可惜它也没反应。"
    zeke "现在的狗可能已经被殖民，听不懂英文。"
    show lh1 upsetout at center_left 
    show lh2 normalout at center_right
    levi "......"
    
    zeke "如果您看到它，麻烦通知我一声。"
    zeke "虽然我觉得它大概率已经跑远了。"
    
    "利威尔看着那张歪歪扭歪的寻狗启示。"

    show lh1 normalout at center_left 
    show lh2 normalout at center_right
    levi "是我也想跑。"
    
    zeke "真伤人啊，利威尔先生。"
    "利威尔没理他，电梯抵达一楼，他刷卡走进去。"
    #下面这句话可以黑屏显示
    scene black2 with dissolve  

    "这事到此为止，至少他是这么认为的。"

    scene supermarket with dissolve  # 
    show text "{size=40}Saturday | 02:00 PM{/size}" at truecenter with dissolve:
        xalign 0.05
        yalign 0.05
        
    $ renpy.pause(1.5) 
    
    hide text with dissolve
    show lh1 normalout at center_left 
    "全世界所有的超市在周六都会爆满。"
    "利威尔推着购物车站在入口闸机前，会员卡在感应区刷了第三次，红灯依然顽固地亮着。"
    查卡员 "过期了。"
    "站在旁边的工作人员听到动静，指了指屏幕。"

    查卡员 "先生，您的卡过期两个月了。"
    levi "我知道，我现在续费。"
    查卡员 "续费请去那边的服务台排队，这边不能办理。"

    "利威尔看一眼服务台前蜿蜒的长龙，那里至少排了三十个人。"
    levi "……"
    levi "。"
    "正当他准备离开去办理续费，或者干脆换个地方买的时候，有只手越过他的肩膀，\"滴\"的一声刷开了闸机。"
    "利威尔回头，看见吉克正站在他身后，带着一副莫名其妙的微笑，让他更加心烦意乱一百倍。"
    "怎么最近哪都有他？"
    "利威尔没吭声，侧过身让路，想把购物车推到服务台。"
    "吉克却没有走进去，而是站在闸机里，冲工作人员笑了笑，再指指利威尔。"
    play sound "audio/clothes3.mp3"
    show lh1 normalout at center_left 
    show lh2 normalout at center_right
    zeke "一起的。"
    show lh1 annoyedout at center_left 
    show lh2 normalout at center_right
    levi "？"
    zeke "这是我爱人，我这张卡是副卡，应该能带家属吧？"

    "工作人员愣了一下，视线在两个男人之间游移。"

    zeke "怎么？你们超市歧视同性恋？"
    "工作人员" "啊？不不不，当然不......"
    zeke "不歧视？那太好了。"
    zeke "快让…我老公进来吧，家里孩子等着吃饭呢。"

    "利威尔转身就走，吉克抓住了他的手腕。"
    "力道不大，莫名有种粘人的感觉。"

    levi "放手。"
    zeke "别走，我有事想跟你说。"
    levi "如果三秒内你不放手，我不保证你的尺骨会不会断掉。"

    "吉克立刻松开了手。"

    zeke "暴力倾向太严重了 ，利威尔。"
    show lh1 amazedout at center_left 
    show lh2 normalout at center_right
    levi "你跟踪我？"
    zeke "嗯，Galgame里都是这样的。"

    levi "哈？"

    "他又要走，吉克去抓，这次被利威尔侧身躲过。"
    show lh1 normalout at center_left 
    show lh2 upsetout at center_right

    zeke "等等，我是真的有事找你。"
    zeke "…昨晚那条狗找到了。"
    levi "恭喜，那你现在可以去照顾它了，而不是在这里造谣我。"
    zeke "就在地下车库，但我没抓回来。"
    levi "因为你是个废物？"
    zeke "因为情况有点怪。"
    levi "……什么意思。"
    levi "实在不行你就去报警，我没有那么热心肠。"
    zeke "但看你也不像是会放着不管的人。"

    "利威尔冷笑一声。"
    show lh1 annoyedout at center_left 
    show lh2 normalout at center_right

    levi "那你错了，我这辈子最讨厌的就是麻烦。"

    scene pet_section with dissolve  #   # 假设有超市背景图片


    "超市内部，宠物用品区"
    
    "利威尔站在超市的货架前，把两提卷纸扔进购物车里，发出的哐当的响声。"
    show lh1 annoyedout at center_left 
    show lh2 normalout at center_right
    levi "到底又怎么了？"
    play sound "audio/pickup.mp3"
    "吉克正在挑选狗粮，拿起来看一眼配料表，又放回去。"
    
    zeke "嗯？"
    levi "别装傻，你说它情况不对劲。"
    zeke "哦...我只看到了一个虚影。"
    zeke "就车库角落里。"
    zeke "我刚凑近，它就跑了……"
    zeke "速度很快，完全不像是做过手术的样子。"
    zeke "而且总感觉看见了不止一只..."
    
    "利威尔挑眉。"
    
    levi "流浪狗扎堆取暖，很正常。"
    zeke "不……"
    zeke "它的头不太对。"
    zeke "太暗了看不清，但轮廓很奇怪。"
    zeke "而且周围有一圈像是触须一样的东西在晃动。"
    levi "触须？"
    zeke "嗯，像是寄生虫，或者别的什么东西。"
    levi "喂喂？能不能拜托你在讲恐怖故事前，先去换个眼镜。"
    zeke "我也希望是我看错了，所以我打算回去之后再去看一眼。"
    zeke "……"
    zeke "你能跟我一起吗？"
    
    "利威尔沉默了一会。"
    show lh1 annoyedout at center_left 
    show lh2 laughout at center_right
    levi "理由？"
    zeke "我们都是一家人了，还跟我计较这些。"
    levi "吉克，等出了这个门，我就把这袋狗粮塞进你嘴里。"
    zeke "那我挑个无谷配方的吧，最近消化不好。"
    zeke "...开个玩笑而已，看在你昨天救它一命的份上，再救第二次吧。"
    zeke "或者救救我，要是真有什么变异生物，我一个人就死定了。"
    zeke "而且，我也找不到别人了。"
    
    "最后那句话说是很轻，带着一种奇怪的坦诚。"
    "利威尔看着他推着购物车的背影。"
    "肩膀很宽，但是有点垮。像个没长大的巨婴。"
    
    levi "...你买单。"
    zeke "好嘞，老公。"
    
# 假设有车内背景图片
    show lh1 normalout at center_left 
    show lh2 normalout at center_right
    scene car with dissolve  # 假设有车内背景图片
    play sound "audio/car_start.mp3"
    "吉克开着一辆和他本人气质很不符的SUV，车里点了香薰，只为了掩盖弥漫的烟味。"
    "利威尔坐在副驾驶，看着窗外倒退的街景。"
    "冬日白昼短，天已经完全黑了。"

    zeke "…既然你愿意帮我，那晚上我请你吃饭？"
    levi "没兴趣。"
    zeke "别这么冷淡嘛，吃饱了才有力气干活。"
    zeke "附近有家不错的日料，我上次去过，挺不错的，你呢？你平时吃鱼生吗。"
    levi "不去。之前路过看到厨师在后门戴着手套抽烟。"
    zeke "汉堡怎么样，你别说话，我帮你要儿童套餐。"
    levi "非要听我骂你，你才高兴。"
    zeke "开个玩笑，那火锅？"
    levi "太吵。而且身上会有味。"
    zeke "披萨呢，西餐？"
    levi "我不跟陌生人分同一张饼。"
    zeke "……"

    "吉克握着方向盘的手指紧了紧，面部肌肉微微抽动。"

    zeke "太棒了！你怎么知道我买了狗粮，我们可以吃那个，无谷无盐，还不会弄脏碗！实在干净又卫生。"
    levi "去你家。"
    zeke "...什么？"
    levi "我会做饭。"
    scene kitchen with dissolve 
    show text "{size=40}DEC KITCHEN | 03:00 PM{/size}" at truecenter with dissolve:
        xalign 0.05
        yalign 0.05
        
    $ renpy.pause(1.5) 
    
    hide text with dissolve

    "吉克的厨房意外的干净，只有刀具被拆开了，孤零零地挂在架子上。"
    play sound "audio/knife_chop.mp3"
    "利威尔熟练地把买来的牛肉切丁，洋葱切碎。刀刃撞击砧板的声音居然有一种奇异的解压感。"
    "吉克靠在门框上看着他。"
    show lh1 normalin at center_left 
    show lh2 normalin at center_right
    zeke "需要帮忙吗？"
    levi "问的真好，那你会什么。"

    "利威尔停下动作抬头看他，吉克想了又想，决定老老实实坐在那里等饭。"
    play sound "audio/fork_chop.mp3"
    "十分钟后，两盘牛肉意面端上了桌。"
    "没有什么精致的摆盘，就是很扎实的美国菜。热气腾腾，意面裹着油脂的香气。" 
    show lh1 normalin at center_left 
    show lh2 upsetin at center_right
    
    "吉克坐在对面，手里拿着叉子。"
    "他卷起一团送进嘴里，咀嚼了两下，动作停住了。"
    show lh1 normalin at center_left 
    show lh2 normalin at center_right

    zeke "……"
    levi "毒死了？"
    zeke "叹为观止。利威尔先生。"
    
    "利威尔没看他，只是低头进食。"
    "他的吃相和他切菜时一样利索，没有任何多余的动作。"
    scene apartment2 with dissolve 
    "吃完饭，利威尔回到自己的公寓，吉克在入户门罚站。"
    "很快，利威尔走出来，向他展示那把黑色的金属造物。"
    "那是一把枪。"
    show lh1 normalin at center_left 
    show lh2 annoyedin at center_right
    show text "{size=40} | 08:00 PM{/size}" at truecenter with dissolve:
        xalign 0.05
        yalign 0.05
        
    $ renpy.pause(1.5) 
    
    hide text with dissolve

    "吉克双手抱胸，挑了挑眉。"
    
    zeke "你还有这个…抓条狗而已，需要动用热武器吗？"
    levi "以防万一，如果真出了什么事，我是等死还是等你救我？"
    zeke "也是，保险开了吗？"
    play sound "audio/gunreload.mp3"
    "利威尔将枪上膛，咔哒一声脆响，金属的冰冷感在空气中蔓延。"
    "吉克站在门口，看着利威尔检查弹夹。"
    
    show lh1 normalin at center_left 
    show lh2 normalin at center_right

    levi "现在开了。"
    zeke "你以前到底是做什么的？求你不要告诉我是通缉犯好吗。"
    levi "当兵的。"
    zeke "怪不得，特种部队？还是雇佣兵？"
    levi "后勤，专门负责照顾你这种猪。"
    zeke "别这么说，我肯定更想要眼神更和善的人来照顾我。"
    play sound "audio/door_open1.mp3"
    "利威尔不再解释，推开门走了出去。"

    scene garage2 with dissolve  # 假设有车库背景图片
    show lh1 normalout at center_left 
    show lh2 normalout at center_right
    play sound "audio/feet_walk.mp3"
    "地下车库的感应灯坏了一半。昏黄的灯光把两人的影子拉得很长。"
    "这里安静得过分，连风刮过空旷地库的声音都显得格外刺耳。"
    "空气中弥漫着一股潮湿的霉味，混杂着机油的气息。"
    "两人并排，脚步声在空旷的空间里回荡。"

    show lh1 annoyedout at center_left 
    show lh2 annoyedout at center_right

    levi "这地方比你家安静多了。"
    
    zeke "那是，毕竟这里的住户大多不会说话，只会漏水。"
    
    levi "你是指那些车，还是指你的脑子？"
    levi "确定是这里吗？"
    play sound "audio/紧张.mp3"
    "话音未落，一道黑影从两人左侧的立柱后闪过。"
    "它的速度快得夸张，甚至不像是在奔跑，而是一帧画面直接跳到了另一帧。"
    show lh1 normalout at center_left 
    show lh2 upsetout at center_right
    levi "来了。"
    levi "在那边！"
    
    "利威尔的反应比利刃出鞘还要快。"
    "他瞬间转身，望向声音停顿的来源，右手已经摸向了后腰。"
    play sound "audio/hit.mp3"
    "——黑影停在了十米开外的一辆报废轿车顶上。"
    "那就是吉克一直在找的那条'狗'。"
    "或者说、曾经是。"
    "它的体型在放大缩小，皮毛像融化的蜡一样蠕动。"
    "从外貌上看，它有点像狼，双目炽热，下颌突起，但轮廓却不停变换。"
    "上一秒它还是一条脏兮兮的中型犬，下一秒它的脖颈处突然裂开，那颗狗头诡异地向后折叠，取而代之的是一只指节扭曲的人手。"
    "骨骼发出断裂时的脆响。"
    "从头上长出的人手有超过五根手指，指尖正对着他们，像是在打招呼。"
    zeke "……乖狗狗？"
    play sound "audio/scream1.mp3"
    '"手"猛地张开，一声尖锐的嘶吼从那道缝隙里爆开，声波几乎震碎了头顶的灯管。'
    
    show lh1 normalout at center_left 
    show lh2 annoyedout at center_right

    "吉克闭上了嘴。"
    "这玩意儿显然不需要医生，它更需要的是神父。"
    "利威尔一把将吉克拽到身后。"
    "与此同时，那东西凭空消失，利威尔回过头。"
    "紧接着，一股腥风直接出现在他的右侧耳边。"
    play sound "audio/gunshot.mp3"
    "砰！"
    scene CG5 with dissolve  
    "利威尔在千钧一发之际侧身开火，子弹击中了那团正在实体化的血肉，溅起一片发光的液体。"
    "怪物发出凄厉的惨叫，被冲击力撞飞出去。"
    "但利威尔也没能完全躲开。他的左臂衣袖被撕裂，一道深可见骨的抓痕瞬间渗出了血。"
    scene garage2 with dissolve 
    show lh1 normalout at center_left 
    show lh2 annoyedout at center_right
    zeke "利威尔！"
    menu:
        "别过来！":
            pass
        "这畜生会瞬移！":
            levi "这畜生会瞬移！"
            "利威尔说出这句话的同时，再次举枪射击。"
            play sound "audio/gunshot.mp3"
            "但他低估了对方的愚蠢，或者说，高估了和平年代人们的自保意识。"
            "吉克并没有停下，反而因为那触目惊心的血迹，加快脚步冲进了两辆车之间的空隙。"
            scene BE1 with dissolve   
            play music "audio/red sex.mp3"
            zeke "喂——"
            
            "那一瞬间，空气里的硫磺味浓烈到了令人作呕的地步。"
            "利威尔的瞳孔骤然收缩。"
            "在吉克身侧那辆废弃轿车的后视镜夹角里，一团肉红色的物质正在像高压水枪一样喷涌而出。"
            scene CG6 with dissolve  
            "嗤"
            "……只有利刃切开黄油般的'噗嗤'声。"
            
            "吉克的动作停滞了，一道整齐的红线出现在他的脖颈上。"
            "——刹那之间，血液从断裂的颈动脉里冲上天花板。"
            "四处飞溅的血液挤占了视野，长年接触的铁锈味充斥鼻腔。"
            "温热的。"
            "腥甜的。"
            "生命的温度正在以一种荒谬的速度流逝。"
            "利威尔站在原地，手里的枪滑落在地。"
            "世界开始旋转。"
            "眼前的画面开始扭曲，重叠。"
            "耳边响起了防空警报的尖啸声，还有那些永远无法停止的哭喊。"
            
            levi "……啊。"
            
            "你感觉自己的思绪变得迟钝。"
            "不止是这样，你的全部都因为惊讶而麻木不已。"
            "是因为还没能理解现在的状况吗"
            "现在"
            "面前……"
            "……面前有一堆正在变冷的肉块，血珠因为冲击力溅在脸上。"
            "黑暗彻底吞没了他。"
            "……"
            "END：死角"
            stop music fadeout 1.5 
            return
    scene garage2 with dissolve  
    "混乱持续了大概两分钟，感应灯因为打斗而不停闪烁。"
    play sound "audio/untitled.mp3"
    "枪声"
    "滴答声"
    "利爪刮擦"
    "非人类的嘶吼"

    "利威尔展现出了惊人的战斗素养，他利用立柱和车辆作为掩体，预判着那东西出现的方位，每一次开枪都精准地逼退对方的进攻。"
    "但这东西实在太诡异了。"
    "它总能从意想不到的角落钻出来。"
    "情况僵持到远处传来嘈杂的人声和手电筒的光束。"
    保安A "什么声音？！那边有人！"
    保安B "好像是枪声！快报警！"

    "怪物显然不想面对大群人类，身体融化着扭曲，钻进了墙角的一道阴影里……"
    "再次消失不见。"
    scene CG3-1 with dissolve  
    "利威尔喘着粗气，捂着流血的左臂，眼神死死盯着它消失的方向。"
    "一大群保安冲了过来，手电筒的光乱晃，刺得人睁不开眼。"
    "为首的保安队长手里拿着电击枪，紧张地指着他们。"
    
    保安 "不许动！都在干什么！把手举起来！"
    保安 "刚刚那是枪声吗？你们在械斗？！"
    scene CG3-2 with dissolve 
    "手电筒的光束打在利威尔身上。"
    "他半边身子染着血，手里还握着那把刚刚开过火的枪，一脸阴沉的煞气，比监狱里的家伙更像杀人犯。"
    
    保安 "呃…"
    保安 "放下武器！不然我们不客气了！"
    scene garage2 with dissolve 
    "周围的保安拿着防暴叉，谁也不敢上前。"
    "那把枪太有威慑力了。"
    "利威尔依然维持着举枪的姿势，胸口剧烈起伏。"
    "他在思考。"
    "杀出去？"
    "不可能，那他下半辈子别想安生了。"
    "解释？"
    "怎么解释？"
    "说刚刚有一条会变形的四足生物瞬移跑了？谁会相信？"
    "心里的烦躁如同岩浆一般涌上来，手臂应该是撕裂伤，不知道有没有伤到骨头，可能需要缝针。"
    play sound "audio/drop1.mp3"
    "「哐当！」"
    
    "利威尔突然甩手，那把枪重重地砸在水泥地上，滑出去几米远。"
    "对面的保安吓得集体后退了一步，他面无表情地抬起头。"
    show lh1 annoyedout at center_left 
    
    levi "我有病。"
    show lh1 annoyedout at center_left 
    show lh2 normalout at center_right
    zeke "……"
    保安 "？"
    levi "狂躁症…或者是精神分裂，随便你们怎么叫。"
    levi "我刚刚什么也没干，没人被我杀。"
    levi "我只是发病了，在乱开枪听响。"
    levi "……那把枪也是假的，模型。你要是不信自己去捡。"
    zeke "……………………"  
    "保安队长一脸你在逗我的表情，他看着地上的枪，又看看利威尔那副随时可能暴起伤人的样子，一时间竟然不知道该不该信。"
    
    保安 "你有病？病例呢？"
    levi "上次犯病的时候被我吃了。"
    
    "利威尔不再说话，保安的嘴角抽搐了一下。"
    "吉克从立柱后走出来，一边剧烈的咳嗽，一边快步凑近利威尔。"
    
    zeke "……咳！"
    zeke "咳，咳咳咳！咳！"
    
    "他摸遍了全身上下的口袋，最后从裤兜里掏出两片薄荷糖，哆哆嗦嗦地塞进利威尔嘴里。"
    show lh1 amazedout at center_left 
    show lh2 shyout at center_right

    zeke "你看你……又忘记吃药了，早说了别来这种阴暗的地方，容易刺激病情……"
    
    "利威尔开始冷笑，他把吉克推开半米，还补了一脚，吉克疲惫地转头。"
    
    zeke "实在抱歉……我是他的医生…兼监护人。"
    zeke "他这几天病情不太稳定，刚才是出现了幻觉。"
    zeke "我叫吉克·耶格尔，这是我的钱包，里面有行医资格证和驾照，还有一些现金……"
    
    "保安打断他的话。"
    show lh1 normalout at center_left 
    show lh2 annoyedout at center_right
    保安 "那这血是怎么回事？"
    zeke "啊，他不小心把自己弄伤了。"
    zeke "你们可能不知道，但这种病发作时很难控制。"
    zeke "我会带他回去处理伤口的，顺便加大剂量。"
    zeke "如果有什么损失，或者罚款，尽管来找我。"
    zeke "抱歉给各位添麻烦了。"
    
    "吉克一边说着，一边极其自然地伸手揽住利威尔没受伤的那边肩膀，半强迫地带着他往电梯口走。"
    jump day4

transform center_left:
    xalign 0.1  # 屏幕20%位置
    yalign 1.0

transform center_right:
    xalign 0.9  # 屏幕75%位置
    yalign 1.0