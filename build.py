print('site push')
top = open('templates/top.html').read()

body = open('body/activities.html').read()

body2 = open('body/funfacts.html').read()

bottom = open('templates/bottom.html').read()


combined_html = top + body + bottom 
open('docs/built_file.html', 'w+').write(combined_html)


combined_html_activities = top + body2 + bottom
open('docs/built_file_activities.html', 'w+').write(combined_html_activities)





