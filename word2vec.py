from gensim.models import KeyedVectors


model_path = r"D:\AI_Learning\test\model\wiki-news-300d-1M.vec"

model = KeyedVectors.load_word2vec_format(model_path, binary=False, limit=100000)
print(f"加载成功，当前词条数: {len(model.key_to_index)}")

vector_king = model['king']
print(f"'king' 向量的前10个数值: {vector_king[:10]}")

similarity = model.similarity('cat', 'cute')
print(f"猫和可爱的相似度: {similarity}")

result = model.most_similar(positive=['king', 'women'], negative=['man'], topn=1)
print(f"国王-男人+女人的结果: {result[0][0]}(相似度: {result[0][1]:.4f})")