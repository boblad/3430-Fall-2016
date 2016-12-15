import nltk.stem
import scipy as sp
import sys
import os
import sklearn.datasets
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


num_clusters = 50
english_stemmer = nltk.stem.SnowballStemmer('english')
train_groups = ['rec.autos', 'rec.motorcycles']
train_data = sklearn.datasets.fetch_20newsgroups(subset='train', categories=train_groups)

class StemmedTfidfVectorizer(TfidfVectorizer):
    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

tfidf_vectorizer = StemmedTfidfVectorizer(min_df=1, stop_words='english', decode_error='ignore') ## vectorizor object

train_data_feat_mat = tfidf_vectorizer.fit_transform(train_data.data)
num_samples, num_features = train_data_feat_mat.shape
print('#samples: %d, #features: %d' % (num_samples, num_features))
km = KMeans(n_clusters=num_clusters, n_init=1, verbose=1, random_state=3)
clustered_data = km.fit(train_data_feat_mat)


def find_top_n_closest_posts(new_post, vectorizer, kmeans, n):
	new_post_vec = vectorizer.transform([new_post])
	top_new_post_label = kmeans.predict(new_post_vec)[0]
	similar_post_indices = (kmeans.labels_ == top_new_post_label).nonzero()[0]
	similar_posts = []
	for i in similar_post_indices:
	    dist = sp.linalg.norm((new_post_vec - train_data_feat_mat[i]).toarray())
	    similar_posts.append((dist, train_data.data[i]))
	similar_posts = sorted(similar_posts)

	for i in range(0, n):
		print('Post :', i , 'Distance is', similar_posts[i][0])
		print(similar_posts[i][1])

find_top_n_closest_posts('is fuel injector cleaning necessary?', tfidf_vectorizer, km, 2);
