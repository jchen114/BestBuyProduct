import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as features
import math


def Analyze_Sentiment(text):
	nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(version='2017-02-27',
																username='e2c9eecb-2e13-4777-88b1-7520bb2e9edb',
																password='jksggBXNcyps')

	sentiment = features.Sentiment()
	sentiment._dataTuples[0] = (True, 'document')
	stuff = nlu.analyze(
		text='this is my experimental text.  Bruce Banner is the Hulk and Bruce Wayne is BATMAN! Superman fears not Banner, but Wayne.',
		features=[sentiment]
	)

	docu_score = stuff['sentiment']['document']['score'] + 1

	star = int(round(docu_score/0.5 + 1))

	return star




if __name__ == '__main__':
	Analyze_Sentiment('This TV exceeded my expectations. It made an amazing early Christmas gift for my not so tech savvy mother!')