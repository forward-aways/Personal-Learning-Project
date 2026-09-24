from sklearn.feature_extraction.text import TfidfVectorizer
import jieba


def chinese_tokenizer(text: str) -> list:
    return list(jieba.cut(text))

docs = [
    "我喜欢猫",
    "我喜欢狗",
    "猫和狗是朋友"
]


vectorizer = TfidfVectorizer(tokenizer=chinese_tokenizer)
tfidf_matrix = vectorizer.fit_transform(docs)

feature_names = vectorizer.get_feature_names_out()

print("特征词列表: ", feature_names)

print("\n文档1 '我喜欢猫' 的tf-idf向量: ")

print(tfidf_matrix[0].toarray())