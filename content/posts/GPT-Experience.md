---
title: "GPT 使用体验"
date: 2023-03-20T19:20:22+08:00
categories: ["未分类"]
toc:
    enable: false
---

最近 OpenAI 的对话类大语言模型产品 ChatGPT 异常火爆，以其出色的对话、信息归纳等能力，引发人们对通用人工智能、搜索引擎、人机交互的重新思考，有人甚至称它开启新一轮的工业革命。

以下是笔者的几个简单测试问题，可以从中感受一二。首先是一个物理+哲学问题：

> Q: what is the purpose of the universe?
> 
> A: The purpose of the universe is a philosophical and existential question that has been debated by scholars and thinkers for centuries. There is no one definitive answer to this question, as it ultimately depends on one's beliefs, values, and worldview.
> 
> Some people believe that the purpose of the universe is to serve a divine plan or to fulfill a specific destiny. Others believe that the universe has no inherent purpose or meaning, and that it is up to individuals to create their own purpose and meaning in life.
> 
> From a scientific perspective, the purpose of the universe can be seen as the result of natural processes and physical laws that have led to the formation of galaxies, stars, planets, and life. The universe exists as a complex and interconnected system, and its purpose can be seen as the ongoing exploration and discovery of its own nature and potential.
> 
> Ultimately, the purpose of the universe is a deeply personal and subjective question that each individual must answer for themselves.

对于同样的问题，Google 给出的答案如下：

> The universe is simply the collection of galaxies, stars, planets, comets, meteorites, and other solar system detritus, plus whatever dark matter and dark energy turn out to be. The universe is governed by laws of nature that themselves have no purpose other than dictating what matter and energy do.

GPT 是否清楚自己是如何被创造出来的呢？

> Q: how to train a GPT model?
> 
> A: Training a GPT model involves several steps, including data preparation, model architecture selection, hyperparameter tuning, and training.
> 
> Here's a general overview of the steps involved in training a GPT model:
> 
> Data preparation: Gather a large corpus of text data that is representative of the domain you want the GPT model to generate text for. This can include books, articles, web pages, and other sources of text data.
> 
> Preprocessing: Clean and preprocess the text data to remove noise, punctuation, and other irrelevant information. You may also want to tokenize the text data into individual words or subwords, depending on the model architecture you choose.
> 
> Model architecture selection: Choose a GPT model architecture that is appropriate for your task and data. This can include GPT-2, GPT-3, or other variants of the GPT model.
> 
> Hyperparameter tuning: Tune the hyperparameters of the GPT model, such as the learning rate, batch size, and number of training epochs, to optimize performance on your task and data.
> 
> Training: Train the GPT model on the preprocessed text data using a large-scale language modeling objective, such as maximum likelihood estimation or perplexity minimization.
> 
> Fine-tuning: Fine-tune the trained GPT model on your specific task, such as text generation, summarization, or question answering, by fine-tuning the model on a smaller dataset of task-specific examples.
> 
> Evaluation: Evaluate the performance of the trained and fine-tuned GPT model on a held-out test set, using metrics such as perplexity, accuracy, or F1 score.
> 
> Keep in mind that training a GPT model can be a computationally intensive and time-consuming process, requiring specialized hardware and software. It's also important to ensure that the data you use to train the model is representative of the domain you want the model to generate text for, and that the model is evaluated on a diverse and representative set of test examples.

上面的长篇大论好像回答了，又好像没回答。训练大语言模型不是简单就可以描述清楚的，因此问一下相关的代码实现吧！

> Q: show me the python code that trains a GPT model
> 
> A: Training a GPT model from scratch can be quite complex and resource-intensive. However, you can use the Hugging Face Transformers library to fine-tune a pre-trained GPT model on your specific task. Here's an example using the GPT-2 model:
> 
> First, install the Hugging Face Transformers library:
> ```shell
> pip install transformers
> ```
> 
> Next, create a Python script to fine-tune the GPT-2 model:
> ```python
> import torch
> from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config, TextDataset, DataCollatorForLanguageModeling
> from transformers import Trainer, TrainingArguments
> 
> # Load pre-trained GPT-2 model and tokenizer
> model_name = "gpt2"
> tokenizer = GPT2Tokenizer.from_pretrained(model_name)
> config = GPT2Config.from_pretrained(model_name)
> model = GPT2LMHeadModel.from_pretrained(model_name, config=config)
> 
> # Prepare training data
> train_file = "path/to/your/train.txt"
> train_dataset = TextDataset(
>     tokenizer=tokenizer,
>     file_path=train_file,
>     block_size=128
> )
> 
> # Prepare data collator
> data_collator = DataCollatorForLanguageModeling(
>     tokenizer=tokenizer,
>     mlm=False
> )
> 
> # Set up training arguments
> training_args = TrainingArguments(
>     output_dir="./output",
>     overwrite_output_dir=True,
>     num_train_epochs=1,
>     per_device_train_batch_size=4,
>     save_steps=10_000,
>     save_total_limit=2,
> )
> 
> # Create Trainer instance
> trainer = Trainer(
>     model=model,
>     args=training_args,
>     data_collator=data_collator,
>     train_dataset=train_dataset,
> )
> 
> # Train the model
> trainer.train()
> ```
> Replace `path/to/your/train.txt` with the path to your preprocessed training data file. Adjust the training arguments, such as the number of epochs and batch size, according to your needs and available resources.
> 
> This example demonstrates how to fine-tune a pre-trained GPT-2 model using the Hugging Face Transformers library. For more advanced use cases and customization, refer to the [Transformers documentation](https://huggingface.co/transformers/).

同样，好像回答了又好像没回答。要获得更深入的解答需要更详细的问题，不过从现有的答案可以看出 GPT 系列模型是基于 transformer 结构（这是显然的，GPT 全称就是 Generative Pre-trained Transformers）。代码演示了训练（其实是 fine tune）的大致流程：读取预训练模型，从训练文本提取token，设置训练参数，开始训练。

然后是一道几何问题，回答的正文里有一行公式没有显示出来，可能是前端的 bug。根据后面的代码，推断缺失的公式应该是 $\Omega=2\pi(1-\cos\theta)(1-\cos\phi)$.

> Q: how to compute the solid angle of a rectangle in 3D space
> 
> A: To compute the solid angle of a rectangle in 3D space, we can use the formula:
> 
> where Ω is the solid angle, θ is the angle between the normal vector of the rectangle and the observer's line of sight, and φ is the angle between the edges of the rectangle that intersect at the observer's position.
> 
> Here's an example Python function that computes the solid angle of a rectangle in 3D space:
> ```python
> import numpy as np
> 
> def solid_angle(rectangle, observer):
>     # Compute the normal vector of the rectangle
>     v1 = rectangle[1] - rectangle[0]
>     v2 = rectangle[2] - rectangle[0]
>     normal = np.cross(v1, v2)
>     normal /= np.linalg.norm(normal)
> 
>     # Compute the angle between the normal vector and the observer's line of sight
>     observer_dir = observer - rectangle[0]
>     observer_dir /= np.linalg.norm(observer_dir)
>     cos_theta = np.dot(normal, observer_dir)
> 
>     # Compute the angle between the edges of the rectangle that intersect at the observer's position
>     edge1 = rectangle[1] - observer
>     edge2 = rectangle[3] - observer
>     cos_phi = np.dot(edge1, edge2) / (np.linalg.norm(edge1) * np.linalg.norm(edge2))
> 
>     # Compute the solid angle
>     omega = 2 * np.pi * (1 - cos_theta) * (1 - cos_phi)
> 
>     return omega
> ```
> In this example, `rectangle` is a 3x3 array of the rectangle's vertices in 3D space, and observer is a 1D array of the observer's position in 3D space. The function returns the solid angle of the rectangle in steradians.
> 
> Note that this formula assumes that the rectangle is a planar surface and that the observer is outside the rectangle. If the `observer` is inside the rectangle, the formula needs to be modified accordingly.

这个回答的正确性未知，至少不能一眼发现明显的破绽。

可以看出，GPT 已经具备了相当不错的文字组织的能力，并且看上去拥有一定的逻辑推理能力，不能断定是真的学到了推理的本质，还是只是匹配到了训练数据中类似的逻辑关系，不管怎样，都已经能满足目前人们的很多方面的需求了。
期待看到大语言模型未来还有怎样的潜力。
