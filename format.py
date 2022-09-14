
import os
import glob
import markdown
import json

import csv

print()

title, desc,  = '', ''

template = """
<div class="box resource-box" id="resource-{{num}}">
<button class="add-fav" onclick="toggle_favs(this.parentElement.id)"></button>
<h1>{{title}}</h1>
<div class="meta info">
<p class="desc">{{desc}}</p>
<p class="duration">duration: {{duration}}</p>
</div>
<div class="meta buttons">
<div class="tags-list">{{tags}}</div>
<a href="{{url}}" target="_blank">
<div class="use-button">
<p>use me!</p>
</div></a>
</div>
</div>
"""

tags_template = """<span class="tag">{{tagname}}</span>"""

favs_template = """
<div class="fav-item box" id="fav-resource-{{num}}">
<button class="add-fav in-fav-box" onclick="remove_favs(this.parentElement.id)"></button>
<h1>{{title}}</h1>
<a href="{{url}}" target="_blank">
<div class="use-button">
<p>use me!</p>
</div></a>
</div>
"""

resources = []

with open("resources.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        resources.append(line)


# ok this is easy.

formatted = ""
favs_formatted = ""
count = 0
for resource in resources:
    print(resource)
    cur = template
    curf = favs_template

    cur = cur.replace("{{num}}", str(count))
    cur = cur.replace("{{title}}", resource[0])
    cur = cur.replace("{{url}}", resource[1])
    cur = cur.replace("{{desc}}", resource[2])
    tags = resource[3].split(', ')

    formatted_tags = ""
    for tag in tags:
        curtag = tags_template.replace("{{tagname}}", tag)
        formatted_tags += curtag
    cur = cur.replace("{{tags}}", formatted_tags)

    cur = cur.replace("{{duration}}", resource[4])

    curf = curf.replace("{{num}}", str(count))
    curf = curf.replace("{{title}}", resource[0])
    curf = curf.replace("{{url}}", resource[1])

    formatted += cur
    favs_formatted += curf

    count += 1

print()
print(formatted)
print()
print()
print()
print()
print(favs_formatted)
