from django.http import HttpResponse,HttpResponseRedirect, HttpRequest
from django.shortcuts import render_to_response
from django.conf import settings
import urllib
import urllib2
import json
def obtainAccess(request):
        
    code = request.GET['code']

    OAuthSettings = { 'client_id'    : settings.CLIENT_ID,
                      'client_secret':  settings.CLIENT_SECRET,
                      'grant_type'   : 'authorization_code',
                      'redirect_uri' : 'http://localhost:8000/User/choose',
                      'code'         : code  
                     }
    #encoding data so it can POSTed by urllib2
    data = urllib.urlencode(OAuthSettings)
    #setting up request
    req = urllib2.Request(settings.URL,data)
    #executing the request

    response = urllib2.urlopen(req)
    #Turn the response into a JSON object
    data = json.load(response)
    
    settings.ACCESS_TOKEN = data['access_token']
    
    user_id = getUserId(data['user']['username'])

    return render_to_response('User/decision.html')

def instagramConnect(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    return response

def getUserId(username):
    url = 'https://api.instagram.com/v1/users/search?q=%s/&access_token=%s' % (username, settings.ACCESS_TOKEN)
    userData = instagramConnect(url)
    data = json.load(userData)
    return data['data'][0]['id']

def images(request):
    url='https://api.instagram.com/v1/users/%s/media/recent/?access_token=%s&count=8' %(settings.USER_ID,settings.ACCESS_TOKEN)
    imageData = instagramConnect(url)
    data = json.load(imageData)
    images = []

    for element in data['data']:
        images.append(element['images']['low_resolution']['url'])
    
    return render_to_response('User/images.html',{'images':images})
  
def getFollows(userIdNumber):
    url='https://api.instagram.com/v1/users/%s/follows?access_token=%s' % (userIdNumber, access_token)
    followsData = instagramConnect(url)
    data = json.load(followsData)
    array =[]
    for element in data['data']:
        array.append(element['profile_picture'])

    return render_to_response('User/images.html',{'images':array})



