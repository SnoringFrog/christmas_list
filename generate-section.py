#!/usr/bin/env python

from sys import argv as argv

item = argv[1];
item_nows = argv[1].replace(" ","")
link = argv[2]
img_link = argv[3]

print('''<section>
    <input class="toggle" type="checkbox" id="%(item_nows)s">
    <label for="%(item_nows)s" class="item-heading">%(item)s</label>
    <div class="expanding-box">
        <a href="%(link)s" target="_blank">&lt;online link&gt;</a>
        <br>
        <img class="item-img" src="%(img_link)s"> 
        <p class="item-desc">details</p>
    </div>
</section>''' % locals())
