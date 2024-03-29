---
title: "[游戏评论] 超阈限空间"
date: 2023-06-03T19:20:33+08:00
categories: ["游戏"]
toc:
    enable: false
---

> 道理我都懂，但鸽子为什么这么大？

对于《超阈限空间》而言，这个问题的回答是：因为鸽子真的有这么大。

《超阈限空间》是一个第一人称的解谜游戏，主要的解谜要素为透视类的错觉，结合了一点空间传送机制。

所谓透视错觉，在游戏里的直观体验就是利用近大远小的原理，将近处的实际很小的物体变为远处实际很大的物体，或者反过来，而在物体缩放尺度变化的过程中，物体在屏幕上的大小是不变的。
玩家需要控制镜头，让物体在屏幕中心，从而可以用鼠标抓住它。
但游戏提供的交互十分有限，不支持拖动物体，而只能行走和转镜头。于是如果玩家要控制物体的远近（进而控制物体大小）就需要抓住物体走到合适的位置，并转到一个合适的角度。游戏会根据屏幕中心 raycast 到的场景碰撞体的距离决定当前控制所物体的实际位置和大小，物体会沿着视线方向尽量往远处推移，直到发生碰撞。想要物体变小，只要走到远处，抓起它，放到脚下就行了，反之亦然。

游戏总共分为 9 个大关卡，其中每个又有若干小关卡，多数大关卡完成后会进入电梯，这个设计颇有《传送门》的风格。
解谜难度不大，比传送门还要稍简单一点，初见通关流程大约需要 3 个小时。下面是一个视频演示：
{{< bilibili id=BV1oV4y1672j >}}

玩家在解谜时可做的操作非常少，因此往往只需要做一些尝试就能解开谜题，这也是游戏难度不大的主要原因。也有一些地方需要进行一番思考，解法也特别离谱，在为自己的机智而得意的同时赞赏制作人巧妙的设计。把几个游戏机制相结合，可以创造更多的玩法，例如有几个谜题涉及到了传送门，从一个门进去，会从另一个门出来；进入时人相对于门的大小与出来时保持相同，类似于哆啦A梦里的缩小隧道，因此可以同控制门的大小来控制人的大小。遗憾的是这种谜题不多，大部分关卡解法都比较类似。

剧情方面，有网络上的专业评论家从哲学的角度分析游戏中的各种细节，包括看似不知所云的旁白、游戏名字的含义、贯穿整个游戏的梦境的隐喻等等。
是否真的如这些分析所说，只有游戏制作人本人才知道了。
游戏通关后解锁的附加内容有一部分就是讲述开发者在设计关卡时的想法，类似于电影的拍摄花絮。看得出游戏开发者是真的非常满意自己的点子，并且乐于分享出来。

游戏从各个方面都很有 V 家的 Source 引擎那味儿，包括光影、控制，甚至连晕 3D 的感觉也是，毕竟 Source 引擎最擅长的就是 FPS，各种第一人称控制游戏自然是不在话下。但它实际上是用 Unity 制作的。



