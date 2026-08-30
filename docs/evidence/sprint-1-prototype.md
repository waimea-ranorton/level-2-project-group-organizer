# Sprint 1 - Developing a DB and UI Prototype


## Sprint Goals

Develop a design for the database and a UI prototype that simulates the key functionality of the system. Test and refine the UI so that it can serve as the model for the next phase of development in Sprint 2.

### Specific Goals

- Design the database:
    - Tables
    - Fields / types
    - Primary keys
    - Default / nullable values
    - Relationships (foreign keys)

- Design the UI
    - Key pages
    - User interactions and 'flow'
    - Page layouts / features
    - Colour palette
    - Etc.

## Initial Database Design
![Tables](screenshots/Tables.png)

### Required Data Input

The system will get

- When people make an account, they are required to put a name and contact/s, this can be viewed on a profile page/drop-down.

- When people create a project they are required to enter who is apart of the project,
(they could add the person through the id that is automatically given to the user when they create an account, or they could look up their name), this can be viewed in a section about project details.

- When people create a project they are required to enter a name for it, and if it has a deadline, during the project they can change the status between unfinished and finished, this can be viewed on the projects page.

- When people add a file to a project they can give it a "use", they will be suggested to say "Working file" or "Resource" but can put anything they like, this should be viewable just under the file.

### Required Data Output

The system will display
- integers
- text
- text? (some text can be null, see design screenshot above)

### Required Data Processing

Replace this text with a description of how the data will be processed to achieve the desired output(s) - any processes / formulae?


## UI 'Flow'

The first stage of prototyping was to explore how the UI might 'flow' between states, based on the required functionality.

This Figma demo shows the initial design for the UI 'flow':
![Flow](screenshots/flow1.png)

*https://design.penpot.app/#/view?file-id=81f57451-85cc-819d-8008-76dbd5996cf3&page-id=81f57451-85cc-819d-8008-76dbd5996cf4&section=interactions&index=0&share-id=3be9e5e1-190f-8090-8008-76dc16543f9c*

### Testing

I showed this UI flow template to my end-user, they didn't like how it opened right to the home screen, they asked if there could be some sort of loading screen/splash screen before hand.

### Changes / Improvements

I added a splash screen.
![Flow](screenshots/flow2.png)

*https://design.penpot.app/#/view?file-id=81f57451-85cc-819d-8008-76dbd5996cf3&page-id=81f57451-85cc-819d-8008-76dbd5996cf4&section=interactions&index=0&share-id=3be9e5e1-190f-8090-8008-76ea4f9686b4*


## Initial UI Prototype

The next stage of prototyping was to develop the layout for each screen of the UI.

### Changes / Improvements

When I was making my layouts for each screen, I resized that having only one page for all finished and upcoming projects could make the user scroll a lot. So I separated them (see below).

I also decided that projects on the home page should separated into due and finished projects, so its easier for users to find things, and that due projects should be displayed in order of when its due.

![Flow](screenshots/flow3.png)

*https://design.penpot.app/#/view?file-id=3be9e5e1-190f-8090-8008-6de71b4fba1b&page-id=3be9e5e1-190f-8090-8008-6de71b4fba1c&section=interactions&index=0&share-id=81f57451-85cc-819d-8008-76ef30d55776*

### Testing

I realized that having the home page may be unessisary, and maybe the app should just immediately go to the upcoming projects. I asked my user what they thought of this.

I showed the template above to my end user.

### Changes / Improvements
My end user said they liked the splash screen, and the add project page, only asking for minor tweaks.
We agreed that the home page as it was held little function, instead of removing it my end user decided to repurpose it, now the user can see recent acititiy, and click to acess projects, this side pannel would scroll if needed. My end user also asked if the navigation could be moved to the bottom of the screen, and hover over top of everything else.
The asked me to add on a settings page, somthing we hadnt previously discussed.

### Testing
After I developed this template with the feedback from my user, showing them often as I worked on it, making minor tweaks based on their opions, leading to this end result.

![Flow](screenshots/flow4.png)

*https://design.penpot.app/#/view?file-id=81f57451-85cc-819d-8008-772f6aae5fb0&page-id=81f57451-85cc-819d-8008-772f6aae5fb1&section=interactions&index=0&share-id=3be9e5e1-190f-8090-8008-7962b28e1c45*


## Refined UI Prototype     

Having established the layout of the UI screens, the prototype was refined visually, in terms of colour, fonts, etc.

### Colour
I has a conversation with my user before I began this project, where asked specifically for a dull, "peaceful", purple, colour palette, that uses black and white for details.
So I came up with these colour palletes:
![Colour pallete](screenshots/colorpallete.png)
![Colour pallete](screenshots/colorpallete2.png)
![Colour pallete](screenshots/colorpallete3.png)

### Testing
After shpowing those palletes to my end user, they asked for the colour palette to be monochromatic, and said they liked the more destaturated one. So I produced these.

![Colour pallete](screenshots/colorpallete4.png)
![Colour pallete](screenshots/colorpallete5.png)
![Colour pallete](screenshots/colorpallete6.png)
![Colour pallete](screenshots/colorpallete7.png)
![Colour pallete](screenshots/colourpallete8.png)

### Testing
My end user said, They quiet liked those colours but wanted to make minor changes, after some discussion, they sent back this color palette they produced.
![Colour pallete](screenshots/colourpallete9.png)

### Fonts
My end user asked for the app/website to use Garamond or Times New Roman, or both, depending on what I thought would work best.

### Shapes
My end user asked for the website to be rounded, litterally, here are some examples they sent and xhfdhgvfduilfhfsd....

## Sprint Review

I think that I could have benifited in time if I had shown my user the templates more freqwently during development and asked further qeastions, as to prevent extreme changes that ended up happening.

