print('combining html files ')

top = open('templates/top.html').read()

body = open('contents/activities.html').read()

body2 = open('contents/funfacts.html').read()

bottom = open('templates/bottom.html').read()


combined_html = top + body + bottom 
open('docs/built_file.html', 'w+').write(combined_html)


combined_html_activities = top + body2 + bottom
open('docs/built_file_activities.html', 'w+').write(combined_html_activities)





