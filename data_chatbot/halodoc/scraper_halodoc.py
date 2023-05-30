from bs4 import BeautifulSoup
import json
import requests
import string
for i in range(ord('a'),ord('z')+1):
	f=requests.get(f'https://magneto.api.halodoc.com/api/cms/categories?per_page=100&search_text={chr(i)}')
	html_doc=json.loads(f.text)
	print(f'scraping {chr(i)}')
	data=open('data_halodoc.txt','a')
	title=None
	content=''
	for i in html_doc['result']:
		soup=BeautifulSoup(i['content'],'html.parser')
		for i in soup.children:
			if '<h2' in str(i):
				if content!='' and title!=None:
					title=title.rstrip().strip(' ').replace(';','.').replace("\n",'.')
					content=content.rstrip().strip(' ').replace(';','.').replace("\n",'.')
					try:
						posisi_ref=content.index('Referensi:')
						content=content[:posisi_ref]
					except:
						pass
					if 'halodoc' in content or 'Halodoc' in content:
						posisi_titik=content.index('.')
						content=content[:posisi_titik]
					if '%3Ch2' in content:
						posisi_char=content.index('%3Ch2')
						content=content[:posisi_char]
					if title!='' and content!='':
						data_tulis=f"{title};{content}\n"
						data.write(data_tulis)
				title=i.text.rstrip()
				content=''
			else:
				if i.text!=' ':
					content+=i.text.rstrip()
	#soup = BeautifulSoup(f.text, 'html.parser')
