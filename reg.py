# -*- coding: UTF-8 -*-
import  sys, termios, urllib2, requests
list_tags = """style, img, src, js, script, class, id, type, link, rel"""
tags = []
preTags = []
def make_request(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'pl-PL,pl;q=0.8',
       'Connection': 'keep-alive'}
	try:
	    req = requests.get(str(url), headers=hdr)
	except urllib2.HTTPError, e:
	    print e.fp.read()
	return str(req.content)
def links(url):
	req = make_request(url)
	tagss = findTags(str(req))
	links = filtering('href', tagss, 'link')
	return links
def dirs(url):
	req = make_request(url)
	tagsss = findTags(str(req))
	dirs = filtering('href', tagsss, 'dir')
	return dirs
def href(url):
	req = make_request(url)
	tags = findTags(str(req))
	hrefs = filtering('href', tags, None)
	return hrefs
def getContent(url, tag):
	termios.tcflush(sys.stdin,termios.TCIFLUSH)
	sys.stdout.flush()
	req = make_request(url)
	req = str(req).split('>')
	realStr = []
	for i in req:
		if '</' in i and str(tag) in i:
			i = i.replace('</','')
			realStr.append(i)
		elif str(tag) in i:
			i = i.replace(tag, '')
			realStr.append(i)
		else:
			pass
	for fix in realStr:
		if '<' in str(fix):
			realStr.remove(fix)
		else:
			pass
	termios.tcflush(sys.stdin,termios.TCIFLUSH)
	sys.stdout.flush()
	return realStr
def imgs(url):
	req = make_request(url)
	tags = findTags(str(req))
	imgs = filtering('src', tags, 'img')
	return imgs
def files(url):
	req = make_request(url)
	tags = findTags(str(req))
	typer = filtering('href', tags, 'pdf')
	typer1 = filtering('href', tags, 'torrent')
	typer2 = imgs = filtering('src', tags, 'img')
	res = list(set(list(typer + typer1 + typer2)))
	return res
def findTags(string):
	termios.tcflush(sys.stdin,termios.TCIFLUSH)
	sys.stdout.flush()
	global tags
	global preTags
	if '<' in string:
		string = string.split('<')
		for stri in string:
			if '>' in stri:
				preTags.append(stri)
			else:
				pass
		for tag in preTags:
			if '>' in tag and tag.endswith('>'):
				tags.append(tag)
			elif '>' in tag and tag.endswith('>') == False:
				tag = tag.split('>')
				tags.append(tag[0])
			else:
				pass
		termios.tcflush(sys.stdin,termios.TCIFLUSH)
		sys.stdout.flush()
		return tags
	else:
		return False
def filtering(filters, arrayTags, typer):
	termios.tcflush(sys.stdin,termios.TCIFLUSH)
	sys.stdout.flush()
	filtros = []
	if filters in str(arrayTags):
		for it in arrayTags:
			if filters in it:
				it = it.split(filters)
				it = it[1].split('/"')
				it = it[0].strip('=').strip('\'').replace('\"',"").split(' ')
				if typer != None:
					if typer == 'img':
						if '.jpeg' in str(it) or '.jpg' in str(it):
							if 'set=' in str(it):
								it = it[0]
								it = it.split('=')
								filtros.append(it[1])
							else:
								filtros.append(it[0])
						elif '>' in str(it):
							pass
						elif '.png' in str(it):
							if 'set=' in str(it):
								it = it[0]
								it = it.split('=')
								filtros.append(it[1])
							else:
								filtros.append(it[0])
						else:
							pass
					elif typer == 'pdf':
						if '.pdf' in str(it):
							filtros.append(it[0])
						else:
							pass
					elif typer == 'link':
						if 'http' in str(it):
							filtros.append(it[0])
						else:
							pass
					elif typer == 'torrent':
						if 'magnet:' in str(it):
							filtros.append(it[0])
						else:
							pass
					elif typer == 'dir':
						dire = str(it[0])
						if dire.startswith('/'):
							filtros.append(it[0])
						else:
							pass
					else:
						pass
				else:
					filtros.append(it[0])
			else:
				pass
		termios.tcflush(sys.stdin,termios.TCIFLUSH)
		sys.stdout.flush()
		return filtros


	else:
		return False


def getIn(url, param, typer):
	termios.tcflush(sys.stdin,termios.TCIFLUSH)
	sys.stdout.flush()
	req = make_request(url)
	if param in list_tags:
		tagsIn = findTags(req)
		tagR = filtering(param, tagsIn, typer)
		termios.tcflush(sys.stdin,termios.TCIFLUSH)
		sys.stdout.flush()
		return tagR
	else:
		return False
