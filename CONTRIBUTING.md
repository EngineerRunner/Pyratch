# **Welcome to the contributing guidelines!**
You might want to contribute to Pyratch and these guidelines will help you!
Please follow the Github Community Guidelines along with these guidelines when contributing.
This will be split into a few sections:

**1. Get Started**

**2. What Kind Of Code**

**3. Styling Suggestions**

**4. Name And Description**

## 1. Get Started
**Notice: You will need experience with the following things:**

**1. Python**<br>
**2. Flask**<br>
**3. Scratchattach**<br>
**4. Jinja**<br>

To get started first download Pyratch of course by following the installation guide.

After that there are a few components you will see.
1. **interface.py** - This is the main Flask application and where you will be likely spending most of your time on, here you'll add new routes so your pages can be used and all of the server-side logic is here.
2. **templates** - This holds the HTML files (templates) for your pages, these use Jinja which is a templating language so that you can access data you pass in through Flask here
3. **static** - This holds static assets such as CSS files and images in the future, basically all not dynamic content goes here
4. **settings.json** - This is where the settings are stored, if your adding settings here you'll set a default value for them and check if they are working

You might not know where to start contributing, you can look at the issues for issues that you can fix or look for suggestions on the forum topic to implement. You can also just do quality of life changes or changes to the contributing guidelines (these!) or the README.

## 2. What Kind Of Code
**You can contribute the following code:**
1. Bug fixes and resolving issues
2. Adding suggestions and features
3. Making quality-of-life improvements

**We do not accept the following code though:**
1. Purely cosmetic changes
2. Changes that wouldn't generally be useful to anyone except you
3. Changes that would require massive overhaul without any reasons to do them

## 3. Styling Suggestions
1. Use tabs which translate to four spaces so that it remains consistent for everyone
2. Structure your code in a very modular way so removing parts of your code would lose functionality but Pyratch will still work
3. Don't use global variables, instead make a new manager class that stores them and can change them, then create an instance of it and use it
4. Have no comments, only on rare ocassions, comments are annoying and can clutter up code, instead attempt to write very readable code

## 4. Name And Description
Now that you have made your pull request, you likely want to know how to write the name and description.

The name must be formatted as this:

`version: desc`

Here version is the version that you are commiting to, so if your code is for Developer Build 4 for example then say:

`Developer Build 4: desc`

You can also include Pyratch before hand but this is not required and could clutter up your name:

`Pyratch Developer Build 4: desc`

The description should be short and brief, it is recommended to start with an action like `update` or `create` then up to five more words describing the action further, here are some examples:

`Developer Build 4: Updated userpage`

`Developer Build 4: Rewrote functions to be faster`

`Developer Build 4: Created studiopage`

If your action doesn't belong to a version or is too general then you can prefix with General:

`General: Added contributing guidelines`

Or you can also just have no prefix but this might be confusing for some people:

`Added contributing guidelines`

If your code is complicated then of course this name alone will probably not describe your changes well so use the description then but it is recommended to have no description for simple pull requests
