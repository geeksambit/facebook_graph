import urllib.request

def fetch_app_access_token(fb_app_id, fb_app_secret):
  resp = urllib.request.urlopen(
    'https://graph.facebook.com/oauth/access_token?client_id=' +
    fb_app_id + '&client_secret=' + fb_app_secret +
    '&grant_type=client_credentials')
  if resp.getcode() == 200:
    return resp.read().split("=")[1]
  else:
    return None

if __name__ == '__main__':
  from optparse import OptionParser
  parser = OptionParser()
  parser.add_option('--app_id', dest='131285656905938')
  parser.add_option('--secret', dest='90342e5fcc7079d3474945079ddbeb7b')
  (options, args) = parser.parse_args()

#  print (fetch_app_access_token(options.fb_app_id, options.fb_app_secret))
  print (fetch_app_access_token('131285656905938','90342e5fcc7079d3474945079ddbeb7b'))


