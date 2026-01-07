label day5:
    scene garage2 with dissolve
    show lh1 normalout at center_left 
    show lh2 normalout at center_right
    
    play sound "audio/stretch.mp3"
    "吉克站起身，在原地蹬腿，缓解膝盖的酸痛。"
    zeke "行了，我不干了。"
    zeke "也许她根本就是个鬼魂，或者幻觉，幽灵，一个小孩大半夜出现在这里，本来就足够可疑。"
    zeke "既然她不想走，我们也别在这儿浪费时间。"
    zeke "我已经感觉我的脚趾头要被冻得坏死了。"
    
    show lh1 annoyedout at center_left 
    levi "你把她一个人扔在这儿？"
    zeke "是她自己不走的！而且那个怪物还没找到，你记得吗，很危险。"
    zeke "我们走吧，利威尔。"
    zeke "我只想回去睡觉，现在我可以告诉自己是良心在痛，而不是头，毕竟是我见死不救。"
    
    levi "不行，至少要报警，活人待在这个温度没多久就会冻僵，何况一个小女孩。"
    zeke "报警？你想跟警察说什么？说我们在地下车库发现了一个没有舌头和瞳孔的幽灵？"
    zeke "如果警察来了她又不见了，这次我们要编什么理由？"
    zeke "集体精神分裂吗。"
    zeke "就算我们能把她强行带走，那被监控拍下来也完蛋了，你还在候审阶段，被发现了只有死路一条。"
    
    show lh2 normalout at center_right
    play sound "audio/footsteps_leave.mp3"
    "吉克边说边转身，直接朝门口走去。"
    
    zeke "我们先回去从长计议，或者去拿毛毯给她......"
    zeke "这里有零下几十度，利威尔，再坚持下去，率先失温的会是我。"
    
    "利威尔看一眼吉克。这家伙的脸色确实苍白得厉害，额头上甚至渗出了一层不正常的淡青色。"
    "确实，继续耗在这里毫无意义。"
    
    
    show lh1 normalout at center_left 
    "利威尔最后看了女孩一眼，也转身跟上了吉克。"
    "吉克松了一口气。"
    zeke "走吧。"
    play sound "audio/barefoot_step.mp3"
    "——在他说出那两个字的那一刻，身后传来了细碎的脚步声。"
    "啪嗒，啪嗒。"
    "像是赤脚踩在水泥地上的声音。"
    "利威尔停下脚步，回过头。"
    
    show lh1 amazedout at center_left 
    levi "......吉克，看来她听懂了。"
    zeke "什么？"
    
    show lh2 upsetout at center_right
    "吉克也回过头，他刚刚走出去不近的一段路，而现在女孩距离他只有两米。"
    "女孩跟了上来，在他说出那两个字之后。"
    
    zeke "......你是她说懂了'走吧'？"
    levi "显而易见。"
    zeke "刚才我劝了半天她不动，我说我要走了她反而跟上来了？"
    zeke "这是什么逻辑？叛逆期？"
    levi "看来她确实比较喜欢你。"
    
    show lh1 normalout at center_left 
    "利威尔抱着胳膊，不管是因为任何原因，至少今晚她都不会被冻死了。"
    
    levi "恭喜你，耶格尔医生，也许你长得像她爸。"
    show lh2 annoyedout at center_right
    zeke "别开这种玩笑，一点都不好笑。"

    "吉克看着那个只到他腰部的小女孩，感到一阵莫名的头皮发麻。"
    "这种无缘无故的顺从比刚才的沉默更让他觉得诡异。"

    levi "既然她愿意跟着你，那就带上去。"
    levi "总比扔在这儿强。"
    zeke "我讨厌小孩，利威尔，我后悔了，你现在能去报警吗。"
    levi "别抱怨了，救人一命是好事，这是你说的。"
    zeke "重点不是这个！重点是你难道不觉得诡异？！"
    zeke "我昨天晚上刚梦到她压在我身上，现在又来这一出，我怀疑自己根本没醒！"
    show lh1 annoyedout at center_left 
    levi "停，她不是聋子，你能别在小孩面前说这种恶心的话吗。"
    zeke "你还在在乎这个？我刚刚都没考虑过邻居看我带一个小女孩回家会怎么想。"
    levi "想你终于把你那个私生女接回来了。"
    show lh2 normalout at center_right
    "吉克翻了个白眼。"
    zeke "利威尔，如果真的有人问，我就说这是我给你生的。"
    scene black with dissolve
    "To be continued..."

label list1:  
image credits_text = Text(
    "{size=+12}{b}制作团队{/b}{/size}\n\n"
    "{size=+9}美术 |   周麻美     wb@周麻美{/size}\n"
    "{size=+9}编剧 |   闲云野猪   wb@爱我吧安德鲁{/size}\n"
    "{size=+9}程序 |   Ekur1     wb@Ekur1{/size}\n\n"
    "{size=+12}{b}其他贡献者{/b}{/size}\n\n"
    "{size=+9}{i}测试人员{/i}{/size}\n"
    "{size=+8}爱踩电门 洗特勤 汐 魁蛇{/size}\n\n"
    "{size=+9}{i}音乐{/i}{/size}\n"
    "{size=+8}red Sex_Vessel{/size}",
    
    xalign=0.5, 
    yalign=0.5,
    text_align=0.5,
    line_spacing=20,
    slow_cps=20
)

# 滚动效果定义
transform credits_scroll:
    ypos 1.0  # 从屏幕底部开始
    linear 20.0 ypos -1.0  # 20秒内从底部滚动到顶部

label end:
    # 游戏结束后的片尾滚动
    scene black3
    show credits_text at credits_scroll
    $ renpy.pause(20.0, hard=True)  # 20秒不可跳过的暂停
    hide credits_text with dissolve
    jump else
    
label else:
    zeke "说起来，明天就是圣诞节了吧。"
    levi "你有安排？我可以照顾她。"
    zeke "倒是……没有。"
    zeke "圣诞节快乐。"
    levi "明天才是圣诞节。"
    zeke "现在已经过了十二点了，所以，圣诞节快乐，利威尔。"
    levi "……"
    levi "哼……"
    

    menu:
        "圣诞节快乐":
            pass
    return

# 删除最后的 jump end 语句
