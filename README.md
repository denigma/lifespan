Lifespan App
============

This repository is devoted to the visualization of lifespan experiment data.

Inside it there are itself experiments with lifespan data and chats.

Warning: temporarily you will have to do:

    cake build

on semantic folder inside static


Setup
-----

1. Git in:

        git clone https://github.com/denigma/lifespan

        vitualenv env

        . env/bin/activate

        pip install -r requirements.txt

        ./manage.py syncdb
        ./manage.py runserver

2. Install Nodejs, CoffeeScript and LESS:

   Install nodejs ( http://nodejs.org/ ).
   Nodejs is used as a compiler for CoffeeScript and LESS
   It is better to install the version from the website as various linux repositories contain outdated versions

   After installation you will have npm at your disposal.
   With npm install:

        sudo npm install -g coffeescript
        sudo npm install -g batman
        sudo npm install -g less

Architecture
------------

Lifespan charts are based on d3js library and also use some features of Batmanjs library.
It is highly recommended to learn a little bit of d3.js before looking at the code.
There are a lot of good tutorials and even books at d3js website ( https://github.com/mbostock/d3/wiki/Tutorials )
It is enough to read anyone of them.

Basic charts workflow
---------------------

Both Denigma.BarCharts and Denigma.Curves inherit from Denigma.Charts and preserve some common methods and workflow.

So let's take a look at it.
  On construction you pass the id of the element where you want to insert your charts to
    and the name of the class for your basic elements

  When you want to draw something you call draw(data) function of the chart and path your data there.
  ```coffeescript
  draw: (data)->
      sel =  @select(data)
      @hide(sel.exit())
      novel = @append(sel.enter())
      @update(sel)
  ```
  Here the data is selected with select function and bound to svg elements that will be containers.
  ```coffeescript
  select: (data)->
      @svg.selectAll("svg.#{@subclass}").data(data)

  ```
  The data is bound to appropriate visual elements.
  The data that has no visual elements is retrieved by sel.enter() and will be used to create them by:
   ```coffeescript
   novel = @append(sel.enter())
   ```
  The elements for which there is no data (for instance you removed some points) is called sel.exit() and the will be hidden and then removed.
  After all new elements have been added we update all visual elements in accordance with the data received
  Other elements will be simply updated
  ```coffeescript
  @update(sel)
  ```
  Denigma.BarCharts and Denigma.Curves use some classes to do parts of work
  like Denigma.Icon for legend in bars and Denigma.BarView to render bars themselves.
  Most of these auxiliary classes inherit from Denigma.BasicView which works with selections and
  has similar workflow, append, and update functions.