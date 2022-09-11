
import os
import glob
import markdown
import json

import csv

print()

title, desc,  = '', ''

template = """
<div class="box resource-box">
<h1>{{title}}</h1>
<div class="meta info">
<p class="desc">{{description}}</p>
<p class="duration">duration: {{duration}}</p>
</div>
<div class="meta buttons">
<div class="tags-list">{{tags}}</div>
<a href="{{url}}" target="_blank"><div class="use-button">
<p>use me!</p>
</div></a>
</div>
</div>
"""

tags_template = """
<span class="tag">{{tagname}}</span>"""

resources = []

with open("resources.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")

    for line in tsv_file:
        resources.append(line)


# ok this is easy.

formatted = ""

for resource in resources:
    print(resource)
    cur = template

    cur = cur.replace("{{title}}", resource[0])
    cur = cur.replace("{{url}}", resource[1])
    cur = cur.replace("{{description}}", resource[2])
    tags = resource[3].split(', ')

    formatted_tags = ""
    for tag in tags:
        curtag = tags_template.replace("{{tagname}}", tag)
        formatted_tags += curtag
    cur = cur.replace("{{tags}}", formatted_tags)

    cur = cur.replace("{{duration}}", resource[4])
    
    formatted += cur

print()
print(formatted)
