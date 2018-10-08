from lxml import html
import requests
page = requests.get('https://www.imdb.com/title/tt7638344/fullcredits?ref_=tt_cl_sm#cast')
tree = html.fromstring(page.content)

#movie_name =  tree.xpath('//div[@class="titleBar"]/div[@class="title_wrapper"]/h1/text()[normalize-space()]')
movie_name =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@class="subpage_title_block"]/div[@class="parent"]/h3/a/text()[normalize-space()]')

if movie_name:
	movie_name = movie_name[0].strip()
else:
	# movie name cound not be found
	movie_name = ''
print (movie_name.center(100, "*").upper())
print('-'*100)
print()

directed_by =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/h4[1]/text()[normalize-space()]')

directed_by_detail =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/table[1]/tbody/tr')

if directed_by:
	directed_by = directed_by[0].strip()
else:
	# movie name cound not be found
	directed_by = ''
print (directed_by.center(50, "*").upper())


for directed_by_detail_row in directed_by_detail[0:]:
	director_name = directed_by_detail_row.xpath('./td[1]/a/text()')

	if director_name:
		director_name = director_name[0].strip()
		director_name = " ".join(director_name.split())
	else:
		director_name = ''

	print(director_name)



print('-'*50)


writing_credits =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/h4[2]/text()[normalize-space()]')
writing_credits_detail =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/table[2]/tbody/tr')

if writing_credits:
	writing_credits = writing_credits[0].strip()
else:
	# movie name cound not be found
	writing_credits = ''
print (writing_credits.center(50, "*").upper())

for writing_credits_detail_row in writing_credits_detail[0:]:

	writing_credits_name = writing_credits_detail_row.xpath('./td[1]/a/text()')
	if writing_credits_name:
		writing_credits_name = writing_credits_name[0].strip()
		writing_credits_name = " ".join(writing_credits_name.split())
	else:
		writing_credits_name = ''

	writing_credits_name1 = writing_credits_detail_row.xpath('./td[3]/a/text()')

	if writing_credits_name1:
		writing_credits_name1 = writing_credits_name1[0].strip()
		writing_credits_name1 = " ".join(writing_credits_name1.split())

	else:
		writing_credits_name1 = writing_credits_detail_row.xpath('./td[3]/text()')
		if writing_credits_name1:
			writing_credits_name1 = writing_credits_name1[0].strip()
			writing_credits_name1 = " ".join(writing_credits_name1.split())
		else:
			writing_credits_name1 = ''

	print('{writing_credits_name: <40}{writing_credits_name1: <10}'.format(writing_credits_name=writing_credits_name,writing_credits_name1=writing_credits_name1))

print('-'*50)



cast_title =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/h4[3]/text()[normalize-space()]')
cast_rows = tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/table[3]/tr')

if cast_title:
	cast_title = cast_title[0].strip()
else:
	# movie name cound not be found
	cast_title = ''
print (cast_title.center(50, "*").upper())

for row in cast_rows[1:]:
	tds = row.xpath('./td')

	# 1st td is icon, 2nd is Actor, and 4rd is Character
	actor = row.xpath('./td[2]/a/text()')

	if actor:
		actor = actor[0].strip()
		actor = " ".join(actor.split())
	else:
		actor = ''

	character = row.xpath('./td[4]/a/text()')

	if character:
		character = character[0].strip()
		character = " ".join(character.split())

	else:
		character = row.xpath('./td[4]/text()')
		if character:
			character = character[0].strip()
			character = " ".join(character.split())
		else:
			character = ''

	print('{actor: <40}{chracter: <10}'.format(actor=actor,chracter=character))

print('-'*50)


produced_by =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/h4[4]/text()[normalize-space()]')
produced_by_detail =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/table[4]/tbody/tr')

if produced_by:
	produced_by = produced_by[0].strip()
else:
	# movie name cound not be found
	produced_by = ''
print (produced_by.center(50, "*").upper())

for produced_by_detail_row in produced_by_detail[0:]:

	producer_name = produced_by_detail_row.xpath('./td[1]/a/text()')
	if producer_name:
		producer_name = producer_name[0].strip()
		producer_name = " ".join(producer_name.split())
	else:
		producer_name = ''

	producer_name1 = produced_by_detail_row.xpath('./td[3]/a/text()')

	if producer_name1:
		producer_name1 = producer_name1[0].strip()
		producer_name1 = " ".join(producer_name1.split())

	else:
		producer_name1 = produced_by_detail_row.xpath('./td[3]/text()')
		if producer_name1:
			producer_name1 = producer_name1[0].strip()
			producer_name1 = " ".join(producer_name1.split())
		else:
			producer_name1 = ''

	print('{producer_name: <40}{producer_name1: <10}'.format(producer_name=producer_name,producer_name1=producer_name1))

print('-'*50)


music_by =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/h4[5]/text()[normalize-space()]')
music_by_detail =  tree.xpath('//div[@id="main"]/div[@class="article listo"]/div[@id="fullcredits_content"]/table[5]/tbody/tr')

if music_by:
	music_by = music_by[0].strip()
else:
	# movie name cound not be found
	music_by = ''
print (music_by.center(50, "*").upper())

for music_by_detail_row in music_by_detail[0:]:

	musician = music_by_detail_row.xpath('./td[1]/a/text()')
	if musician:
		musician = musician[0].strip()
		musician = " ".join(musician.split())
	else:
		musician = ''


	print('{musician: <40}'.format(musician=musician))

print('-'*50)
