---
title: "译介丨Maxwell Foxman 团结则立：Unity 引擎带来的平台、工具与创新 (2019)"
date: 2023-12-20T20:37:08+08:00
toc:
    enable: true
hiddenFromHomePage: true
hiddenFromSearch: true
---

<br/>

{{% noindent %}}

作者: Maxwell Foxman

译者: 赵晟苏, 松果, 叶梓涛, RMHO

来源: https://www.gcores.com/articles/172111

原文: [Link](https://journals.sagepub.com/doi/full/10.1177/2056305119880177) 

{{% /noindent %}}

<br/>

无论我们承认与否、游戏引擎的幽灵始终飘荡于一切基于此引擎所构建的游戏之中

## 按

2023 年 9 月 12 日，Unity 官方宣布将执行新的收费标准。9 月 18 日，Unity 发布道歉声明，表示将会对新收费方案进行调整。10 月 9 日，Unity 总裁、首席执行官兼董事长 John Riccitiello 辞职。

这场围绕 Unity 收费政策的新闻着实让行业热闹了一把，而这关联的并非某个游戏，或某位游戏制作人，而是一场由常常隐身于游戏开发背后与基底的引擎（engine），也就是本文所说的平台（platform）所引起的动荡。

虽然诸如 Godot 等晚近的引擎竞争者借此风波赚了一把名声，朋友圈纷纷充满了「卸载 Unity 到安装 Godot 只要五分钟」，「我 UE5 才是天下第一」的声音，但是大概率这场事件过后，原先的开发者依旧会每天登入 Unity 账号，一边骂着一遍激活个人的 license，继续开始之前重复了几百天的日常。

这就是平台的力量。

游戏引擎扮演着一股无处不在的力量，贯穿在游戏创意，商业，类型化的始终，同引擎公司的愿景，使用者的需要而发展，不断调整其形态。毫无疑问，不同的引擎都有其适合构建的游戏世界的形态，也预先蕴藏着对这种虚拟世界可能性合集的意识形态判断。这就是为什么我们要鼓励看到诸如 Bitsy，Twine，Pico-8，Godot 这类游戏引擎的多样性的可能，以及诸如 Bogost 等研究者提倡的平台研究（Platform Studies）的实践。

引擎在这个意义上可以说是「做游戏的游戏」，而开发者也在逐渐变为这「游戏」的「玩工」（playbour），掌握着从不同的软件和引擎 bug 之间连接起的脆弱的工作流，并依赖着这张由硬件/软件/插件/素材围绕游戏引擎的平台而连接成的复杂网络。过去人们仰赖于自己的双手与斧钺来生存，而今天的许多开发者则将自己的技艺与未来寄托在脆弱的平台与连接之上。

无论我们承认与否，游戏引擎的幽灵始终飘荡于一切基于此引擎所构建的游戏之中，并始终成为其不可忽视的一部分。

叶梓涛

落日间

## Maxwell Foxman

麦克斯韦·福克斯曼是俄勒冈大学（University of Oregon）新闻与传播学院媒体研究/游戏研究助理教授。他的主要研究重点是游戏如何在非游戏环境中表现出来，包括社交媒体、政治和新闻机构。他的作品始终如一地探索媒体制作人在活动和职业生活中构建游戏和游戏的方式。

翻译：赵晟苏

校对：松果 叶梓涛

编辑：RMHO

原文链接：[点击跳转](https://journals.sagepub.com/doi/full/10.1177/2056305119880177)

###  United We Stand: Platforms, Tools and Innovation With the Unity Game Engine

团结则存：Unity 引擎带来的平台，工具与创新 

## 摘要

游戏引擎 Unity 和 Unreal 之间的遭遇战为文化生产的平台化（plaformization）开辟了一条新战线。本文认为，这些程序是「平台工具」（platform tools）。它们虽然能让业余爱好者和专业人士为平台构建内容，但却在数字创意作品的构思、制作、实现和发行过程中「锁定」（lock-in）行业意识形态，从而导致开发者、实践和产品的同质化。Unity 引擎的历史、功能和其在游戏制作流程中的地位使其成为 「平台工具」的典范。对 90 名 VR 爱好者的访谈结果表明，Unity 为开发者的日常活动设定了界限或「规则」，尽管他们对这一媒介的潜力充满热情，但却不得不按照流行的游戏类型和标准来创作内容。

数字平台的发展一直受到「战争」的困扰。Windows/Mac、Google/Yahoo、Facebook/Myspace 和 iOS/Android 之间的冲突为平台制造商建立了战场，以保持对「创意内容生产条件」的控制（Gillespie, 2010, 358）。虽然此类争斗有据可查，但 Epic Games 和 Unity Technologies 之间的另一场争斗却暗流涌动，这两家公司的游戏引擎「正在争夺人心」（Takahashi, 2015）。除了游戏，两者还在争夺对虚拟现实（VR）和其他沉浸式媒体的控制权。最终，通过其软件的技术规范、与其他平台的互操作性（interoperability）和商业模式，战争的胜利者将拥有制作交互内容的实际「工具」。

本文探讨了 Unity 游戏引擎是如何为游戏和新兴技术（如 VR）设定标准的。为此，我首先回顾了有关「平台化」的文献，这些文献揭示了平台的经济、社会和技术构成中蕴含的一种持久逻辑。这种逻辑的一个基本组成部分是「锁定」，即平台之间相互依赖、相互操作，以确保市场的可行性。然而，「锁定」也限制了创造性和意识形态的替代方案。这些限制正是我所说的「平台工具」或生产力软件的典型特征，它们同时支持与锁定了业余爱好者和专业人士为平台构建数字内容的方式。

Unity 让我们看到了平台工具对创作者的影响力。它既为虚拟世界的构建提供了必要的元素，又迫使开发者采用其所涉及的游戏和科技行业的规范。为了揭示软件对创作实践的影响，我们对一些 VR 爱好者进行了半结构化访谈。他们的观点阐明了引擎在当前和未来制作模式中的作用。Unity 开启了玩转 VR 的便捷入口，同时也锁定了数字游戏文化和产业的类型、用户身份、专业标准，甚至该媒介的潜在未来。

## 平台的问题

对于「平台」（platforms），「没有一致的定义」（Martens, 2016）。该术语描述了各种现象：从社交网络（Helmond, 2015）到音乐发行服务、游戏主机（Montfort & Bogost, 2009），以及广义上发生交换的任何多方市场（Martens, 2016）。

注：这一情况的部分原因是管理研究、媒体研究、文化研究和政治经济学等多个领域都在研究平台。详情参见 Plantin, Lagoze, Edwards, 和 Sandvig（2016）

因此，Nieborg 和 Poell（2018）根据平台能够「依势而变」（contingency）的特点对其加以界定（第 4276 页），即**它们既相互依赖，又不断变化。**

因此，可以将平台理解为一种应用程序、软件环境或服务：它们在经济上（通过多方市场）和技术上（通过可互操作的代码）依赖于其他平台，在可变性和模块性上依赖于其他平台，并在功能上依赖于用户内容和反馈。

### 平台化

鉴于平台的定义和影响范围广泛，学者们也试图提炼出平台的共性。 Schwarz（2017） 指出，从基于代码的本地控制到全球网络，所有层面的使用都有一个复杂的「平台逻辑」（第 94 页）。「平台化」，正如 Nieborg 和 Poell 所命名的这一逻辑，指的是「数字平台在经济、政府和基础设施扩建中的渗透」（第4276页）。这代表了文化生产中哲学和政治学的三个根本性转变：第一，平台在塑造多方市场中的作用；第二，平台提供者对用户的控制；第三，软件本身的基础架构（第4281页）。

其结果是，平台对数字内容的生产、消费甚至创意都施加了限制：生产者修改其产品以适应平台化的商业模式，而开发者则有动力生产「适时的、模块化的、不断改变的、并为平台盈利而优化的」内容（第 4282 页）。

最后，平台化将权力和股权整合到少数全球「平台巨头」手中，由于平台经济固有的互联性和互操作性，这些巨头可以进一步巩固自己的地位。 Bechmann（2013）将这一现象称为「内操作性」（intraoperability），以强调终端用户与「在市场份额、态度或默认许可（acquiescence）方面占主导地位」的提供商之间权力关系的不平等（第75页）。最终，留住用户或将他们 「锁定」（第 84 页）在平台化生态系统中是平台领导者的意识形态特权。

### 锁定

「锁定」虽然很少成为平台研究的明确重点，但却是进一步解释平台化影响的一个有用概念。「锁定」是公司、产品和消费者之间的一种协商，在这种协商中，围绕产品的规范和用途被设定和采用。在此过程中，不同的标准和产品被模糊化，因为转移到或引入替代品变得更加困难和昂贵。

这一概念源于经济学和对路径依赖的研究，即「存在有限数量的完美稳定替代状态，其中之一将根据特定的初始条件出现」（Margolis & Liebowitz, 1998）。锁定解释了历史、社会因素和商业战略如何导致劣质消费品和服务被采用。经典的例子包括 QWERTY 键盘战胜了更为理想的 Dvorak 键盘，VHS 录像带战胜了 Betamax 录像带。

> Dvorak 键盘于 1936 由 Auguse Dvorak 教授提出，这款键盘的支持者认为，它的键位分布相比 QWERTY 键盘更符合人体工程学，因此可以提升使用者的打字速度，减少肌肉劳损。

注：有人批评这些例子夸大了竞争产品之间的差异（Cantner & Vannuccini, 2017; Liebowitz & Margolis, 1995）

在这两个案例中，劣质产品之所以在市场上占据主导地位，在标准化竞争之前，它们就「锁定」在用户那里了。除了消除竞争性替代品之外（Cantner & Vannuccini, 2017, 第 11 页），锁定的价值还在于，一旦在消费者的生活中确立，它既会保留产品或服务的盈利性，也会保留其失败性。

在对平台的批判中，锁定被认为是寡头控制市场（Bodle, 2011）、用户、开发者和供应商的根源（Nieborg & Poell, 2018；Plantin, Lagoze, Edwards, & Sandvig, 2016）。然而，这些文本并未将这一概念放在研究的首位。

这可能是因为它的应用太过广泛了。仅在商业研究中，供应商、创新和技术都可能被锁定。 Shapiro 和 Varian（1998）也描述了锁定客户的好处；由于从被锁定的产品转移需要高昂的成本，用户可能会被诱导继续使用这些产品多年（如微软 Office）。锁定既是一种技术规范，也是一种商业策略，甚至是对采用创新的一种简单解释。

我认为，锁定也是一种阻碍竞争选择的意识形态，反映了流行技术哲学家 Lanier（2011）的担忧：

> 如果某些想法难以融入已成为主流的数字化再现方案，锁定就排斥它们……通过抹除自然语言和程序语言意义间的神秘界限，减损和限制数字化再现方案(p. 10)
> 
> Lock-in removes ideas that do not fit into the winning digital representation scheme . . . and reduces or narrows the ideas it immortalizes, by cutting away the unfathomable penumbra of meaning that distinguishes a word in natural language from a command in a computer program.

当文化生产者被特定软件规训后，他的创造潜能就会被抑制，它就限制了文化生产者的创造潜能。因此，「锁定」对文化生产有三个作用：它设定了消费者对使用的期望，为通用做法建立了技术和社会流程，并且，也许最重要的是，它使企业的要求和理念得到了巩固和制度化。

因此，锁定是评估平台化和突发事件影响的重要途径。它确立了公司、消费者和生产者与平台互动的技术和经济标准，同时限制了他们的创造可能性，并为他们提供了创作的标准化参数。换句话说，平台可以锁定用户工作、娱乐和生产的工具。

### 平台工具

在考虑我所说的「平台工具」时，锁定具有特别重要的意义。与 Facebook 等社交平台、Spotify 等分发平台，甚至 Etsy 等在线市场相比，这些软件使业余爱好者和专业人士都能通过平台或为平台制作内容，从而达到明确的功利目的。作为工具，它们是整个制作过程中不可或缺的一部分——从项目的构思到创作、制作，直至最终发行。但作为平台工具，软件在每个阶段都「锁定」了特定的做法，根据平台化的数字媒体生态系统设定了规则和准则。

与平台一样，这些工具的经济可行性也依赖于其他平台，并不断变化以满足现有平台和新平台的需求，最终依赖于消费者/制作者使用它们制作内容。但它们在一些关键方面是不同的：它们产生的应用程序和创意作品可能并不明确地与某个平台挂钩或托管在某个平台上（尽管它们通常是这样），而且它们并不被称作市场。

注：就 Unity 而言，市场是其特性，但不是引擎的核心组件

相反，平台工具充当行业与平台之间的中介，协助构建独立的应用程序。然而，这一功能的副产品是，它锁定了与这些行业相关的特定意识形态。

因此，平台工具类似于「中间件」（middlebroware；Lesage, 2015）或一套「商品化媒体软件及其相关设计实践」（第 90 页），作为「粘合剂」来「同时促进和限制文化内容的生产、流通和欣赏」（第 92 页）。Lesage 以 Adobe Photoshop 为例，他指出，Adobe Photoshop 也是一款面向专业人士和业余爱好者的软件，它不断增加格式、功能和第三方插件，使其成为塑造数码照片再生产的主体和方式的重要力量。在我的概念中，平台工具与 Lesage 所关注的内容的「符号秩序」（symbolic order）并不相同。此外，Photoshop 并不需要可互操作的或可内操作的平台来成功创作或传播照片。

注：与此同时，平台工具可被视为中间件的进化，并体现了 Lesage（2015 年）的研究成果，即用户沉迷于「有趣的、不太严谨的实验」（第 106 页）。

在内容创作方面，它也没有广泛使用预制软件包、工具包和应用程序接口（API；软件程序中使用现有代码的底层规则集。有关平台化方面的分析，请参见 Helmond, 2015）。这些都加深了路径依赖，因为对开发人员来说，使用兼容软件和预制代码比从头开始编程更省事。然而，软件包通过提供可被设计的路线图，进一步定义了应用程序之间的交互方式。这些技术限制是软件研究对平台批评的核心。 Bogost (2008) 指出，它们「既促进又限制了话语生产，就像自然语言规则限制了诗歌，光学规则限制了摄影一样」（第 66 页）。不过，他补充说，这种限制可以增强用户的能力，甚至可以发挥创造性的作用。同样，Plantin 等人（2016 年）描述了平台如何通过 API「同时允许和限制表达」（第 298 页），API 充当「门户，允许其他系统与主导平台互动」（第 303 页），而主导平台「将群体锁定在由主导公司定义和控制的格局中」。这一论断强调了一个概念，即像 Unity 游戏引擎这样的平台工具是一个节点，通过它我们可以看到平台化和锁定对平台和制作者的影响。

## 作为平台工具的 Unity

Unity 的功能和市场选择使其成为典型的「平台工具」。作为一个「引擎」，它是一种实用工具，其明确目的是为更广泛的发行而构建游戏和应用程序。此外，它还与游戏制作的各个方面相连接，并通过自己的多方市场和兼容软件包与现有平台对接。

尽管 Unity 在游戏开发中无处不在——45% 的独立开发者使用 Unity，而根据流行报道（Beschizza, 2018），虚幻引擎（Unreal）只占据了 2% 的市场份额——但有关该引擎的批评性文献却少得令人吃惊。 Schmalz（2015 年）在其关于 2000 年代视频游戏创新史的论文中简要提到了虚幻引擎。 Panourgias、Nandhakumar 和 Scarbrough（2014） 写到通过 Unity（没有特别提到它）等引擎进行的游戏设计；他们认为，开发需要创意意图与编程中的实际限制之间的相互作用。 Whitson（2018）则更进一步，论证了 Unity 在游戏工作室中扮演的重要角色。随着 Unity 成为一种流行的开发工具，即使路径依赖被固定下来，学者们也没有解决锁定、平台和文化生产等问题。

### 为什么是 Unity？

Unity 与其他「游戏引擎」一样，是一个「软件框架」或一套工具，可帮助开发人员进行渲染、物理处理和输入，使他们不必从头开始构建虚拟空间（Ward, 2008）。该引擎为三维（3D）和二维（2D）虚拟世界提供了构建模块，这可不轻松；想想我们认为理所当然的无数自然法则——从重力到我们接触他人时他人的反应。要使虚拟空间具有可玩性，就必须考虑到生活的这些基本方面。

2009 年之前，大多数游戏引擎都是专有的，由公司严密保护。Unity 从一开始就摒弃了这种模式，直接向爱好者提供工具。引擎的发展势头来自于「模组」（modding）运动，即爱好者根据发行商提供的足够代码来修改游戏。 [Kücklich（2005） 将这种「模组开发者」（modder）活动定义为「玩工」（playbor）](https://mp.weixin.qq.com/s?__biz=MzIzMjM0NDk1NQ==&amp;mid=2247488489&amp;idx=1&amp;sn=6b7d574ae383100f07fe84b8de03602e&amp;chksm=e8970ffddfe086eb6113f62987d814595c88b2a6ea61004c08b1c41ea21d90d0e6811ea6173b)，这些活动利用了客户的忠诚度，通过让 模组开发者生成新内容来增加现有产品的生命力和价值，并充当创意的试验场，而这一切都源于用户的热情和过分的努力。

玩工的出现让 Unity 从一个付费应用程序转变成一个只在开发者获得一定收入后才向其收费的应用程序： 在我的研究期间，这一标准是 10 万美元（Downie, 2016）。通过这种方式，他们的商业模式利用了独立和移动开发者的热情和工作所取得的成功（Haas, 2014，第 10 页）。此外，随着知名度的提高，该引擎还拓展了新的市场，包括企业软件和数字动画。

这些策略使 Unity 成为制作游戏和其他交互材料的首选工具。 Whitson（2018） 描述了开发人员如何将该应用程序视为制作的「最小公分母」（第 2319 页），因为它可以与不同团队和工作室的软件对接。这强调了 Unity 作为「平台工具」的依势而变（contingency），以及该引擎在用户「学徒化」和「社会化」（第 2321 页）方面的作用；Unity 传授基本技能，甚至「共同目标」（第 2322 页）。正如我在访谈中证实的那样，Unity 从内心里塑造了整个制作体验。

这与该公司希望传达的形象不谋而合：为「世界各地的开发者提供工具，以创建丰富的交互式 2D、3D、VR 和 AR 体验」。事实上，随着硬件成本的降低，沉浸式技术近来大受欢迎的原因之一可以归结为软件的互操作性和易用性。开发者可以制作跨设备的内容，并通过苹果公司的 App Store 和 Steam 游戏库等低成本市场进行分发，这促使商业 VR 软件层出不穷。与此同时，包括谷歌、Facebook 旗下的 Oculus 和微软在内的平台巨头也与 Unity 联手制造头显，以促进内容创作。

Unity 的流行让人们对该引擎产生了一种自相矛盾的看法。一方面，它被认为实现了游戏制作的民主化。Ars Technica 的一篇文章表达了一种常见的说法： Unity「真正做到了让任何人都能制作游戏」，「在过去的半个世纪里，独立游戏和艺术游戏蓬勃发展，Unity 功不可没」（Axon, 2016）。另一方面，该引擎也可能让缺乏经验的开发者创造出大量劣质内容。文章接着说，民主化有一个「意想不到的副作用——它降低了玩家的质量标准。更糟糕的是……新的 Unity 游戏的泛滥使本已困难重重的市场更难盈利」（Axon，2016）。总之，引擎除了在游戏开发和 3D 制作中发挥作用外，还与为各种平台制作内容的对象、方式和方法密不可分。

### Unity 的平台特性

Unity 包含许多与其他平台相当的功能。首先，它具有互操作性。为了能在多种平台和游戏主机上发布游戏，Unity 开发了一种「构建并运行」（build and run）协议，只需轻点按钮即可在不同设备上加载并开始播放内容。代码会不断更新，以适应新兴格式的构建。

与此同时，Unity 的业务扩展还包括开设自己的多方市场。他们的「资源商店」（Asset Store）允许业余爱好者和专业人士上传自制场景、代码、附加组件和头像，供其他用户下载（免费或收费）并填充虚拟空间。

最后，该引擎大量使用可内操作的代码。开发人员不仅可以使用 Unity「资源包」（package）将自己的资料轻松导出到其他计算机，还可以导入硬件制造商编写的代码。资源包通常包括定制的「场景」（scenes）或虚拟世界设置，在这些场景或设置中，硬件和软件的能力被建模和评估。如果有新设备问世，例如手部追踪的「Leap Motion」控制器，就可以通过引擎下载场景，这样开发人员就可以测试硬件，并利用它们制作游戏和应用程序。

因此，Unity 将自己定位为不可或缺的中间人。它在制作的每一个阶段，从汇集内容、在虚拟空间中重构内容，到出版和发行，都能与各种可内操作的平台和市场互动，使其成为一种标志性的平台工具。

### Unity 中的制作流程

为了更好地理解 Unity 在平台和视频游戏生态中的地位，需要对游戏开发的制作流程进行简要说明。根据计算机科学家 Labschütz、Krösl、Aquino、Grashäftl 和 Kohl（2011 年）的研究，游戏开发包括四个步骤：构思或「概念阶段」（第 3 页）、制作或「三维内容创作管线」（第 3 页）、实现（第 6 页）以及发行或「发布」（第 7 页）。

注：虚拟现实（VR）、增强现实（AR）和其他形式的虚拟世界构建也采用了相同的制作流程。

游戏开发是迭代式的，而且经常是递归式的。用户在开发过程中会在各个阶段之间来回切换。（注：Whitson 还通过 Unity 和三维（3D）Studio Max 介绍了这一过程，2018）如图 1 和以下章节所示，每个阶段都巩固了 Unity 在游戏制作中的关键中介角色，同时将现有平台的标准锁定在开发流程中。

图 1. 包括 Unity 平台工具功能在内的游戏开发制作流程
- 构思（Ideation）：将概念带入 Unity 中进行制作。Concepts brought into Unity for production.
- 制作（Production）：从现有建模程序和 Unity 资源商店导入资源。Assets imported from existing modeling programs and Unity Asset Store.
- 实现（Implementation）：默认设置、SDK 和 Unity 资源包为现有平台控件提供易于使用的接口。Defaults, SDKs, and Unity Packages provide easy-to-use interfaces for existing platforms' controls.
- 发布（Distribution）：Unity 向现有平台和相关市场发布。Unity publishes to existing platforms and related marketplaces.

### 构思

在构思阶段，最初的概念、美学、机制和关卡在经过头脑风暴后，会被引入引擎。即使在用户构思游戏时，Unity 也会将自己锁定为平台工具。从某种程度上说，正是因为内容可以轻松地从构思推进到发布，Unity 才对用户具有吸引力。Labschütz 等人（2011 年）选择该引擎的原因之一是其简单的拖放功能，这意味着几乎无需编码即可导入美术内容（第 2 页）。

### 制作

制作包括创建将在游戏虚拟空间中使用的「资源」（角色、对象和其他材料）以及关卡设计。一些功能（如照明、动画和「原始」对象）已作为默认设置内置在引擎中，但 Unity 还提供与更复杂的 3D 图形应用程序（如 Maya 和 Blender）的集成。对于那些精通游戏开发或建模的人来说，这将他们锁定在兼容的软件中。对于新手来说，Unity 还提供了另一种锁定途径：其预装的资源商店提供内容、插件、资源包和其他实用工具，可简化制作过程。

### 实现

在实现过程中，玩家的控制方式以及与资产和对象的交互都被编入游戏中。软件开发工具包（SDK，一套可以导入 Unity 的代码和示例。）、应用程序接口和资源包通过整合游戏控制和其他形式的交互功能，将项目变为现实。在这一过程中，开发者通常需要根据游戏所需的硬件为玩家、其他对象和角色编码。例如，VR 中的导航和交互需要使用控制器和头显。为了帮助这两者的编程，资源商店中提供了内置代码的资源，例如由 VR 硬件制造商 HTC 生产的 Vive 输入工具。这些软件也把用户制作的项目锁定在特定平台里。要切换到另一款硬件，他们必须重新编辑内容，通常还要使用其他软件包。Unity 越来越多地尝试在其引擎中实现此类代码的标准化，这对硬件开发者来说就更加重要了。

### 分发

在这一阶段，游戏的环境、代码和资源将被编译到特定平台，包括手机、电脑、游戏主机等。在 Unity 中，发行是通过其「构建并运行」功能进行的。由于被排除在外的格式对于设计者来说管理难度大大增加，而且该引擎会定期删除未被充分利用的平台，如 Tizen 移动平台和三星电视格式（Akshay，2017 年），因此 Unity 已成为发布游戏、VR 和其他 3D 内容的理想舞台的仲裁者。

### Unity 和锁定

在工作流程的每个阶段，Unity 都会在功能层面锁定现有平台。它通过内操作性来实现这一点：它的资源商店和其他平台影响着制作流程的每个阶段。因此，Unity 重新定义并进一步巩固了现有平台，促进这些平台的使用，来使自己受益。

因此，游戏引擎加剧了学者们对平台的不信任。通过争夺市场主导地位并使用自己的资源包和工具包，Unity 正在通过平台依赖性「排挤……例外和替代品」（Nieborg & Poell, 2018，第 4289 页）。同样，Unity 向其他市场渗透的举动，以及为 3D 物体和代码推出资源商店的做法，最终也符合「平台的基本逻辑」（Helmond, 2015，第 8 页），其作用是使数据不仅具有扩展性和可访问性，而且具有商品性和限制性。

由于该引擎的生产性及其作为创建应用程序的工具的明确营销定位，它对平台的依赖似乎是不可避免的。它利用了平台固有的力量，平台为用户带来了「不可否认的好处」，用户可以通过平台轻松制作作品，但与此同时，平台也让大公司「站稳脚跟，成为 19 世纪和 20 世纪铁路、电话和电力公用事业的现代垄断者」（Plantin et al., 2016，第 295 页）。Unity 最终建立了一个制作流程，在这一流程中，使用平台似乎是构思、制作和发行游戏的最佳选择（如果不是唯一选择的话）。

正如 Lanier 所说，这给用户带来的后果是，越来越多的创意可能性被锁定，这影响到游戏开发的各个阶段，并以无数种方式表现出来。引擎本身将游戏惯例锁定在任何 3D 流程中——例如，在引擎中浏览场景就采用了计算机游戏中常见的 W、A、S、D 键配置。核心资源的名称如「FPSController」，就直接源自第一人称射击游戏（first-person shooter games）。

然而，Lanier 也认为，这种锁定与用户之间有着深刻而复杂的关系，不仅限制了用户的操作，还提供了用户进行创作的规则。 Whitson（2018） 同样指出，程序员称 Unity 为「巫毒软件」，它表现出「自己的思想……与用户的输入和目标背道而驰」（第 2324 页）。这导致了「计划外的」功能（第 2327 页），并影响了开发人员对项目的构思和互动。

那么，当用户采用 Unity 等工具并与之互动，甚至成为玩工时，这些工具会对用户产生怎样的影响？锁定的意识形态对创作过程有什么影响，尤其是对新的创新？通过对 VR 开发人员和爱好者的访谈，我们对这些问题有了更深入的了解。

## 方法

作为一个研究沉浸式技术的大型项目（Foxman, 2018）的一部分，我们对 VR 和增强现实（AR）硬件的内容创作者、爱好者和开发者进行了半结构式访谈。受访者来自美国的爱好者聚会；其中一些明确以游戏开发为中心，而另一些则侧重于新兴媒体的商业、教育和技术方面。因此，Unity 不同专业水平的用户都有代表参加。此外，我们还采访了一个私人 VR 实验室的成员，该实验室明确使用了游戏引擎。

访谈从 2016 年开始，历时一年半。受访者中共有 76% 是开发人员或内容创作者，34% 在开发型企业工作。77%的受访者为男性，这反映了聚会的总体参与情况。

我总共进行了 90 次访谈，时间从 15 分钟到 2.5 小时不等，访谈方式包括电话、面谈和电子邮件。所有受访者都可以选择匿名，因此我没有透露他们的身份。

虽然每次访谈都涉及类似的主题，但我采取了一种立足于实际的方法，不断从主要问题中重新整理后续问题。这直接影响了对 Unity 的调查。我最初的调查涉及工作流程、VR 开发体验、设备/开发工具包的使用以及对该媒介的总体看法，但引擎的出现频率如此之高，以至于我重新整理了我的询问方向。

这个结果并不是对使用 Unity 的完整描述，而是分析了开发者和爱好者在日常工作中对该引擎的看法、它与游戏行业的关系以及它在 VR 传播中的意义。

## Unity、虚拟现实和平台工具的局限性

许多通过聚会和实验室接触到 Unity 的人都看好 VR 的潜力；它实现了儿时长久以来的梦想，并且是进入游戏和技术行业的底层机会。他们使用了「革命性的」、「变革性的」和 「包罗万象的」等词语来表述，并大胆宣称 Unity 及其对世界的影响。「就释放潜能而言，每个人都在谈论这个话题——释放孩子的潜能。这些都是空谈，但 Unity 确实做到了。而且他们是免费提供给你的……」

受访者称赞 Unity 易于使用。只需 30 分钟就能制作出内容，并作为一个初步项目发布。一位受访者认为其直接的结果「令人欣慰」，并认为这将激励那些不熟悉编程的人进一步涉足 VR 开发。它还很高效，尤其是它的「拖放」功能，几乎不费吹灰之力就能将资源放置到虚拟环境中。此外，该平台的互操作性也很受欢迎。开发者在开始项目时会先尝试使用 Unity 资源包；其中一位开发者描述了她是如何下载演示程序，然后「因为我不会编程」而对其进行修改，直到新硬件可以正常工作为止。另一位开发者在提到 Unity 资源商店时说，许多预制资源和脚本可以方便地购买、下载和「拖放」，这可以让任何用户熟悉该引擎，然后「拼凑」成一个应用程序。兼容资源包的范围也受到了称赞。另一位受访者提到，每次 SDK 发布时，网上都会出现「很酷」甚至「很美」的讨论。

Unity 的互联性和互操作性的优势还延伸到了发行领域。在 App Store、Google Play 或 Steam 等流行的市场平台上进行发布的低廉费用被认为是发行方获得成功和增加效能的一种方法。由于 Unity 的构建和运行功能，同一个项目可以在所有这些平台上流通，从而实现大规模曝光：一位爱好者建议初学者不要参加无薪实习，而是花 25 美元购买一次性开发者许可证，然后在这些商店上发布「一堆东西」。

然而，一些人对 Unity 的乐观情绪有所收敛，因为特定形式的社会和技术封锁限制了与 VR 相关的类型、开发者的身份、专业兴趣，并最终限制了其未来的发展方向。

### 锁定类型

在我的采访中，许多受访者都有内容创作的背景，但不一定有游戏开发的背景。然而，正如一位受访者所说，「VR 和 AR 几乎就是游戏的同义词」。另一位受访者称游戏和娱乐媒体是 VR 的明显「入口」。这种假设延伸到了 Unity。一位受访者说：「我一直想制作游戏。」因为他想制作 3D 内容，所以他开始使用 Unity，「然后最终发现了虚拟现实」。引擎和媒介在游戏方向上是相通的。

对于那些喜欢游戏的人来说，这是一件令人高兴的事。一位受访者将整个过程描述为「建立一个沙盒，人们可以在其中玩耍并创造回忆……对我来说，这就是生活的全部」。他将 Unity 与 Adobe Photoshop 相比，他在青少年时期就曾摆弄过 Adobe Photoshop，他喜欢 「看所有的工具，然后你会看到什么是可能的」，他说「这在很大程度上是一种游玩」。当他开始制作游戏和 VR 项目时，他甚至喜欢向家人、朋友和爱好者炫耀每一项小小的成就。

但对于那些对游戏不感兴趣的人来说，正如一位受访者所说，Unity 只是强化了 VR 由游戏类型主导的整体印象： 「如果人们要在 Unity 中学习 VR，我真的认为他们应该选修一些......电子游戏设计课程，甚至是编码课程」。言下之意，游戏、游戏设计甚至游戏产业都被锁定在 VR 的传播范围内。引擎和媒介可以用于多种用途，如建筑、艺术和电影，但对于早期的爱好者来说，Unity 主要是用于游戏的。一位正在设计零售服务应用程序的受访者最能说明这一点。在寻找 Unity 开发人员时，他担心该引擎「定义了一套游戏规则」和机制，而这些规则和机制构成了关于 VR 和沉浸式媒体的「我们用于交流的语汇」。他很矛盾，不知道这些规则是否就是他想要的应用程序。

具有讽刺意味的是，那些了解 Unity 可以应用的各种选项的人往往具有游戏背景，并且他们在使用该工具时往往感到如鱼得水。

注：分析中缺少的一种类型是色情，这被认为是 VHS 锁定 Betamax 的一个原因（Johnson，1996 年）。受访者很少提及色情内容，这可能反映了他们的招募方式——通过半专业实验室和聚会。

### 锁定身份

那些「知情者」也往往在年龄、性别和社会经济方面抱有成见： 一位 VR 社区的受访者通过电子邮件写道：「我也会笼统地把白人年轻男性称为「哥们」，他们是程序员或数字艺术家，同时也是狂热的游戏玩家，」他补充道，「我还猜测他们的收入高于平均水平。我只见过一位 Unity 的专家级女性开发者，她的全职工作就是编写 VR 应用程序。」另一位受访者总结道：「更多的男性，更多的技术人员……」

相比之下，一位年长的女性实验室参与者则害怕参加每周例会，因为她缺乏编程背景。另一位参与者说，她必须同时学习 Unity 及其互操作代码（C# 编程语言），这让她感到「无能为力」和「震惊」。引擎和 VR 被视为男孩俱乐部的一部分，与更多边缘化群体的利益背道而驰。

受访者还感觉到发烧友群体中缺少有色人种。两名女性受访者指出，男性所占比例较高，随后又说非裔美国人的比例特别低。一名韩国学生说她没有人可以「联系」。一位非裔美国人开发者说，她必须学会「适应」聚会，才能「感到舒适」。因此，正如引擎锁定了一种特定的类型（游戏）以及特定类型的爱好者（游戏玩家或游戏开发者）一样，它也锁定了周围游戏玩家文化的规范，这种文化被批评为只关注、营销和支持富裕的白人男性，而排斥其他社会群体（Shaw, 2011）。正是这部分人拥有成功使用和部署 VR 内容的文化知识、收入和能力。

### 锁定专业人员

由于在游戏制作中，Unity 被锁定在一套更广泛的平台上，因此精通这些工具集的专业人员在新兴媒体中最为成功。要胜任 VR 制作，不仅需要熟悉 Unity，还需要学习 3D 图形程序，如制作 VR 的 Maya。一位受访者描述说，对于没有 3D 建模背景的人来说，学习曲线是「陡峭的」。另一位新手说，很难「提高」Unity 的性能，并讲述了自己花了很多时间在网上研究和测试引擎。

因此，Unity 往往将开发人员拒之门外，并将几乎所有其他行业拒之门外。电影和视频剪辑师没有耐心学习新软件，因为他们已经掌握了成熟的设计应用软件（如 Adobe Creative Suite 中的应用软件）。一位有电影背景的业余爱好者批评引擎难以使用。她无法轻松完成 「简单」的事情，比如创建视频或音频循环。最终，她认为该引擎「错综复杂、杂乱无章」，是「一种计算机编程中的‘蝇王’」。在我的访谈中，几乎可以感觉到人们希望有一种更适合非游戏制作者需求和实践的工具。

这些话透露出开发人员已经意识到，即使他们将 Unity 的创造力发挥到 VR 的极致，他们的工作也会受到限制。该引擎主要为游戏创作提供了一个平台，但只有在付出巨大努力后才能将其用于其他目的。

这也延伸到了发行方面，引擎的成功又一次取决于专业人士已经了解或拥有的平台和工具。游戏玩家和开发者拥有使用 Unity 轻松构建 VR 项目所需的硬件，他们已经做好了制作和实验内容的准备。相比之下，普通用户则需要花费数千美元和大量时间才能获得制作和发布 VR 所需的技术。

### 锁定 VR 的未来

前面的观察预示了 Unity 在塑造 VR 未来中的作用。那些没有专业背景或不认同「游戏玩家」身份的人在使用引擎和相关平台时感到困惑，或者至少阻碍了他们的创造力。受访者强调了最终会阻碍 VR 发展的隐性和显性限制。一位爱好者说：「我看到关于未来 AR 和 VR 的某些事情，我就想，我们应该谨慎考虑我们正在建造的东西……」他接着将 VR 的发展与游戏行业在宣传暴力方面的失误进行了比较，然后总结道：「在全速前进之前，我们应该稍微考虑一下我们正在建造什么以及为什么要建造。」因此，尽管 Unity 具有革命性的潜力，但人们始终担心，在 Unity 本身的支持下，游戏和游戏长期以来的传统最终会如何塑造 VR。

Unity 在 VR 制作中的流行表明，路径依赖伴随着普遍的锁定。谁可以使用该软件（游戏开发者）、如何使用（主要用于游戏开发）、可以发布什么（与游戏相关的内容）以及在哪里发布（已经与 Unity 和游戏相连接的应用程序商店），尽管商业 VR 还处于起步阶段，但这些都是既定的事实。

## 游戏规则：讨论

这些访谈描绘了一幅关于 Unity 的矛盾图景：它既是一个对用户友好的程序，对实现一种新兴媒体的潜力至关重要，同时也适合于一批习惯于游戏的特定用户。

锁定存在于制作的各个阶段，它设定了技术和意识形态参数。该引擎在知识和内涵层面上影响着开发者的每一个决策，并要求开发者意识到甚至默许他们的工作条件。开发人员需要 Unity 来成功驾驭 VR 制作。此外，由于许多早期用户既是内容的制作者，也是消费者（或玩家），这就造成了一种自我选择——对于那些渴望使用 Unity 制作内容的人来说，VR 成为了一种乐趣。

在这种情况下，我认为遵守 Unity 支持的标准是通过「玩工」这一应对机制来维持的。正如 Kücklich 所描述的，玩工的基本原则反映在开发者的活动中，从而为公司带来利益：他们自制的资源和脚本最终会进入 Unity 资源商店，成为事实上的市场营销；用户的努力增加了引擎的功能，从而延长了引擎的「保质期」，他们会在新硬件（如 VR 头显）发布时测试新功能。他们甚至渴望受雇于 Unity 或与该引擎兼容的相关行业。

更广义地说，玩工在平台化的劳动实践中发挥着「游玩」的作用。Unity 的使用者是在「规则内游玩」，这就需要「锁定」引擎的规范和技术要求。采访中也提到了这一点： 「感觉我们已经被锁定成靶子和企业工具」。对于某些人（尤其是那些精通围绕 Unity 的文化生产‘规则’的人）来说，掌握玩工既有成就感又有乐趣，正反馈循环（游戏和游戏的另一个关键特征）又强化了这一点。这种乐趣解释了某些 VR 追随者的热情；对他们来说，同步性和低门槛是继续在引擎中工作的强大动力。但是，对于那些既没有玩的欲望也没有玩的条件的人来说，这种环境就不那么令人愉快了。

这些规则不仅适用于 Unity，也适用于其业务和市场合作伙伴。平台的互操作性扩大了 Unity 可以发挥作用的「竞技场」，但也要求开发人员进一步投入时间和精力，了解兼容公司和应用程序的指导方针。同时，这些公司还必须在引擎的范围内进行对接和工作。因此，作为一种平台工具，Unity 通过锁定生产环境中的特定工作方式来设定条件。此外，Unity 还能在内容创作的各个层面上实现这一点：从开始到发布。这些规则最终支持了游戏制作者和游戏制作者在其经济、技术和社会限制条件下工作。

从企业对企业的角度来看，平台工具是不可或缺的。互操作性使几乎所有行业都能尝试使用虚拟现实技术——在建筑、游戏或医疗领域（举例来说）使用虚拟现实技术时，无需再回到绘图板上。然而，这也造成了一种反直觉的情况：引擎为生产开辟了新天地，同时也决定了生产的条件。

最后一个考虑因素是，当像 Unity 这样的平台工具被标准化、锁定和游玩时，会对产业产生什么影响。受访者的观点显示，Unity 是重构的重要媒介。VR 硬件制造商发布的头显带有与 Unity 兼容的应用程序接口、资源包和代码。然后，开发人员利用它们创建内容，这些内容在现有平台生态系统中扩散，因为这是 Unity 创新和发布流程的必要组成部分。因此，已经在 VR 和沉浸式媒体领域投资的平台「巨头」进一步巩固了其技术领导者的地位。Unity 还通过锁定行业、相关市场和自身在其中的地位，巩固了其作为重要使者的地位。实际上，这意味着在可预见的未来，VR 将与游戏联系在一起，而这正是 Unity 的立足之本。

此外，Whitson（2018）断言，这些工具是许多爱好者接触交互内容的第一个界面。随着对这些「代理人……导师、制作者和社区组织者」的熟悉程度加深，「开发者与工具开发者」（第 2329 页）之间的差距也在扩大，从而赋予后者更多的权力。随着未来的创新进入市场，像 Unity 这样的软件在各种新兴领域的传播使这种权力失衡得以延续。总之，锁定、游戏/玩工以及兼容行业的重新整合正在成为数字创作的传统。

## 达到极限：结论

本文以 Unity 作为平台工具的典型例子，展示了平台如何提供技术、社会和经济条件，锁定特定行业、设计实践和不平等现象。通过对 VR 和其他沉浸式媒体爱好者的访谈，我们对这种锁定产生了发自内心的担忧，即新兴媒体潜在的无限可能性及其创作主体将受到引擎的限制。这并不意味着创造力受到了阻碍，而是受到了嵌入工具中的规范和规则的影响。

对于用户来说，当他们在尝试学习引擎和设计游戏以外的内容时，这种感受是隐性的。然而，这些只是用户的印象。未来的研究应该探究受访者表达的观点如何影响他们的日常实践，以进一步阐明锁定对创作过程的影响。

然而，这些发现凸显了平台和平台化研究中的三大问题。首先，对平台工具的研究仍然严重不足。Unity 并不是唯一一款高度平台化的、在某种程度上「去专业化」的并且已被开发人员日常使用的先进生产力软件。这些应用程序会让新用户更有信心，他们会默认应用程序的完整性,而不会批判性地评估其中的意识形态基础。因此，必须继续对其进行学术分析和严格批判。

第二个问题是「平台巨头」与消费者锁定之间的密切关系。平台工具可以维系和巩固当权者，而 Unity 只是其中的一个例子。开发者需要使用行业提供的资源包、工具包和资源——更不用说要投入额外的精力、时间和金钱来制作成功的 VR 内容。因此，他们必须屈从于现有行业的束缚，而 Unity 等公司就深深扎根于这个行业之中。亚马逊的「Sumerian」游戏引擎和谷歌的「Stadia」流媒体服务只是其中的两个例子。这些收购扩大了这些巨头的业务范围，使其不再局限于简单地获取用户数据，而是想方设法利用爱好者的劳动成果。

第三，平台工具体现了内操作性对传统文化生产的破坏程度，以及平台化逻辑对当代经济的影响。访谈揭示了单一平台工具如何通过规定开发者的资质、生产方式和议程来影响用户的生活。本文以新兴媒体为重点，提出了平台如何塑造从机器人到人工智能等新技术的问题，但更重要的是，平台将如何塑造那些在这些创新中发挥重要作用的人和思想。

总之，文化生产者遇到了一套越来越受规则约束的工具，他们必须用它来构建内容。这些规则自上而下，而不是自下而上，从而造成了对创造力的路径依赖。尽管如此，这种路径依赖并不必然导致纯粹的负面结果。锁定确实会掩盖各种形式的创造力和发展，但限制也可能是有利的。在规则范围内进行游戏，既能获得乐趣，又能有机会提高制作水平，最终还能要求玩家遵守规则，从而掌握游戏技巧。毕竟，只有当所有人都知道游戏规则时，游戏才能玩得好。对规则的了解也会促使对规则进行颠覆和修改，而这正是游戏中普通（甚至必要）的元素。如果规则是强加的，而不是共同商定的，那么更严重的问题就会持续存在。只有了解文化生产者的游戏规则和标准，各方才能找到获胜的方法。

---
## References

- Akshay. (2017, November 6). Unity drops support for Tizen mobile and Samsung TVs in the latest Beta release. IoT Gadgets. Retrieved from https://www.iotgadgets.com/2017/11/unity-drops-supporttizen-mobile-samsung-tvs-latest-beta-release/

- Axon, S. (2016, September 27). Unity at 10: For better—or worse—game development has never been easier. Retrieved from https://arstechnica.com/gaming/2016/09/unity-at-10-for-better-or-worse-game-development-has-never-been-easier/

- Bechmann, A. (2013). Internet profiling: The economy of data intraoperability on Facebook and Google. MedieKultur: Journal of Media and Communication Research, 29, 72–91.

- Beschizza, R. (2018, July 17). The most popular engines for indie games. Retrieved from https://boingboing.net/2018/07/17/the-most-popular-engines-for-i.html

- Bodle, R. (2011). Regimes of sharing: Open APIs, interoperability, and Facebook. Information, Communication and Society, 14, 320–337.

- Bogost, I. (2008). Unit operations: An approach to videogame criticism. Cambridge, MA: MIT Press.

- Cantner, U., & Vannuccini, S. (2017). Innovation and lock-in. In H. Bathelt, P. Cohendet, S. Henn, & L. Simon (Eds.), The Elgar companion to innovation and knowledge creation (pp. 165–181). Cheltenham, UK: Edward Elgar.

- Downie, C. (2016, June 16). Evolution of our products and pricing. Unity Blog. Retrieved from https://blogs.unity3d.com/2016/06/16/evolution-of-our-products-and-pricing/

- Foxman, M. H. (2018). Playing with virtual reality: Early adopters of commercial immersive technology. New York, NY: Columbia University. Retrieved from http://academiccommons.columbia.edu/download/fedora_content/download/ac:6q573n5tc8/content/Foxman_columbia_0054D_14522.pdf

- Gillespie, T. (2010). The politics of “platforms.” New Media & Society, 12, 347–364.

- Haas, J. (2014). A history of the unity game engine. Worcester, UK: Worcester Polytechnic Institute. Retrieved from http://web.wpi.edu/Pubs/E-project/Available/E-project-030614-143124/unrestricted/Haas_IQP_Final.pdf

- Helmond, A. (2015). The platformization of the web: Making web data platform ready. Social Media + Society, 1(2). doi:10.1177/2056305115603080

- Johnson, P. (1996). Pornography drives technology: Why not to censor the Internet. Federal Communications Law Journal, 49, 217–226.

- Kücklich, J. (2005). Precarious playbour: Modders and the digital games industry. Fibreculture, 5(1). Retrieved from http://five.fibreculturejournal.org/fcj-025-precarious-playbour-modders-and-the-digital-games-industry/

- Labschütz, M., Krösl, K., Aquino, M., Grashäftl, F., & Kohl, S. (2011). Content creation for a 3D game with Maya and Unity 3D. Institute of Computer Graphics and Algorithms, Vienna University of Technology. Retrieved from https://www.researchgate.net/profile/Reinhold_Preiner/publication/267417785_Content_Creation_for_a_3D_Game_with_Maya_and_Unity_3D/links/554788c70cf26a7bf4d93df6.pdf

- Lanier, J. (2011). You Are Not a Gadget: A Manifesto. New York, NY: Vintage. Leap Motion. (n.d.). Available from https://www.leapmotion.com/

- Lesage, F. (2015). Middlebroware. Fibreculture Journal, 25, 89–114.

- Liebowitz, S. J., & Margolis, S. E. (1995). Path dependence, lock-in, and history. Journal of Law, Economics, & Organization, 11, 205–226.

- Margolis, S., & Liebowitz, S. J. (1998). Path dependence: New Palgrave dictionary of economics and law. London, England: Palgrave MacMillan.

- Martens, B. (2016). An economic policy perspective on online platforms. Retrieved from https://doi.org/10.2139/ssrn.2783656

- Montfort, N., & Bogost, I. (2009). Racing the beam: The Atari video computer system. Cambridge, MA: MIT Press.

- Nieborg, D. B., & Poell, T. (2018). The platformization of cultural production: Theorizing the contingent cultural commodity. New Media & Society, 20, 4275–4292.

- Panourgias, N. S., Nandhakumar, J., & Scarbrough, H. (2014). Entanglements of creative agency and digital technology: A sociomaterial study of computer game development. Technological Forecasting and Social Change, 83, 111–126.

- Plantin, J.-C., Lagoze, C., Edwards, P. N., & Sandvig, C. (2016). Infrastructure studies meet platform studies in the age of Google and Facebook. New Media & Society, 20, 293–310.

- Schmalz, M. (2015). Limitation to innovation in the North American console video game industry 2001-2013: A critical analysis. London, Ontario, Canada: Western University. Retrieved from https://ir.lib.uwo.ca/etd/3393/

- Schwarz, J. (2017). Platform logic: An interdisciplinary approach to the platform-based economy. Policy & Internet, 9, 374–394.

- Shapiro, C., & Varian, H. R. (1998). Information rules: A strategic guide to the network economy. Cambridge, MA: Harvard Business Press.

- Shaw, A. (2011). Do you identify as a gamer? Gender, race, sexuality, and gamer identity. New Media & Society, 14, 28–44.

- Takahashi, D. (2015, August 16). In the game engine wars, Epic and Unity aim at enabling VR. Retrieved from https://venturebeat.com/2015/08/16/in-the-game-engine-wars-epic-and-unity-aim-at-enabling-vr/

- Unity public relations fact page. (n.d.). Retrieved from https://unity3d.com/public-relations

- VIVE input utility—Asset store. (n.d.). Retrieved from https://assetstore.unity.com/packages/tools/integration/vive-input-utility-64219

- Ward, J. (2008, April 29). What is a game engine? GameCareerGuide.com. Retrieved from https://www.gamecareerguide.com/features/529/what_is_a_game_.php

- Whitson, J. R. (2018). Voodoo software and boundary objects in game development: How developers collaborate and conflict with game engines and art tools. New Media & Society, 20, 2315–2332.

