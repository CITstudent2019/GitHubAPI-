# author: kyle bogart
# desc: utilizes github api to receive python repository data
# 02/05/2019

import requests 
import time

while(True):
	lang = raw_input("Language to Query: ")

	url = 'https://api.github.com/search/repositories?q=language:' + lang + '&sort=stars'
	r = requests.get(url)

	print("Status code: " + str(r.status_code))

	response_dict = r.json()
	# keys are total_count, items, incomplete_results
	print("Number of Repos: " + str(response_dict['total_count']))
	print("------------------------------------------------------------------")

	repo_dicts = response_dict['items']
	print("Top Repositories: ")

	count = 1
	for repo_dict in repo_dicts:
		print(str(count) + ". " + repo_dict['name'])
		count += 1
		time.sleep(.100)

	print("------------------------------------------------------------------")


