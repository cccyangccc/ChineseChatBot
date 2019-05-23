"""
    对语句进行特征工程处理

    --> 清洗：去空格、去标点、去除停用词

    --> 分词：按照不同模式进行分词、特殊字典

    --> 过滤：剔除敏感词汇、剔除不雅词汇

    --> 数值化：构建词向量、生成句子向量

    --> 特征提取：提取关键词、判断主题类型、构建其他特征

    --> 句子长度约束：补全短句，删减长句（或直接拒绝）

"""