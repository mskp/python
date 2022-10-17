from github import Github
import json
import base64

git = Github('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')
file = 'sushant.jpeg'
data = {}
with open(f'img/profile-photo/{file}', 'rb') as pic:
    photo = pic.read()
    # mycommunity_storage = git.get_repo('mskp/MyCommunity-Storage-heroku')
    # mycommunity_storage.create_file(f'img/{file}', 'photo-upload', photo, branch='main')
    # print(mycommunity_storage)
data['img'] = base64.encodebytes(photo).decode('utf-8')
print(json.dumps(data))
json.