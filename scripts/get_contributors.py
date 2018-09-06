API_BASE = "https://api.github.com/"

import requests as req

date_filter="merged:>2018-07-01"
query_str = "repo:rwengine/openrw%20{}".format(date_filter)
r = req.get("{}search/issues?q={}".format(API_BASE, query_str))

issues = r.json()['items']

users = [issue['user'] for issue in issues]
user_count = {}
user_data = {}
for user in users:
  if user['login'] not in user_data:
    user_data[user['login']] = user
    user['pr_count'] = 1
  else:
    user_data[user['login']]['pr_count'] += 1

users = sorted(user_data.items(), key=lambda a: a[1]['pr_count'], reverse=True)

user_template = '<a href="{url}" style="display: inline-block">' +\
                '<img src="{avatar_url}" style="width: 64px" alt="{descr}" title="{descr}"/></a>'
print("\n".join(
  [user_template.format(
    descr="{login} (PRs: {pr_count})".format(**user[1]), **user[1])
    for user in users]))
