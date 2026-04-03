## 概念总结

机器学习：从数据中学习一个映射函数或者决策规则。

监督学习：训练数据包含标签；无监督学习：训练数据不含标签；强化学习：与环境交互，根据返回信号激励学习策略

深度学习：利用多层神经网络进行学习，深度学习也是属于机器学习，对图像，语音，自然语言等复杂数据更容易能够提取特征。

#### 大模型与生成式 AI (Large Models & Generative AI)

大语言模型 (LLM): 像 ChatGPT 一样的“超级大脑”，通过海量文本训练，具备强大的语言理解、创作和逻辑推理能力。

多模态大模型 (Multimodal LLMs): 不再局限于文字，能够同时处理和理解图像、视频、音频等多种信息形式。

生成式人工智能 (AIGC): 侧重于“创造”，例如 AI 生成图片（Midjourney）、生成视频或 3D 模型，让 AI 从“识别者”变为“生产者”。

知识图谱 (Knowledge Graph): 像是一张巨大的知识网，将碎片化的信息连接起来，帮助 AI 理解现实世界的逻辑关系。

#### 具身智能与机器人 (Embodied AI & Robotics)

具身智能 (Embodied AI): 强调 AI 必须有实体（如机器人或自动驾驶车），通过在真实环境中感知、移动和操作来学习，而不是只待在电脑屏幕里。
智能体 (Agent): 能够自主感知环境、进行决策并采取行动以实现特定目标的系统。
多智能体协同 (Multi-agent Coordination): 研究一群 AI 之间如何像蜂群或球队一样配合工作。

#### 计算机视觉与感知 (CV & Perception)
三维视觉/3D 重建: 不仅是看平面照片，而是理解物体的空间深度，甚至是根据 2D 图形还原出 3D 立体模型。

行为分析/视频理解: AI 不仅能认出图里有个人，还能理解这个人是在“挥手”还是在“跑步”。

## 论文相关的阅读

### https://arxiv.org/abs/1706.03762 Attention is all you need 

论文的最重要的是提出了注意力机制，提出了Transformer模型。

实验的进行。

使用两个经典数据集：
WMT 2014 English → German
WMT 2014 English → French
进行训练，进行机器翻译的任务

通过对比，将Transformer模型与RNN-based,CNN-based所成的模型进行比较。任务是机器翻译评价是翻译的质量

### https://arxiv.org/abs/1810.04805 BERT: Pre-training of Deep Bidirectional Transformers

BERT利用Transformer通过预训练训练语言模型，在加上微调实现具体任务

实验的进行：通过MLM(随机遮住一些词，让模型预测它们),NSP(判断两个句子是否连续)进行预训练

BERT 在多个任务上测试：

文本分类（GLUE）
问答（SQuAD）
自然语言推理（MNLI）
命名实体识别（NER）

在 11 个 NLP 任务中刷新 SOTA
显著优于之前方法（包括 ELMo、GPT）
### https://arxiv.org/abs/2103.00020 Learning Transferable Visual Models From Natural Language Supervision

**idea:** 在 CLIP 出现之前，计算机视觉界最主流的范式是有监督学习：用人工标注好标签的数据集（比如 ImageNet 有 1000 个类别，上百万张图片）来训练模型（如 ResNet）。
CLIP放弃人工标定的数字标签，通过互联网的海量图文来训练

实验：
1.爬取大量数据
2.为了探索性能上限，他们训练了不同大小的模型。Image Encoder 测试了 5 个不同大小的 ResNet 和 3 个不同大小的 Vision Transformer (ViT)；Text Encoder 统一使用了 Transformer 架构。
3. 零样本迁移测试 (Zero-Shot Transfer) 不需要在下游任务上做任何微调，就可以直接去做各种图像分类任务。

### https://arxiv.org/abs/2210.03629 论文：ReAct: Synergizing Reasoning and Acting

**idea:** ReAct 的结构非常简单：Thought -> Action -> Observation (自环境反馈) -> Repeat。

核心流程：Thought-Action-Observation 循环

Thought: 描述模型当前的判断和接下来的计划（例如：“我需要先找到 A 的父亲，才能查他父亲的生日”）。

Action: 输出一个具体的指令（例如：Search[A's father]）。

Observation: 这是一个外部输入。程序会执行上述 Action（比如调用维基百科 API），然后将搜索结果喂回给模型。


**实验** ：

作者选择了两个极具挑战性的领域来验证：

知识密集型推理 (HotpotQA, StrategyQA)：这类任务需要多跳搜索（Multi-hop search），即回答一个问题需要先查 A，再根据 A 的结果查 B。

决策任务 (ALFWorld)：模型需要在一个虚拟的文字环境中操作（如：进入厨房，打开冰箱，拿走苹果），并处理环境反馈。

作者对比了以下几种方案：

Act-only: 只有搜索，没有思考。

CoT (Reasoning-only): 只有思考，没有搜索。

ReAct: 思考 + 搜索。

### https://arxiv.org/abs/2305.19118 Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate

**背景** 大模型的Self-Reflection会产生思维退化（DoT）。

**idea** 利用多个智能体进行辩论反思相互竞争消除思维退化（DoT）。设计了MAD框架

核心流程：双人辩论 + 裁判总结
智能体 A & B：分别针对问题给出答案。在后续轮次中，它们会看到对方上一轮的输出，并被要求寻找对方的漏洞并捍卫（或修正）自己的观点。

裁判 (Judge)：负责监控整个辩论过程。如果双方达成共识且答案看起来正确，或者达到了预设的轮次上限，裁判就会出面总结并给出最终答案。

Tit-for-Tat（针锋相对）：这是该论文最特别的设定。系统会提示智能体：“不要轻易妥协，要努力发现对方推导中的错误”。

**实验**：
常识性谬误纠正：给出一个带有陷阱的逻辑题，看模型是否会被诱导。

翻译任务：针对一些有歧义或难以翻译的俚语，看多轮辩论是否能得到更地道的译文。

数学逻辑推理：在需要多步推算的数学题上，观察智能体如何互相纠错。

通过对比MAD与以往的模型以及对易混淆的问题的回答来展现MAD的作用。

