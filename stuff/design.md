---
title: "Design Guidelines"
layout: experiment
theme: base
permalink: /design-guide/
---


# MANGOIN' DESIGN GUIDELINES

These guidelines are writting for me to personally adhere to, for consistancy in the design of my
projects.

I want to create my own, semi-unique style to use in my website and future projects like computer
programs, and to do so, I need to lay out some rules for my self.

## Da Rules:

The rules will be split into 2 sections: what to do, and what not to do. This is for me, as it would
be easiest to seperate the pros and cons of something to me, thus it would be easier to seperate the
good and bad for my sake.

### WHAT TO DO:

#### 1. **Include a linkbar**
A linkbar is what I call navigation bars, because I created the one in my website before I even knew
it had a real name. The linkbar should contain only the most IMPORTANT links and such. The links on
the linkbar should change depending on the page's content/subject. 

For instance, if you are on the memes page(RIP at the moment), the linkbar should include a link to 
all the pictures, all the videos, and to submit a meme. 

speaking of "submit a meme", the length of the all the text in those quotes is about 13 characters. 
Lets add one more to that, now it would be 14. Thats an even number now, and it is the maximum 
amount of characters that should be in a link in the linkbar. 
If a link is too long, it will take up valuable space. 

Speaking of valuable space, the links themselves take up some pretty big space. This is fine, how-
-ever, there is a point when I consider them to take up too much space.

If you look at the linkbar on [this site](https://yeetfolio.github.io/design-guide), you will 
notice that the links are centered in the bar. There is blank space between the links and the side's
borders. That space should be minimum 1.75mm(about half the length of a standard headphone cord) long
on a phone.

#### 2. **Small devices in mind**
This website was originally designed on a mobile phone. This actually has a lot of advantages, as the
layout, by heart, is designed to be able to be smushed down on a 5 inch screen in portrait mode.

By keeping my phone in mind(by literally making the thing on it), the site can enlarge and widen the
layout for larger screens, such as tablets, laptops and PCs. All without dropping a million `@media`
queries. But, it still doesn't hurt to have *some* `@media`s, but only to change small things, such
as text size. This is to keep maximum consistancy, which brings us to the next point:

#### 3. **Consistancy**

Don't make a button that has sharp corners when every other button has rounded corners, and dont 
change the layout of individual pages, no matter HOW different they are. My site has a certain type
of corner rounding, eclipse borders, and those borders are used throughout the WHOLE site. 

The standard border width on my site is `2px` as I recall, and every border starts out with that sizeunless it's too small to. 

Even the animations for stuff you can interact with are the same: enlarge on hover, shrink on click. Consistancy is key to a decent user experience.

#### 4. **No funky javascript hacks**
No fancy javascript animations in websites, and no delaying stuff to do those animations.
If css is an option, use it.

Javascript on my site should be used to actually do stuff, and should only interact with HTML Docum-
-ents, not the stylesheets.

also no complicated 3rd party scripts like `video.js` and the like, those just make the experience
sluggier and bad.

#### 5. **COLORS**
Always use a vibrant color for each page. Don't ever use something like black-on-white or white-on-b--lack unless its for a specific reason. Always use vibrant colors that contrast with eachother 
decently and don't look bugshit ugly.

Also, red as a main color should be used on error pages, and nowheres else.


